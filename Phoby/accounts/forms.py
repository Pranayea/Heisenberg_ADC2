from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import PasswordInput
from django.contrib.auth.models import User

#Created PhobyForm for registration using UserCreationForm
class PhobyForm(UserCreationForm):
    email = forms.EmailField(required=True)
   
#Meta class to overrride
    class Meta:
        model = User
        fields = (
            'username', 
            'email', 
            'password1', 
            'password2'
            )

    def save(self, commit=True):
        user = super(PhobyForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        return user
