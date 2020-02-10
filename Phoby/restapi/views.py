from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from posts.models import CreatePosts  # custom database
from posts.forms import OurForm  # Custom Form
from accounts.decorators import unauthenticated_user
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User  # Custom Form
import json
from userProfile.models import UserProfile
# Create your views here.

def show_posts_data(request):
    post = CreatePosts.objects.all()
    print(type(post))
    dict_type = {"post": list(post.values(
        "post_image", "post_caption", "uploaded_on"))}
    return JsonResponse(dict_type)

def show_user_data(request):
    user = User.objects.all()
    print(type(user))
    dict_type = {"user": list(user.values("username", "email"))}
    return JsonResponse(dict_type)

def show_profile_data(request):
    profile = UserProfile.objects.all()
    print(type(profile))
    dict_type = {"profile": list(profile.values("profilePic", "bio"))}
    return JsonResponse(dict_type)


@csrf_exempt
def update_posts_json(request, pk):
    post= CreatePosts.objects.get(pk=pk)
    if request.method == "GET":
        return JsonResponse({"post_image": post.post_image, "post_caption": post.post_caption, "uploaded_on": post.uploaded_on})
    else:
        json_body = request.body.decode('utf-8')
        json_data = json.loads(json_body)
        post.post_image = json_data['post_image']
        post.post_caption = json_data['post_caption']
        post.uploaded_on = json_data['uploaded_on']
        post.save()
        return JsonResponse({"message":"Successful!!"})

@csrf_exempt
def update_user_json(request, pk):
    user= User.objects.get(pk=pk)
    if request.method == "GET":
        return JsonResponse({"username": user.username, "email": user.email})
    else:
        json_body = request.body.decode('utf-8')
        json_data = json.loads(json_body)
        user.username= json_data['username']
        user.email = json_data['email']
        user.save()
        return JsonResponse({"message":"Successful!!"})

@csrf_exempt
def update_profile_json(request, pk):
    profile= UserProfile.objects.get(pk=pk)
    if request.method == "GET":
        return JsonResponse({"profilePic": profile.profilePic, "bio": profile.bio})
    else:
        json_body = request.body.decode('utf-8')
        json_data = json.loads(json_body)
        profile.profilePic= json_data['profilePic']
        profile.bio = json_data['bio']
        profile.save()
        return JsonResponse({"message":"Successful!!"})

@csrf_exempt
def post_objects_paginations(request,int_page,int_size):
    skip = int_size * (int_page -1)
    post = CreatePosts.objects.all() [skip:(int_page * int_size)]
    dict ={
            "post":list(CreatePosts.values("post_image","post_caption","uploaded_on"))
        }
    return JsonResponse(dict)

@csrf_exempt
def user_objects_paginations(request,int_page,int_size):
    skip = int_size * (int_page -1)
    user = User.objects.all() [skip:(int_page * int_size)]
    dict ={
            "user":list(User.values("username","email"))
        }
    return JsonResponse(dict)

@csrf_exempt
def profile_objects_paginations(request,int_page,int_size):
    skip = int_size * (int_page -1)
    profile = UserProfile.objects.all() [skip:(int_page * int_size)]
    dict ={
            "profile":list(UserProfile.values("username","email"))
        }
    return JsonResponse(dict)

