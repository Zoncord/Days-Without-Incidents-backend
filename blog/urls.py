from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import PostViewSet, CommentViewSet, AnswerViewSet

router = DefaultRouter()
router.register(r'post', PostViewSet, basename="post")
router.register(r'comment', CommentViewSet, basename="comment")
router.register(r'answer', AnswerViewSet, basename="answer")

urlpatterns = [
    path('', include(router.urls)),
]
