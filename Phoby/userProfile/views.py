from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from .form import OurForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from posts.models import *

# add bio and profile pic
def bio(request):
    form = OurForm()
    if request.method == "POST":
        form = OurForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user_of = request.user #saves instance of user
            form.save()#saves form
            return redirect('userProfile:profile')#redirects to profile page
        else:
            form = OurForm()
    return render(request, "userProfile/bio.html", {"form": form})

# gives profile
def profile_list(request):
    current_user = request.user
    #created objects
    post = CreatePosts.objects.all()
    profile = UserProfile.objects.filter(user_of=current_user)
    return render(request, "userProfile/profile.html", context={"Profile": profile, "post": post})

# update profile pic, bio 
def update_profile(request, id=None):
    profile = get_object_or_404(UserProfile, id=id)
    form = OurForm()
    if request.method == "POST":
        form = OurForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('userProfile:profile')
    else:
        return render(request, "userProfile/bio.html", {"form": form})



