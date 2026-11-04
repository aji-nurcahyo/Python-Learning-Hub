"""Unit Tests untuk CSV & JSON Data Manager
Python Learning Hub - Chapter 17: File Handling & Data Serialization
"""

import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "code"))

from data_manager import TelemetryDataManager, RecordValidationError


class TestTelemetryDataManager(unittest.TestCase):
    def setUp(self):
        self.manager = TelemetryDataManager()
        self.test_dir = Path(__file__).parent / "temp_test_dir"
        self.test_dir.mkdir(parents=True, exist_ok=True)
        self.csv_test = self.test_dir / "test_bts.csv"
        self.json_test = self.test_dir / "test_bts.json"

    def tearDown(self):
        if self.csv_test.exists():
            self.csv_test.unlink()
        if self.json_test.exists():
            self.json_test.unlink()
        if self.test_dir.exists():
            self.test_dir.rmdir()

    def test_load_csv_valid_and_summary(self):
        csv_content = (
            "id,lokasi,frekuensi_mhz,daya_dbm,status\n"
            "B-1,Lampung,1800,40.0,ACTIVE\n"
            "B-2,Metro,2100,50.0,ACTIVE\n"
        )
        self.csv_test.write_text(csv_content, encoding="utf-8")
        loaded = self.manager.load_from_csv(self.csv_test)
        self.assertEqual(loaded, 2)
        self.assertEqual(len(self.manager.records), 2)

        summary = self.manager.calculate_summary()
        self.assertEqual(summary["total_records"], 2)
        self.assertEqual(summary["avg_power_dbm"], 45.0)
        self.assertEqual(summary["active_count"], 2)

    def test_add_and_update_record(self):
        res1 = self.manager.add_or_update_record({
            "id": "BTS-X",
            "lokasi": "Kotabumi",
            "frekuensi_mhz": 900,
            "daya_dbm": 43.5,
            "status": "ACTIVE"
        })
        self.assertEqual(res1, "ADDED")
        self.assertEqual(len(self.manager.records), 1)

        # Update ID yang sama
        res2 = self.manager.add_or_update_record({
            "id": "BTS-X",
            "lokasi": "Kotabumi Utara",
            "frekuensi_mhz": 900,
            "daya_dbm": 46.0,
            "status": "MAINTENANCE"
        })
        self.assertEqual(res2, "UPDATED")
        self.assertEqual(len(self.manager.records), 1)
        self.assertEqual(self.manager.records[0]["lokasi"], "Kotabumi Utara")
        self.assertEqual(self.manager.records[0]["daya_dbm"], 46.0)

    def test_export_and_json_structure(self):
        self.manager.add_or_update_record({
            "id": "BTS-99",
            "lokasi": "Bakauheni",
            "frekuensi_mhz": 1800.0,
            "daya_dbm": 41.2
        })
        exported_count = self.manager.export_to_json(self.json_test)
        self.assertEqual(exported_count, 1)
        self.assertTrue(self.json_test.exists())

        # Load file JSON dan verifikasi konten
        import json
        with open(self.json_test, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["id"], "BTS-99")

    def test_missing_csv_file_raises_not_found(self):
        missing_path = self.test_dir / "non_existent.csv"
        with self.assertRaises(FileNotFoundError):
            self.manager.load_from_csv(missing_path)

    def test_corrupt_row_skipped(self):
        csv_content = (
            "id,lokasi,frekuensi_mhz,daya_dbm,status\n"
            "B-1,Lampung,1800,40.0,ACTIVE\n"
            "B-BAD,Metro,INVALID_FREQ,40.0,ACTIVE\n"
            "B-2,Kalianda,2100,50.0,ACTIVE\n"
        )
        self.csv_test.write_text(csv_content, encoding="utf-8")
        loaded = self.manager.load_from_csv(self.csv_test)
        # Hanya 2 rekaman valid yang dimuat, 1 baris cacat dilewati
        self.assertEqual(loaded, 2)


if __name__ == "__main__":
    unittest.main()

