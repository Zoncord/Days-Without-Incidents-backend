from rest_framework import serializers
from rating import models


class AchievementRatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.AchievementRating
        fields = '__all__'


class PostRatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PostRating
        fields = '__all__'


class UserRatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.UserRating
        fields = '__all__'
