"""Manajer Klaster Perangkat Berbasis Komposisi (Chapter 23)
Python Learning Hub - Professional Python Engineering
"""

from pattern_models import AbstractDevice
from strategies import DiagnosticStrategy


class DeviceClusterManager:
    """Manajer klaster yang menggunakan komposisi perangkat dan injeksi strategi diagnostik."""

    def __init__(self, cluster_name: str, diagnostic_strategy: DiagnosticStrategy) -> None:
        self.cluster_name = cluster_name
        self.diagnostic_strategy = diagnostic_strategy
        self._devices: dict[str, AbstractDevice] = {}

    def add_device(self, device: AbstractDevice) -> None:
        self._devices[device.metadata.device_id] = device

    def remove_device(self, device_id: str) -> bool:
        return self._devices.pop(device_id, None) is not None

    def run_cluster_diagnostics(self) -> list[str]:
        reports: list[str] = []
        for dev in self._devices.values():
            health = dev.run_health_check()
            report = self.diagnostic_strategy.evaluate(health)
            reports.append(report)
        return reports
