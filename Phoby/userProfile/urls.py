from django.urls import path
from . import views


app_name = "userProfile"


urlpatterns = [
    path('bio/', views.bio, name="bio"), # add bio and profile pic
    path('profile/',views.profile_list, name='profile'), #gives profile
    path('bio/<int:id>/', views.update_profile, name="update"), #for updating bio and profile pic
]