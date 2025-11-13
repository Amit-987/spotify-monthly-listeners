from typing import Any, Dict, Optional

import requests

from utils.logger import get_logger

class SessionManager:
    """
    Thin wrapper around requests.Session that centralises HTTP configuration.
    """

    def __init__(self, user_agent: Optional[str] = None, timeout: int = 10) -> None:
        self.logger = get_logger(self.__class__.__name__)
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": user_agent
                or (
                    "Mozilla/5.0 (X11; Linux x86_64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/120.0 Safari/537.36"
                ),
                "Accept-Language": "en-US,en;q=0.9",
            }
        )
        self.timeout = timeout

    def get_text(self, url: str, params: Optional[Dict[str, Any]] = None) -> str:
        self.logger.debug("GET %s", url)
        try:
            response = self.session.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            return response.text
        except requests.RequestException as exc:  # noqa: PERF203
            self.logger.error("HTTP error while fetching %s: %s", url, exc)
            raise

    def get_json(self, url: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        text = self.get_text(url, params=params)
        try:
            return response_json(text)  # type: ignore[name-defined]
        except NameError:
            # Fallback if helper is not defined; use requests' json method.
            # This code path will normally not be hit, but keeps the method safe.
            self.logger.debug("Falling back to requests' JSON parsing.")
            response = self.session.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            return response.json()

def response_json(text: str) -> Dict[str, Any]:
    """
    Separate helper for JSON parsing so it can be swapped or tested in isolation.
    """
    import json

    return json.loads(text)