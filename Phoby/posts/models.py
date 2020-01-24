from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User
# Create your models here.

class createPosts(models.Model):
    user = models.ForeignKey(User,default="1" ,on_delete=models.CASCADE)
    post_image = models.ImageField(upload_to='posts/posts_images/',blank=False)
    post_caption = models.TextField(max_length=140)
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_caption
        