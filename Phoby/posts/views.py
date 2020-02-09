from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import createPosts  # custom database
from .forms import OurForm  # Custom Form
from accounts.decorators import unauthenticated_user
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User  # Custom Form
import json
# Create your views here.

# upload feature for posts app


@unauthenticated_user
def posts(request):
    form = OurForm()
    if request.method == "POST":

        # uploaded_by = request.user.username
        # POSTing caption and images
        form = OurForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.uploaded_by = request.user
            form.save()
            # redirects when a set value is saved in the database
            return redirect('posts:view')
        else:
            form = OurForm()
    # sends custom form to the html file
    return render(request, "main/upload.html", {"form": form})


@unauthenticated_user
def posts_view(request):
    # takes and sends all the from databsse to html
    return render(request, template_name="main/posts_list.html", context={"Posts": createPosts.objects.all})


@unauthenticated_user
def update_posts(request, id=None):  # id of a specific post
    # takes the data from a specific post in the database
    posts = get_object_or_404(createPosts, id=id)
    form = OurForm()
    if request.method == "POST":
        # changes the value of chosen id
        form = OurForm(request.POST, request.FILES, instance=posts)
        if form.is_valid():
            form.save()
            return redirect('posts:view')
    else:
        return render(request, "main/upload.html", {"form": form})


@unauthenticated_user
def delete_posts(request, pk):  # primary key of specific post
    posts = createPosts.objects.get(pk=pk)
    posts.delete()  # deletes the page
    return redirect('accounts:homepage')  # redirects to the list of post



def show_all_data(request):
    post = createPosts.objects.all()
    print(type(post))
    dict_type = {"post": list(post.values("post_image","post_caption","uploaded_on"))}
    return JsonResponse(dict_type)


@csrf_exempt
def update_data_json(request, pk):
    post= createPosts.objects.get(pk=pk)
    if request.method == "GET":
        return JsonResponse({"post_image":post.post_image, "post_caption":post.post_caption,"uploaded_on":post.uploaded_on})
    else:
        json_body = request.body.decode('utf-8')
        json_data = json.loads(json_body)
        post.post_image = json_data['post_image']
        post.post_caption = json_data['post_caption']
        post.uploaded_on = json_data['uploaded_on']
        post.save()
        return JsonResponse({"message":"Successful!!"})

def post_objects_paginations(request,PAGENO,SIZE):
    skip = SIZE * (PAGENO -1)
    post = createPosts.objects.all() [skip:(PAGENO * SIZE)]
    dict ={
            "post":list(createPosts.values("post_image","post_caption","uploaded_on"))
        }
    return JsonResponse(dict)