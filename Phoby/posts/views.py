from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.

def posts(request):

    return render(request, template_name='main/upload.html')