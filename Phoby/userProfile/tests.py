from django.test import TestCase

# from . import views
from django.contrib.auth.models import User
from .models import UserProfile # importing custom model
from datetime import datetime
# Create your tests here.
class profileTest(TestCase):
    def setUp(self): #method to create new profile
      UserProfile.objects.create(bio="Trying to test", profilePic="Zoro.png")#creating profile
    
    def test_ORM(self):#testing UserProfile model
        profile = UserProfile.objects.get(bio="Trying to test", profilePic="Zoro.png")#getting objects from UserProfile model
        self.assertEqual(profile.bio, "Trying to test") # testing bio field
        self.assertEqual(profile.profilePic, "Zoro.png")# tesing profilePic field