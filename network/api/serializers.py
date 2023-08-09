from blogs.models import Follow, Post, ReadStatus
from rest_framework import serializers
from users.models import CustomUser

from . import constants


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('pk', 'title', 'text', 'pub_date', 'blog')


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        queryset=CustomUser.objects.all(),
        # default=serializers.CurrentUserDefault(),
    )
    blog = serializers.StringRelatedField()

    class Meta:
        model = Follow
        fields = ('user', 'blog')
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'blog'),
                message=constants.SUBSCRIBE_EXISTS
            ),
        ]

    def validate_blog(self, value):
        if self.initial_data.get('user') == value.author_id:
            raise serializers.ValidationError(
                constants.SUBSCRIBE_SELF
            )
        return value


class ReadStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReadStatus
        fields = ('status',)
