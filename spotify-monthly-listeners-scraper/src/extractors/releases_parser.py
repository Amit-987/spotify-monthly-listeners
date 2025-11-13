import json
from typing import Any, Dict, List

from bs4 import BeautifulSoup

def parse_releases(html: str) -> List[Dict[str, Any]]:
    """
    Parse release metadata (albums, singles, compilations) from HTML.

    Expects a JSON blob under <script id="releases-data" type="application/json">
    with shape: { "releases": [ ... ] }.
    """
    soup = BeautifulSoup(html, "html.parser")
    script = soup.find("script", id="releases-data", type="application/json")

    if not script or not script.string:
        return []

    try:
        raw = json.loads(script.string)
    except json.JSONDecodeError:
        return []

    releases = raw.get("releases") or []
    if not isinstance(releases, list):
        return []

    return [r for r in releases if isinstance(r, dict)]