"""Sistem Manajemen Data Mahasiswa (main.py)

Aplikasi Command-Line Interface (CLI) untuk mengelola data mahasiswa secara interaktif.
Proyek Capstone Level 1: Python Foundations — Python Learning Hub.
"""

import sys
from typing import Any

from student_manager import (
    add_student,
    calculate_statistics,
    delete_student,
    get_all_students,
    get_grade_category,
    search_students,
    sort_students_by_grade,
    update_student,
)


def print_table(students: list[dict[str, Any]], title: str = "DAFTAR DATA MAHASISWA") -> None:
    """Mencetak tabel data mahasiswa dalam format konsol rapi dan proporsional."""
    print(f"\n=== {title} ===")
    if not students:
        print("(Belum ada data mahasiswa yang tersimpan)")
        return

    header = f"{'No':<4} | {'NIM':<12} | {'Nama Lengkap':<30} | {'Nilai':<7} | {'Predikat':<8}"
    separator = "-" * len(header)
    print(separator)
    print(header)
    print(separator)

    for idx, s in enumerate(students, start=1):
        grade_num = float(s["grade"])
        cat = get_grade_category(grade_num)
        print(f"{idx:<4} | {s['nim']:<12} | {s['name']:<30} | {grade_num:<7.2f} | {cat:<8}")

    print(separator)
    print(f"Total: {len(students)} mahasiswa terdaftar.\n")


def ui_add_student(students: list[dict[str, Any]]) -> None:
    """Antarmuka pengguna untuk menambahkan data mahasiswa baru."""
    print("\n--- Tambah Mahasiswa Baru ---")
    nim = input("Masukkan NIM (angka 5-15 digit): ").strip()
    name = input("Masukkan Nama Lengkap: ").strip()
    grade_str = input("Masukkan Nilai Akhir (0 - 100): ").strip()

    success, message, _ = add_student(students, nim, name, grade_str)
    if success:
        print(f"✓ BERHASIL: {message}")
    else:
        print(f"✗ GAGAL: {message}")


def ui_search_student(students: list[dict[str, Any]]) -> None:
    """Antarmuka pengguna untuk mencari data mahasiswa."""
    print("\n--- Cari Mahasiswa ---")
    query = input("Masukkan NIM atau Nama yang dicari: ").strip()
    results = search_students(students, query)

    if results:
        print_table(results, f"HASIL PENCARIAN KATA KUNCI: '{query}'")
    else:
        print(f"✗ Tidak ditemukan mahasiswa yang cocok dengan kata kunci '{query}'.")


def ui_update_student(students: list[dict[str, Any]]) -> None:
    """Antarmuka pengguna untuk memperbarui data mahasiswa."""
    print("\n--- Perbarui Data Mahasiswa ---")
    nim = input("Masukkan NIM mahasiswa yang akan diubah: ").strip()
    found = search_students(students, nim)
    exact = [s for s in found if s["nim"] == nim]

    if not exact:
        print(f"✗ Mahasiswa dengan NIM '{nim}' tidak ditemukan.")
        return

    current = exact[0]
    print(f"Data saat ini: {current['name']} (Nilai: {current['grade']})")
    print("(Tekan ENTER langsung jika bagian data tidak ingin diubah)")

    new_name = input("Nama Baru: ").strip()
    new_grade = input("Nilai Baru: ").strip()

    name_arg = new_name if new_name else None
    grade_arg = new_grade if new_grade else None

    if name_arg is None and grade_arg is None:
        print("ℹ Tidak ada perubahan yang dimasukkan.")
        return

    success, message = update_student(students, nim, name_arg, grade_arg)
    if success:
        print(f"✓ BERHASIL: {message}")
    else:
        print(f"✗ GAGAL: {message}")


def ui_delete_student(students: list[dict[str, Any]]) -> None:
    """Antarmuka pengguna untuk menghapus data mahasiswa."""
    print("\n--- Hapus Data Mahasiswa ---")
    nim = input("Masukkan NIM mahasiswa yang akan dihapus: ").strip()
    found = search_students(students, nim)
    exact = [s for s in found if s["nim"] == nim]

    if not exact:
        print(f"✗ Mahasiswa dengan NIM '{nim}' tidak ditemukan.")
        return

    current = exact[0]
    confirm = input(f"Apakah Anda yakin ingin menghapus '{current['name']}' (NIM: {nim})? [y/N]: ").strip().lower()
    if confirm == "y":
        success, message = delete_student(students, nim)
        if success:
            print(f"✓ BERHASIL: {message}")
        else:
            print(f"✗ GAGAL: {message}")
    else:
        print("ℹ Penghapusan dibatalkan.")


