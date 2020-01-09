from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import createPosts
# Create your views here.

def posts(request):
    if request.method == 'POST':
        post_image = request.FILES['image']
        post_caption = request.POST['caption']
        posts = createPosts(post_image=post_image, post_caption=post_caption)
        posts.save() 
        print('Upload Complete')
     

        return redirect('/')
    else:
        return render(request, template_name="main/upload.html", context={"Posts":createPosts.objects.all})