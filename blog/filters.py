from django_filters import rest_framework as filters

from rating.models import AchievementRating
from .models import Post, Comment


class LikeFilter(filters.Filter):
    def label(self):
        return 'user favorites'

    def filter(self, qs, value):
        if value is None or not value.isdigit():
            return qs
        achievements_ratings = AchievementRating.objects.filter(user_id=value)
        posts = Post.objects.none()
        for achievement_rating in achievements_ratings.all():
            posts = posts | achievement_rating.achievement.posts.all()
        return qs & posts


class PostFilter(filters.FilterSet):
    user_favorite = LikeFilter()

    class Meta:
        model = Post
        fields = ['author', 'achievement', 'user_favorite']


class CommentFilter(filters.FilterSet):
    class Meta:
        model = Comment
        fields = ['author', 'post']