def ui_show_statistics(students: list[dict[str, Any]]) -> None:
    """Menampilkan ringkasan statistik nilai seluruh mahasiswa."""
    stats = calculate_statistics(students)
    print("\n==========================================")
    print("      RINGKASAN STATISTIK AKADEMIK        ")
    print("==========================================")
    if stats["total_students"] == 0:
        print("Belum ada data mahasiswa untuk dikalkulasi.")
        return

    print(f"Total Mahasiswa Terdaftar : {stats['total_students']}")
    print(f"Nilai Rata-rata Kelas     : {stats['average_grade']:.2f}")
    print(f"Nilai Tertinggi           : {stats['highest_grade']:.2f}")
    print(f"Nilai Terendah            : {stats['lowest_grade']:.2f}")

    print("\nMahasiswa dengan Nilai Tertinggi:")
    for s in stats["top_students"]:
        print(f"  - {s['name']} (NIM: {s['nim']}) : {s['grade']}")

    print("\nMahasiswa dengan Nilai Terendah:")
    for s in stats["lowest_students"]:
        print(f"  - {s['name']} (NIM: {s['nim']}) : {s['grade']}")
    print("==========================================\n")


def ui_sort_students(students: list[dict[str, Any]]) -> None:
    """Tantangan Tambahan: Menampilkan daftar terurut berdasarkan nilai."""
    print("\n--- Pengurutan Data Mahasiswa Berdasarkan Nilai ---")
    print("1. Nilai Tertinggi ke Terendah (Descending)")
    print("2. Nilai Terendah ke Tertinggi (Ascending)")
    pilih = input("Pilih metode urut (1/2): ").strip()
    desc = pilih != "2"
    sorted_list = sort_students_by_grade(students, descending=desc)
    mode_str = "TERTINGGI KE TERENDAH" if desc else "TERENDAH KE TERTINGGI"
    print_table(sorted_list, f"DAFTAR MAHASISWA TERURUT ({mode_str})")


def run_app() -> None:
    """Fungsi pengontrol utama alur interaktif aplikasi CLI."""
    # Data awal simulasi kelas
    database: list[dict[str, Any]] = [
        {"nim": "121140001", "name": "Budi Santoso", "grade": 86.50},
        {"nim": "121140002", "name": "Siti Nurhaliza", "grade": 92.00},
        {"nim": "121140003", "name": "Ahmad Fauzi", "grade": 74.25},
        {"nim": "121140004", "name": "Dewi Lestari", "grade": 68.00},
    ]

    while True:
        print("\n==============================================")
        print("       STUDENT DATA MANAGEMENT SYSTEM         ")
        print("       Python Learning Hub — Chapter 12       ")
        print("==============================================")
        print("1. Tampilkan Semua Mahasiswa")
        print("2. Tambah Mahasiswa Baru")
        print("3. Cari Mahasiswa (NIM / Nama)")
        print("4. Perbarui Data Mahasiswa")
        print("5. Hapus Data Mahasiswa")
        print("6. Tampilkan Statistik Nilai")
        print("7. Urutkan Mahasiswa Berdasarkan Nilai")
        print("8. Keluar dari Aplikasi")
        print("==============================================")

        pilihan = input("Masukkan pilihan menu (1-8): ").strip()

        if pilihan == "1":
            print_table(get_all_students(database))
        elif pilihan == "2":
            ui_add_student(database)
        elif pilihan == "3":
            ui_search_student(database)
        elif pilihan == "4":
            ui_update_student(database)
        elif pilihan == "5":
            ui_delete_student(database)
        elif pilihan == "6":
            ui_show_statistics(database)
        elif pilihan == "7":
            ui_sort_students(database)
        elif pilihan == "8":
            print("\nTerima kasih telah menggunakan Student Data Management System!")
            print("Selamat, Anda telah menyelesaikan Level 1: Python Foundations.\n")
            sys.exit(0)
        else:
            print(f"✗ Pilihan '{pilihan}' tidak valid. Silakan pilih menu antara 1 s.d. 8.")


if __name__ == "__main__":
    try:
        run_app()
    except KeyboardInterrupt:
        print("\n\nOperasi dihentikan oleh pengguna. Keluar...")
        sys.exit(0)

