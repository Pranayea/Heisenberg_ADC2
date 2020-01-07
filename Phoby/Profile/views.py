from django.shortcuts import render
from .models import Profile
# Create your views here.
def profile(request):
    return render(request=request, template_name="Profile/profile.html", context={"Profile":Profile.objects.all})