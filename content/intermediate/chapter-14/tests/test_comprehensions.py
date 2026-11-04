"""Unit Tests: Comprehensions & Iterators Toolkit
Chapter 14: Comprehensions & Iterators — Python Learning Hub
"""

import os
import sys
import unittest

CODE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "code"))
if CODE_DIR not in sys.path:
    sys.path.insert(0, CODE_DIR)

from transform_toolkit import (
    build_index_map,
    extract_unique_categories,
    filter_and_transform,
    flatten_matrix,
    stream_transformed_data,
)


class TestComprehensions(unittest.TestCase):
    """Pengujian utilitas comprehensions dan iterators."""

    def setUp(self):
        self.sample_data = [
            {"id": "A", "val": 10.0, "cat": " sensor "},
            {"id": "B", "val": 25.0, "cat": "GATEWAY"},
            {"id": "C", "val": 5.0, "cat": "Sensor"},
            {"id": "D", "val": 30.0, "cat": "Node"},
        ]

    def test_filter_and_transform(self):
        res = filter_and_transform(self.sample_data, "val", threshold=20.0, multiplier=2.0)
        self.assertEqual(len(res), 2)
        self.assertEqual(res[0]["id"], "B")
        self.assertEqual(res[0]["val"], 50.0)
        self.assertEqual(res[1]["id"], "D")
        self.assertEqual(res[1]["val"], 60.0)

    def test_build_index_map(self):
        peta = build_index_map(self.sample_data, "id", "val")
        self.assertEqual(peta["A"], 10.0)
        self.assertEqual(peta["B"], 25.0)
        self.assertEqual(len(peta), 4)

    def test_extract_unique_categories(self):
        cats = extract_unique_categories(self.sample_data, "cat")
        self.assertEqual(cats, {"Sensor", "Gateway", "Node"})

    def test_flatten_matrix(self):
        mat = [[1, 2], [3, 4], [5]]
        flat = flatten_matrix(mat)
        self.assertEqual(flat, [1, 2, 3, 4, 5])

        empty_flat = flatten_matrix([])
        self.assertEqual(empty_flat, [])

    def test_stream_transformed_data(self):
        vals = [10.0, 4.0, 20.0]
        gen = stream_transformed_data(vals, threshold=10.0)
        # Gen evaluasi: [10*1.5, 20*1.5] = [15.0, 30.0]
        out = list(gen)
        self.assertEqual(out, [15.0, 30.0])


if __name__ == "__main__":
    unittest.main()

