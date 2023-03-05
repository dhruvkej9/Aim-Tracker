
from django.contrib import admin
from django.urls import path
from Aim_trainer_App import views

urlpatterns = [
    path("", views.index,name = "home"),
    path("signin", views.loginUser,name = "signin"),
    path("register", views.Signup,name = "signup"),
    path("statistic", views.statistic,name = "statistics"),
    path('profile', views.profile,name = 'profile'),
    path("play", views.play,name = "play"),
    path('logout', views.logoutUser,name = "logout"),
]
