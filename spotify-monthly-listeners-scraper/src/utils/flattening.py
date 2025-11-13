from typing import Any, Dict, Iterable, List

def flatten_artists(artists: Iterable[Dict[str, Any]], mode: str = "artists") -> List[Dict[str, Any]]:
    """
    Convert nested artist dictionaries into row-based records for CSV export.

    Supported modes:
      - "artists": one row per artist (top-level scalar fields only).
      - "releases": one row per release with artist context.
      - "tracks": one row per top track with artist context.
      - "playlists": one row per discovery playlist with artist context.
    """
    mode = mode.lower()
    rows: List[Dict[str, Any]] = []

    for artist in artists:
        if mode == "artists":
            rows.append(_flatten_artist_core(artist))
        elif mode == "releases":
            rows.extend(_flatten_releases(artist))
        elif mode == "tracks":
            rows.extend(_flatten_tracks(artist))
        elif mode == "playlists":
            rows.extend(_flatten_playlists(artist))
        else:
            raise ValueError(f"Unsupported flatten mode: {mode}")

    return rows

def _flatten_artist_core(artist: Dict[str, Any]) -> Dict[str, Any]:
    """
    Flatten only scalar top-level fields for an artist.
    """
    core: Dict[str, Any] = {}
    for key, value in artist.items():
        if isinstance(value, (list, dict)):
            continue
        core[key] = value
    return core

def _flatten_releases(artist: Dict[str, Any]) -> List[Dict[str, Any]]:
    releases = artist.get("releases") or []
    rows: List[Dict[str, Any]] = []
    for release in releases:
        if not isinstance(release, dict):
            continue
        row: Dict[str, Any] = {
            "artist_id": artist.get("artist_id"),
            "artist_name": artist.get("artist_name"),
        }
        row.update(release)
        rows.append(row)
    return rows

def _flatten_tracks(artist: Dict[str, Any]) -> List[Dict[str, Any]]:
    tracks = artist.get("topTracks") or []
    rows: List[Dict[str, Any]] = []
    for track in tracks:
        if not isinstance(track, dict):
            continue
        row: Dict[str, Any] = {
            "artist_id": artist.get("artist_id"),
            "artist_name": artist.get("artist_name"),
        }
        row.update(track)
        rows.append(row)
    return rows

def _flatten_playlists(artist: Dict[str, Any]) -> List[Dict[str, Any]]:
    playlists = artist.get("discoveredOn") or []
    rows: List[Dict[str, Any]] = []
    for playlist in playlists:
        if not isinstance(playlist, dict):
            continue
        row: Dict[str, Any] = {
            "artist_id": artist.get("artist_id"),
            "artist_name": artist.get("artist_name"),
        }
        row.update(playlist)
        rows.append(row)
    return rows