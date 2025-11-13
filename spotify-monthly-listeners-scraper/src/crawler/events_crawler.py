from typing import Any, Dict, List

from extractors.cities_parser import parse_events
from utils.logger import get_logger

from .session_manager import SessionManager

class EventsCrawler:
    """
    Crawler responsible for collecting event and touring information.

    It can be used on dedicated event landing pages or URLs returned from the
    artist profile data.
    """

    def __init__(self, session: SessionManager | None = None) -> None:
        self.session = session or SessionManager()
        self.logger = get_logger(self.__class__.__name__)

    def crawl_events(self, event_urls: List[str]) -> List[Dict[str, Any]]:
        events: List[Dict[str, Any]] = []
        for url in event_urls:
            self.logger.info("Fetching events page: %s", url)
            try:
                html = self.session.get_text(url)
                parsed = parse_events(html)
                events.extend(parsed)
            except Exception as exc:  # noqa: BLE001
                self.logger.error("Failed to parse events page %s: %s", url, exc)
        return events