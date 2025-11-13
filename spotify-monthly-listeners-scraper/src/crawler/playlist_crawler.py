from typing import Any, Dict, List

from extractors.playlists_parser import parse_playlists
from utils.logger import get_logger

from .session_manager import SessionManager

class PlaylistCrawler:
    """
    Crawler that focuses on playlist pages (e.g., discovery playlists).

    It is primarily used to support deeper catalog analysis if you want to
    explore playlists returned from artist discovery, but it can also be used
    standalone.
    """

    def __init__(self, session: SessionManager | None = None) -> None:
        self.session = session or SessionManager()
        self.logger = get_logger(self.__class__.__name__)

    def crawl_playlists(self, playlist_urls: List[str]) -> List[Dict[str, Any]]:
        playlists: List[Dict[str, Any]] = []

        for url in playlist_urls:
            self.logger.info("Fetching playlist page: %s", url)
            try:
                html = self.session.get_text(url)
                parsed = parse_playlists(html)
                playlists.extend(parsed)
            except Exception as exc:  # noqa: BLE001
                self.logger.error("Failed to parse playlist page %s: %s", url, exc)

        return playlists