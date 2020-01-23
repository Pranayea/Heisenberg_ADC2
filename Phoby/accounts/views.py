from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from . models import Hobby
from .forms import PhobyForm
# Create your views here.


def homepage(request):
    return render(request, template_name="main/home.html",context={"hobbys":Hobby.objects.all})

def register(request):
    form = PhobyForm()
    if request.method == "POST":
        form = PhobyForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
        return redirect('accounts:login')
    
    #return render(request, template_name="main/accounts.html", context={"form":form})
    return render(request, template_name="main/register.html", context={"form":form})


def loginpage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:

                login(request, user)
               
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request,
                    template_name = "main/login.html",
                    context={"form":form})


def logout_page(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("accounts:login")
