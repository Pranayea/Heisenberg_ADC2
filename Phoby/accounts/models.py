from django.db import models


# Create your models here.
class Hobby(models.Model):
    hobby_id=models.AutoField(primary_key=True)
    hobby_name = models.CharField(max_length = 15)
    followers = models.IntegerField()
    posts = models.IntegerField()

    

    def __str__(self):
        return  self.hobby_name

