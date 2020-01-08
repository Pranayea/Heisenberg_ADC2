from django.shortcuts import render, redirect
from .models import Users
from django.contrib.auth.models import User, auth

# Create your views here.
# def homepage(request):
#     return render(request, template_name="home.html", context={"users":Users.objects.all})



def homepage(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']


        user= User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
        user.save()
        print('User Created')
     

        return redirect('/')
    else:
        return render(request, template_name="home.html", context={"users":Users.objects.all})