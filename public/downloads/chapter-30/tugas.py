"""Tugas Proyek Akhir Chapter 30: Python Data Monitoring & Automation Platform
Platform: Python Learning Hub
Institusi: Institut Teknologi Sumatera (ITERA)

Petunjuk:
Lengkapi implementasi arsitektur platform telemetri di bawah ini.
Pastikan seluruh layer (Domain, Storage, Sources, Engine, Reporter, CLI) terintegrasi dengan baik.
"""

import csv
from dataclasses import dataclass
from enum import Enum
import io
import os
import threading
from typing import Any, Optional, Protocol


# ==============================================================================
# 1. DOMAIN LAYER
# ==============================================================================

class DeviceStatus(str, Enum):
    HEALTHY = "HEALTHY"
    DEGRADED = "DEGRADED"
    CRITICAL = "CRITICAL"


@dataclass(frozen=True)
class TelemetryRecord:
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
class ClusterSummary:
    cluster_name: str
    total_nodes: int
    healthy_nodes: int
    avg_packet_loss: float
    avg_cpu_load: float

    @property
    def health_rate(self) -> float:
        return round((self.healthy_nodes / self.total_nodes) * 100.0, 1) if self.total_nodes > 0 else 0.0


# ==============================================================================
# 2. CONFIGURATION LAYER
# ==============================================================================

@dataclass(frozen=True)
class PlatformConfig:
    app_name: str
    environment: str
    alert_loss_threshold: float
    alert_temp_threshold: float

    @classmethod
    def load(cls) -> "PlatformConfig":
        env = os.environ.get("APP_ENV", "production")
        loss = float(os.environ.get("ALERT_LOSS", "5.0"))
        temp = float(os.environ.get("ALERT_TEMP", "75.0"))
        return cls("DataMonitoringPlatform", env, loss, temp)


# ==============================================================================
# 3. STORAGE LAYER (Thread-Safe)
# ==============================================================================

class StorageEngine:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._data: dict[str, TelemetryRecord] = {}

    def save(self, record: TelemetryRecord) -> None:
        with self._lock:
            self._data[record.device_id] = record

    def save_all(self, records: list[TelemetryRecord]) -> int:
        with self._lock:
            for r in records:
                self._data[r.device_id] = r
            return len(records)

    def get_all(self) -> list[TelemetryRecord]:
        with self._lock:
            return list(self._data.values())

    def count(self) -> int:
        with self._lock:
            return len(self._data)


# ==============================================================================
# 4. DATA SOURCES LAYER
# ==============================================================================

class TelemetrySource(Protocol):
    def read_records(self) -> list[TelemetryRecord]: ...


class CsvTelemetrySource:
    def __init__(self, raw_csv: str) -> None:
        self.raw_csv = raw_csv

    def read_records(self) -> list[TelemetryRecord]:
        records = []
        reader = csv.DictReader(io.StringIO(self.raw_csv.strip()))
        for row in reader:
            records.append(
                TelemetryRecord(
                    device_id=row["device_id"],
                    timestamp=float(row.get("timestamp", 0.0)),
                    rssi_dbm=float(row["rssi_dbm"]),
                    packet_loss_pct=float(row["packet_loss_pct"]),
                    cpu_load_pct=float(row["cpu_load_pct"]),
                    temperature_c=float(row["temperature_c"]),
                    status=DeviceStatus(row.get("status", "HEALTHY")),
                )
            )
        return records


class MockApiSource:
    def read_records(self) -> list[TelemetryRecord]:
        return [
            TelemetryRecord("API-GW-01", 1000.0, -72.0, 0.4, 45.0, 52.0, DeviceStatus.HEALTHY),
            TelemetryRecord("API-GW-02", 1010.0, -94.0, 6.5, 86.0, 78.0, DeviceStatus.CRITICAL),
        ]


# ==============================================================================
# 5. PROCESSING & ANALYTICS ENGINE
# ==============================================================================

