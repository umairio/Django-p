from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
   path('', index, name='index'),
   path('home/', index, name='index'),
   path('home2/', ibase, name='ibase'),
   path('contact/', contact, name='contact'),
   path("api/", include(router.urls)),
   path('api/login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
   path('api/logout/', TokenRefreshView.as_view(), name='token_refresh'),
   path('api/register/', RegisterView.as_view(), name='auth_register'),
]
