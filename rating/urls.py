from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rating import views

router = DefaultRouter()
router.register(r'achievement', views.AchievementRatingViewSet, basename='achievementrating')
router.register(r'post', views.PostRatingViewSet, basename='postrating')
router.register(r'user', views.UserRatingViewSet, basename='userrating')

urlpatterns = [
    path('', include(router.urls)),
]
