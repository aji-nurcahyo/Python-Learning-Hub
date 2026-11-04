"""Unit Tests: Searching & Sorting Algorithms
Chapter 15: Searching & Sorting Algorithms — Python Learning Hub
Pengujian komprehensif: kasus kosong, satu elemen, duplikat, terurut, terbalik, negatif, target nihil.
"""

import os
import sys
import unittest

CODE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "code"))
if CODE_DIR not in sys.path:
    sys.path.insert(0, CODE_DIR)

from search_sort import (
    binary_search,
    bubble_sort,
    insertion_sort,
    linear_search,
    rank_records,
    selection_sort,
)


class TestSearchSortAlgorithms(unittest.TestCase):
    """Pengujian menyeluruh algoritma pencarian dan pengurutan."""

    def test_linear_search_found_and_missing(self):
        data = [10, 20, 30, 40]
        self.assertEqual(linear_search(data, 30), 2)
        self.assertEqual(linear_search(data, 10), 0)
        self.assertIsNone(linear_search(data, 99))
        self.assertIsNone(linear_search([], 5))

    def test_binary_search_edge_cases(self):
        sorted_data = [-15, -2, 0, 5, 12, 45, 100]
        # Target di awal, tengah, akhir
        idx_first, _ = binary_search(sorted_data, -15)
        self.assertEqual(idx_first, 0)
        idx_mid, _ = binary_search(sorted_data, 5)
        self.assertEqual(idx_mid, 3)
        idx_last, _ = binary_search(sorted_data, 100)
        self.assertEqual(idx_last, 6)

        # Target tidak ditemukan
        idx_miss, _ = binary_search(sorted_data, 50)
        self.assertIsNone(idx_miss)

        # Dataset kosong
        idx_empty, _ = binary_search([], 10)
        self.assertIsNone(idx_empty)

        # Dataset satu elemen
        idx_single, _ = binary_search([42], 42)
        self.assertEqual(idx_single, 0)

    def test_sorting_algorithms_correctness(self):
        cases = [
            [],                                 # Kosong
            [42],                               # Satu elemen
            [5, 5, 5, 5],                       # Semua duplikat
            [1, 2, 3, 4, 5],                    # Sudah terurut
            [5, 4, 3, 2, 1],                    # Terbalik
            [-10, 5, -20, 0, 15, -2],           # Nilai negatif
            [9, 2, 8, 3, 7, 4, 6, 5],           # Acak
        ]

        for case in cases:
            expected_asc = sorted(case)
            expected_desc = sorted(case, reverse=True)

            # Bubble Sort
            self.assertEqual(bubble_sort(case), expected_asc)
            self.assertEqual(bubble_sort(case, reverse=True), expected_desc)

            # Selection Sort
            self.assertEqual(selection_sort(case), expected_asc)
            self.assertEqual(selection_sort(case, reverse=True), expected_desc)

            # Insertion Sort
            self.assertEqual(insertion_sort(case), expected_asc)
            self.assertEqual(insertion_sort(case, reverse=True), expected_desc)

    def test_rank_records(self):
        records = [
            {"name": "A", "score": 75},
            {"name": "B", "score": 95},
            {"name": "C", "score": 85},
        ]
        ranked_desc = rank_records(records, "score", reverse=True)
        self.assertEqual(ranked_desc[0]["name"], "B")
        self.assertEqual(ranked_desc[-1]["name"], "A")

        ranked_asc = rank_records(records, "score", reverse=False)
        self.assertEqual(ranked_asc[0]["name"], "A")
        self.assertEqual(ranked_asc[-1]["name"], "B")


if __name__ == "__main__":
    unittest.main()

