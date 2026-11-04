"""Chapter 30: Professional Capstone Project
Storage Layer: Penyimpanan Lokal Thread-Safe dengan Snapshot Indexing
"""

import threading
from typing import Optional

try:
    from platform_models import TelemetryRecord
except ImportError:
    from .platform_models import TelemetryRecord


class LocalTelemetryStorage:
    """Mesin penyimpanan data teragregasi yang thread-safe menggunakan threading.Lock."""

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._storage: dict[str, TelemetryRecord] = {}

    def save(self, record: TelemetryRecord) -> None:
        with self._lock:
            self._storage[record.device_id] = record

    def save_batch(self, records: list[TelemetryRecord]) -> int:
        with self._lock:
            for rec in records:
                self._storage[rec.device_id] = rec
            return len(records)

    def get_by_id(self, device_id: str) -> Optional[TelemetryRecord]:
        with self._lock:
            return self._storage.get(device_id)

    def get_all(self) -> list[TelemetryRecord]:
        with self._lock:
            return list(self._storage.values())

    def count(self) -> int:
        with self._lock:
            return len(self._storage)

