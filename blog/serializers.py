from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['url', 'id', 'author', 'achievement', 'slug', 'title', 'description', 'date_time_of_creation']
