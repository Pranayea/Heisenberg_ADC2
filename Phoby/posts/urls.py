<<<<<<< HEAD
<<<<<<< HEAD
from django.contrib import admin
from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('upload/', views.posts, name='uploads'),
    path('view/',views.posts_view,name='view'),
    path('upload/<int:pk>/', views.update_posts, name='update'),
    path('view/<int:pk>/',views.delete_posts,name='delete'),
]
=======
=======
>>>>>>> parent of be3fd2b... 1stpost delete
from django.urls import path
from . import views

urlpatterns = [
    path('posts/',views.posts,name='posts'),
    path('view/',views.posts_view,name='view'),
    path('<int:pk>/',views.posts_edit,name='posts_update'),
    path('delete/<int:pk>/',views.posts_delete,name='posts_delete'),
    ]
<<<<<<< HEAD
>>>>>>> parent of be3fd2b... 1stpost delete
=======
>>>>>>> parent of be3fd2b... 1stpost delete
