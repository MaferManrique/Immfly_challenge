from django.core.management.base import BaseCommand
from immfly_challenge.api.models import Channel
import csv

def get_rating(channel: Channel, channel_averages: tuple[str, float]) :
    subchannels: list[Channel] = channel.subchannels.all()

    if subchannels:
        subchannels_ratings = [get_rating(subchannel, channel_averages) for subchannel in subchannels]
        subchannel_ratings_without_none = [rating for rating in subchannels_ratings if rating is not None]
        if len(subchannel_ratings_without_none) == 0:
            channel_averages.append((channel.title, None))
            return None
        else:
            subchannel_average = sum(subchannel_ratings_without_none)/ len(subchannel_ratings_without_none)
            channel_averages.append((channel.title, subchannel_average))
            return subchannel_average
    else:
        content_ratings = channel.content.values_list("rating", flat=True)
        if content_ratings:
            content_average = sum(content_ratings)/len(content_ratings)
            channel_averages.append((channel.title, content_average))
            return content_average
        else:
            channel_averages.append((channel.title, None))
            return None


class Command(BaseCommand):
    help = "Export a csv file with channels and their ratings"

    def handle(self, *args, **options):
        channels = Channel.objects.filter(parent_channel = None)
        channel_averages = []
        for channel in channels:
            get_rating(channel, channel_averages)

        sorted_average = sorted(channel_averages, key= lambda x: x[1] if x[1] else 0, reverse=True)

        with open("channel_average.csv", mode="w", newline="") as csv_file:
            fieldnames = ["Channel Title", "Average Rating"]
            writer = csv.writer(csv_file)
            writer.writerow(fieldnames)

            for channel_average in sorted_average:
                writer.writerow(channel_average)
        
        self.stdout.write("File with average created at channel_average.csv")


