from django.urls import path
from . import views


app_name = "accounts"


urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('register/', views.register, name="register"),
    path("login/", views.loginpage, name="login"),
    path('logout/', views.logout_page, name="logout"),
]
