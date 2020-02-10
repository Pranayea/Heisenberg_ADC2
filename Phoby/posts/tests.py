from django.test import TestCase

# from . import views
from .models import CreatePosts, Comments, Hobby #importing custom models from posts 
from django.contrib.auth.models import User # User model form accounts class
from datetime import datetime
# Create your tests here.
class PostTest(TestCase):
    def setUp(self):  # setUp method to create a new user,hobby and a post to test case
      user = User.objects.create(username="Pranaya", email="prms@gmail.com") #user creation with name and email
      hobby = Hobby.objects.create(hobbyName = "Art") # hobby creation with hobby name
      #creating a post with user and hobby as foreign keys 
      CreatePosts.objects.create(post_caption ="I know something", post_image="Zoro.png",uploaded_by=user,hobby=hobby)
    
    def test_CreatePost(self): #method to test the validity of CreatePost model 
        post = CreatePosts.objects.get(post_caption="I know something",post_image="Zoro.png")# getiing objects with given values
        self.assertEqual(post.post_caption, "I know something") #testing validity of post_cation field 
        self.assertEqual(post.post_image, "Zoro.png") #testing validity of post_image


class CommentTest(TestCase):
  def setUp(self): # setUp method to create a new user,hobby ,a post and comment to test case
    user = User.objects.create(username="Pranaya", email="prms@gmail.com")#user creation with name and email
    hobby = Hobby.objects.create(hobbyName = "Art")# hobby creation with hobby name
     #creating a post with user and hobby as foreign keys 
    posts = CreatePosts.objects.create(post_caption ="I know something", post_image="Zoro.png",uploaded_by=user,hobby=hobby)
    # creating comments with post and users as Foreign key 
    Comments.objects.create(user=user,post=posts,comment="Testing Comment")

  def test_Comments(self): #method to test the validity of Comments model 
    comment1 = Comments.objects.get(comment="Testing Comment")# getting objects with given values
    self.assertEqual(comment1.comment,"Testing Comment") # testing comments


class HobbyTest(TestCase):
  def setUp(self): #setUp to create a new Hobby
    Hobby.objects.create(hobbyName="Art")

  def test_hobby(self):# TestCase for Hobby
    hobby = Hobby.objects.get(hobbyName="Art") # getting object from Hobby Model
    self.assertEqual(hobby.hobbyName,"Art")# testing with Hobby