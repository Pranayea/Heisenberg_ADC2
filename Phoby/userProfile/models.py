from django.db import models
from django.contrib.auth.models import User

# this class contains users profile picture and short bio


class userProfile(models.Model):
    user_of = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profilePic = models.ImageField(
        upload_to='profile/profilePic/', blank=False)

    def __str__(self):
        return self.user
