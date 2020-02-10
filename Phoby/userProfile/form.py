from django import forms
from .models import UserProfile

class OurForm(forms.ModelForm):
# Meta Class Is used to override a class
    class Meta:
        model = UserProfile #adding custom fields
        fields = ('bio', 'profilePic')