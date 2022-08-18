from django.core.management.base import BaseCommand
import feedparser
from dateutil import parser
from podcasts.models import Episode


def save_new_episodes(feed):

    podcast_title = feed.channel.title
    podcast_image = feed.channel.image['href']

    for item in feed.entries:

        if not Episode.objects.filter(guid=item.guid).exists():

            episode = Episode(
                title=item.title,
                description=item.description,
                pub_date=parser.parse(item.published),
                link=item.link,
                image=podcast_image,
                podcast_name=podcast_title,
                guid=item.guid
            )
            episode.save()

def fetch_realpython_episodes():
    feed = feedparser.parse("https://realpython.com/podcasts/rpp/feed")
    save_new_episodes(feed)


def fetch_talkpython_episodes():

    feed = feedparser.parse("https://talkpython.fm/episodes/rss")
    save_new_episodes(feed)

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        fetch_realpython_episodes()
        fetch_talkpython_episodes()