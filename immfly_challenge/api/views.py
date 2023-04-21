from rest_framework import viewsets
from .serializers import ChannelSerializer, ContentSerializer
from .models import Channel, Content

class ChannelViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ChannelSerializer

    def get_queryset(self):
        queryset = Channel.objects.prefetch_related("groups").all()
        group_id = self.request.query_params.get("group", None)
        if group_id:
            queryset = queryset.filter(groups__id=group_id)
        if self.action == "list":
            queryset = queryset.filter(parent_channel = None)
        return queryset

class ContentViewSet(viewsets.ReadOnlyModelViewSet):
     queryset = Content.objects.all()
     serializer_class = ContentSerializer