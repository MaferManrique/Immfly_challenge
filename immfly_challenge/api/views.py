from rest_framework import viewsets
from .serializers import ChannelSerializer
from .models import Channel

class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
