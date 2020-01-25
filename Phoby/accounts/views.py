from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
#imported class Hobby from models.py
from . models import Hobby
#imported class PhobyForm from forms.py
from .forms import PhobyForm


#this method shows all the hobby present
def homepage(request):
    return render(request, template_name="main/home.html",context={"hobbys":Hobby.objects.all})
#this method registers user 
def register(request):
    form = PhobyForm()
    if request.method == "POST": #checks whether the request method is post
        form = PhobyForm(request.POST)
        if form.is_valid():
            user = form.save()
        return redirect('accounts:login')
    
    return render(request, template_name="main/register.html", context={"form":form})

#this method authenticates user to login
def loginpage(request):
    if request.method == 'POST': #checks whether the request method is post
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username') #cleaned data turns username to caseinsensitive
            password = form.cleaned_data.get('password') #cleaned data turns username to caseinsensitive
            user = authenticate(username=username, password=password) #authenicating user if username and password exists or not
            if user is not None:

                login(request, user)
               
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.") #shows message if user doesnot exists
        else:
            messages.error(request, "Invalid username or password.") #shows message if form is not valid
    form = AuthenticationForm()
    return render(request,
                    template_name = "main/login.html", #returns to login.html
                    context={"form":form})


#this method logouts the user
def logout_page(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("accounts:login")
