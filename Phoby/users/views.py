from django.shortcuts import render, redirect
from .models import Users
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate

# Create your views here.
# def homepage(request):
#     return render(request, template_name="home.html", context={"users":Users.objects.all})


def login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']

        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/test.html')
        else:
            messages.info(request,'invalid')
            return redirect('login')

def homepage(request):

    # if request.POST.get('submit') == 'Login':
    #         # your sign in logic goes here
    #     username= request.POST['username']
    #     password= request.POST['password']

    #     user=auth.authenticate(username=username, password=password)

    #     if user is not None:
    #         auth.login(request,user)
    #         return redirect('/test.html')
    #         else:
    #         messages.info(request,'invalid')
    #         return redirect('login')

    # elif request.POST.get('submit') == 'Register':
    #         # your sign up logic goes here
    #     first_name = request.POST['first_name']
    #     last_name = request.POST['last_name']
    #     username = request.POST['username']
    #     password1 = request.POST['password1']
    #     password2 = request.POST['password2']
    #     email = request.POST['email']


    #     user= User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
    #     user.save() 
    #     print('User Created')
    
    # else:
    #     return render(request, template_name="home.html", context={"users":Users.objects.all}) 





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



