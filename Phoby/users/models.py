from django.db import models


class Users(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_name = models.CharField(max_length = 15)
    user_password = models.CharField(max_length = 15)
    user_email = models.EmailField(max_length = 100)
    user_DOB = models.DateTimeField('date')
    user_address = models.CharField(max_length = 45)
    

    def __str__(self):
        return  self.user_name