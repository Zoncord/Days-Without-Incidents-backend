import datetime

from rest_framework import serializers

from achievements.models import Achievement, Incident


class FollowersCountField(serializers.ReadOnlyField):
    def to_representation(self, value):
        return value.likes.count()


class DaysField(serializers.ReadOnlyField):
    def to_representation(self, value):
        return (datetime.datetime.now() - value.incidents.first().date_time).days


class AchievementSerializer(serializers.HyperlinkedModelSerializer):
    days = DaysField(source='*')
    likes_count = FollowersCountField(source='*')

    def create(self, validated_data):
        owners = validated_data.pop('owners')

        # set general information
        achievement = Achievement.objects.create(**validated_data)
        achievement.slug = str(achievement.id)
        achievement.owners.add(*owners)

        # adding an incident
        incident = Incident.objects.create()
        incident.save()
        achievement.incidents.add(incident)

        achievement.save()
        return achievement

    class Meta:
        model = Achievement
        fields = ['url', 'id', 'owners', 'slug', 'title', 'description', 'tags', 'category', 'days', 'likes',
                  'likes_count']
