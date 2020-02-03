from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import userProfile
from .form import OurForm
from django.http import HttpResponse


# add bio and profile pic
def bio(request):
    form = OurForm()
    if request.method == "POST":
        form = OurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('userProfile:profile')
        else:
            form = OurForm()
    return render(request, "userProfile/bio.html", {"form": form})

# gives profile


def profile_list(request):
    return render(request, "userProfile/profile.html", context={"Profile": userProfile.objects.all})

# update profile pic, bio etc


def update_profile(request, id=None):
    profile = get_object_or_404(userProfile, id=id)
    form = OurForm()
    if request.method == "POST":
        form = OurForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('userProfile:profile')
    else:
        return render(request, "userProfile/bio.html", {"form": form})
