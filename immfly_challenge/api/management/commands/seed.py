from django.core.management.base import BaseCommand
from immfly_challenge.api.models import Channel, Group
from random import choice, uniform

DESCRIPTION_PLACEHOLDER = "This is a placeholder description for a content of this project"
IMAGES_PLACEHOLDER = [
    "https://i0.wp.com/litdarlings.com/wp-content/uploads/2022/06/Kdramaswithlessthan16episodes-scaled.webp?fit=2560%2C2560&ssl=1",
    "https://e00-marca.uecdn.es/assets/multimedia/imagenes/2020/02/10/15813555323272.jpg",
    "https://i.blogs.es/4755f7/accion/1366_2000.jpeg"
]
CONTENT_TITLE_PLACEHOLDERS = ["Love Story",  "Bad Blood", "Matilda"]

def create_channel(title):
    channel = Channel(title=title, picture=choice(IMAGES_PLACEHOLDER), language="English")
    channel.save()
    return channel

def create_subchannel(parent_channel, title):
    subchannel = parent_channel.subchannels.create(title=title, picture=choice(IMAGES_PLACEHOLDER), language="English")
    subchannel.save()
    return subchannel

def create_content(channel):
    content = channel.content.create(name=choice(CONTENT_TITLE_PLACEHOLDERS), rating = uniform(0,10))
    content.save()
    content.files.create(type="video", path=choice(IMAGES_PLACEHOLDER)).save()
    content.files.create(type="audio_en", path=choice(IMAGES_PLACEHOLDER)).save()
    content.files.create(type="audio_es", path=choice(IMAGES_PLACEHOLDER)).save()
    content.metadata.create(key="duration", value="1000").save()
    content.metadata.create(key="author", value="Mafer").save()
    content.metadata.create(key="description", value=DESCRIPTION_PLACEHOLDER)


class Command(BaseCommand):
    help = "Seed database for testing"

    def handle(self, *args, **options):
        #Delete all data
        Channel.objects.all().delete()
        Group.objects.all().delete()

        
        #we create new test data
        main_channels_title = ["Drama", "Romance", "Sports", "Action", "Kdrama"]
        for channel in main_channels_title:
            # we create a test group
            group = Group(name = "test_group")
            group.save()
            new_channel = create_channel(channel)
            group.channels.add(new_channel)
            group.save()
            new_subchannel_titles = ["Last Dance", "Matilda", "Pasapalabra"]
            for subchannel_title in new_subchannel_titles:
                subchannel = create_subchannel(new_channel, subchannel_title)
                group.channels.add(subchannel)
                group.save()
                create_content(subchannel)
        self.stdout.write("Seed data succesfully created")






