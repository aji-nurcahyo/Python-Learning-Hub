"""Unit Test Suite: Validasi Hierarki Inheritance, Polymorphism & Special Methods
Python Learning Hub - Chapter 20: Object-Oriented Programming II
"""

import unittest
import sys
from pathlib import Path

code_dir = Path(__file__).resolve().parent.parent / "code"
sys.path.insert(0, str(code_dir))

from models import Device, RouterDevice, SwitchDevice, SensorDevice
from manager import MultiDeviceManager

class TestMultiDeviceSystem(unittest.TestCase):
    def setUp(self):
        self.router = RouterDevice("RT-10", "Gateway", "10.0.0.1", 150.0, 40.0, "BGP")
        self.switch = SwitchDevice("SW-20", "Access", "10.0.0.2", 50.0, 24, poe_enabled=True)
        self.sensor = SensorDevice("SN-30", "Thermal", "10.0.0.3", 10.0, "Temp", 42.0, "°C")
        self.mgr = MultiDeviceManager("Lab Site")

    def test_inheritance_and_super(self):
        self.assertTrue(isinstance(self.router, Device))
        self.assertTrue(isinstance(self.switch, Device))
        self.assertTrue(issubclass(RouterDevice, Device))
        self.assertEqual(self.router.throughput_gbps, 40.0)

    def test_method_overriding_and_diagnostics(self):
        diag_r = self.router.diagnostics()
        self.assertEqual(diag_r["type"], "Core Router")
        self.assertIn("Throughput: 40.0 Gbps", diag_r["metric"])

        diag_s = self.switch.diagnostics()
        self.assertEqual(diag_s["type"], "Network Switch")
        self.assertIn("PoE Supported", diag_s["metric"])

    def test_polymorphism_in_manager(self):
        self.mgr.register_device(self.router)
        self.mgr.register_device(self.switch)
        self.mgr.register_device(self.sensor)

        diags = self.mgr.run_all_diagnostics()
        self.assertEqual(len(diags), 3)
        self.assertEqual(self.mgr.calculate_total_power(), 210.0)

    def test_special_methods_and_hashability(self):
        # Test __str__ and __repr__
        self.assertIn("Gateway", str(self.router))
        self.assertTrue(repr(self.router).startswith("Device("))

        # Test __eq__
        clone_router = RouterDevice("RT-10", "OtherName", "192.168.1.1", 200.0, 10.0, "OSPF")
        self.assertEqual(self.router, clone_router)
        self.assertFalse(self.router is clone_router)

        # Test __hash__ and set deduplication
        device_set = {self.router, clone_router}
        self.assertEqual(len(device_set), 1)

if __name__ == "__main__":
    unittest.main()
