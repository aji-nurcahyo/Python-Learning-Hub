"""Unit Tests: Algorithm Analysis & Benchmarker Toolkit
Chapter 16: Algorithm Analysis & Problem Solving — Python Learning Hub
"""

import os
import sys
import unittest

CODE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "code"))
if CODE_DIR not in sys.path:
    sys.path.insert(0, CODE_DIR)

from benchmarker import (
    analyze_theoretical_growth,
    benchmark_function,
    compare_duplicate_detectors,
)


class TestBenchmarker(unittest.TestCase):
    """Pengujian modul analisis algoritma."""

    def test_analyze_theoretical_growth(self):
        growth = analyze_theoretical_growth(100)
        self.assertEqual(growth["N"], 100)
        self.assertEqual(growth["O(1)"], 1)
        self.assertEqual(growth["O(log_n)"], 7)  # ceil(log2(100)) = 7
        self.assertEqual(growth["O(n)"], 100)
        self.assertEqual(growth["O(n2)"], 10_000)

        # Kasus batas N = 0 dan N = 1
        g0 = analyze_theoretical_growth(0)
        self.assertEqual(g0["O(log_n)"], 0)
        self.assertEqual(g0["O(n2)"], 0)

        g1 = analyze_theoretical_growth(1)
        self.assertEqual(g1["O(log_n)"], 0)
        self.assertEqual(g1["O(n_log_n)"], 0)

    def test_benchmark_function(self):
        def sample_add(a, b):
            return a + b

        res = benchmark_function(sample_add, 10, 20, repetitions=3)
        self.assertEqual(res["function_name"], "sample_add")
        self.assertEqual(res["sample_output"], 30)
        self.assertGreaterEqual(res["average_duration_ms"], 0.0)
        self.assertEqual(res["repetitions"], 3)

    def test_compare_duplicate_detectors(self):
        data_unique = [1, 2, 3, 4, 5]
        res_u = compare_duplicate_detectors(data_unique)
        self.assertFalse(res_u["has_duplicates"])
        self.assertEqual(res_u["dataset_size"], 5)

        data_dup = [1, 2, 3, 2, 5]
        res_d = compare_duplicate_detectors(data_dup)
        self.assertTrue(res_d["has_duplicates"])
        self.assertEqual(res_d["dataset_size"], 5)


if __name__ == "__main__":
    unittest.main()
