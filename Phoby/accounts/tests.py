from django.test import TestCase

# from . import views
from django.contrib.auth.models import User
from datetime import datetime
# Create your tests here.
class UserTest(TestCase):
    def setUp(self):
      User.objects.create(username="Pranaya", email="prms@gmail.com")
    
    def test_ORM(self):
        post = User.objects.get(username="Pranaya", email="prms@gmail.com")
        self.assertEqual(post.username, "Pranaya")
        self.assertEqual(post.email, "prms@gmail.com")