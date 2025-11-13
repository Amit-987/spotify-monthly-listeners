import json
from typing import Any, Dict, List

from bs4 import BeautifulSoup

def parse_top_cities(html: str) -> List[Dict[str, Any]]:
    """
    Parse top listener cities from HTML.

    Expects a JSON blob under <script id="cities-data" type="application/json">
    with shape: { "topCities": [ ... ] }.
    """
    soup = BeautifulSoup(html, "html.parser")
    script = soup.find("script", id="cities-data", type="application/json")

    if not script or not script.string:
        return []

    try:
        raw = json.loads(script.string)
    except json.JSONDecodeError:
        return []

    top_cities = raw.get("topCities") or []
    if not isinstance(top_cities, list):
        return []

    return [c for c in top_cities if isinstance(c, dict)]

def parse_events(html: str) -> List[Dict[str, Any]]:
    """
    Parse upcoming events from HTML.

    Expects a JSON blob under <script id="events-data" type="application/json">
    with shape: { "events": [ ... ] }.
    """
    soup = BeautifulSoup(html, "html.parser")
    script = soup.find("script", id="events-data", type="application/json")

    if not script or not script.string:
        return []

    try:
        raw = json.loads(script.string)
    except json.JSONDecodeError:
        return []

    events = raw.get("events") or []
    if not isinstance(events, list):
        return []

    return [e for e in events if isinstance(e, dict)]