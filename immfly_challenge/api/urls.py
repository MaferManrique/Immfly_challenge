from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'channels', views.ChannelViewSet, basename="channel")
router.register(r'content', views.ContentViewSet, basename="content")


urlpatterns = [path("", include(router.urls))]