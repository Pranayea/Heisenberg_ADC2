from django import forms
from .models import userProfile

class OurForm(forms.ModelForm):
# Meta Class Is used to override a class
    class Meta:
        model = userProfile #adding custom fields
        fields = ('bio', 'profilePic')