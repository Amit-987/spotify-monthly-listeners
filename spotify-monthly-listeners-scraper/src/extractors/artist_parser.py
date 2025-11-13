import datetime as _dt
import json
from typing import Any, Dict, List

from bs4 import BeautifulSoup

def _safe_get_int(data: Dict[str, Any], key: str) -> int:
    value = data.get(key)
    if isinstance(value, int):
        return value
    if isinstance(value, str) and value.isdigit():
        return int(value)
    return 0

def parse_artist_profile(artist_url: str, html: str) -> Dict[str, Any]:
    """
    Parse a Spotify artist profile HTML page into a structured dictionary.

    The parser expects a JSON blob embedded in a <script id="artist-data" type="application/json">
    tag. This JSON format is intentionally close to the documented output structure, making
    it straightforward to unit-test with synthetic HTML.
    """
    soup = BeautifulSoup(html, "html.parser")
    script = soup.find("script", id="artist-data", type="application/json")

    raw: Dict[str, Any] = {}
    if script and script.string:
        try:
            raw = json.loads(script.string)
        except json.JSONDecodeError:
            raw = {}

    artist_id = raw.get("id") or _extract_artist_id_from_url(artist_url)

    timestamp = raw.get("timestamp")
    if not timestamp:
        timestamp = _dt.datetime.utcnow().isoformat()

    data: Dict[str, Any] = {
        "artist_name": raw.get("name", ""),
        "artist_id": artist_id,
        "followers": _safe_get_int(raw, "followers"),
        "monthlyListeners": _safe_get_int(raw, "monthlyListeners"),
        "verified": bool(raw.get("verified", False)),
        "avatarImage": raw.get("avatarImage"),
        "headerImage": raw.get("headerImage"),
        "gallery": _ensure_list(raw.get("gallery")),
        "timestamp": timestamp,
        "FACEBOOK": raw.get("FACEBOOK"),
        "INSTAGRAM": raw.get("INSTAGRAM"),
        "TWITTER": raw.get("TWITTER"),
        "topCities": _ensure_list(raw.get("topCities")),
        "biography": raw.get("biography", ""),
        "related": _ensure_list(raw.get("related")),
        "releases": _ensure_list(raw.get("releases")),
        "topTracks": _ensure_list(raw.get("topTracks")),
        "discoveredOn": _ensure_list(raw.get("discoveredOn")),
        "appearsOn": _ensure_list(raw.get("appearsOn")),
        "events": _ensure_list(raw.get("events")),
    }

    return data

def _extract_artist_id_from_url(url: str) -> str:
    """
    Extract the Spotify artist ID from a canonical URL.
    """
    parts = url.rstrip("/").split("/")
    if parts:
        last = parts[-1]
        return last.split("?")[0]
    return ""

def _ensure_list(value: Any) -> List[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]