from rest_framework import serializers
from rest_framework.authtoken.models import Token

from achievements.models import Achievement, Incident
from users.services import get_user_data
from users.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    user_data = get_user_data('123')
    # first_name = serializers.HiddenField(default=user_data['first_name'])
    # user_last_name = serializers.ReadOnlyField(default=user_data['last_name'])

    class Meta:
        model = User
        fields = ['url', 'id', 'first_name', 'last_name', 'description', 'followers_count',
                  'achievement_rating']


class ProfileSerializer(serializers.Serializer):
    user_data = get_user_data('123')
    id = serializers.IntegerField()
    user_first_name = serializers.ReadOnlyField(default='Yaroslav') #user_data['first_name'])
    user_last_name = serializers.ReadOnlyField(default='Filippw',) #user_data['last_name'])
    description = serializers.CharField(default='123')
    image = serializers.CharField(
        default='https://ic.pics.livejournal.com/instaforex_ru/25000283/168859/168859_900.jpg')
    count_followers = serializers.IntegerField(default=132)
    # token = serializers.CharField(default=Token.objects.get_or_create(user_id=2)[0])
