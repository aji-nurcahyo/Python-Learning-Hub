"""Chapter 30: Professional Capstone Project
Domain Layer: Model Data Entitas Telemetri & Status Perangkat
"""

from dataclasses import dataclass
from enum import Enum
import time


class DeviceStatus(str, Enum):
    HEALTHY = "HEALTHY"
    DEGRADED = "DEGRADED"
    CRITICAL = "CRITICAL"
    MAINTENANCE = "MAINTENANCE"


@dataclass(frozen=True)
class TelemetryRecord:
    """Entitas telemetri yang merepresentasikan data pengukuran dari simpul jaringan."""
    device_id: str
    timestamp: float
    rssi_dbm: float
    packet_loss_pct: float
    cpu_load_pct: float
    temperature_c: float
    status: DeviceStatus = DeviceStatus.HEALTHY

    @property
    def is_healthy(self) -> bool:
        return (
            self.rssi_dbm >= -85.0
            and self.packet_loss_pct < 2.0
            and self.cpu_load_pct < 80.0
            and self.temperature_c < 75.0
        )


@dataclass(frozen=True)
class ClusterMetricSummary:
    """Ringkasan agregasi metrik dari satu klaster perangkat."""
    cluster_name: str
    total_records: int
    healthy_count: int
    avg_packet_loss: float
    avg_cpu_load: float
    generated_at: float = time.time()

    @property
    def health_rate(self) -> float:
        return round((self.healthy_count / self.total_records) * 100.0, 1) if self.total_records > 0 else 0.0

