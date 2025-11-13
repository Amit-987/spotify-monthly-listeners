import csv
from pathlib import Path
from typing import Any, Dict, Iterable, List

from utils.flattening import flatten_artists

def export_csv(
    artists: Iterable[Dict[str, Any]], path: Path | str, mode: str = "artists"
) -> None:
    """
    Export artists to CSV using a given flattening mode.
    """
    rows: List[Dict[str, Any]] = flatten_artists(artists, mode=mode)
    if not rows:
        out_path = Path(path)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        # Create an empty file to indicate that export ran.
        out_path.touch()
        return

    # Collect all keys across rows to build a stable header.
    fieldnames: List[str] = []
    for row in rows:
        for key in row.keys():
            if key not in fieldnames:
                fieldnames.append(key)

    out_path = Path(path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with out_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)