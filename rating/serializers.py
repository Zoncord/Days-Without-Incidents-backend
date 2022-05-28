from rest_framework import serializers
from rest_framework.exceptions import NotAuthenticated

from rating import models
from rating.models import AchievementRating, UserRating, PostRating


class AchievementRatingSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(read_only=True, view_name='user-detail')

    def create(self, validated_data):
        request = self.context.get('request', None)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        rating = AchievementRating.objects.create(user=request.user, **validated_data)
        return rating

    class Meta:
        model = models.AchievementRating
        fields = '__all__'


class PostRatingSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(read_only=True, view_name='user-detail')

    def create(self, validated_data):
        request = self.context.get('request', None)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        rating = PostRating.objects.create(user=request.user, **validated_data)
        return rating

    class Meta:
        model = models.PostRating
        fields = '__all__'


class UserRatingSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(read_only=True, view_name='user-detail')

    def create(self, validated_data):
        request = self.context.get('request', None)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        rating = UserRating.objects.create(user=request.user, **validated_data)
        return rating

    class Meta:
        model = models.UserRating
        fields = '__all__'
