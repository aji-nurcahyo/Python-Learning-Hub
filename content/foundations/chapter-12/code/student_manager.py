"""Modul Pengelola Data Mahasiswa (student_manager.py)

Menyediakan fungsi inti pemrosesan data mahasiswa (CRUD, pencarian, dan statistik).
Seluruh fungsi bersifat independen dari masukan konsol (input) agar mudah diuji secara otomatis.
"""

from typing import Any
try:
    from validators import validate_grade, validate_name, validate_nim
except ImportError:
    from .validators import validate_grade, validate_name, validate_nim


def add_student(
    students: list[dict[str, Any]],
    nim: str,
    name: str,
    grade_input: Any
) -> tuple[bool, str, dict[str, Any] | None]:
    """Menambahkan data mahasiswa baru ke dalam koleksi list of dicts.

    Args:
        students: Koleksi list rekaman data mahasiswa.
        nim: Nomor Induk Mahasiswa (string).
        name: Nama lengkap mahasiswa.
        grade_input: Nilai angka (0.0 - 100.0).

    Returns:
        tuple[bool, str, dict | None]: Status sukses, pesan detail, dan data record baru jika berhasil.
    """
    valid_nim, msg_nim = validate_nim(nim, students)
    if not valid_nim:
        return False, msg_nim, None

    valid_name, msg_name = validate_name(name)
    if not valid_name:
        return False, msg_name, None

    valid_grade, msg_grade, grade_val = validate_grade(grade_input)
    if not valid_grade or grade_val is None:
        return False, msg_grade, None

    new_record: dict[str, Any] = {
        "nim": nim.strip(),
        "name": name.strip(),
        "grade": grade_val
    }
    students.append(new_record)
    return True, f"Mahasiswa '{new_record['name']}' (NIM: {new_record['nim']}) berhasil ditambahkan.", new_record


def get_all_students(students: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Mengembalikan seluruh rekaman data mahasiswa (salinan referensi)."""
    return list(students)


def find_student_by_nim(students: list[dict[str, Any]], nim: str) -> dict[str, Any] | None:
    """Mencari rekaman mahasiswa berdasarkan kecocokan NIM secara eksak."""
    clean_nim = nim.strip() if isinstance(nim, str) else ""
    for item in students:
        if item.get("nim") == clean_nim:
            return item
    return None


def search_students(students: list[dict[str, Any]], query: str) -> list[dict[str, Any]]:
    """Mencari data mahasiswa berdasarkan kecocokan NIM atau substring nama (case-insensitive).

    Args:
        students: Koleksi data mahasiswa.
        query: Kata kunci pencarian (string NIM atau bagian nama).

    Returns:
        list[dict]: Daftar rekaman mahasiswa yang cocok dengan kata kunci.
    """
    if not isinstance(query, str) or not query.strip():
        return []

    q = query.strip().lower()
    matches: list[dict[str, Any]] = []

    for item in students:
        item_nim = item.get("nim", "").lower()
        item_name = item.get("name", "").lower()
        if q in item_nim or q in item_name:
            matches.append(item)

    return matches


def update_student(
    students: list[dict[str, Any]],
    nim: str,
    new_name: str | None = None,
    new_grade: Any = None
) -> tuple[bool, str]:
    """Memperbarui informasi nama dan/atau nilai mahasiswa berdasarkan NIM.

    Args:
        students: Koleksi data mahasiswa.
        nim: NIM mahasiswa yang akan diperbarui.
        new_name: Nama baru (opsional).
        new_grade: Nilai baru (opsional).

    Returns:
        tuple[bool, str]: Status keberhasilan operasi dan pesan keterangan.
    """
    clean_nim = nim.strip() if isinstance(nim, str) else ""
    target: dict[str, Any] | None = None

    for item in students:
        if item.get("nim") == clean_nim:
            target = item
            break

    if target is None:
        return False, f"Mahasiswa dengan NIM '{clean_nim}' tidak ditemukan."

    if new_name is not None and new_name.strip() != "":
        valid_name, msg_name = validate_name(new_name)
        if not valid_name:
            return False, f"Pembaruan nama gagal: {msg_name}"
        target["name"] = new_name.strip()

    if new_grade is not None and str(new_grade).strip() != "":
        valid_grade, msg_grade, grade_val = validate_grade(new_grade)
        if not valid_grade or grade_val is None:
            return False, f"Pembaruan nilai gagal: {msg_grade}"
        target["grade"] = grade_val

    return True, f"Data mahasiswa NIM '{clean_nim}' berhasil diperbarui."


def delete_student(students: list[dict[str, Any]], nim: str) -> tuple[bool, str]:
    """Menghapus data mahasiswa dari koleksi berdasarkan NIM.

    Args:
        students: Koleksi data mahasiswa.
        nim: NIM mahasiswa yang akan dihapus.

    Returns:
        tuple[bool, str]: Status keberhasilan dan pesan keterangan.
    """
    clean_nim = nim.strip() if isinstance(nim, str) else ""
    for idx, item in enumerate(students):
        if item.get("nim") == clean_nim:
            removed = students.pop(idx)
            return True, f"Data mahasiswa '{removed['name']}' (NIM: {clean_nim}) berhasil dihapus."

    return False, f"Data mahasiswa dengan NIM '{clean_nim}' tidak ditemukan."


def get_grade_category(grade: float) -> str:
    """Mengonversi nilai numerik (0-100) menjadi kategori predikat huruf (A, B, C, D, E)."""
    if grade >= 80.0:
        return "A"
    if grade >= 70.0:
        return "B"
    if grade >= 60.0:
        return "C"
    if grade >= 50.0:
        return "D"
    return "E"


def calculate_statistics(students: list[dict[str, Any]]) -> dict[str, Any]:
    """Menghitung ringkasan statistik nilai mahasiswa (rata-rata, tertinggi, terendah).

    Args:
        students: Koleksi data mahasiswa.

    Returns:
        dict: Kamus berisi ringkasan statistik nilai (total, rata-rata, tertinggi, terendah).
    """
    if not students:
        return {
            "total_students": 0,
            "average_grade": 0.0,
            "highest_grade": None,
            "lowest_grade": None,
            "top_students": [],
            "lowest_students": []
        }

    total_count = len(students)
    total_grade = 0.0
    max_val = float("-inf")
    min_val = float("inf")

    for item in students:
        g = float(item["grade"])
        total_grade += g
        if g > max_val:
            max_val = g
        if g < min_val:
            min_val = g

    avg_val = round(total_grade / total_count, 2)

    top_students = [s for s in students if float(s["grade"]) == max_val]
    lowest_students = [s for s in students if float(s["grade"]) == min_val]

    return {
        "total_students": total_count,
        "average_grade": avg_val,
        "highest_grade": max_val,
        "lowest_grade": min_val,
        "top_students": top_students,
        "lowest_students": lowest_students
    }


def sort_students_by_grade(
    students: list[dict[str, Any]],
    descending: bool = True
) -> list[dict[str, Any]]:
    """Mengurutkan salinan data mahasiswa berdasarkan nilai grade."""
    return sorted(students, key=lambda s: float(s["grade"]), reverse=descending)
