from django import forms
from .models import CreatePosts, Comments


class OurForm(forms.ModelForm):
    # Meta Class Is used to override a class
    class Meta:
        model = CreatePosts
        fields = ('post_image','post_caption','uploaded_by')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields=('comment',)