import json
from pathlib import Path
from typing import Any, Dict, Optional

from .logger import get_logger

BASE_DIR = Path(__file__).resolve().parents[2]
logger = get_logger(__name__)

def _load_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)

def load_settings(path: Optional[str] = None) -> Dict[str, Any]:
    """