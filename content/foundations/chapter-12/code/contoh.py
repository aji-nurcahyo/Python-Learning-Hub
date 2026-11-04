"""Demonstrasi Komprehensif: Student Data Management System

Capstone Project Level 1: Python Foundations
Pengembang: Aji Pamungkas Tri Nurcahyo — Institut Teknologi Sumatera
Platform: Python Learning Hub

Program ini mendemonstrasikan seluruh 10 fitur utama sistem manajemen data mahasiswa:
1. Inisialisasi struktur data in-memory (list of dicts).
2. Penambahan rekaman baru dengan validasi data.
3. Pencegahan duplikasi NIM dan penanganan masukan tidak valid.
4. Tampilan tabel seluruh data terformat rapi.
5. Pencarian multi-kriteria (berdasarkan NIM dan bagian nama).
6. Pembaruan data mahasiswa secara selektif.
7. Penghapusan data mahasiswa.
8. Analisis statistik nilai akademik (rata-rata, tertinggi, terendah).
9. Tantangan ekstensi: pengurutan data terurut nilai (descending).
10. Validasi batas dan edge-cases.
"""

from typing import Any


# --- 1. MODUL VALIDATOR ---
def validate_nim(nim: str, students: list[dict[str, Any]] | None = None) -> tuple[bool, str]:
    """Validasi format string dan keunikan NIM."""
    if not isinstance(nim, str):
        return False, "NIM harus berupa teks."
    cleaned = nim.strip()
    if not cleaned:
        return False, "NIM tidak boleh kosong."
    if not cleaned.isdigit():
        return False, "NIM harus berupa angka digit."
    if len(cleaned) < 5 or len(cleaned) > 15:
        return False, "Panjang NIM harus antara 5 s.d. 15 digit."
    if students is not None:
        for s in students:
            if s.get("nim") == cleaned:
                return False, f"NIM '{cleaned}' sudah terdaftar."
    return True, "NIM valid."


def validate_name(name: str) -> tuple[bool, str]:
    """Validasi teks nama lengkap mahasiswa."""
    if not isinstance(name, str):
        return False, "Nama harus berupa teks."
    cleaned = name.strip()
    if len(cleaned) < 2:
        return False, "Nama minimal 2 karakter."
    allowed = {" ", ".", "'", "-"}
    for char in cleaned:
        if not (char.isalpha() or char in allowed):
            return False, "Nama hanya boleh memuat huruf dan karakter pemisah wajar."
    return True, "Nama valid."


def validate_grade(grade_input: Any) -> tuple[bool, str, float | None]:
    """Validasi nilai angka numerik dalam rentang 0.0 - 100.0."""
    try:
        val = float(grade_input)
    except (ValueError, TypeError):
        return False, "Nilai harus berupa angka numerik.", None
    if val < 0.0 or val > 100.0:
        return False, f"Nilai {val:.2f} di luar rentang valid (0.0 - 100.0).", None
    return True, "Nilai valid.", round(val, 2)


# --- 2. MODUL PENGELOLA DATA (CRUD & ANALISIS) ---
def add_student(students: list[dict[str, Any]], nim: str, name: str, grade_raw: Any) -> tuple[bool, str]:
    """Menambahkan mahasiswa baru ke daftar."""
    ok_nim, msg_nim = validate_nim(nim, students)
    if not ok_nim:
        return False, msg_nim
    ok_name, msg_name = validate_name(name)
    if not ok_name:
        return False, msg_name
    ok_gr, msg_gr, grade_val = validate_grade(grade_raw)
    if not ok_gr or grade_val is None:
        return False, msg_gr

    students.append({
        "nim": nim.strip(),
        "name": name.strip(),
        "grade": grade_val
    })
    return True, f"Mahasiswa '{name.strip()}' (NIM: {nim.strip()}) berhasil ditambahkan."


def search_students(students: list[dict[str, Any]], query: str) -> list[dict[str, Any]]:
    """Mencari data mahasiswa berdasarkan kecocokan NIM atau nama (case-insensitive)."""
    q = query.strip().lower()
    return [
        s for s in students
        if q in s["nim"].lower() or q in s["name"].lower()
    ]


def update_student(
    students: list[dict[str, Any]],
    nim: str,
    new_name: str | None = None,
    new_grade: Any = None
) -> tuple[bool, str]:
    """Memperbarui informasi nama dan/atau nilai mahasiswa."""
    target = None
    for s in students:
        if s["nim"] == nim:
            target = s
            break
    if not target:
        return False, f"Mahasiswa NIM '{nim}' tidak ditemukan."

    if new_name is not None and new_name.strip():
        ok, msg = validate_name(new_name)
        if not ok:
            return False, msg
        target["name"] = new_name.strip()

    if new_grade is not None and str(new_grade).strip():
        ok, msg, g_val = validate_grade(new_grade)
        if not ok or g_val is None:
            return False, msg
        target["grade"] = g_val

    return True, f"Data NIM '{nim}' berhasil diperbarui."


def delete_student(students: list[dict[str, Any]], nim: str) -> tuple[bool, str]:
    """Menghapus rekaman data mahasiswa berdasarkan NIM."""
    for idx, s in enumerate(students):
        if s["nim"] == nim:
            removed = students.pop(idx)
            return True, f"Mahasiswa '{removed['name']}' (NIM: {nim}) telah dihapus."
    return False, f"Mahasiswa NIM '{nim}' tidak ditemukan."


