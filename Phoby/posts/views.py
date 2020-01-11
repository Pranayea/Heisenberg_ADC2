from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import createPosts
from PIL import Image
# Create your views here.

def posts(request):
    if request.method == 'POST':
        # post_image = request.FILES['image']
        post_caption = request.POST['caption']
        # posts = createPosts(post_image=post_image, post_caption=post_caption)
        posts = createPosts(post_caption=post_caption)
        posts.save() 

        return redirect('/posts/view')
    else:
        return render(request, template_name="main/upload.html")

def posts_view(request):
    return render(request, template_name="main/posts_list.html", context={"Posts":createPosts.objects.all})

def posts_edit(request,pk=0):
    # if request.method == 'POST':
        posts_edit=createPosts.objects.get(pk=pk)
        # posts = createPosts(instance=posts_edit)
        return render(request, template_name="main/upload.html", context={"posts":posts})


def posts_delete(request,pk):
    posts=createPosts.objects.get(pk=pk)
    posts.delete()
    return redirect('/posts/view')
