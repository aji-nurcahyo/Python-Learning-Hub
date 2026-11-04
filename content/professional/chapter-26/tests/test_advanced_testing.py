"""Unit Test Komprehensif untuk Chapter 26: Advanced Testing & Logging
Python Learning Hub - Professional Python Engineering
"""

import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

# Setup path ke folder code
code_dir = Path(__file__).resolve().parent.parent / "code"
sys.path.insert(0, str(code_dir))

from monitoring_service import ExternalApiClient, TelecomMonitoringService
from logging_config import configure_service_logger


class TestAdvancedTestingAndLogging(unittest.TestCase):
    def setUp(self) -> None:
        """Fixture setUp: Inisialisasi mock client dan instance service sebelum setiap test."""
        self.mock_client = MagicMock(spec=ExternalApiClient)
        self.service = TelecomMonitoringService(self.mock_client)

    def tearDown(self) -> None:
        """Fixture tearDown: Pembersihan state setelah setiap test."""
        self.mock_client.reset_mock()

    def test_mocking_healthy_node(self) -> None:
        """Memverifikasi pemanggilan external client diisolasi menggunakan MagicMock."""
        self.mock_client.fetch_node_metrics.return_value = {"rsrp_dbm": -85.0, "status": "UP"}

        result = self.service.check_node_health("NODE-01")
        self.assertEqual(result["status"], "HEALTHY")
        self.mock_client.fetch_node_metrics.assert_called_once_with("NODE-01")

    def test_mocking_warning_poor_signal(self) -> None:
        """Memverifikasi deteksi sinyal lemah ketika RSRP di bawah -100 dBm."""
        self.mock_client.fetch_node_metrics.return_value = {"rsrp_dbm": -105.0, "status": "UP"}

        result = self.service.check_node_health("NODE-02")
        self.assertEqual(result["status"], "WARNING_POOR_SIGNAL")

    def test_exception_handling_with_assertRaises(self) -> None:
        """Memverifikasi service meneruskan exception jika external client mengalami network crash."""
        self.mock_client.fetch_node_metrics.side_effect = ConnectionError("Koneksi timeout")

        with self.assertRaises(ConnectionError) as ctx:
            self.service.check_node_health("NODE-CRASH")
        self.assertIn("timeout", str(ctx.exception))

    def test_parameterized_subtests(self) -> None:
        """Memverifikasi beragam level sinyal menggunakan subTest()."""
        scenarios = [
            (-75.0, "HEALTHY"),
            (-95.0, "HEALTHY"),
            (-100.5, "WARNING_POOR_SIGNAL"),
            (-115.0, "WARNING_POOR_SIGNAL"),
        ]
        for rsrp, expected_status in scenarios:
            with self.subTest(rsrp=rsrp, expected=expected_status):
                self.mock_client.fetch_node_metrics.return_value = {"rsrp_dbm": rsrp}
                res = self.service.check_node_health("SUBTEST-NODE")
                self.assertEqual(res["status"], expected_status)

    def test_logging_output_with_assertLogs(self) -> None:
        """Memverifikasi pencatatan log level WARNING saat sinyal lemah menggunakan assertLogs."""
        self.mock_client.fetch_node_metrics.return_value = {"rsrp_dbm": -108.0}

        with self.assertLogs("telecom.service", level="WARNING") as cm:
            self.service.check_node_health("LOG-NODE")

        self.assertTrue(any("Sinyal lemah" in msg for msg in cm.output))

    def test_temp_directory_isolation(self) -> None:
        """Memverifikasi pengujian I/O berkas dalam lingkungan terisolasi tempfile."""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file = os.path.join(temp_dir, "audit.log")
            with open(temp_file, "w", encoding="utf-8") as f:
                f.write("LOG: Test line 1\n")

            self.assertTrue(os.path.exists(temp_file))
            with open(temp_file, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertIn("Test line 1", content)
        # Direktori otomatis terhapus setelah keluar dari blok with
        self.assertFalse(os.path.exists(temp_dir))


if __name__ == "__main__":
    unittest.main()
