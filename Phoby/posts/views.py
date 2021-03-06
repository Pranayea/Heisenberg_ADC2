from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import CreatePosts, Comments  # custom database
from .forms import OurForm, CommentForm  # Custom Form
from accounts.decorators import unauthenticated_user
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User  # Custom Form
from django.http import HttpResponseRedirect
import json


# upload feature for posts app
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
            return redirect('userProfile:profile')
        else:
            form = OurForm()
    # sends custom form to the html file
    return render(request, "posts/upload.html", {"form": form})

# this method is for posting comments
def postComment(request, pk):
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user #takes instance of user
            form.instance.post = get_object_or_404(CreatePosts, id=pk) #takes instance of posts
            form.save()
            return HttpResponseRedirect("") 
        else:
            form = CommentForm()

    return render(request, "posts/comments.html", {"form": form, "posts": CreatePosts.objects.all, "Comments": Comments.objects.all})


def posts_view(request):
    # takes and sends all the from databsse to html
    return render(request, template_name="posts/posts_list.html", context={"Posts": CreatePosts.objects.all})


def update_posts(request, id=None):  # id of a specific post
    # takes the data from a specific post in the database
    posts = get_object_or_404(CreatePosts, id=id)
    form = OurForm()
    if request.method == "POST":
        # changes the value of chosen id
        form = OurForm(request.POST, request.FILES, instance=posts)
        if form.is_valid():
            form.save() #saves form
            return redirect('userProfile:profile') #redirects to method profile
    else:
        return render(request, "posts/upload.html", {"form": form})


def delete_posts(request, pk):  # primary key of specific post
    posts = CreatePosts.objects.get(pk=pk)
    posts.delete()  # deletes the page
    return redirect('userProfile:profile')  # redirects to the list of post

