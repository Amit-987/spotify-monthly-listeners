from typing import Any, Dict, List, Set, Tuple

from extractors.artist_parser import parse_artist_profile
from utils.logger import get_logger

from .session_manager import SessionManager

class ArtistCrawler:
    """
    High-level crawler that fetches and parses Spotify artist pages.

    It starts from one or more artist profile URLs and optionally recurses into
    related artists up to a given depth.
    """

    def __init__(
        self,
        session: SessionManager | None = None,
        max_depth: int = 0,
        max_artists: int = 100,
    ) -> None:
        self.session = session or SessionManager()
        self.max_depth = max_depth
        self.max_artists = max_artists
        self.logger = get_logger(self.__class__.__name__)

    def crawl(self, artist_urls: List[str]) -> List[Dict[str, Any]]:
        """
        Crawl a list of artist URLs and return a list of parsed artist dictionaries.
        """
        results: List[Dict[str, Any]] = []
        visited_ids: Set[str] = set()
        queue: List[Tuple[str, int]] = [(url, 0) for url in artist_urls]

        while queue and len(results) < self.max_artists:
            url, depth = queue.pop(0)
            self.logger.info("Fetching artist page: %s (depth=%s)", url, depth)

            try:
                html = self.session.get_text(url)
                artist_data = parse_artist_profile(url, html)
                artist_id = artist_data.get("artist_id")

                if not artist_id:
                    self.logger.warning("Could not determine artist_id for %s", url)
                    continue

                if artist_id in visited_ids:
                    self.logger.debug("Already visited artist %s, skipping.", artist_id)
                    continue

                visited_ids.add(artist_id)
                results.append(artist_data)

                if depth < self.max_depth:
                    related = artist_data.get("related") or []
                    for rel in related:
                        rel_id = rel.get("id")
                        if not rel_id or rel_id in visited_ids:
                            continue
                        related_url = f"https://open.spotify.com/artist/{rel_id}"
                        queue.append((related_url, depth + 1))
                        self.logger.debug(
                            "Queued related artist %s at depth %s", rel_id, depth + 1
                        )

            except Exception as exc:  # noqa: BLE001
                self.logger.error("Failed to process %s: %s", url, exc)

        return results