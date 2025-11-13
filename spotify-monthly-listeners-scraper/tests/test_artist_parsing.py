import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC_DIR = ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.append(str(SRC_DIR))

from extractors.artist_parser import parse_artist_profile  # noqa: E402

def test_parse_artist_profile_basic() -> None:
    artist_json = {
        "name": "Cruel Diagonals",
        "id": "0C7jgMYmKXPmy5bHH5ebEN",
        "followers": 1670,
        "monthlyListeners": 3524,
        "verified": True,
        "FACEBOOK": "https://facebook.com/crueldiagonals/",
        "INSTAGRAM": "https://instagram.com/crueldiagonals",
        "TWITTER": "https://twitter.com/crueldiagonals",
        "topCities": [
            {
                "numberOfListeners": 57,
                "city": "Warsaw",
                "country": "PL",
                "region": "14",
            }
        ],
    }

    html = f"""
    <html>
      <body>
        <script id="artist-data" type="application/json">
        {json.dumps(artist_json)}
        </script>
      </body>
    </html>
    """

    url = "https://open.spotify.com/artist/0C7jgMYmKXPmy5bHH5ebEN"
    data = parse_artist_profile(url, html)

    assert data["artist_name"] == "Cruel Diagonals"
    assert data["artist_id"] == "0C7jgMYmKXPmy5bHH5ebEN"
    assert data["monthlyListeners"] == 3524
    assert data["followers"] == 1670
    assert data["verified"] is True
    assert data["topCities"][0]["city"] == "Warsaw"
    assert data["FACEBOOK"].startswith("https://facebook.com/")