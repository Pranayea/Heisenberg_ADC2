from django.test import TestCase

# from . import views
from django.contrib.auth.models import User
from .models import userProfile
from datetime import datetime
# Create your tests here.
class profileTest(TestCase):
    def setUp(self):
      userProfile.objects.create(bio="Trying to test", profilePic="Zoro.png")
    
    def test_ORM(self):
        profile = userProfile.objects.get(bio="Trying to test", profilePic="Zoro.png")
        self.assertEqual(profile.bio, "Trying to test")
        self.assertEqual(profile.profilePic, "Zoro.png")