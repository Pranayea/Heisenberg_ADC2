from django.urls import path
from . import views


app_name = "accounts"


urlpatterns = [
    path('', views.homepage, name="homepage"),#url for homepage
    path('register/', views.register, name="register"), #url for register
    path("login/", views.loginpage, name="login"),#url for login
    path('logout/', views.logout_page, name="logout"),#url for logout
]
