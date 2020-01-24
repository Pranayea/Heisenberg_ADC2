from django.shortcuts import render, redirect
from .models import phobyUsers
from django.contrib.auth.models import User
from django.db.models import Q
from posts.models import createPosts


# Create your views here.

def userop(request):
    users = phobyUsers.objects.all()
    query = ""
    if request.GET:
        query = request.GET['q']
        user = get_data_queryset(str(query))
    return render(request,"main/search.html", context={"user":users})


   
def get_data_queryset(query):
    queryset =[]
    queries = query.split(" ")    
    for q in queries:
        users = User.objects.filter(
            Q(username__icontains= q) | 
            Q(email__icontains = q)
        ).distinct()
        
        for user in users:
            queryset.append(user)
    return list(set(queryset))
    
