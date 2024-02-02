from django.urls import path
from .views import index, ibase, contact


urlpatterns = [
   path('', index, name='index'),
   path('home', index, name='index'),
   path('home2/', ibase, name='ibase'),
   path('contact', contact, name='contact')
]
