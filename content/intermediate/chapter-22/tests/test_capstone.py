"""Comprehensive Unit Test Suite: Validasi Inventory Management System (Capstone)
Python Learning Hub - Chapter 22: Intermediate Capstone Project
"""

import unittest
import sys
import tempfile
import shutil
from pathlib import Path

code_dir = Path(__file__).resolve().parent.parent / "code"
sys.path.insert(0, str(code_dir))

from exceptions import DuplicateDeviceError, DeviceNotFoundError, ValidationError
from domain_models import Device, NetworkDevice, ServerDevice, SensorDevice
from storage import JSONStorageHandler
from inventory_manager import InventoryManager

class TestInventoryCapstone(unittest.TestCase):
    def setUp(self):
        # Buat temporary directory untuk persistensi berkas pengujian
        self.test_dir = tempfile.mkdtemp()
        self.db_path = Path(self.test_dir) / "test_inventory.json"
        self.storage = JSONStorageHandler(self.db_path)
        self.mgr = InventoryManager("Lab Site", self.storage)

        self.rtr = NetworkDevice("RTR-01", "Core Gateway", 15000000.0, 120.0, 16, "BGP")
        self.srv = ServerDevice("SRV-01", "Main Blade", 50000000.0, 500.0, 64, 256)
        self.sns = SensorDevice("SNS-01", "Temp Sensor", 250000.0, 10.0, "Thermal", "°C")

    def tearDown(self):
        # Hapus temporary directory setelah pengujian selesai
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_model_creation_and_inheritance(self):
        self.assertEqual(self.rtr.serial_id, "RTR-01")
        self.assertEqual(self.rtr.category, "Network")
        self.assertTrue(isinstance(self.rtr, Device))
        self.assertEqual(self.rtr.ports, 16)

    def test_model_validation_errors(self):
        # Harga negatif
        with self.assertRaises(ValidationError):
            Device("DEV-01", "Invalid Dev", "Network", -500.0, 50.0)
        # Serial format salah
        with self.assertRaises(ValidationError):
            Device("invalid_serial", "Dev", "Network", 1000.0, 50.0)
        # Kategori ilegal
        with self.assertRaises(ValidationError):
            Device("DEV-01", "Dev", "UnknownCategory", 1000.0, 50.0)

    def test_crud_lifecycle(self):
        # CREATE
        self.mgr.create_device(self.rtr)
        self.assertEqual(len(self.mgr.list_all()), 1)

        # READ
        fetched = self.mgr.get_device("RTR-01")
        self.assertEqual(fetched.name, "Core Gateway")

        # UPDATE price & status
        self.mgr.update_price("RTR-01", 17500000.0)
        self.assertEqual(self.mgr.get_device("RTR-01").price, 17500000.0)
        self.mgr.toggle_status("RTR-01")
        self.assertFalse(self.mgr.get_device("RTR-01").is_active)

        # DELETE
        deleted = self.mgr.delete_device("RTR-01")
        self.assertEqual(deleted.serial_id, "RTR-01")
        self.assertEqual(len(self.mgr.list_all()), 0)

    def test_duplicate_and_not_found_errors(self):
        self.mgr.create_device(self.rtr)
        with self.assertRaises(DuplicateDeviceError):
            self.mgr.create_device(self.rtr)
        with self.assertRaises(DeviceNotFoundError):
            self.mgr.get_device("NON-EXISTENT")
        with self.assertRaises(DeviceNotFoundError):
            self.mgr.delete_device("NON-EXISTENT")

    def test_search_and_sorting(self):
        self.mgr.create_device(self.rtr)
        self.mgr.create_device(self.srv)
        self.mgr.create_device(self.sns)

        # Keyword search
        results = self.mgr.search_by_keyword("Gateway")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].serial_id, "RTR-01")

        # Sort by price ascending
        sorted_asc = self.mgr.sort_devices(key="price", descending=False)
        self.assertEqual(sorted_asc[0].serial_id, "SNS-01")   # Termurah 250rb
        self.assertEqual(sorted_asc[-1].serial_id, "SRV-01")  # Termahal 50jt

    def test_json_persistence(self):
        self.mgr.create_device(self.rtr)
        self.mgr.create_device(self.srv)

        # Buat manager baru yang membaca file JSON yang sama
        fresh_mgr = InventoryManager("Lab Site", self.storage)
        fresh_devices = fresh_mgr.list_all()
        self.assertEqual(len(fresh_devices), 2)

        # Verifikasi pemulihan tipe class turunan spesifik
        rtr_loaded = fresh_mgr.get_device("RTR-01")
        self.assertTrue(isinstance(rtr_loaded, NetworkDevice))
        self.assertEqual(rtr_loaded.routing_protocol, "BGP")

    def test_portfolio_summary(self):
        self.mgr.create_device(self.rtr)
        self.mgr.create_device(self.srv)
        summary = self.mgr.calculate_summary()

        self.assertEqual(summary["total_count"], 2)
        self.assertEqual(summary["total_valuation_idr"], 65000000.0)
        self.assertEqual(summary["total_power_active_w"], 620.0)

if __name__ == "__main__":
    unittest.main()
