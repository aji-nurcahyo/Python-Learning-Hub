"""Chapter 30: Professional Capstone Project
Data Sources Layer: Penyerapan Data dari File Lokal & API Endpoint
"""

import csv
import io
import json
from typing import Any, Protocol

try:
    from platform_models import DeviceStatus, TelemetryRecord
except ImportError:
    from .platform_models import DeviceStatus, TelemetryRecord


class TelemetrySource(Protocol):
    def read_records(self) -> list[TelemetryRecord]:
        ...


class LocalCsvTelemetrySource:
    """Sumber data yang membaca stream telemetri dari file atau string CSV terstruktur."""

    def __init__(self, raw_csv_data: str) -> None:
        self.raw_data = raw_csv_data

    def read_records(self) -> list[TelemetryRecord]:
        records: list[TelemetryRecord] = []
        stream = io.StringIO(self.raw_data.strip())
        reader = csv.DictReader(stream)

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


class MockApiTelemetrySource:
    """Sumber data yang mensimulasikan pemanggilan REST API eksternal secara offline."""

    MOCK_PAYLOAD = [
        {"device_id": "API-NODE-01", "timestamp": 1700000030, "rssi_dbm": -71.2, "packet_loss_pct": 0.10, "cpu_load_pct": 42.0, "temperature_c": 54.0, "status": "HEALTHY"},
        {"device_id": "API-NODE-02", "timestamp": 1700000040, "rssi_dbm": -92.5, "packet_loss_pct": 6.80, "cpu_load_pct": 88.0, "temperature_c": 79.5, "status": "CRITICAL"},
    ]

    def read_records(self) -> list[TelemetryRecord]:
        records: list[TelemetryRecord] = []
        for item in self.MOCK_PAYLOAD:
            records.append(
                TelemetryRecord(
                    device_id=item["device_id"],
                    timestamp=float(item["timestamp"]),
                    rssi_dbm=float(item["rssi_dbm"]),
                    packet_loss_pct=float(item["packet_loss_pct"]),
                    cpu_load_pct=float(item["cpu_load_pct"]),
                    temperature_c=float(item["temperature_c"]),
                    status=DeviceStatus(item["status"]),
                )
            )
        return records

