"""Unit Test untuk Chapter 24: Decorators, Generators & Context Managers
Python Learning Hub - Professional Python Engineering
"""

import sys
import unittest
from pathlib import Path

# Setup path ke folder code
code_dir = Path(__file__).resolve().parent.parent / "code"
sys.path.insert(0, str(code_dir))

from decorators import validate_record_schema
from generators import (
    stream_telemetry_source,
    filter_degraded_signals,
    transform_telemetry_metrics,
)
from context_managers import SafeFileSession, execution_timer
from pipeline import execute_pipeline


class TestChapter24Pipeline(unittest.TestCase):
    def test_schema_decorator_validates_keys(self) -> None:
        """Memverifikasi decorator melempar KeyError jika kunci wajib tidak ada."""

        @validate_record_schema(required_keys=["id", "val"])
        def sample_func(rec: dict[str, str]) -> str:
            return rec["id"]

        self.assertEqual(sample_func({"id": "A1", "val": "OK"}), "A1")
        with self.assertRaises(KeyError):
            sample_func({"id": "A1"})

    def test_generator_pipeline_filtering(self) -> None:
        """Memverifikasi generator pipeline memfilter dan mentransformasi secara lazy."""
        raw = [
            {"cell_id": "C1", "snr_db": 15.0, "rsrp_dbm": -80.0},
            {"cell_id": "C2", "snr_db": 5.0, "rsrp_dbm": -105.0},
            {"cell_id": "C3", "snr_db": 20.0, "rsrp_dbm": -70.0},
        ]
        source = stream_telemetry_source(raw)
        filtered = filter_degraded_signals(source, min_snr=10.0)
        transformed = list(transform_telemetry_metrics(filtered, calibration_offset=1.0))

        self.assertEqual(len(transformed), 2)
        self.assertEqual(transformed[0]["cell_id"], "C1")
        self.assertEqual(transformed[0]["calibrated_rsrp"], -79.0)
        self.assertEqual(transformed[1]["cell_id"], "C3")

    def test_execution_timer_context_manager(self) -> None:
        """Memverifikasi context manager timer mengukur durasi dan status sukses."""
        with execution_timer("UnitTestBlock") as timer_data:
            val = sum(x for x in range(1000))

        self.assertTrue(timer_data["success"])
        self.assertGreaterEqual(timer_data["elapsed_sec"], 0.0)
        self.assertEqual(timer_data["label"], "UnitTestBlock")

    def test_full_pipeline_execution(self) -> None:
        """Memverifikasi integrasi penuh fungsi execute_pipeline."""
        raw = [
            {"cell_id": "A", "rsrp_dbm": -85.0, "snr_db": 15.0},
            {"cell_id": "B", "rsrp_dbm": -95.0, "snr_db": 8.0},
        ]
        res = execute_pipeline(raw, min_snr=10.0)
        self.assertEqual(res["processed_count"], 1)
        self.assertEqual(res["results"][0]["cell_id"], "A")
        self.assertTrue(res["timer"]["success"])


if __name__ == "__main__":
    unittest.main()

