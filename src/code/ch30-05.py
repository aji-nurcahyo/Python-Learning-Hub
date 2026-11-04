"""Chapter 30 Example 05: Capstone Thread-Safe Persistence Storage Engine
Python Learning Hub - Professional Capstone Project
"""

import threading
from typing import Any


class ThreadSafeTelemetryStorage:
    """Mesin penyimpanan in-memory thread-safe dengan snapshot indexing."""

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._records: dict[str, dict[str, Any]] = {}

    def upsert(self, key: str, data: dict[str, Any]) -> None:
        with self._lock:
            self._records[key] = data

    def count(self) -> int:
        with self._lock:
            return len(self._records)

    def get_all_keys(self) -> list[str]:
        with self._lock:
            return sorted(self._records.keys())


def main() -> None:
    print("Mendemonstrasikan Thread-Safe Persistence Engine (Capstone Layer 5):\n")
    storage = ThreadSafeTelemetryStorage()

    storage.upsert("BTS-01", {"rssi": -72.0, "vendor": "Huawei"})
    storage.upsert("BTS-02", {"rssi": -81.5, "vendor": "Ericsson"})
    storage.upsert("BTS-03", {"rssi": -94.0, "vendor": "Nokia"})

    print(f"Total entri tersimpan di storage: {storage.count()}")
    print(f"Indeks kunci aktif               : {storage.get_all_keys()}")


if __name__ == "__main__":
    main()

