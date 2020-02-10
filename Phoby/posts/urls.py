from django.contrib import admin
from django.urls import path
from . import views # views from posts

app_name = "posts"

urlpatterns = [
    path('upload/', views.posts, name='uploads'), # view in the for uploading
    path('view/',views.posts_view,name='view'), # displays the datas in createpost database
    path('upload/<int:id>/', views.update_posts, name='update'),# editing a data
    path('view/<int:pk>/',views.delete_posts,name='delete'), # deleting a data
    path('comment/<int:pk>',views.postComment,name="comment"),
    path('updateapi/<int:pk>/',views.update_data_json,name='updatejson'),
    path('list/<int:PAGENO>/<int:SIZE>/',views.post_objects_paginations,name='pagination'),
]
