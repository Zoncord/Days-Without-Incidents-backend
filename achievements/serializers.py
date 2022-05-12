from rest_framework import serializers

from achievements.models import Achievement, Incident, Category, Tag


class AchievementSerializer(serializers.HyperlinkedModelSerializer):
    slug = serializers.CharField(required=False)

    def create(self, validated_data):
        request = self.context.get('request', None)
        tags = validated_data.pop('tags')

        # set general information
        achievement = Achievement.objects.create(**validated_data)
        achievement.slug = str(achievement.id)
        achievement.owners.add(request.user)
        achievement.tags.set(tags)

        # adding an incident
        incident = Incident.objects.create()
        incident.save()
        achievement.incidents.add(incident)

        achievement.save()
        return achievement

    class Meta:
        model = Achievement
        fields = ['url', 'id', 'title', 'slug', 'description', 'tags', 'category',
                  'days_since_the_last_incident', 'likes_count']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
