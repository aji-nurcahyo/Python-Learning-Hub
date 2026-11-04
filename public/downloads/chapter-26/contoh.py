"""Chapter 26: Mini Project Demonstrator
Reliable Application Testing & Structured Logging
Python Learning Hub - Professional Python Engineering
"""

import io
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).parent))

from monitoring_service import ExternalApiClient, TelecomMonitoringService
from logging_config import configure_service_logger


class SimulatedApiClient(ExternalApiClient):
    """Implementasi klien simulasi untuk demonstrasi lokal tanpa jaringan eksternal."""

    def __init__(self, sample_data: dict[str, dict[str, Any]]) -> None:
        self.sample_data = sample_data

    def fetch_node_metrics(self, node_id: str) -> dict[str, Any]:
        if node_id not in self.sample_data:
            raise KeyError(f"Node '{node_id}' tidak ditemukan pada basis data remote")
        return self.sample_data[node_id]


def run_demonstration() -> None:
    print("=" * 65)
    print("DEMO: RELIABLE APPLICATION TESTING & LOGGING (CHAPTER 26)")
    print("=" * 65)

    # 1. Konfigurasi Structured Logger
    log_stream = io.StringIO()
    logger = configure_service_logger(name="telecom.service", stream=log_stream)

    # 2. Inisialisasi Mock Client & Service
    dataset = {
        "BTS-01": {"rsrp_dbm": -82.0, "snr_db": 19.5, "status": "UP"},
        "BTS-02": {"rsrp_dbm": -108.5, "snr_db": 4.0, "status": "UP"},
    }
    client = SimulatedApiClient(dataset)
    service = TelecomMonitoringService(client)

    # 3. Eksekusi Pemeriksaan
    res1 = service.check_node_health("BTS-01")
    print(f"Hasil Node 1: {res1['node_id']} -> Status: {res1['status']}")

    res2 = service.check_node_health("BTS-02")
    print(f"Hasil Node 2: {res2['node_id']} -> Status: {res2['status']}")

    try:
        service.check_node_health("BTS-99")
    except KeyError as err:
        print(f"Hasil Node 99: Exception tertangkap -> {err}")

    # 4. Tampilkan Log Terstruktur yang Tertangkap
    print("\nLog Audit Terstruktur yang Dihasilkan:")
    logs = log_stream.getvalue().strip().split("\n")
    for log_line in logs:
        print(f" * {log_line}")


if __name__ == "__main__":
    run_demonstration()
