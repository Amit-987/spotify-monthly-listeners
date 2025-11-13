import pathlib
import sys
from typing import Any, Dict, List

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC_DIR = ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.append(str(SRC_DIR))

from utils.flattening import flatten_artists  # noqa: E402

def _sample_artist() -> Dict[str, Any]:
    return {
        "artist_name": "Cruel Diagonals",
        "artist_id": "0C7jgMYmKXPmy5bHH5ebEN",
        "followers": 1670,
        "monthlyListeners": 3524,
        "verified": True,
        "timestamp": "2024-01-27T18:19:36.713298",
        "releases": [
            {
                "id": "4LLeRNBrcuwxj6QrhMmQ0K",
                "name": "Fractured Whole",
                "type": "ALBUM",
            }
        ],
        "topTracks": [
            {
                "id": "6IZrWKNy07OMGLKU24KJhQ",
                "name": "Innate Abstraction",
            }
        ],
        "discoveredOn": [
            {
                "id": "37i9dQZF1DX8OUvJF6ATAB",
                "name": "Exospheres",
            }
        ],
    }

def test_flatten_artists_core() -> None:
    artists: List[Dict[str, Any]] = [_sample_artist()]
    rows = flatten_artists(artists, mode="artists")
    assert len(rows) == 1
    row = rows[0]
    assert row["artist_id"] == "0C7jgMYmKXPmy5bHH5ebEN"
    assert "releases" not in row
    assert "topTracks" not in row

def test_flatten_releases_tracks_playlists() -> None:
    artists: List[Dict[str, Any]] = [_sample_artist()]

    releases_rows = flatten_artists(artists, mode="releases")
    assert len(releases_rows) == 1
    assert releases_rows[0]["artist_id"] == "0C7jgMYmKXPmy5bHH5ebEN"
    assert releases_rows[0]["name"] == "Fractured Whole"

    tracks_rows = flatten_artists(artists, mode="tracks")
    assert len(tracks_rows) == 1
    assert tracks_rows[0]["name"] == "Innate Abstraction"

    playlists_rows = flatten_artists(artists, mode="playlists")
    assert len(playlists_rows) == 1
    assert playlists_rows[0]["name"] == "Exospheres"