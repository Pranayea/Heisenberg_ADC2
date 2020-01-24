from django.db import models

# Create your models here.

class Users(models.Model): #models.Model le charfield haru use garna dincha
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.FileField()  

    def __str__(self):
        return self.username
