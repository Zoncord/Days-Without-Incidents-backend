from rest_framework import serializers

from achievements.models import Achievement, Incident, Category, Tag
from blog.errors import NotTheOwnerOfTheAchievement


class AchievementSerializer(serializers.HyperlinkedModelSerializer):
    slug = serializers.CharField(required=False)
    owners = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='user-detail')

    def create(self, validated_data):
        request = self.context.get('request', None)
        tags = validated_data.pop('tags', set())

        # set general information
        achievement = Achievement.objects.create(**validated_data)
        achievement.slug = str(achievement.id)
        achievement.owners.add(request.user)
        achievement.tags.set(tags)

        # adding an incident
        incident = Incident.objects.create(achievement=achievement)
        incident.save()

        achievement.save()
        return achievement

    class Meta:
        model = Achievement
        fields = ['url', 'id', 'owners', 'title', 'slug', 'description', 'tags', 'category',
                  'days_since_the_last_incident', 'likes_count']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        category = Category.objects.get_or_create(title=validated_data.pop('title'))[0]
        return category

    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.HyperlinkedModelSerializer):
    slug = serializers.ReadOnlyField()
    description = serializers.ReadOnlyField()

    def create(self, validated_data):
        tag, created = Tag.objects.get_or_create(title=validated_data.pop('title'))
        if created:
            slug = str(tag.id)
        return tag

    class Meta:
        model = Tag
        fields = '__all__'


class IncidentSerializer(serializers.HyperlinkedModelSerializer):
    date_time = serializers.ReadOnlyField()

    def create(self, validated_data):
        request = self.context.get('request', None)
        achievement = validated_data.pop('achievement')
        achievement = Achievement.objects.get(id=achievement.id)
        if request.user not in achievement.owners.all():
            raise NotTheOwnerOfTheAchievement()

        incident = Incident.objects.create(achievement=achievement)
        return incident

    class Meta:
        model = Incident
        fields = '__all__'
