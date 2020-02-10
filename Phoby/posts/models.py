from django.db import models

from datetime import datetime, date
from django.contrib.auth.models import User  # for linking
# Create your models here.


class createPosts(models.Model):
    post_image = models.ImageField(
        upload_to='posts/posts_images/', blank=False)
    post_caption = models.TextField(max_length=140)
    uploaded_on = models.DateTimeField(
        auto_now_add=True)  # adds value automatically
    uploaded_by = models.ForeignKey(
        User, default=1, on_delete=models.CASCADE, unique=False)
    comment = models.ForeignKey(User, null=True,related_name='comment', on_delete=models.CASCADE)


    def __str__(self):
        return self.post_caption
