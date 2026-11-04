"""Chapter 29 Example 05: Structured Logging & Observability Basics
Python Learning Hub - Professional Python Engineering
"""

import json
import logging
import sys


class JsonLogFormatter(logging.Formatter):
    """Formatter kustom untuk menghasilkan log terstruktur dalam format JSON standar industri."""

    def format(self, record: logging.LogRecord) -> str:
        # Menggunakan timestamp simulasi statis demi determinisme pengujian
        log_payload = {
            "timestamp": "2026-11-04T12:00:00Z",
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        if record.exc_info:
            log_payload["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_payload)


def setup_observability_logger(name: str = "telecom.pipeline") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.handlers.clear()

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JsonLogFormatter())
    logger.addHandler(handler)
    return logger


def main() -> None:
    print("Mendemonstrasikan Pencatatan Log Terstruktur JSON untuk Observabilitas Cloud:")
    logger = setup_observability_logger()

    logger.info("Pipeline telemetri berhasil diinisialisasi")
    logger.warning("Batas ambang memori mendekati 80%")
    logger.error("Koneksi gateway node-03 timeout setelah 3000ms")


if __name__ == "__main__":
    main()
