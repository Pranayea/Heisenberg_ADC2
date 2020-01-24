from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class phobyUsers(models.Model):
    username = models.ForeignKey(User, on_delete = models.CASCADE, related_name="custom_user")
    email = models.ForeignKey(User, on_delete = models.CASCADE, related_name="custom_email")
    # password = models.FileField()  

    def __str__(self):
        return self.username
