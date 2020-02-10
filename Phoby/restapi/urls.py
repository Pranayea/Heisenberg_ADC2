from django.contrib import admin
from django.urls import path
from . import views # views from posts

app_name = "restapi"

urlpatterns = [
    path('list/',views.show_posts_data,name='jsonlist'),
    path('updateapi/<int:pk>/',views.update_posts_json,name='updatePosts'),
    path('profile/',views.show_profile_data,name='jsonprofile'),
    path('user/',views.show_user_data,name='userJson'),
    path('userupdate/<int:pk>/',views.update_user_json,name='updateUser'),
    path('profileupdate/<int:pk>/',views.update_profile_json,name='updateprofile'),
    path('page/<int:int_page>/<int:int_size>/',views.post_objects_paginations,name='pagination'),
    path('userpage/<int:int_page>/<int:int_size>/',views.user_objects_paginations,name='userpagination'),
    path('profilepage/<int:int_page>/<int:int_size>/',views.profile_objects_paginations,name='profilepagination'),

]
