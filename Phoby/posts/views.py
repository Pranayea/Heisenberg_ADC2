from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import createPosts  # custom database
from .forms import OurForm  # Custom Form
from accounts.decorators import unauthenticated_user
from django.contrib.auth.models import User  # Custom Form
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
