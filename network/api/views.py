from blogs import models
from rest_framework import filters, permissions, viewsets

from . import serializers


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
