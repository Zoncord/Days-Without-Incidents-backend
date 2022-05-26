from django_filters import rest_framework as filters

from blog.models import Post
from .models import AchievementRating, UserRating, PostRating


class AchievementRatingFilter(filters.FilterSet):
    user = filters.Filter(field_name='user')
    achievement = filters.Filter(field_name='achievement')

    class Meta:
        model = AchievementRating
        fields = ['user', 'achievement']


class PostRatingFilter(filters.FilterSet):
    user = filters.Filter(field_name='user')
    post = filters.Filter(field_name='post')

    class Meta:
        model = PostRating
        fields = ['user', 'post']


class UserRatingFilter(filters.FilterSet):
    user = filters.Filter(field_name='user')
    evaluated_user = filters.Filter(field_name='evaluated_user')

    class Meta:
        model = UserRating
        fields = ['user', 'evaluated_user']
