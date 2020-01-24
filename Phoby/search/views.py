from django.shortcuts import render, redirect
from .models import phobyUsers
# from django.contrib.auth.models import User
from django.db.models import Q
from posts.models import createPosts


# Create your views here.

def userop(request):
    posts = createPosts.objects.all()
    query = ""
    if request.GET:
        query = request.GET['q']
        posts = get_data_queryset(str(query))
    return render(request, "main/searrch.html", {"posts":posts})


   
def get_data_queryset(query):
    queryset = []
    
    queries = query.split(" ") 
    for q in queries:
        posts = createPosts.objects.filter(
            Q(post_caption__icontains = q) #| Q(email__icontains = q)
        ).distinct()
        
        for p in posts:
            queryset.append(p)
#set() vaneko typecasting gareko, queryset lai set ma convert gareko #query set ma repeatition hatauna
#queryset lai set ma convert garcha ani feri list ma
    return list(set(queryset))
    
