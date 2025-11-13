import logging
from logging import Logger
from typing import Optional

def get_logger(name: Optional[str] = None) -> Logger:
    """
    Create or retrieve a named logger with a consistent formatting style.
    """
    logger_name = name or "spotify_monthly_listeners_scraper"
    logger = logging.getLogger(logger_name)

    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger