from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users import views
from users.views import UserViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet, basename="user")

urlpatterns = [
    path('authorization/', views.AuthorizationView.as_view()),
    path('profile/', views.ProfileView.as_view()),
    path('', include(router.urls)),
]
