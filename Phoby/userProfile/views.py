from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import userProfile
from .form import OurForm
from django.http import HttpResponse
from django.contrib.auth.models import User

# add bio and profile pic
def bio(request):
    form = OurForm()
    if request.method == "POST":
        form = OurForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user_of = request.user
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


def send_follow(request,id):
    if request.user.is_authenticated():
        user =get_object_or_404(User,id=id)
        fo_request= Followers.objects.get_or_create(
            from_user = request.user, 
            to_user = user
        )
    return redirect("accounts:homepage") 

def accept_follow(request,id):
    from_user = get_object_or_404(User,id=id)
    fo_request=Followers.objects.filter(from_user=from_user, to_user=request.user).first()
    user1 = fo_request.to_user
    user2 = from_user
    user1.userProfile.friends.add(user2.userProfile)
    user2.userProfile.friends.add(user1.userProfile)
    fo_request.delete()

    return redirect("accounts:homepage")