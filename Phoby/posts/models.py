from django.db import models
from datetime import datetime, date
# Create your models here.

class createPosts(models.Model):
    post_id = models.AutoField(primary_key = True)
    post_image = models.ImageField(upload_to='posts_images/',blank=False)
    post_caption = models.TextField(max_length=140)
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_caption
        