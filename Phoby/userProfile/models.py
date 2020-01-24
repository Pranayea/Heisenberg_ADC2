from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userProfile(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profilePic = models.ImageField(upload_to='profile/profilePic/',blank=False) 

    def __str__(self):
        return self.user
