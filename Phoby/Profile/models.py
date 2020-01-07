from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_ID = models.AutoField(primary_key=True)

class User(models.Model):
    user_ID = models.AutoField(primary_key=True)
    user_uname = models.CharField(max_length = 100)
    user_fname = models.CharField(max_length = 50)
    user_lname = models.CharField(max_length = 50)
    user_password = models.CharField(max_length = 30)

class SavedPost(models.Model):
    # post_ID = models.ForeignKey(Post.post_ID,on_delete=models.CASCADE)
    user_ID = models.ForeignKey(User,on_delete=models.CASCADE)

