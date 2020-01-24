from django.shortcuts import render, redirect
from .models import Users

from django.db.models import Q


# Create your views here.

def userop(request):
    user = Users.objects.all()
    query = ""
    if request.GET:
        query = request.GET['q']
        user = get_data_queryset(str(query))
    return render(request, "main/search.html", {"users" : user})


   
def get_data_queryset(query=None):
    queryset = []
    
    queries = query.split(" ") 
    for q in queries:
        user = Users.objects.filter(
            Q(username__icontains = q) | 
            Q(email__icontains = q)
        ).distinct()
        
        for users in user:
            queryset.append(users)
#set() vaneko typecasting gareko, queryset lai set ma convert gareko #query set ma repeatition hatauna
#queryset lai set ma convert garcha ani feri list ma
    return list(set(queryset))
    
