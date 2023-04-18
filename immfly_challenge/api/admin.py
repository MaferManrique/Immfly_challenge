from django.contrib import admin
from .models import Channel, Content, File, Metadata

admin.site.register(Channel)
admin.site.register(Content)
admin.site.register(File)
admin.site.register(Metadata)