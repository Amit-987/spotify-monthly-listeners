"""
Crawler package responsible for fetching Spotify artist, playlist, and event data.
"""

from .artist_crawler import ArtistCrawler
from .playlist_crawler import PlaylistCrawler
from .events_crawler import EventsCrawler

__all__ = ["ArtistCrawler", "PlaylistCrawler", "EventsCrawler"]