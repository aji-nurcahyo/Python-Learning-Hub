"""Unit Test Suite: Validasi Class Device & DeviceInventory
Python Learning Hub - Chapter 19: Object-Oriented Programming I
"""

import unittest
import sys
from pathlib import Path

# Memasukkan folder code ke sys.path
code_dir = Path(__file__).resolve().parent.parent / "code"
sys.path.insert(0, str(code_dir))

from device import Device
from inventory import DeviceInventory

class TestDeviceInventory(unittest.TestCase):
    def setUp(self):
        self.inv = DeviceInventory("Test Site")
        self.dev1 = Device("D1", "Router Core", "Network", 100.0)
        self.dev2 = Device("D2", "Sensor Thermal", "Sensor", 25.0)

    def test_device_initialization_and_properties(self):
        self.assertEqual(self.dev1.device_id, "D1")
        self.assertEqual(self.dev1.power_watts, 100.0)
        self.assertTrue(self.dev1.is_active)
        self.dev1.deactivate()
        self.assertFalse(self.dev1.is_active)

    def test_power_watts_validation(self):
        with self.assertRaises(ValueError):
            self.dev1.power_watts = -10.0
        with self.assertRaises(ValueError):
            self.dev1.power_watts = 9999.0

    def test_add_and_duplicate_error(self):
        self.inv.add_device(self.dev1)
        self.assertEqual(len(self.inv.list_all()), 1)
        with self.assertRaises(KeyError):
            self.inv.add_device(self.dev1)

    def test_total_power_calculation(self):
        self.inv.add_device(self.dev1)
        self.inv.add_device(self.dev2)
        self.assertEqual(self.inv.total_power_consumption(active_only=True), 125.0)
        self.dev2.deactivate()
        self.assertEqual(self.inv.total_power_consumption(active_only=True), 100.0)
        self.assertEqual(self.inv.total_power_consumption(active_only=False), 125.0)

    def test_filter_by_category(self):
        self.inv.add_device(self.dev1)
        self.inv.add_device(self.dev2)
        net_devs = self.inv.filter_by_category("Network")
        self.assertEqual(len(net_devs), 1)
        self.assertEqual(net_devs[0].device_id, "D1")

if __name__ == "__main__":
    unittest.main()
