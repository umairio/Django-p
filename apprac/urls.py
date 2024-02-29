from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import routers


router = routers.DefaultRouter()

urlpatterns = [
   path('', index, name='index'),
   path('home/', index, name='index'),
   path('home2/', ibase, name='ibase'),
   path('contact/', contact, name='contact'),
   path("api/", include(router.urls)),
   path('api/register/', RegisterView.as_view(), name='auth_register'),
   path('api/login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
   path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('api/logout/', LogoutView.as_view(), name='logout'),
   path('api/projects/', ProjectView.as_view(), name='projects'),
   path('api/projects/<int:pk>/', ProjectView.as_view(), name='projects'),
   path('api/tasks/', TaskView.as_view(), name='tasks'),
   path('api/tasks/<int:pk>/', TaskView.as_view(), name='tasks'),
   path('api/tasks/<int:pk>/assign/', TaskAssignView.as_view(), name='tasks'),
]
