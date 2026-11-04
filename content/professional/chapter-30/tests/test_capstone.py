"""Unit Test Suite untuk Chapter 30: Professional Capstone Project
Memvalidasi Domain Model, Config, Multi-Sources, Thread-Safe Storage, Analytics Engine, Reporter, dan CLI.
"""

import os
import sys
import unittest

# Menambahkan direktori code ke sys.path agar modul dapat diimpor
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CODE_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "code")
if CODE_DIR not in sys.path:
    sys.path.insert(0, CODE_DIR)

from platform_cli import run_platform_cli
from platform_config import PlatformConfig
from platform_engine import TelemetryProcessingEngine
from platform_models import DeviceStatus, TelemetryRecord
from platform_reporter import TelemetryReportGenerator
from platform_sources import LocalCsvTelemetrySource, MockApiTelemetrySource
from platform_storage import LocalTelemetryStorage


class TestProfessionalCapstonePlatform(unittest.TestCase):
    """Test suite komprehensif untuk memvalidasi seluruh lapisan arsitektur Capstone."""

    def setUp(self) -> None:
        self.storage = LocalTelemetryStorage()
        self.engine = TelemetryProcessingEngine(storage=self.storage)
        self.sample_csv = """device_id,timestamp,rssi_dbm,packet_loss_pct,cpu_load_pct,temperature_c,status
BTS-01,1700000000,-68.0,0.05,45.2,52.1,HEALTHY
BTS-02,1700000010,-82.4,1.10,62.0,61.4,HEALTHY
BTS-03,1700000020,-104.5,8.90,92.5,82.0,CRITICAL
"""

    def test_telemetry_record_health_evaluation(self) -> None:
        """Memvalidasi aturan bisnis domain untuk penentuan status sehat TelemetryRecord."""
        healthy = TelemetryRecord("N-1", 1000.0, -70.0, 0.5, 50.0, 60.0, DeviceStatus.HEALTHY)
        degraded = TelemetryRecord("N-2", 1000.0, -90.0, 3.5, 60.0, 70.0, DeviceStatus.DEGRADED)

        self.assertTrue(healthy.is_healthy)
        self.assertFalse(degraded.is_healthy)

    def test_platform_config_loading_and_defaults(self) -> None:
        """Memvalidasi parsing konfigurasi Twelve-Factor dengan fallback nilai aman."""
        os.environ["APP_ENV"] = "production"
        os.environ["ALERT_LOSS_THRESHOLD"] = "4.5"
        config = PlatformConfig.load()

        self.assertEqual(config.app_name, "DataMonitoringPlatform")
        self.assertEqual(config.environment, "production")
        self.assertEqual(config.alert_loss_threshold, 4.5)

    def test_local_csv_source_parsing(self) -> None:
        """Memvalidasi pembacaan dan konversi tipe data dari sumber CSV lokal."""
        src = LocalCsvTelemetrySource(self.sample_csv)
        records = src.read_records()

        self.assertEqual(len(records), 3)
        self.assertEqual(records[0].device_id, "BTS-01")
        self.assertEqual(records[0].rssi_dbm, -68.0)

    def test_mock_api_source_reading(self) -> None:
        """Memvalidasi pengambilan data telemetri dari sumber REST API mock."""
        api_src = MockApiTelemetrySource()
        api_records = api_src.read_records()

        self.assertEqual(len(api_records), 2)
        self.assertEqual(api_records[0].device_id, "API-NODE-01")

    def test_thread_safe_storage_crud(self) -> None:
        """Memvalidasi operasi penyimpanan dan penarikan data pada LocalTelemetryStorage."""
        rec = TelemetryRecord("STORE-01", 1000.0, -75.0, 0.2, 40.0, 50.0)
        self.storage.save(rec)

        self.assertEqual(self.storage.count(), 1)
        retrieved = self.storage.get_by_id("STORE-01")
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved.device_id, "STORE-01")

    def test_engine_cluster_analysis_and_aggregation(self) -> None:
        """Memvalidasi agregasi statistik klaster dan rasio kesehatan."""
        csv_src = LocalCsvTelemetrySource(self.sample_csv)
        self.engine.ingest_from_sources([csv_src])

        summary = self.engine.analyze_cluster("Sumatera-Core")
        self.assertEqual(summary.total_records, 3)
        self.assertEqual(summary.healthy_count, 2)
        self.assertEqual(summary.health_rate, 66.7)

    def test_engine_anomaly_detection_thresholds(self) -> None:
        """Memvalidasi deteksi anomali pelanggaran ambang batas SLA."""
        csv_src = LocalCsvTelemetrySource(self.sample_csv)
        self.engine.ingest_from_sources([csv_src])

        anomalies = self.engine.detect_anomalies(loss_threshold=5.0, temp_threshold=75.0)
        self.assertEqual(len(anomalies), 1)
        self.assertEqual(anomalies[0]["device_id"], "BTS-03")

    def test_markdown_report_generation(self) -> None:
        """Memvalidasi pembuatan laporan ringkasan Markdown dengan informasi SLA yang akurat."""
        csv_src = LocalCsvTelemetrySource(self.sample_csv)
        self.engine.ingest_from_sources([csv_src])
        summary = self.engine.analyze_cluster("Sumatera-Core")

        report = TelemetryReportGenerator.generate_markdown(summary, anomaly_count=1)
        self.assertIn("Laporan Eksekutif", report)
        self.assertIn("Sumatera-Core", report)
        self.assertIn("Total Simpul Terpantau :** 3 unit", report)

    def test_platform_cli_execution_flags(self) -> None:
        """Memvalidasi antarmuka CLI terpadu menjalankan alur ingest, analisis, dan reporting."""
        cli_res = run_platform_cli(
            self.engine,
            ["--run", "--report", "--cluster", "Metro-Test"],
            self.sample_csv,
        )
        self.assertEqual(cli_res["total_nodes"], 5)  # 3 CSV + 2 Mock API
        self.assertIn("report_markdown", cli_res)


if __name__ == "__main__":
    unittest.main()
