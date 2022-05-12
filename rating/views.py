from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from rating import models
from rating.filters import AchievementRatingFilter, PostRatingFilter, UserRatingFilter
from rating.permissions import RatingPermission
from rating.serializers import AchievementRatingSerializer, PostRatingSerializer, UserRatingSerializer


class AchievementRatingViewSet(viewsets.ModelViewSet):
    queryset = models.AchievementRating.objects.all()
    serializer_class = AchievementRatingSerializer

    permission_classes = [RatingPermission]

    filter_backends = [DjangoFilterBackend]
    filterset_class = AchievementRatingFilter


class PostRatingViewSet(viewsets.ModelViewSet):
    queryset = models.PostRating.objects.all()
    serializer_class = PostRatingSerializer

    permission_classes = [RatingPermission]

    filter_backends = [DjangoFilterBackend]
    filterset_class = PostRatingFilter


class UserRatingViewSet(viewsets.ModelViewSet):
    queryset = models.UserRating.objects.all()
    serializer_class = UserRatingSerializer

    permission_classes = [RatingPermission]

    filter_backends = [DjangoFilterBackend]
    filterset_class = UserRatingFilter
