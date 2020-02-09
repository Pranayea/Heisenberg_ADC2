from django.db import models
from django.contrib.auth.models import User

# this class contains users profile picture and short bio


class userProfile(models.Model):
    user_of = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profilePic = models.ImageField(upload_to='profile/profilePic/',blank=False) 
    friends = models.ManyToManyField("userProfile", blank=True)

    def __str__(self):
        return self.user

class Followers(models.Model):
    to_user = models.ForeignKey(User, null=True, on_delete = models.CASCADE, related_name='to_user')
    from_user = models.ForeignKey(User, null=True, on_delete = models.CASCADE, related_name='from_user')

    def __str__(self):
        return "From {}, to {}".format(self.from_user.username, self.to_user.username)


