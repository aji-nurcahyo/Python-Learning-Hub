"""Konfigurasi Structured Logging (Chapter 26)
Python Learning Hub - Professional Python Engineering
"""

import io
import logging
from typing import TextIO


def configure_service_logger(
    name: str = "telecom.service",
    level: int = logging.INFO,
    stream: TextIO | None = None,
) -> logging.Logger:
    """Mengonfigurasi logger terstruktur dengan stream handler dan format terstandar."""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.handlers.clear()

    target_stream = stream if stream is not None else io.StringIO()
    handler = logging.StreamHandler(target_stream)
    formatter = logging.Formatter("[%(levelname)s] [%(name)s] %(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.propagate = False
    return logger

