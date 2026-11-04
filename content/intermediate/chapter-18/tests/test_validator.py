"""Unit Tests untuk Robust Data Validator
Python Learning Hub - Chapter 18: Exception Handling & Debugging
"""

import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "code"))

from validator import (
    TelecomRecordValidator,
    ValidationError,
    MissingFieldError,
    InvalidRangeError,
)


class TestTelecomRecordValidator(unittest.TestCase):
    def setUp(self):
        self.validator = TelecomRecordValidator()

    def test_valid_record_passes(self):
        rec = {
            "id": "BTS-OK",
            "lokasi": "Bandar Lampung",
            "frekuensi_mhz": "1800.5",
            "daya_dbm": "43.0",
            "status": "ACTIVE"
        }
        res = self.validator.validate_single_record(rec)
        self.assertEqual(res["id"], "BTS-OK")
        self.assertEqual(res["frekuensi_mhz"], 1800.5)
        self.assertEqual(res["daya_dbm"], 43.0)

    def test_missing_field_raises_missing_field_error(self):
        rec = {
            "id": "BTS-NO-LOC",
            # lokasi missing
            "frekuensi_mhz": 1800.0,
            "daya_dbm": 43.0
        }
        with self.assertRaises(MissingFieldError):
            self.validator.validate_single_record(rec)

    def test_out_of_range_raises_invalid_range_error(self):
        # Frekuensi di bawah 100 MHz
        rec = {
            "id": "BTS-LOW-F",
            "lokasi": "Metro",
            "frekuensi_mhz": 10.0,
            "daya_dbm": 43.0
        }
        with self.assertRaises(InvalidRangeError):
            self.validator.validate_single_record(rec)

        # Daya di atas 60 dBm
        rec_high_power = {
            "id": "BTS-HIGH-P",
            "lokasi": "Metro",
            "frekuensi_mhz": 1800.0,
            "daya_dbm": 120.0
        }
        with self.assertRaises(InvalidRangeError):
            self.validator.validate_single_record(rec_high_power)

    def test_batch_processing_and_summary(self):
        batch = [
            {"id": "B-1", "lokasi": "A", "frekuensi_mhz": 900, "daya_dbm": 40},
            {"id": "B-2", "lokasi": "B", "frekuensi_mhz": "INVALID", "daya_dbm": 40},
            {"id": "B-3", "lokasi": "C", "frekuensi_mhz": 1800, "daya_dbm": 42},
        ]
        summary = self.validator.process_batch(batch)
        self.assertEqual(summary["total_diproses"], 3)
        self.assertEqual(summary["total_valid"], 2)
        self.assertEqual(summary["total_invalid"], 1)
        self.assertEqual(summary["valid_ratio_pct"], 66.7)
        self.assertEqual(len(self.validator.invalid_records), 1)


if __name__ == "__main__":
    unittest.main()