def get_grade_category(grade: float) -> str:
    """Mengonversi nilai numerik ke predikat huruf."""
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
    """Menghitung ringkasan statistik nilai (rata-rata, nilai ekstrem)."""
    if not students:
        return {
            "total": 0, "avg": 0.0, "max": None, "min": None,
            "top": [], "lowest": []
        }
    grades = [float(s["grade"]) for s in students]
    avg_val = round(sum(grades) / len(grades), 2)
    max_val = max(grades)
    min_val = min(grades)
    return {
        "total": len(students),
        "avg": avg_val,
        "max": max_val,
        "min": min_val,
        "top": [s for s in students if float(s["grade"]) == max_val],
        "lowest": [s for s in students if float(s["grade"]) == min_val]
    }


def print_table(students: list[dict[str, Any]], title: str) -> None:
    """Format visual tabel CLI."""
    print(f"\n--- {title} ---")
    if not students:
        print("(Tidak ada data yang tersedia)")
        return
    header = f"{'No':<3} | {'NIM':<10} | {'Nama Lengkap':<26} | {'Nilai':<6} | {'Predikat':<8}"
    print(header)
    print("-" * len(header))
    for idx, s in enumerate(students, start=1):
        g = float(s["grade"])
        print(f"{idx:<3} | {s['nim']:<10} | {s['name']:<26} | {g:<6.2f} | {get_grade_category(g):<8}")
    print("-" * len(header))


# --- 3. EKSEKUSI DEMO LENGKAP ---
def main() -> None:
    """Eksekusi demonstrasi alur kerja Student Data Management System."""
    print("==========================================================")
    print("DEMONSTRASI CAPSTONE: STUDENT DATA MANAGEMENT SYSTEM")
    print("Python Learning Hub - Level 1: Foundations Capstone")
    print("==========================================================")

    # 1. Inisialisasi basis data simulasi in-memory
    database: list[dict[str, Any]] = [
        {"nim": "121140001", "name": "Budi Santoso", "grade": 86.50},
        {"nim": "121140002", "name": "Siti Nurhaliza", "grade": 92.00},
        {"nim": "121140003", "name": "Ahmad Fauzi", "grade": 74.25},
    ]
    print_table(database, "1. Data Awal Mahasiswa")

    # 2. Tambah mahasiswa baru
    print("\n2. Uji Penambahan Mahasiswa:")
    ok, msg = add_student(database, "121140004", "Dewi Lestari", "81.0")
    print(f"Status tambah sukses: {ok} -> {msg}")

    # 3. Uji penanganan duplikasi NIM & nilai invalid
    print("\n3. Uji Validasi (NIM Duplikat & Nilai Tak Valid):")
    ok_dup, msg_dup = add_student(database, "121140001", "Budi Kloning", 75.0)
    print(f"Hasil duplikasi NIM : {ok_dup} -> {msg_dup}")

    ok_inv, msg_inv = add_student(database, "121140005", "Rina Gunawan", 150.0)
    print(f"Hasil nilai di luar rentang: {ok_inv} -> {msg_inv}")

    # 4. Tampilkan tabel terkini
    print_table(database, "4. Data Setelah Penambahan")

    # 5. Cari data mahasiswa
    print("\n5. Uji Pencarian Mahasiswa:")
    hasil_nama = search_students(database, "siti")
    print(f"Pencarian nama 'siti': Ditemukan {len(hasil_nama)} mahasiswa.")
    for s in hasil_nama:
        print(f"  -> NIM: {s['nim']} | Nama: {s['name']} | Nilai: {s['grade']}")

    hasil_nim = search_students(database, "0004")
    print(f"Pencarian fragmen NIM '0004': Ditemukan {len(hasil_nim)} mahasiswa ({hasil_nim[0]['name']}).")

    # 6. Perbarui data
    print("\n6. Uji Pembaruan Data:")
    ok_upd, msg_upd = update_student(database, "121140003", new_grade=78.50)
    print(f"Hasil update nilai Ahmad: {ok_upd} -> {msg_upd}")

    # 7. Hapus data
    print("\n7. Uji Penghapusan Data:")
    ok_del, msg_del = delete_student(database, "121140004")
    print(f"Hasil hapus Dewi Lestari: {ok_del} -> {msg_del}")

    # 8. Analisis statistik akademik
    stats = calculate_statistics(database)
    print("\n8. Ringkasan Statistik Nilai:")
    print(f"Total Mahasiswa : {stats['total']}")
    print(f"Rata-rata Nilai : {stats['avg']:.2f}")
    print(f"Nilai Tertinggi : {stats['max']:.2f} ({stats['top'][0]['name']})")
    print(f"Nilai Terendah  : {stats['min']:.2f} ({stats['lowest'][0]['name']})")

    # 9. Tantangan Ekstensi: Pengurutan data (Ranking)
    print_table(
        sorted(database, key=lambda s: float(s["grade"]), reverse=True),
        "9. Data Mahasiswa Terurut Ranking Nilai (Descending)"
    )

    print("\nSemua alur sistem Student Data Management System berhasil dijalankan.")


if __name__ == "__main__":
    main()
