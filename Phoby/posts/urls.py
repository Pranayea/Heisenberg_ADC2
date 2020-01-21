from django.contrib import admin
from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('upload/', views.posts, name='uploads'),
    path('view/',views.posts_view,name='view'),
]
