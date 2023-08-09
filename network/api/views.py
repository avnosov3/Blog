from blogs.models import Follow, Post
from django.db.models import F
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import filters, mixins, permissions, viewsets
from users.models import CustomUser

from . import serializers


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class FollowViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Follow.objects.all()
    serializer_class = serializers.FollowSerializer


class FeedViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = serializers.PostSerializer

    def get_queryset(self):
        user = get_object_or_404(CustomUser, pk=self.kwargs.get('user_id'))
        return Post.objects.filter(blog__followers__user=user)
