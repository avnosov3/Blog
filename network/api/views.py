from blogs.models import Follow, Post, ReadStatus
from django.core.cache import cache
from django.db.models import F
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import filters, mixins, pagination, permissions, viewsets
from users.models import CustomUser

from . import constants, serializers


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def clear_cache_for_subscribers(self, blog):
        cache.delete_many([
            constants.FEED_CACHE_PATH.format(subscriber_id)
            for subscriber_id in blog.followers.values_list(
                'user_id', flat=True
            )
        ])

    def perform_create(self, serializer):
        super().perform_create(serializer)
        self.clear_cache_for_subscribers(serializer.instance.blog)

    def perform_destroy(self, instance):
        self.clear_cache_for_subscribers(instance.blog)
        super().perform_destroy(instance)


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
    pagination_class = pagination.PageNumberPagination

    # def get_queryset(self):
    #     user = get_object_or_404(CustomUser, pk=self.kwargs.get('user_id'))
    #     return Post.objects.filter(
    #         blog__followers__user=user
    #     )[:constants.FEED_LIMITS]

    def get_queryset(self):
        user = get_object_or_404(CustomUser, pk=self.kwargs.get('user_id'))
        cache_key = constants.FEED_CACHE_PATH.format(user.id)
        cached_queryset = cache.get(cache_key)
        if not cached_queryset:
            queryset = Post.objects.filter(
                blog__followers__user=user
            )[:constants.FEED_LIMITS]
            cache.set(cache_key, queryset, constants.CACHE_TIME)
            return queryset
        return cached_queryset


class ReadStatusViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    queryset = ReadStatus.objects.all()
    serializer_class = serializers.ReadStatusSerializer

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        user = get_object_or_404(CustomUser, pk=self.kwargs.get('user_id'))
        read_status, _ = ReadStatus.objects.get_or_create(reader=user, post=post)
        read_status.status = serializer.validated_data['status']
        read_status.save()
