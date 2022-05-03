from rest_framework import serializers
from rest_framework.authtoken.models import Token

from achievements.models import Achievement, Incident
from users.services import get_user_data
from users.models import User


class FollowersCountField(serializers.ReadOnlyField):
    def to_representation(self, value):
        return value.followed_users.count()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    user_data = get_user_data('123')
    user_first_name = serializers.ReadOnlyField(default=user_data['first_name'])
    user_last_name = serializers.ReadOnlyField(default=user_data['last_name'])
    followers_count = FollowersCountField(source='*')

    class Meta:
        model = User
        fields = ['url', 'id', 'user_first_name', 'user_last_name', 'description', 'followers_count',
                  'achievement_likes']


class ProfileSerializer(serializers.Serializer):
    user_data = get_user_data('123')
    id = serializers.IntegerField()
    user_first_name = serializers.ReadOnlyField(default=user_data['first_name'])
    user_last_name = serializers.ReadOnlyField(default=user_data['last_name'])
    description = serializers.CharField(default='123')
    image = serializers.CharField(
        default='https://ic.pics.livejournal.com/instaforex_ru/25000283/168859/168859_900.jpg')
    count_followers = serializers.IntegerField(default=132)
    token = serializers.CharField(default=Token.objects.get_or_create(user_id=1)[0])
