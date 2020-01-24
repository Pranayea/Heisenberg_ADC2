from django.urls import path
from . import views


app_name = "userProfile"


urlpatterns = [
    path('bio/', views.bio, name="bio"),
    path('profile/',views.profile_list, name='profile'),
    path('bio/<int:id>/', views.update_profile, name="update"),
]