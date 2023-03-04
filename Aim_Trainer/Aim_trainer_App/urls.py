
from django.contrib import admin
from django.urls import path
from Aim_trainer_App import views

urlpatterns = [
    path("", views.Signup,name = "home"),
    path("signin", views.loginUser,name = "signin"),
    path("register", views.Signup,name = "signup"),
    path('profile', views.loginUser,name = 'profile'),
    path("play", views.loginUser,name = "play"),
]
