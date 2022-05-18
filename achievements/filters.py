from django_filters import rest_framework as filters

from .models import Achievement


class AchievementFilter(filters.FilterSet):
    owners = filters.Filter(field_name='owners', lookup_expr='in')

    class Meta:
        model = Achievement
        fields = ['owners']
