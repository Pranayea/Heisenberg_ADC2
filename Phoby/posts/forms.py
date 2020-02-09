from django import forms
from .models import createPosts


class OurForm(forms.ModelForm):
    # Meta Class Is used to override a class
    class Meta:
        model = createPosts
<<<<<<< HEAD
        fields = ('post_image', 'post_caption', 'uploaded_by')
=======
        fields = ('post_image','post_caption','uploaded_by')
>>>>>>> c3e0b5f0cae27db958c7021207cb34e991db6bda
