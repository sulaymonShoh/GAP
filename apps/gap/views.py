from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from apps.gap.forms import OpinionCreateForm, CommentCreateForm
from apps.gap.models import Room, Opinion, Comment, OpinionLike, CommentLike


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


class OpinionDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        opinion = Opinion.objects.get(pk=pk)
        comments = opinion.comments.all().order_by("-created_at")
        context = {
            "opinion": opinion,
            "comments": comments,
            # "is_liked": already_liked,
        }
        return render(request, "gap/comments.html", context=context)


class OpinionCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = OpinionCreateForm()
        return render(request, 'gap/opinion_form.html', {"form": form})

    def post(self, request):
        form = OpinionCreateForm(request.POST)
        if form.is_valid():
            opinion = form.save(commit=False)
            opinion.author = request.user
            opinion.save()
            messages.success(request, "Opinion saved successfully")
            return redirect(reverse("gap:opinion_detail", kwargs={"pk": opinion.id}))
        else:
            return render(request, 'gap/opinion_form.html', {"form": form})


class LikeOpinionView(LoginRequiredMixin, View):
    def get(self, request, pk):
        opinion = Opinion.objects.get(pk=pk)
        like, created = OpinionLike.objects.get_or_create(user=request.user, opinion=opinion)
        if not created:
            like.delete()
        return redirect(reverse("gap:room", kwargs={"pk": opinion.room.pk}))


class CommentOpinionView(LoginRequiredMixin, View):
    def get(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        like, created = CommentLike.objects.get_or_create(user=request.user, comment=comment)
        if not created:
            like.delete()
        return redirect(reverse("gap:opinion_detail", kwargs={"pk": comment.opinion.room.pk}))

# class CommentCreateView(LoginRequiredMixin, View):
#     def get(self, request):
#         form = CommentCreateForm()
#         return render(request, 'gap/opinion_form.html', {"form": form})
#
#     def post(self, request):
#         form = CommentCreateForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author = request.user
#             comment.save()
#             messages.success(request, "Opinion saved successfully")
#             return redirect(reverse("gap:opinion_detail", kwargs={"pk": comment.opinion.id}))
#         else:
#             return render(request, 'gap/opinion_form.html', {"form": form})
# bitmagan
