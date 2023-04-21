from django.test import TestCase
from immfly_challenge.api.models import Channel
from immfly_challenge.api.management.commands.getratings import get_rating

class TestGetRating(TestCase):

    def test_subchannels_with_content(self):
        # Crea un Channel con dos subchannels y contenido para cada subchannel
        channel = Channel(title = "channel 1")
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

    
    def test_subchannels_without_content(self):
        channel = Channel(title = "channel 1")
        channel.save()
        subchannel1 = channel.subchannels.create(title = "subchannel 1")
        subchannel1.save()
        subchannel2 = channel.subchannels.create(title = "subchannel 2")
        subchannel2.save()

        channel_average = []
        rating = get_rating(channel, channel_average)
        self.assertIsNone(rating)


    def test_channel_with_multiple_content(self):
        channel = Channel(title = "channel 1")
        channel.save()
        channel.content.create(rating=4)
        channel.content.create(rating=3)
        channel.content.create(rating=2)

        channel_averages = []
        rating = get_rating(channel, channel_averages)
        self.assertEqual(rating, 3)

    def test_no_subchannels_no_content(self):
        channel = Channel(title = "channel 1")
        channel.save()
        channel_average = []
        rating = get_rating(channel, channel_average)
        self.assertIsNone(rating)