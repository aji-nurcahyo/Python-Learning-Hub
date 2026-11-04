"""Unit Test untuk Chapter 23: Advanced OOP & Design Patterns
Python Learning Hub - Professional Python Engineering
"""

import sys
import unittest
from pathlib import Path

# Setup path ke folder code
code_dir = Path(__file__).resolve().parent.parent / "code"
sys.path.insert(0, str(code_dir))

from pattern_models import AbstractDevice, DeviceMetadata, RadioNode, SwitchNode
from strategies import StandardDiagnostic, DeepDiagnostic
from factory import DeviceFactory
from cluster_manager import DeviceClusterManager


class TestDesignPatterns(unittest.TestCase):
    def test_factory_creation(self) -> None:
        """Memverifikasi DeviceFactory membuat instansiasi tipe yang tepat."""
        radio = DeviceFactory.create("radio", "R-01", "ModelX", "1.0", 500.0)
        self.assertIsInstance(radio, RadioNode)
        self.assertEqual(radio.metadata.device_id, "R-01")

        switch = DeviceFactory.create("switch", "S-01", "ModelY", "2.0", 1000.0)
        self.assertIsInstance(switch, SwitchNode)

    def test_factory_invalid_type_raises(self) -> None:
        """Memverifikasi exception dilempar saat tipe tidak dikenal diminta."""
        with self.assertRaises(ValueError) as ctx:
            DeviceFactory.create("invalid_type", "X", "M", "1", 100.0)
        self.assertIn("tidak terdaftar", str(ctx.exception))

    def test_abstract_class_cannot_instantiate(self) -> None:
        """Memverifikasi AbstractDevice tidak dapat diinstansiasi langsung."""
        meta = DeviceMetadata("D-01", "M", "1.0", 100.0)
        with self.assertRaises(TypeError):
            AbstractDevice(meta)  # type: ignore[abstract]

    def test_strategy_pattern_evaluation(self) -> None:
        """Memverifikasi strategi diagnostik dapat dipertukarkan secara dinamis."""
        radio = DeviceFactory.create("radio", "R-01", "ModelX", "1.0", 500.0)
        radio.is_online = True

        health = radio.run_health_check()
        std_strat = StandardDiagnostic()
        deep_strat = DeepDiagnostic()

        std_rep = std_strat.evaluate(health)
        deep_rep = deep_strat.evaluate(health)

        self.assertIn("[STANDARD]", std_rep)
        self.assertIn("SEHAT", std_rep)
        self.assertIn("[DEEP AUDIT]", deep_rep)
        self.assertIn("vswr=1.15", deep_rep)

    def test_cluster_manager_composition(self) -> None:
        """Memverifikasi manajer klaster mengelola perangkat melalui komposisi."""
        manager = DeviceClusterManager("Klaster-Test", StandardDiagnostic())
        radio = DeviceFactory.create("radio", "R-01", "M1", "1.0", 100.0)
        manager.add_device(radio)

        reports = manager.run_cluster_diagnostics()
        self.assertEqual(len(reports), 1)
        self.assertIn("OFFLINE", reports[0])

        removed = manager.remove_device("R-01")
        self.assertTrue(removed)
        self.assertEqual(len(manager.run_cluster_diagnostics()), 0)


if __name__ == "__main__":
    unittest.main()
