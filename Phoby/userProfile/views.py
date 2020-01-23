from django.shortcuts import render
from django.shortcuts import render, redirect , get_object_or_404
from .models import userProfile
from .form import OurForm
from django.http import HttpResponse

# Create your views here.
def profile(request):
    form = OurForm()
    if request.method == "POST":
        form = OurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('userProfile/profile.html')
        else:
            form = OurForm()
    return render(request, "userProfile/profile.html", {"form": form})
