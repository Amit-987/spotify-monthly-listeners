import json
import pathlib
import sys
from typing import Any, Dict, List

import pytest  # type: ignore[import]

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC_DIR = ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.append(str(SRC_DIR))

import runner as runner_module  # noqa: E402

class DummyCrawler:
    """
    Lightweight stand-in for ArtistCrawler used to avoid external HTTP calls
    during integration tests.
    """

    def __init__(
        self,
        session: Any | None = None,
        max_depth: int = 0,
        max_artists: int = 100,
    ) -> None:
        self.session = session
        self.max_depth = max_depth
        self.max_artists = max_artists

    def crawl(self, artist_urls: List[str]) -> List[Dict[str, Any]]:
        return [
            {
                "artist_name": "Dummy Artist",
                "artist_id": "dummy-id",
                "followers": 100,
                "monthlyListeners": 500,
                "verified": False,
                "timestamp": "2024-01-01T00:00:00Z",
            }
        ]

def test_runner_integration(tmp_path: pathlib.Path) -> None:
    # Monkeypatch the ArtistCrawler used inside runner.
    runner_module.ArtistCrawler = DummyCrawler  # type: ignore[assignment]

    settings_path = tmp_path / "settings.json"
    output_dir = tmp_path / "output"
    settings = {
        "maxDepth": 0,
        "maxArtists": 10,
        "outputDir": str(output_dir),
        "flatten": "artists",
    }
    settings_path.write_text(json.dumps(settings), encoding="utf-8")

    input_path = tmp_path / "input.json"
    input_payload = {
        "startUrls": ["https://open.spotify.com/artist/dummy-id"],
        "maxDepth": 0,
        "maxArtists": 1,
        "flatten": "artists",
    }
    input_path.write_text(json.dumps(input_payload), encoding="utf-8")

    artists = runner_module.run(
        settings_path=str(settings_path), input_path=str(input_path)
    )

    assert len(artists) == 1
    assert artists[0]["artist_id"] == "dummy-id"

    json_output = output_dir / "artists.json"
    csv_output = output_dir / "artists_artists.csv"

    assert json_output.is_file()
    assert csv_output.is_file()

    # Validate JSON contents are decodable.
    content = json.loads(json_output.read_text(encoding="utf-8"))
    assert isinstance(content, list)
    assert content[0]["artist_name"] == "Dummy Artist"

spotify-monthly-listeners-scraper/Dockerfile
DockerfileFROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src
COPY configs ./configs
COPY data ./data

CMD ["python", "src/main.py"]