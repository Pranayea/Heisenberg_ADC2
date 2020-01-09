from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   profile_bio = models.CharField(max_length=200)
#    saved_posts = models.ForeignKey(Posts, on_delete=models.CASCADE)
#    hobbies_followed = models.ForeignKey(Hobbies, on_delete=models.CASCADE)
#    followers = models.ForeignKey(Followers, on_delete=models.CASCADE)
#    profile_pic = models.ImageField(default='smth.jpeg', upload_to='profile.pics')

   def __str__(self):
       return f'{self.user.username} Profile'



