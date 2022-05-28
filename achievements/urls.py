from django.urls import path, include
from rest_framework.routers import DefaultRouter
from achievements.views import AchievementViewSet, CategoryViewSet, TagViewSet, IncidentViewSet

router = DefaultRouter()
router.register(r'achievement', AchievementViewSet, basename='achievement')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'tag', TagViewSet, basename='tag')
router.register(r'incident', IncidentViewSet, basename='incident')

urlpatterns = [
    path('', include(router.urls)),
]
