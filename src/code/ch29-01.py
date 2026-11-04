"""Chapter 29 Example 01: Modular Project Architecture & Separation of Concerns
Python Learning Hub - Professional Python Engineering
"""

from dataclasses import dataclass
from typing import Protocol


# 1. Domain Layer: Representasi entitas bisnis murni nir-dependensi
@dataclass(frozen=True)
class NetworkDevice:
    device_id: str
    hostname: str
    ip_address: str
    is_active: bool


# 2. Port / Interface: Kontrak abstraksi data access
class DeviceRepository(Protocol):
    def get_by_id(self, device_id: str) -> NetworkDevice | None:
        ...


# 3. Infrastructure Layer: Implementasi konkret in-memory repository
class InMemoryDeviceRepository:
    def __init__(self) -> None:
        self._storage: dict[str, NetworkDevice] = {
            "DEV-01": NetworkDevice("DEV-01", "gw-core-lampung", "10.10.1.1", True),
            "DEV-02": NetworkDevice("DEV-02", "bts-utara-02", "10.10.2.1", False),
        }

    def get_by_id(self, device_id: str) -> NetworkDevice | None:
        return self._storage.get(device_id)


# 4. Service / Application Layer: Logika orkestrasi bisnis
class DeviceService:
    def __init__(self, repository: DeviceRepository) -> None:
        self.repository = repository

    def check_health(self, device_id: str) -> str:
        device = self.repository.get_by_id(device_id)
        if not device:
            return f"Status: Perangkat {device_id} tidak ditemukan"
        status = "AKTIF" if device.is_active else "NONAKTIF / MAINTENANCE"
        return f"Perangkat: {device.hostname} ({device.ip_address}) -> Status: {status}"


def main() -> None:
    print("Mendemonstrasikan Pemisahan Layer Arsitektur Perangkat Lunak:")
    repo = InMemoryDeviceRepository()
    service = DeviceService(repository=repo)

    print(" ->", service.check_health("DEV-01"))
    print(" ->", service.check_health("DEV-02"))
    print(" ->", service.check_health("DEV-99"))


if __name__ == "__main__":
    main()

