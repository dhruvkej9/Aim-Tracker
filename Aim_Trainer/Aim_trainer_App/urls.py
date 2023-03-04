
from django.contrib import admin
from django.urls import path
from Aim_trainer_App import views

urlpatterns = [
    path("", views.loginUser,name = "home"),
    path("signin", views.loginUser,name = "signin"),
    path("signup", views.signup,name = "signup"),
    # path('profile', views.p,name = 'profile'),
    path("play", views.signup,name = "play"),
]
