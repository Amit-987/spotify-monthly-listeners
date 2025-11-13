import json
from typing import Any, Dict, List

from bs4 import BeautifulSoup

def parse_playlists(html: str) -> List[Dict[str, Any]]:
    """
    Parse playlists and discovery data from a playlist or discovery page.

    The parser looks for a JSON blob under <script id="playlists-data" type="application/json">
    with the shape: { "playlists": [ ... ] }.
    """
    soup = BeautifulSoup(html, "html.parser")
    script = soup.find("script", id="playlists-data", type="application/json")

    if not script or not script.string:
        return []

    try:
        raw = json.loads(script.string)
    except json.JSONDecodeError:
        return []

    playlists = raw.get("playlists") or []
    if not isinstance(playlists, list):
        return []

    return [p for p in playlists if isinstance(p, dict)]