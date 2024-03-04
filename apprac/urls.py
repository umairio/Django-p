from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from .views import *

router = routers.DefaultRouter()
router.register(r"tasks", TaskViewSet, basename="tasks")
router.register(r"projects", ProjectViewSet, basename="projects")
# router.register(r"comments", CommentViewSet, basename="comments")


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
   path('api/tasks/<int:pk>/assign/', TaskAssignView, name='tasks'),
   path('api/documents/', DocumentView.as_view(), name='documents'),
   path('api/documents/<int:pk>/', DocumentView.as_view(), name='documents'),
   path('api/comments/', CommentView.as_view(), name='comments'),
   path('api/comments/<int:pk>/', CommentView.as_view(), name='comments'),
]
