from django.urls import path
from . import views

urlpatterns = [
    path('posts/',views.posts,name='posts'),
    path('view/',views.posts_view,name='posts'),
    ]
