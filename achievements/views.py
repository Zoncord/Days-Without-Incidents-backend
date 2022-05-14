from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from achievements.filters import AchievementFilter
from achievements.models import Achievement, Category, Tag
from achievements.permissions import IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly
from achievements.serializers import AchievementSerializer, CategorySerializer, TagSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    """
    Achievements are used to create and obtain information about user cards
    """
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['id']
    search_fields = ['title']
    filterset_class = AchievementFilter

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Achievement.objects.filter(is_private=False)

        return Achievement.objects.filter(Q(is_private=False) | Q(owners=self.request.user))


class CategoryViewSet(viewsets.ModelViewSet):
    """
    Achievement categories
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    permission_classes = []

    filter_backends = [DjangoFilterBackend, SearchFilter]
    ordering_fields = ['id']
    search_fields = ['title']


class TagViewSet(viewsets.ModelViewSet):
    """
    Achievement tags
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    permission_classes = []

    filter_backends = [DjangoFilterBackend, SearchFilter]
    ordering_fields = ['id']
    search_fields = ['title']
