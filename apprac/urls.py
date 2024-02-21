from django.urls import path
from .views import home, home2


urlpatterns = [
   path('', home, name='index'),
   path('home', home, name='index'),
   path('home2/', home2, name='home2')
]
