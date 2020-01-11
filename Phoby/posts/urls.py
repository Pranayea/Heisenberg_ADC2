from django.urls import path
from . import views

urlpatterns = [
    path('posts/',views.posts,name='posts'),
    path('view/',views.posts_view,name='view'),
    path('<int:pk>/',views.posts_edit,name='posts_update'),
    path('delete/<int:pk>/',views.posts_delete,name='posts_delete'),
    ]
