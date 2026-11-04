"""Unit Tests: Student Data Management System

Suite pengujian otomatis untuk memvalidasi seluruh fungsi logika bisnis
pada Capstone Project: Chapter 12 (Foundations Capstone Project).
Menggunakan pustaka standar Python `unittest`.
"""

import os
import sys
import unittest

# Menambahkan direktori code ke sys.path agar modul dapat diimpor langsung
CODE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "code"))
if CODE_DIR not in sys.path:
    sys.path.insert(0, CODE_DIR)

from validators import validate_grade, validate_name, validate_nim
from student_manager import (
    add_student,
    calculate_statistics,
    delete_student,
    find_student_by_nim,
    get_all_students,
    get_grade_category,
    search_students,
    sort_students_by_grade,
    update_student,
)


class TestValidators(unittest.TestCase):
    """Pengujian modul validasi masukan (validators.py)."""

    def test_validate_nim_valid(self):
        ok, msg = validate_nim("121140001")
        self.assertTrue(ok)
        self.assertIn("valid", msg.lower())

    def test_validate_nim_empty_or_whitespace(self):
        ok1, msg1 = validate_nim("")
        self.assertFalse(ok1)
        self.assertIn("kosong", msg1.lower())

        ok2, msg2 = validate_nim("   ")
        self.assertFalse(ok2)
        self.assertIn("kosong", msg2.lower())

    def test_validate_nim_non_digit(self):
        ok, msg = validate_nim("12114000A")
        self.assertFalse(ok)
        self.assertIn("digit", msg.lower())

    def test_validate_nim_length_constraints(self):
        ok_short, _ = validate_nim("1234")  # 4 digit (kurang dari 5)
        self.assertFalse(ok_short)

        ok_long, _ = validate_nim("1234567890123456")  # 16 digit (lebih dari 15)
        self.assertFalse(ok_long)

        ok_bound, _ = validate_nim("12345")  # 5 digit (batas bawah valid)
        self.assertTrue(ok_bound)

    def test_validate_nim_duplicate(self):
        existing = [{"nim": "121140001", "name": "Budi Santoso", "grade": 85.0}]
        ok, msg = validate_nim("121140001", existing)
        self.assertFalse(ok)
        self.assertIn("sudah terdaftar", msg.lower())

        ok_unique, _ = validate_nim("121140002", existing)
        self.assertTrue(ok_unique)

    def test_validate_name_valid(self):
        ok, msg = validate_name("  Budi Santoso  ")
        self.assertTrue(ok)

    def test_validate_name_empty(self):
        ok, msg = validate_name("   ")
        self.assertFalse(ok)
        self.assertIn("kosong", msg.lower())

    def test_validate_name_too_short(self):
        ok, msg = validate_name("A")
        self.assertFalse(ok)
        self.assertIn("minimal", msg.lower())

    def test_validate_grade_valid_float_and_int(self):
        ok, msg, val = validate_grade(85.5)
        self.assertTrue(ok)
        self.assertEqual(val, 85.5)

        ok_int, msg_int, val_int = validate_grade("90")
        self.assertTrue(ok_int)
        self.assertEqual(val_int, 90.0)

    def test_validate_grade_boundaries(self):
        ok_min, _, val_min = validate_grade(0)
        self.assertTrue(ok_min)
        self.assertEqual(val_min, 0.0)

        ok_max, _, val_max = validate_grade(100)
        self.assertTrue(ok_max)
        self.assertEqual(val_max, 100.0)

    def test_validate_grade_out_of_range(self):
        ok_neg, msg_neg, _ = validate_grade(-0.5)
        self.assertFalse(ok_neg)
        self.assertIn("rentang", msg_neg.lower())

        ok_high, msg_high, _ = validate_grade(100.5)
        self.assertFalse(ok_high)
        self.assertIn("rentang", msg_high.lower())

    def test_validate_grade_invalid_type(self):
        ok, msg, _ = validate_grade("delapan puluh")
        self.assertFalse(ok)
        self.assertIn("angka numerik", msg.lower())


