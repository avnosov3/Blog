from django.urls import include, path
from rest_framework import routers

from . import views

router_v1 = routers.DefaultRouter()
router_v1.register(r'posts', views.PostViewSet, 'post')
router_v1.register(r'follow', views.FollowViewSet, basename='follow')
router_v1.register(
    r'feed/(?P<user_id>\d+)', views.FeedViewSet, basename='feed'
)
router_v1.register(
    r'feed/(?P<user_id>\d+)/status/(?P<post_id>\d+)',
    views.ReadStatusViewSet,
    basename='read_status'
)


urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
