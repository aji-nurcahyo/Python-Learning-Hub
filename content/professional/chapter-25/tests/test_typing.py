"""Unit Test untuk Chapter 25: Type Hints & Code Quality
Python Learning Hub - Professional Python Engineering
"""

import sys
import unittest
from pathlib import Path

# Setup path ke folder code
code_dir = Path(__file__).resolve().parent.parent / "code"
sys.path.insert(0, str(code_dir))

from domain_types import TelemetryRecord
from protocols import RadioSensor, Transmittable
from containers import EntityRepository
from telemetry_service import TelemetryService


class TestChapter25Typing(unittest.TestCase):
    def test_generic_repository(self) -> None:
        """Memverifikasi EntityRepository generic menyimpan dan mengembalikan tipe konsisten."""
        repo: EntityRepository[str] = EntityRepository()
        repo.save("ITEM-1")
        repo.save("ITEM-2")
        self.assertEqual(repo.count(), 2)
        self.assertEqual(repo.get_all(), ["ITEM-1", "ITEM-2"])

    def test_typeddict_ingestion_and_runtime_validation(self) -> None:
        """Memverifikasi validasi runtime melindungi terhadap data yang menyimpang dari TypedDict."""
        repo: EntityRepository[TelemetryRecord] = EntityRepository()
        svc = TelemetryService(repo)

        valid_rec: TelemetryRecord = {
            "node_id": "N1",
            "frequency_mhz": 1800.0,
            "rsrp_dbm": -85.0,
            "snr_db": 15.0,
            "is_active": True,
        }
        self.assertTrue(svc.ingest_record(valid_rec))
        self.assertEqual(repo.count(), 1)

        # Uji data cacat runtime (node_id bukan str)
        invalid_rec = valid_rec.copy()
        invalid_rec["node_id"] = 12345  # type: ignore[typeddict-item]
        with self.assertRaises(TypeError):
            svc.ingest_record(invalid_rec)

    def test_protocol_structural_conformance(self) -> None:
        """Memverifikasi RadioSensor memenuhi protokol Transmittable tanpa inheritance."""
        sensor = RadioSensor("T-01", 45.0)
        self.assertIsInstance(sensor, Transmittable)
        self.assertEqual(sensor.serialize(), "TEMP_SENSOR:T-01:45.0C")
        self.assertTrue(sensor.check_health())

        # Suhu di atas 70 C tidak sehat
        overheated = RadioSensor("T-02", 75.5)
        self.assertFalse(overheated.check_health())

    def test_service_callable_filtering(self) -> None:
        """Memverifikasi filter_records dengan lambda bertipe aman."""
        repo: EntityRepository[TelemetryRecord] = EntityRepository()
        svc = TelemetryService(repo)

        svc.ingest_record({"node_id": "A", "frequency_mhz": 900.0, "rsrp_dbm": -70.0, "snr_db": 20.0, "is_active": True})
        svc.ingest_record({"node_id": "B", "frequency_mhz": 900.0, "rsrp_dbm": -110.0, "snr_db": 5.0, "is_active": False})

        filtered = svc.filter_records(lambda r: r["is_active"])
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0]["node_id"], "A")


if __name__ == "__main__":
    unittest.main()
