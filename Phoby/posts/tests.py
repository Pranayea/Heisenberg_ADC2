from django.test import TestCase
from . import views 
from .models import createPosts
from datetime import datetime

# Create your tests here.
class postsTest(TestCase):
    def setUp(self):
        createPosts.objects.create(post_caption ="Django is confusing", uploaded_on=datetime.now())
    
    def test_ORM(self):
        posts = createPosts.objects.get(post_caption="Django is confusing")
        self.assertEqual(posts.post_caption, "Django is confusing")
