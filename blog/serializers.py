from rest_framework import serializers

from achievements.models import Achievement
from blog.errors import NotTheOwnerOfTheAchievement
from blog.models import Post, Comment


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(read_only=True, view_name='user-detail')
    slug = serializers.ReadOnlyField()

    def create(self, validated_data):
        request = self.context.get('request', None)
        achievement = validated_data.pop('achievement')
        if request.user not in achievement.owners.all():
            raise NotTheOwnerOfTheAchievement()

        Achievement.objects.get(id=achievement.id)

        # set general information
        post = Post.objects.create(author=request.user, achievement=achievement, **validated_data)
        post.slug = str(post.id)
        post.owner = request.user
        post.save()

        return post

    class Meta:
        model = Post
        fields = ['url', 'id', 'author', 'achievement', 'slug', 'title', 'description', 'date_time_of_creation',
                  'likes_count']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(read_only=True, view_name='user-detail')
    answers = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='comment-detail')
    date_time_of_creation = serializers.ReadOnlyField()

    def create(self, validated_data):
        request = self.context.get('request', None)
        comment = validated_data.pop('comment', None)
        if comment is None:
            return Comment.objects.create(author=request.user, **validated_data)
        else:
            _ = validated_data.pop('post', None)
            return Comment.objects.create(author=request.user, post=comment.post, **validated_data)

    class Meta:
        model = Comment
        fields = ['url', 'id', 'author', 'parent_comment', 'answers', 'text', 'post', 'date_time_of_creation']
