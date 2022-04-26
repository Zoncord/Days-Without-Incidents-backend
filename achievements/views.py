from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from achievements.filters import AchievementFilter
from achievements.models import Achievement, Incident
from achievements.permissions import IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly
from achievements.serializers import AchievementSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['id']
    search_fields = ['title']
    filterset_class = AchievementFilter


    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Achievement.objects.filter(Q(is_private=False) | Q(owners=self.request.user))

        return Achievement.objects.filter(is_private=False)
