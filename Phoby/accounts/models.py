from django.db import models
from django.contrib.auth.models import User
from posts.models import CreatePosts


class Users(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

# Hobby table conatining hobby name and number of followers and posts


class Hobby(models.Model):
    hobby_id = models.AutoField(primary_key=True)
    hobbyName = models.CharField(max_length=15)
    # followers = models.ForeignKey()
    posts = models.IntegerField()

    def __str__(self):
        return self.hobbyName


