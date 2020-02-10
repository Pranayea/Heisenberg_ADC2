from django.db import models

from datetime import datetime, date
from django.contrib.auth.models import User  # for linking
# Create your models here.


class CreatePosts(models.Model):
    post_image = models.ImageField(
        upload_to='posts/posts_images/', blank=False)
    post_caption = models.TextField(max_length=140)
    uploaded_on = models.DateTimeField(
        auto_now_add=True)  # adds value automatically
    uploaded_by = models.ForeignKey(
        User, default=1, on_delete=models.CASCADE, unique=False)

    def __str__(self):
        return self.post_caption


class Comments(models.Model):
    post = models.ForeignKey(CreatePosts, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=140)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