class TestStudentManager(unittest.TestCase):
    """Pengujian logika bisnis manajemen mahasiswa (student_manager.py)."""

    def setUp(self):
        """Menyiapkan kumpulan data pengujian standar."""
        self.students = [
            {"nim": "121140001", "name": "Budi Santoso", "grade": 86.50},
            {"nim": "121140002", "name": "Siti Nurhaliza", "grade": 92.00},
            {"nim": "121140003", "name": "Ahmad Fauzi", "grade": 74.25},
        ]

    def test_add_student_success(self):
        ok, msg, record = add_student(self.students, "121140004", "Dewi Lestari", 88.0)
        self.assertTrue(ok)
        self.assertEqual(len(self.students), 4)
        added = self.students[-1]
        self.assertEqual(added["nim"], "121140004")
        self.assertEqual(added["name"], "Dewi Lestari")
        self.assertEqual(added["grade"], 88.0)
        self.assertIsNotNone(record)

    def test_add_student_duplicate_nim_fails(self):
        ok, msg, record = add_student(self.students, "121140001", "Kloning Budi", 80.0)
        self.assertFalse(ok)
        self.assertIsNone(record)
        self.assertEqual(len(self.students), 3)

    def test_add_student_invalid_data_fails(self):
        ok_grade, _, _ = add_student(self.students, "121140005", "Rina", 150.0)
        self.assertFalse(ok_grade)

        ok_name, _, _ = add_student(self.students, "121140006", "", 80.0)
        self.assertFalse(ok_name)

        self.assertEqual(len(self.students), 3)

    def test_get_all_students_returns_copy(self):
        copy_list = get_all_students(self.students)
        self.assertEqual(len(copy_list), 3)
        copy_list.clear()
        self.assertEqual(len(self.students), 3)

    def test_find_student_by_nim(self):
        found = find_student_by_nim(self.students, "121140002")
        self.assertIsNotNone(found)
        self.assertEqual(found["name"], "Siti Nurhaliza")

        not_found = find_student_by_nim(self.students, "999999999")
        self.assertIsNone(not_found)

    def test_search_students(self):
        # Pencarian sebagian nama (case-insensitive)
        results = search_students(self.students, "siti")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["nim"], "121140002")

        # Pencarian sebagian digit NIM
        results_nim = search_students(self.students, "0003")
        self.assertEqual(len(results_nim), 1)
        self.assertEqual(results_nim[0]["name"], "Ahmad Fauzi")

        # Pencarian tanpa hasil
        results_empty = search_students(self.students, "Zul")
        self.assertEqual(len(results_empty), 0)

        # Kata kunci kosong
        results_blank = search_students(self.students, "   ")
        self.assertEqual(len(results_blank), 0)

    def test_update_student_name_only(self):
        ok, msg = update_student(self.students, "121140001", new_name="Budi Pratama")
        self.assertTrue(ok)
        student = find_student_by_nim(self.students, "121140001")
        self.assertEqual(student["name"], "Budi Pratama")
        self.assertEqual(student["grade"], 86.50)

    def test_update_student_grade_only(self):
        ok, msg = update_student(self.students, "121140003", new_grade="80.5")
        self.assertTrue(ok)
        student = find_student_by_nim(self.students, "121140003")
        self.assertEqual(student["grade"], 80.5)

    def test_update_student_not_found(self):
        ok, msg = update_student(self.students, "999999999", new_grade=90)
        self.assertFalse(ok)
        self.assertIn("tidak ditemukan", msg.lower())

    def test_delete_student(self):
        ok, msg = delete_student(self.students, "121140002")
        self.assertTrue(ok)
        self.assertEqual(len(self.students), 2)
        self.assertIsNone(find_student_by_nim(self.students, "121140002"))

        # Hapus NIM yang sudah tidak ada
        ok_again, msg_again = delete_student(self.students, "121140002")
        self.assertFalse(ok_again)
        self.assertIn("tidak ditemukan", msg_again.lower())

    def test_calculate_statistics_populated(self):
        stats = calculate_statistics(self.students)
        self.assertEqual(stats["total_students"], 3)
        self.assertAlmostEqual(stats["average_grade"], 84.25, places=2)
        self.assertEqual(stats["highest_grade"], 92.00)
        self.assertEqual(stats["lowest_grade"], 74.25)
        self.assertEqual(stats["top_students"][0]["nim"], "121140002")
        self.assertEqual(stats["lowest_students"][0]["nim"], "121140003")

    def test_calculate_statistics_empty(self):
        empty_stats = calculate_statistics([])
        self.assertEqual(empty_stats["total_students"], 0)
        self.assertEqual(empty_stats["average_grade"], 0.0)
        self.assertIsNone(empty_stats["highest_grade"])
        self.assertIsNone(empty_stats["lowest_grade"])
        self.assertEqual(empty_stats["top_students"], [])
        self.assertEqual(empty_stats["lowest_students"], [])

    def test_get_grade_category(self):
        self.assertEqual(get_grade_category(95.0), "A")
        self.assertEqual(get_grade_category(80.0), "A")
        self.assertEqual(get_grade_category(79.9), "B")
        self.assertEqual(get_grade_category(70.0), "B")
        self.assertEqual(get_grade_category(69.9), "C")
        self.assertEqual(get_grade_category(60.0), "C")
        self.assertEqual(get_grade_category(59.9), "D")
        self.assertEqual(get_grade_category(50.0), "D")
        self.assertEqual(get_grade_category(49.9), "E")
        self.assertEqual(get_grade_category(0.0), "E")

    def test_sort_students_by_grade(self):
        sorted_desc = sort_students_by_grade(self.students, descending=True)
        self.assertEqual(sorted_desc[0]["nim"], "121140002")  # 92.00
        self.assertEqual(sorted_desc[-1]["nim"], "121140003")  # 74.25

        sorted_asc = sort_students_by_grade(self.students, descending=False)
        self.assertEqual(sorted_asc[0]["nim"], "121140003")  # 74.25
        self.assertEqual(sorted_asc[-1]["nim"], "121140002")  # 92.00


if __name__ == "__main__":
    unittest.main()
