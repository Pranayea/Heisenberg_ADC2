from django.db import models
from django.contrib.auth.models import User
from posts.models import Hobby
# Create your models here.

class PhobyUsers(models.Model):
    username = models.ForeignKey(User, on_delete = models.CASCADE, related_name="custom_user")
    email = models.ForeignKey(User, on_delete = models.CASCADE, related_name="custom_email")
    hobbyName = models.ForeignKey(Hobby, on_delete = models.CASCADE, related_name="custom_hobby", default=None)
    # password = models.FileField()  

    def __str__(self):
        return self.username
        
