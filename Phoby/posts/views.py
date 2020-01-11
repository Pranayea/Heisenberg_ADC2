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

        return redirect('/view')
    else:
        return render(request, template_name="main/upload.html")

def posts_view(request):
    return render(request, template_name="main/posts_list.html", context={"Posts":createPosts.objects.all})

def delete_posts(request):
    pass 