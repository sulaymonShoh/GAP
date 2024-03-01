from django import template

from apps.gap.models import OpinionLike, CommentLike

register = template.Library()


@register.filter(name="check_opinion_like")
def check_opinion_like(opinion, user):
    return OpinionLike.objects.filter(opinion=opinion, user=user).exists()


@register.filter(name="check_comment_like")
def check_comment_like(comment, user):
    return CommentLike.objects.filter(comment=comment, user=user).exists()
