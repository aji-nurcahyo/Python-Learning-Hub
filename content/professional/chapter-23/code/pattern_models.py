"""Model Domain Perangkat Jaringan (Chapter 23)
Python Learning Hub - Professional Python Engineering
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class DeviceMetadata:
    """Metadata perangkat jaringan menggunakan immutable dataclass."""

    device_id: str
    model: str
    firmware_version: str
    max_bandwidth_mbps: float


class AbstractDevice(ABC):
    """Antarmuka dasar abstrak untuk semua perangkat jaringan."""

    def __init__(self, metadata: DeviceMetadata) -> None:
        self.metadata = metadata
        self._is_online: bool = False

    @property
    def is_online(self) -> bool:
        return self._is_online

    @is_online.setter
    def is_online(self, state: bool) -> None:
        self._is_online = bool(state)

    @abstractmethod
    def run_health_check(self) -> dict[str, str | bool | float]:
        """Menjalankan pemeriksaan kesehatan internal perangkat."""
        pass

    @abstractmethod
    def transmit_packet(self, packet_size_bytes: int) -> bool:
        """Mentransmisikan paket data melalui perangkat."""
        pass


class RadioNode(AbstractDevice):
    """Implementasi perangkat radio BTS nirkabel."""

    def run_health_check(self) -> dict[str, str | bool | float]:
        return {
            "device_id": self.metadata.device_id,
            "type": "Radio",
            "online": self.is_online,
            "vswr": 1.15,
        }

    def transmit_packet(self, packet_size_bytes: int) -> bool:
        return self.is_online and packet_size_bytes <= 1500


class SwitchNode(AbstractDevice):
    """Implementasi perangkat ethernet switch kabel."""

    def run_health_check(self) -> dict[str, str | bool | float]:
        return {
            "device_id": self.metadata.device_id,
            "type": "Switch",
            "online": self.is_online,
            "port_status": "UP",
        }

    def transmit_packet(self, packet_size_bytes: int) -> bool:
        return self.is_online and packet_size_bytes <= 9000
