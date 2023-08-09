from django.urls import include, path
from rest_framework import routers

from . import views

router_v1 = routers.DefaultRouter()
router_v1.register(r'posts', views.PostViewSet, 'post')
router_v1.register(r'follow', views.FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
