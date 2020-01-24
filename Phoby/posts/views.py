from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import createPosts
from .forms import OurForm
# Create your views here.

def posts(request):
    form = OurForm()
    if request.method == "POST":
        form = OurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:view')
        else:
            form = OurForm()
    return render(request, "main/upload.html", {"form": form})

def posts_view(request):
    return render(request, template_name="main/posts_list.html", context={"Posts":createPosts.objects.all})

def update_posts(request, id=None):
    posts = get_object_or_404(createPosts,id=id)
    form = OurForm()
    if request.method == "POST":
        form = OurForm(request.POST, request.FILES,instance=posts)
        if form.is_valid():
            form.save()
            return redirect('posts:view')
    else:
        return render(request,"main/upload.html",{"form":form})



def delete_posts(request, pk):
    posts = createPosts.objects.get(pk=pk)
    posts.delete()
    return redirect('posts:view')