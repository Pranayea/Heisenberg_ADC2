from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# imported all class from models.py
from . models import *
# imported class PhobyForm from forms.py
from .forms import PhobyForm
from .decorators import unauthenticated_user
# , admin_only
from django.contrib.auth.decorators import login_required

# this method shows all the hobby present


@login_required(login_url='accounts:login')
# @admin_only
def homepage(request):
    return render(request, template_name="main/homepage.html", context={"hobbys": Hobby.objects.all})
# this method registers user


@unauthenticated_user
def register(request):
    form = PhobyForm()
    if request.method == "POST":  # checks whether the request method is post
        form = PhobyForm(request.POST)
        if form.is_valid():
            user = form.save()
        return redirect('accounts:login')

    return render(request, template_name="main/register.html", context={"form": form})

# this method authenticates user to login


@unauthenticated_user
def loginpage(request):
    if request.method == 'POST':  # checks whether the request method is post
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # cleaned data turns username to caseinsensitive
            username = form.cleaned_data.get('username')
            # cleaned data turns username to caseinsensitive
            password = form.cleaned_data.get('password')
            # authenicating user if username and password exists or not
            user = authenticate(username=username, password=password)
            if user is not None:

                login(request, user)

                return redirect('accounts:homepage')
            else:
                # shows message if user doesnot exists
                messages.error(request, "Invalid username or password.")
        else:
            # shows message if form is not valid
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request,
                  template_name="main/login.html",  # returns to login.html
                  context={"form": form})


# this method logouts the user
def logout_page(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("accounts:login")
