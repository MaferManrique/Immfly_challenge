from django.test import TestCase
from immfly_challenge.api.models import Channel
from immfly_challenge.api.management.commands.getratings import get_rating

class TestGetRating(TestCase):

    def test_subchannels_with_content(self):
        # Crea un Channel con dos subchannels y contenido para cada subchannel
        channel = Channel(title='channel 1')
        channel.save()
        subchannel1 = channel.subchannels.create(title="subchannel 1")
        subchannel1.save()
        subchannel2 = channel.subchannels.create(title="subchannel 2")
        subchannel2.save()
        subchannel1.content.create(rating=5)
        subchannel2.content.create(rating=7)

        channel_averages = []
        rating = get_rating(channel, channel_averages)
        self.assertEqual(rating, 6)