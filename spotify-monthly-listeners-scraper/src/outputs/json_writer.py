import json
from pathlib import Path
from typing import Any, Iterable, List

def write_json(data: Iterable[Any], path: Path | str) -> None:
    """
    Write a list of Python objects to a JSON file with UTF-8 encoding.
    """
    out_path = Path(path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    # Ensure we materialise the iterable before dumping.
    materialised: List[Any] = list(data)

    with out_path.open("w", encoding="utf-8") as fh:
        json.dump(materialised, fh, ensure_ascii=False, indent=2)