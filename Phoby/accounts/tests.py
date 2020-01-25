from django.test import TestCase

# from . import views
from django.contrib.auth.models import User
from datetime import datetime
# Create your tests here.
class UserTest(TestCase):
    def setUp(self):
      User.objects.create(username="Pranaya", email="prms@gmail.com")
    
    def test_ORM(self):
        users = User.objects.get(username="Pranaya", email="prms@gmail.com")
        self.assertEqual(users.username, "Pranaya")
        self.assertEqual(users.email, "prms@gmail.com")