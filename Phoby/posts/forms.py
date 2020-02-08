from django import forms
from .models import createPosts

class OurForm(forms.ModelForm):
# Meta Class Is used to override a class
    class Meta:
        model = createPosts
        fields = ('post_image','post_caption','uploaded_by')