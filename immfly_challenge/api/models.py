from django.db import models

class Channel(models.Model):
    title = models.CharField(max_length=100)
    picture = models.URLField()
    language = models.CharField(max_length=50)
    parent_channel = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

class Content(models.Model):
    name = models.CharField(max_length=100)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)

class File(models.Model):
    type = models.CharField(max_length=100)
    path = models.URLField()
    content = models.ForeignKey(Content, on_delete=models.CASCADE)

class Metadata(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)

