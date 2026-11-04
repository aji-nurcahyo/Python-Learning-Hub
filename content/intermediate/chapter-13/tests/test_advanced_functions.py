"""Unit Tests: Advanced Functions & Flexible Data Processor
Chapter 13: Advanced Functions — Python Learning Hub
"""

import os
import sys
import unittest

CODE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "code"))
if CODE_DIR not in sys.path:
    sys.path.insert(0, CODE_DIR)

from data_processor import apply_pipeline, make_scaler, make_threshold_filter, summarize_dataset


class TestAdvancedFunctions(unittest.TestCase):
    """Pengujian fungsi tingkat lanjut pada data_processor.py."""

    def test_make_scaler_closure(self):
        double = make_scaler(2.0)
        self.assertEqual(double(10.0), 20.0)

        scale_offset = make_scaler(1.5, 2.0)
        self.assertEqual(scale_offset(4.0), 8.0)

    def test_make_threshold_filter_closure(self):
        t_filter = make_threshold_filter(min_val=10.0, max_val=50.0)
        self.assertTrue(t_filter(10.0))
        self.assertTrue(t_filter(30.0))
        self.assertTrue(t_filter(50.0))
        self.assertFalse(t_filter(9.9))
        self.assertFalse(t_filter(50.1))

    def test_apply_pipeline_chained(self):
        data = [1.0, 2.0, 3.0]
        # (x * 2) lalu (x + 10) -> [12.0, 14.0, 16.0]
        fn1 = make_scaler(2.0)
        fn2 = make_scaler(1.0, 10.0)
        out = apply_pipeline(data, fn1, fn2)
        self.assertEqual(out, [12.0, 14.0, 16.0])

    def test_apply_pipeline_with_filter(self):
        data = [5.0, 15.0, 25.0, 35.0]
        t_filter = make_threshold_filter(min_val=10.0, max_val=30.0)
        double = make_scaler(2.0)
        out = apply_pipeline(data, double, filter_func=t_filter)
        self.assertEqual(out, [30.0, 50.0])

    def test_summarize_dataset_standard_and_custom(self):
        data = [10.0, 20.0, 30.0]
        summary = summarize_dataset(
            data,
            "count", "sum", "avg", "min", "max",
            prefix="Stat",
            spread=lambda d: max(d) - min(d)
        )
        self.assertEqual(summary["total_samples"], 3)
        self.assertEqual(summary["Stat_count"], 3)
        self.assertEqual(summary["Stat_sum"], 60.0)
        self.assertEqual(summary["Stat_avg"], 20.0)
        self.assertEqual(summary["Stat_min"], 10.0)
        self.assertEqual(summary["Stat_max"], 30.0)
        self.assertEqual(summary["Stat_spread"], 20.0)

    def test_summarize_dataset_empty(self):
        summary = summarize_dataset([])
        self.assertEqual(summary["total_samples"], 0)


if __name__ == "__main__":
    unittest.main()
