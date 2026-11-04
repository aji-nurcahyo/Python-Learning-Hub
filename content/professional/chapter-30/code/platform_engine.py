"""Chapter 30: Professional Capstone Project
Processing Services Layer: Transformasi, Konkurensi & Agregasi Metrik
"""

from concurrent.futures import ThreadPoolExecutor
from typing import Any

try:
    from platform_models import ClusterMetricSummary, DeviceStatus, TelemetryRecord
    from platform_sources import TelemetrySource
    from platform_storage import LocalTelemetryStorage
except ImportError:
    from .platform_models import ClusterMetricSummary, DeviceStatus, TelemetryRecord
    from .platform_sources import TelemetrySource
    from .platform_storage import LocalTelemetryStorage


class TelemetryProcessingEngine:
    """Mesin pengolah telemetri data monitoring dan otomasi analisis SLA."""

    def __init__(self, storage: LocalTelemetryStorage) -> None:
        self.storage = storage

    def ingest_from_sources(self, sources: list[TelemetrySource]) -> int:
        """Mengumpulkan data dari multi-sumber (file & API) dan menyimpannya secara terpadu."""
        total_ingested = 0
        for src in sources:
            records = src.read_records()
            total_ingested += self.storage.save_batch(records)
        return total_ingested

    def analyze_cluster(self, cluster_name: str = "Lampung-Core") -> ClusterMetricSummary:
        """Melakukan agregasi statistik dan kalkulasi rasio kesehatan klaster."""
        records = self.storage.get_all()
        if not records:
            return ClusterMetricSummary(
                cluster_name=cluster_name,
                total_records=0,
                healthy_count=0,
                avg_packet_loss=0.0,
                avg_cpu_load=0.0,
            )

        healthy_cnt = sum(1 for r in records if r.is_healthy)
        avg_loss = round(sum(r.packet_loss_pct for r in records) / len(records), 2)
        avg_cpu = round(sum(r.cpu_load_pct for r in records) / len(records), 2)

        return ClusterMetricSummary(
            cluster_name=cluster_name,
            total_records=len(records),
            healthy_count=healthy_cnt,
            avg_packet_loss=avg_loss,
            avg_cpu_load=avg_cpu,
        )

    def detect_anomalies(self, loss_threshold: float = 5.0, temp_threshold: float = 75.0) -> list[dict[str, Any]]:
        """Mendeteksi simpul-simpul jaringan yang melanggar ambang batas SLA."""
        records = self.storage.get_all()
        anomalies = []
        for r in records:
            reasons = []
            if r.packet_loss_pct > loss_threshold:
                reasons.append(f"Packet loss {r.packet_loss_pct}% melebihi ambang {loss_threshold}%")
            if r.temperature_c > temp_threshold:
                reasons.append(f"Suhu {r.temperature_c} C melebihi ambang {temp_threshold} C")

            if reasons:
                anomalies.append({
                    "device_id": r.device_id,
                    "reasons": reasons,
                    "status": r.status.value,
                })
        return anomalies

