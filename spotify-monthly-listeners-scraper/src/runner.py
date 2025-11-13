from pathlib import Path
from typing import Any, Dict, List, Optional

from crawler.artist_crawler import ArtistCrawler
from outputs.csv_exporter import export_csv
from outputs.json_writer import write_json
from utils.config_loader import load_input, load_settings
from utils.logger import get_logger

def run(
    settings_path: Optional[str] = None, input_path: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    Main orchestration function used by CLI, tests, and Docker entrypoint.
    """
    logger = get_logger(__name__)

    settings = load_settings(settings_path)
    user_input = load_input(input_path)

    start_urls = user_input.get("startUrls") or []
    if not start_urls:
        raise ValueError("No 'startUrls' provided in input configuration.")

    max_depth = int(user_input.get("maxDepth", settings.get("maxDepth", 0)))
    max_artists = int(user_input.get("maxArtists", settings.get("maxArtists", 100)))
    flatten_mode = user_input.get("flatten") or settings.get("flatten")
    output_dir = Path(settings.get("outputDir", "data"))
    output_dir.mkdir(parents=True, exist_ok=True)

    logger.info(
        "Starting crawl for %d artist URLs (max_depth=%s, max_artists=%s)",
        len(start_urls),
        max_depth,
        max_artists,
    )

    crawler = ArtistCrawler(max_depth=max_depth, max_artists=max_artists)
    artists = crawler.crawl(start_urls)

    json_path = output_dir / "artists.json"
    write_json(artists, json_path)
    logger.info("Wrote JSON output to %s", json_path)

    if flatten_mode:
        csv_path = output_dir / f"artists_{flatten_mode}.csv"
        export_csv(artists, csv_path, mode=flatten_mode)
        logger.info("Wrote flattened CSV (%s mode) to %s", flatten_mode, csv_path)
    else:
        logger.info("No flatten mode configured, skipping CSV export.")

    logger.info("Crawling complete. Processed %d artists.", len(artists))
    return artists