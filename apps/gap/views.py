from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from apps.gap.models import Room, Opinion, Comment, OpinionLike


class RoomListView(View):
    def get(self, request):
        rooms = Room.objects.all()
        return render(request, 'gap/rooms.html', {"rooms": rooms})


class RoomDetailView(View):
    def get(self, request, pk):
        room = Room.objects.get(pk=pk)

        opinions = sorted(Opinion.objects.filter(room=room), key=lambda o: o.like_count, reverse=True)
        context = {
            "room": room,
            "opinions": opinions
        }
        return render(request, "gap/opinions.html", context=context)


class LikeOpinionView(LoginRequiredMixin, View):
    def get(self, request, pk):
        opinion = Opinion.objects.get(pk=pk)
        like, created = OpinionLike.objects.get_or_create(user=request.user, opinion=opinion)
        if not created:
            like.delete()
        return redirect(reverse("gap:opinion_detail", kwargs={"pk": opinion.pk}))


class OpinionDetailView(View):
    def get(self, request, pk):
        opinion = Opinion.objects.get(pk=pk)
        comments = opinion.comments.all().order_by("-created_at")
        already_liked = OpinionLike.objects.filter(opinion=opinion, user=request.user).exists()
        context = {
            "opinion": opinion,
            "comments": comments,
            "is_liked": already_liked,
        }
        return render(request, "gap/comments.html", context=context)
