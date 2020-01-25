from django.test import TestCase

# from . import views
from .models import createPosts
from datetime import datetime
# Create your tests here.
class PostTest(TestCase):
    def setUp(self):
      createPosts.objects.create(post_caption ="I know all", post_image="Zoro.png")
    
    def test_ORM(self):
        post = createPosts.objects.get(post_caption="I know all",post_image="Zoro.png" )
        self.assertEqual(post.post_caption, "I know all")
        self.assertEqual(post.post_image, "Zoro.png")