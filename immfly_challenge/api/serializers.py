from rest_framework import serializers
from .models import Channel, Content, File, Metadata

class MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metadata
        fields = ("key", "value")

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ("type", "path")

class ContentSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True, read_only=True)
    metadata = MetadataSerializer(many=True, read_only=True)
    class Meta:
        model = Content
        fields = ("name", "files", "metadata")

class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    subchannels = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="channel-detail")
    content = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="content-detail")

    class Meta:
        model = Channel
        fields = ("title", "picture", "language", "subchannels", "content")




