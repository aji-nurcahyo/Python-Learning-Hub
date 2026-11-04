"""Template Tugas Mahasiswa: Chapter 26 - Advanced Testing & Logging
Topik: Automated Test Suite & Production Telemetry System
Platform: Python Learning Hub
Pengembang: Aji Pamungkas Tri Nurcahyo
Institusi: Institut Teknologi Sumatera (ITERA)
"""

import logging
import os
import tempfile
import unittest
from typing import Any
from unittest.mock import MagicMock

# 1. Konfigurasi Logger Sistem
logger = logging.getLogger("telecom.infra")


# 2. Klien I/O Eksternal (Dependensi yang akan di-mock)
class RemoteSwitchGateway:
    def send_reboot_command(self, switch_id: str, port_id: int) -> dict[str, Any]:
        # Dalam produksi nyata, melakukan koneksi SSH/SNMP ke switch fisik
        raise ConnectionError("Gateway perangkat keras fisik tidak dapat dijangkau")


# 3. Layanan Bisnis yang Diuji
class TelecomInfrastructureManager:
    def __init__(self, gateway: RemoteSwitchGateway) -> None:
        self.gateway = gateway

    def reboot_switch_port(self, switch_id: str, port_id: int) -> bool:
        if port_id < 1 or port_id > 48:
            logger.error(f"Nomor port {port_id} di luar batas legal (1-48)")
            raise ValueError(f"Port {port_id} tidak valid")

        logger.info(f"Mengirim instruksi reboot ke {switch_id}:port-{port_id}")
        response = self.gateway.send_reboot_command(switch_id, port_id)

        status = response.get("status", "FAIL")
        if status == "SUCCESS":
            logger.info(f"Port {switch_id}:{port_id} berhasil di-reboot")
            return True
        else:
            logger.warning(f"Reboot port {switch_id}:{port_id} dilaporkan gagal oleh gateway")
            return False

    def export_switch_backup(self, switch_id: str, target_dir: str) -> str:
        filepath = os.path.join(target_dir, f"{switch_id}_backup.cfg")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"SWITCH_ID={switch_id}\nVERSION=17.9.4\nSTATUS=ACTIVE\n")
        return filepath


# 4. Suite Pengujian Otomatis
class TestTelecomInfrastructure(unittest.TestCase):
    def setUp(self) -> None:
        """Fixture setUp: Inisialisasi mock gateway dan instance manager baru."""
        self.mock_gw = MagicMock(spec=RemoteSwitchGateway)
        self.manager = TelecomInfrastructureManager(self.mock_gw)

    def tearDown(self) -> None:
        """Fixture tearDown: Pembersihan mock state."""
        self.mock_gw.reset_mock()

    def test_reboot_port_success(self) -> None:
        """Pengujian skenario reboot sukses menggunakan mock."""
        self.mock_gw.send_reboot_command.return_value = {"status": "SUCCESS", "ack": True}

        success = self.manager.reboot_switch_port("SW-CORE-01", 12)
        self.assertTrue(success)
        self.mock_gw.send_reboot_command.assert_called_once_with("SW-CORE-01", 12)

    def test_reboot_port_failure_logs_warning(self) -> None:
        """Pengujian skenario gagal mencatat log level WARNING."""
        self.mock_gw.send_reboot_command.return_value = {"status": "FAIL"}

        with self.assertLogs("telecom.infra", level="WARNING") as cm:
            result = self.manager.reboot_switch_port("SW-CORE-01", 12)

        self.assertFalse(result)
        self.assertTrue(any("dilaporkan gagal" in msg for msg in cm.output))

    def test_invalid_port_raises_value_error(self) -> None:
        """Pengujian validasi port melempar ValueError."""
        with self.assertRaises(ValueError):
            self.manager.reboot_switch_port("SW-CORE-01", 99)

    def test_parameterized_port_numbers(self) -> None:
        """Pengujian batas nomor port menggunakan subTest."""
        test_ports = [(1, True), (24, True), (48, True)]
        self.mock_gw.send_reboot_command.return_value = {"status": "SUCCESS"}

        for port, is_valid in test_ports:
            with self.subTest(port=port):
                res = self.manager.reboot_switch_port("SW-TEST", port)
                self.assertEqual(res, is_valid)

    def test_backup_export_in_temp_directory(self) -> None:
        """Pengujian I/O ekspor backup dalam lingkungan isolasi tempfile."""
        with tempfile.TemporaryDirectory() as temp_dir:
            backup_path = self.manager.export_switch_backup("SW-ACCESS-05", temp_dir)
            self.assertTrue(os.path.exists(backup_path))
            with open(backup_path, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertIn("SWITCH_ID=SW-ACCESS-05", content)


def main() -> None:
    print("=== MENJALANKAN TEST SUITE INFRASTRUCTURE MANAGER ===")
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestTelecomInfrastructure)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    print("\nHasil Evaluasi Uji:")
    print(f"Total Pengujian  : {result.testsRun}")
    print(f"Status Kelulusan : {'SUKSES' if result.wasSuccessful() else 'GAGAL'}")


if __name__ == "__main__":
    main()

