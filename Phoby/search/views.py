from django.shortcuts import render, redirect
from .models import PhobyUsers
from django.contrib.auth.models import User
from django.db.models import Q
from posts.models import CreatePosts
from accounts.models import Hobby

# Create your views here.

def userop(request):
    user = PhobyUsers.objects.all()
    hobby = Hobby.objects.all()
    query = ""
    if request.GET:
        query = request.GET['q']
        user = get_data_queryset(str(query))
        hobby = get_data_queryset(str(query))
    return render(request,"main/search.html", {"users":user ,"hobbys":hobby})


   
def get_data_queryset(query=None):
    queryset =[]
    queries = query.split(" ")    
    for q in queries:
        users = User.objects.filter(
            Q(username__icontains= q) | 
            Q(email__icontains = q)
        ).distinct()
        hobbys = Hobby.objects.filter(
            Q(hobbyName__icontains= q) 
        ).distinct()
        for user in users:
            queryset.append(user)
        for hobby in hobbys:
            queryset.append(hobby)

    # for q in queries:          
    #     hobbys = Hobby.objects.filter(
    #         Q(hobbyName__icontains= q) 
    #     ).distinct()
    #     for hobby in hobbys:
    #         queryset.append(hobby)
    return list(set(queryset))
    