class TelemetryEngine:
    def __init__(self, storage: StorageEngine) -> None:
        self.storage = storage

    def ingest(self, sources: list[TelemetrySource]) -> int:
        total = 0
        for src in sources:
            records = src.read_records()
            total += self.storage.save_all(records)
        return total

    def evaluate_cluster(self, cluster_name: str) -> ClusterSummary:
        records = self.storage.get_all()
        if not records:
            return ClusterSummary(cluster_name, 0, 0, 0.0, 0.0)

        healthy = sum(1 for r in records if r.is_healthy)
        avg_loss = round(sum(r.packet_loss_pct for r in records) / len(records), 2)
        avg_cpu = round(sum(r.cpu_load_pct for r in records) / len(records), 2)
        return ClusterSummary(cluster_name, len(records), healthy, avg_loss, avg_cpu)

    def find_anomalies(self, loss_limit: float = 5.0, temp_limit: float = 75.0) -> list[str]:
        records = self.storage.get_all()
        anomalies = []
        for r in records:
            if r.packet_loss_pct > loss_limit or r.temperature_c > temp_limit:
                anomalies.append(r.device_id)
        return anomalies


# ==============================================================================
# 6. REPORTER LAYER
# ==============================================================================

class MarkdownReporter:
    @staticmethod
    def render_report(summary: ClusterSummary, anomaly_count: int) -> str:
        status_sla = "LULUS (COMPLIANT)" if summary.health_rate >= 80.0 else "KRITIS (BREACH)"
        return (
            f"# Laporan Telemetri: {summary.cluster_name}\n"
            f"- Status SLA: {status_sla}\n"
            f"- Total Simpul: {summary.total_nodes}\n"
            f"- Simpul Sehat: {summary.healthy_nodes} ({summary.health_rate}%)\n"
            f"- Jumlah Anomali: {anomaly_count}"
        )


# ==============================================================================
# 7. MAIN TEST & VERIFICATION
# ==============================================================================

SAMPLE_CSV = """device_id,timestamp,rssi_dbm,packet_loss_pct,cpu_load_pct,temperature_c,status
BTS-01,1000.0,-69.0,0.1,40.0,50.0,HEALTHY
BTS-02,1010.0,-81.0,1.2,60.0,62.0,HEALTHY
BTS-03,1020.0,-105.0,9.5,92.0,81.0,CRITICAL
"""


def main() -> None:
    print("=== PENGUJIAN MANDIRI: PROFESSIONAL CAPSTONE PROJECT ===")

    # 1. Config Test
    config = PlatformConfig.load()
    print(f"\n[1] Config Loaded: App={config.app_name} | Env={config.environment}")
    assert config.app_name == "DataMonitoringPlatform"

    # 2. Ingestion & Storage Test
    storage = StorageEngine()
    engine = TelemetryEngine(storage=storage)

    csv_src = CsvTelemetrySource(SAMPLE_CSV)
    api_src = MockApiSource()
    total_ingested = engine.ingest([csv_src, api_src])
    print(f"\n[2] Data Ingested: {total_ingested} records")
    assert total_ingested == 5
    assert storage.count() == 5

    # 3. Analytics & Anomaly Detection Test
    summary = engine.evaluate_cluster("Lampung-Metropolitan")
    anomalies = engine.find_anomalies(
        loss_limit=config.alert_loss_threshold,
        temp_limit=config.alert_temp_threshold,
    )
    print(f"\n[3] Cluster Summary: Total={summary.total_nodes} | Healthy={summary.healthy_nodes} ({summary.health_rate}%)")
    print(f"    Anomalies Detected: {anomalies}")
    assert summary.total_nodes == 5
    assert summary.healthy_nodes == 3  # BTS-01, BTS-02, API-GW-01
    assert summary.health_rate == 60.0
    assert len(anomalies) == 2  # BTS-03, API-GW-02

    # 4. Reporter Test
    report = MarkdownReporter.render_report(summary, len(anomalies))
    print(f"\n[4] Markdown Report Output:\n{report}")
    assert "Lampung-Metropolitan" in report
    assert "KRITIS (BREACH)" in report

    print("\n[OK] SELURUH ARSITEKTUR PLATFORM CAPSTONE BERHASIL DIVERIFIKASI 100%!")


if __name__ == "__main__":
    main()
