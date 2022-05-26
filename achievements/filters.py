from django.db.models import QuerySet
from django_filters import rest_framework as filters

from blog.models import Post
from rating.models import AchievementRating
from .models import Achievement


class AchievementFilter(filters.FilterSet):
    owners = filters.Filter(field_name='owners')

    class Meta:
        model = Achievement
        fields = ['owners']
