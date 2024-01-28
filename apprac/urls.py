from django.contrib import admin
from django.urls import path, include
from apprac import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('home2', views.home2, name='home2')
]
