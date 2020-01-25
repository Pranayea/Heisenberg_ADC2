from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import createPosts #custom database
from .forms import OurForm  #Custom Form
# Create your views here.

# upload feature for posts app
def posts(request):
    form = OurForm()
    if request.method == "POST":
        form = OurForm(request.POST, request.FILES) # POSTing caption and images 
        if form.is_valid():
            form.save()
            return redirect('posts:view') #redirects when a set value is saved in the database
        else:
            form = OurForm()
    return render(request, "main/upload.html", {"form": form}) #sends custom form to the html file

def posts_view(request):
    return render(request, template_name="main/posts_list.html", context={"Posts":createPosts.objects.all}) #takes and sends all the from databsse to html 

def update_posts(request, id=None): # id of a specific post
    posts = get_object_or_404(createPosts,id=id) # takes the data from a specific post in the database
    form = OurForm()
    if request.method == "POST":
        form = OurForm(request.POST, request.FILES,instance=posts) # changes the value of chosen id
        if form.is_valid():
            form.save()
            return redirect('posts:view')
    else:
        return render(request,"main/upload.html",{"form":form})



def delete_posts(request, pk): # primary key of specific post 
    posts = createPosts.objects.get(pk=pk)
    posts.delete() #deletes the page
    return redirect('posts:view') # redirects to the list of post