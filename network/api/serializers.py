from blogs import models
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Post
        fields = ('title', 'text', 'pub_date', 'blog')
