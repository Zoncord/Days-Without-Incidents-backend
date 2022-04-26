from django.urls import path, include
from rest_framework.routers import DefaultRouter
from achievements.views import AchievementViewSet

router = DefaultRouter()
router.register(r'achievement', AchievementViewSet, basename="achievement")

urlpatterns = [
    path('', include(router.urls)),
]
