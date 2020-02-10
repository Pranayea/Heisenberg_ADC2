from django.test import TestCase

# from . import views
from django.contrib.auth.models import User
from datetime import datetime
# Create your tests here.
class UserTest(TestCase):
    def setUp(self):# creating new user for testing
      User.objects.create(username="Pranaya", email="prms@gmail.com")
    
    def test_ORM(self):# method to test User
        users = User.objects.get(username="Pranaya", email="prms@gmail.com") # get User Objects from model
        self.assertEqual(users.username, "Pranaya") #testing username field
        self.assertEqual(users.email, "prms@gmail.com") #testing email field