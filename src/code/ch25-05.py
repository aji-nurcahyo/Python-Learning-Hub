"""Chapter 25 Example 05: Generics with TypeVar and Generic[T]
Python Learning Hub - Professional Python Engineering
"""

from typing import Generic, TypeVar

T = TypeVar("T")


class TelemetryRepository(Generic[T]):
    """Wadah repositori generic yang aman tipe untuk menyimpan elemen tipe T."""

    def __init__(self) -> None:
        self._items: list[T] = []

    def add(self, item: T) -> None:
        self._items.append(item)

    def get_latest(self) -> T | None:
        return self._items[-1] if self._items else None

    def count(self) -> int:
        return len(self._items)


def main() -> None:
    # Repositori khusus string
    event_repo: TelemetryRepository[str] = TelemetryRepository()
    event_repo.add("BOOT_COMPLETE")
    event_repo.add("SYNC_SUCCESS")
    print(f"Total events: {event_repo.count()}, Terakhir: {event_repo.get_latest()}")

    # Repositori khusus float
    metric_repo: TelemetryRepository[float] = TelemetryRepository()
    metric_repo.add(-88.5)
    metric_repo.add(-82.1)
    print(f"Total metrics: {metric_repo.count()}, Terakhir: {metric_repo.get_latest()}")


if __name__ == "__main__":
    main()

