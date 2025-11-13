import argparse
from runner import run

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Spotify Monthly Listeners Scraper - CLI entrypoint"
    )
    parser.add_argument(
        "--settings",
        dest="settings_path",
        type=str,
        default=None,
        help="Path to settings JSON file (defaults to configs/settings.json or settings.example.json).",
    )
    parser.add_argument(
        "--input",
        dest="input_path",
        type=str,
        default=None,
        help="Path to input JSON file (defaults to configs/input.json or input.example.json).",
    )
    args = parser.parse_args()

    run(settings_path=args.settings_path, input_path=args.input_path)

if __name__ == "__main__":
    main()