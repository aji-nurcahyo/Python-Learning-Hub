"""Starter Template: Student Data Management System

Tugas Praktik Capstone Project — Chapter 12: Foundations Capstone Project
Platform: Python Learning Hub
Pengembang: Aji Pamungkas Tri Nurcahyo — Institut Teknologi Sumatera

Instruksi:
Lengkapi fungsi-fungsi di bawah ini sesuai spesifikasi pada berkas tugas.md.
Jalankan program ini secara interaktif untuk menguji fungsionalitas sistem Anda.
"""

from typing import Any


# ==============================================================================
# BAGIAN 1: MODUL VALIDASI MASUKAN (VALIDATORS)
# ==============================================================================

def validate_nim(nim: str, students: list[dict[str, Any]] | None = None) -> tuple[bool, str]:
    """Validasi format string NIM dan keunikannya di dalam basis data."""
    # TODO: Implementasikan validasi NIM (tidak kosong, digit angka, 5-15 digit, unik)
    pass


def validate_name(name: str) -> tuple[bool, str]:
    """Validasi format string nama lengkap mahasiswa."""
    # TODO: Implementasikan validasi nama (tidak kosong, minimal 2 karakter)
    pass


def validate_grade(grade_input: Any) -> tuple[bool, str, float | None]:
    """Validasi nilai akademik dalam rentang tertutup 0.0 s.d. 100.0."""
    # TODO: Implementasikan validasi nilai (konversi ke float, cek 0.0 <= grade <= 100.0)
    pass


# ==============================================================================
# BAGIAN 2: LOGIKA BISNIS MANAJEMEN MAHASISWA (STUDENT MANAGER)
# ==============================================================================

def add_student(
    students: list[dict[str, Any]],
    nim: str,
    name: str,
    grade_input: Any
) -> tuple[bool, str, dict[str, Any] | None]:
    """Menambahkan mahasiswa baru ke dalam basis data list of dicts."""
    # TODO: Validasi NIM, nama, nilai, lalu tambahkan ke koleksi students
    pass


def get_all_students(students: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Mengembalikan seluruh rekaman data mahasiswa."""
    return list(students)


def find_student_by_nim(students: list[dict[str, Any]], nim: str) -> dict[str, Any] | None:
    """Mencari data mahasiswa berdasarkan NIM eksak."""
    # TODO: Lakukan pencarian linier berdasarkan NIM
    pass


def search_students(students: list[dict[str, Any]], query: str) -> list[dict[str, Any]]:
    """Mencari data mahasiswa berdasarkan kecocokan NIM atau bagian nama."""
    # TODO: Pencarian substring case-insensitive pada NIM dan nama
    pass


def update_student(
    students: list[dict[str, Any]],
    nim: str,
    new_name: str | None = None,
    new_grade: Any = None
) -> tuple[bool, str]:
    """Memperbarui nama dan/atau nilai mahasiswa yang ada."""
    # TODO: Temukan mahasiswa berdasarkan NIM dan perbarui atributnya
    pass


def delete_student(students: list[dict[str, Any]], nim: str) -> tuple[bool, str]:
    """Menghapus mahasiswa dari koleksi berdasarkan NIM."""
    # TODO: Hapus mahasiswa berdasarkan NIM
    pass


def get_grade_category(grade: float) -> str:
    """Mengonversi nilai numerik ke predikat huruf (A, B, C, D, E)."""
    # TODO: Konversi nilai numerik ke grade category
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
    """Menghitung ringkasan statistik nilai (rata-rata, tertinggi, terendah)."""
    # TODO: Hitung total mahasiswa, rerata, nilai tertinggi, dan nilai terendah
    pass


# ==============================================================================
# BAGIAN 3: ANTARMUKA PENGGUNA CLI (MAIN INTERFACE)
# ==============================================================================

def print_menu() -> None:
    """Menampilkan pilihan menu utama sistem."""
    print("==========================================================")
    print("      STUDENT DATA MANAGEMENT SYSTEM (STARTER)")
    print("==========================================================")
    print("1. Tampilkan Semua Mahasiswa")
    print("2. Tambah Mahasiswa Baru")
    print("3. Cari Mahasiswa (NIM / Bagian Nama)")
    print("4. Perbarui Data Mahasiswa")
    print("5. Hapus Data Mahasiswa")
    print("6. Analisis Statistik Nilai")
    print("7. Keluar dari Aplikasi")
    print("==========================================================")


def main() -> None:
    """Titik masuk utama aplikasi CLI."""
    # Basis data awal untuk pengujian mandiri
    students_database: list[dict[str, Any]] = [
        {"nim": "121140001", "name": "Budi Santoso", "grade": 86.50},
        {"nim": "121140002", "name": "Siti Nurhaliza", "grade": 92.00},
        {"nim": "121140003", "name": "Ahmad Fauzi", "grade": 74.25},
    ]

    while True:
        print_menu()
        choice = input("Pilih menu [1-7]: ").strip()

        if choice == "1":
            print("\n[INFO] Menampilkan daftar data mahasiswa...")
            # TODO: Cetak tabel mahasiswa
        elif choice == "2":
            print("\n[INFO] Menambah data mahasiswa baru...")
            # TODO: Panggil fungsi add_student
        elif choice == "3":
            print("\n[INFO] Pencarian mahasiswa...")
            # TODO: Panggil fungsi search_students
        elif choice == "4":
            print("\n[INFO] Memperbarui data mahasiswa...")
            # TODO: Panggil fungsi update_student
        elif choice == "5":
            print("\n[INFO] Menghapus data mahasiswa...")
            # TODO: Panggil fungsi delete_student
        elif choice == "6":
            print("\n[INFO] Menghitung statistik nilai...")
            # TODO: Panggil fungsi calculate_statistics
        elif choice == "7":
            print("\nTerima kasih telah menggunakan Student Data Management System. Sampai jumpa!")
            break
        else:
            print("\n[PERINGATAN] Pilihan menu tidak valid. Silakan masukkan angka 1-7.")


if __name__ == "__main__":
    main()

