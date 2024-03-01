from django import forms
from apps.gap.models import Opinion, Comment


class OpinionCreateForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ('title', 'body', 'room')

#
# class CommentCreateForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('title', 'body', 'room')
