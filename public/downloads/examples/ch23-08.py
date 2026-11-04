"""Chapter 23 Example 08: Refactoring Coupled Design
Python Learning Hub - Professional Python Engineering
"""

from abc import ABC, abstractmethod


class StorageBackend(ABC):
    @abstractmethod
    def save(self, record: str) -> None:
        pass


class InMemoryStorage(StorageBackend):
    def __init__(self) -> None:
        self.records: list[str] = []

    def save(self, record: str) -> None:
        self.records.append(record)


class DeviceAuditor:
    """Auditor yang fleksibel karena bergantung pada abstraksi StorageBackend."""

    def __init__(self, backend: StorageBackend) -> None:
        self.backend = backend

    def record_audit(self, device_id: str, action: str) -> None:
        entry = f"AUDIT: {device_id} -> {action}"
        self.backend.save(entry)


def main() -> None:
    storage = InMemoryStorage()
    auditor = DeviceAuditor(storage)

    auditor.record_audit("SW-01", "Port 4 rebooted")
    auditor.record_audit("RTR-02", "BGP session established")

    print(f"Total tersimpan: {len(storage.records)} catatan")
    for rec in storage.records:
        print(f" - {rec}")


if __name__ == "__main__":
    main()
