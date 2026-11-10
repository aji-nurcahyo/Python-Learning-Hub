# Chapter 12 — Foundations Capstone Project
> **Student Data Management System (CLI) — Integrasi Fondasi Pemrograman Prosedural & Modular**  
> *Level 1 · Foundations · Intermediate · Estimasi Waktu: 6 Jam Pembelajaran*

---

## 1. Pengantar Proyek Capstone & Arsitektur Perangkat Lunak

Selamat datang di modul puncak **Level 1: Python Foundations** pada platform **Python Learning Hub**. Sepanjang sebelas bab sebelumnya, Anda telah menguasai blok-blok penyusun pemrograman fundamental dalam bahasa Python:
- Variabel, tipe data skalar, dan operator aritmatika (Chapter 01–03).
- Aliran kendali logika kondisional dan perulangan iteratif (Chapter 04–06).
- Manipulasi teks string, struktur data koleksi terurut (*lists, tuples*), dan struktur pemetaan (*dictionaries, sets*) (Chapter 07–09).
- Deklarasi fungsi modular, pengorganisasian modul multi-berkas, serta penanganan eksepsi kokoh (Chapter 10–11).

Proyek Capstone ini dirancang untuk menyatukan seluruh kompetensi tersebut dalam sebuah proyek perangkat lunak nyata: **Student Data Management System** (Sistem Manajemen Data Mahasiswa). Aplikasi ini merupakan perangkat lunak *Command-Line Interface* (CLI) yang mengelola basis data akademik secara interaktif di memori kerja komputer.

### Prinsip Pemisahan Tanggung Jawab (*Separation of Concerns*)

Dalam rekayasa perangkat lunak modern, kode tidak boleh ditulis dalam satu berkas raksasa yang mencampurkan logika bisnis dengan interaksi antarmuka pengguna. Proyek ini membagi sistem ke dalam tiga lapisan modular:

```text
+--------------------------------------------------------------+
|                    LAPISAN ANTARMUKA (main.py)               |
|      Loop menu konsol, penangkapan input(), pemformatan CLI  |
+------------------------------+-------------------------------+
                               | memanggil
                               v
+--------------------------------------------------------------+
|               LAPISAN LOGIKA BISNIS (student_manager.py)     |
|      Operasi CRUD, algoritma pencarian, komputasi statistik  |
+------------------------------+-------------------------------+
                               | memanggil
                               v
+--------------------------------------------------------------+
|               LAPISAN VALIDASI MASUKAN (validators.py)        |
|      Pemeriksaan format NIM, rentang nilai, sanitasi string  |
+--------------------------------------------------------------+
```

Pemisahan ini menjamin bahwa setiap modul dapat diuji secara terisolasi tanpa memerlukan intervensi input manual dari terminal.

---

## 2. Perancangan Struktur Data In-Memory

Aplikasi ini beroperasi menggunakan model data berbasis memori murni (*in-memory database*) tanpa bergantung pada sistem manajemen basis data eksternal (*RDBMS*). Struktur data yang dipilih adalah **List of Dictionaries**:

```python
database_mahasiswa: list[dict[str, object]] = [
    {"nim": "121140001", "name": "Budi Santoso", "grade": 86.50},
    {"nim": "121140002", "name": "Siti Nurhaliza", "grade": 92.00},
    {"nim": "121140003", "name": "Ahmad Fauzi", "grade": 74.25},
]
```

### Mengapa NIM Disimpan Sebagai String?

Pertanyaan mendasar dalam desain data: mengapa Nomor Induk Mahasiswa (NIM) disimpan sebagai string (`str`) dan bukan bilangan bulat (`int`)?
1. **Preservasi Nol di Awal (*Leading Zeros*):** Banyak institusi menggunakan NIM dengan format awalan nol (misalnya `"012114001"`). Mengonversinya menjadi integer akan memotong angka nol tersebut menjadi `12114001`.
2. **Semantik Data:** NIM adalah data pengenal kategoris (*nominal identifier*), bukan kuantitas matematis yang akan dijumlahkan atau dikalikan.
3. **Pencocokan Substring:** String memudahkan operasi pencarian fragmen karakter menggunakan operator `in`.

---

## 3. Modul Validasi Masukan (`validators.py`)

Modul `validators.py` bertindak sebagai penjaga gerbang integritas data sistem. Seluruh fungsi dalam modul ini berupa *pure functions* yang menerima nilai masukan dan mengembalikan status keabsahan.

```python
from typing import Any

def validate_nim(nim: str, students: list[dict[str, Any]] | None = None) -> tuple[bool, str]:
    """Validasi format string NIM dan keunikan identitas."""
    if not isinstance(nim, str):
        return False, "NIM harus berupa teks (string)."
    cleaned = nim.strip()
    if not cleaned:
        return False, "NIM tidak boleh kosong."
    if not cleaned.isdigit():
        return False, "NIM hanya boleh terdiri dari karakter digit angka (0-9)."
    if len(cleaned) < 5 or len(cleaned) > 15:
        return False, "Panjang NIM harus di antara 5 hingga 15 karakter digit."
    if students is not None:
        for student in students:
            if student.get("nim") == cleaned:
                return False, f"Mahasiswa dengan NIM '{cleaned}' sudah terdaftar."
    return True, "NIM valid."
```

### Validasi Nilai Numerik & Penanganan Eksepsi

```python
def validate_grade(grade_input: Any) -> tuple[bool, str, float | None]:
    """Validasi nilai akademik dalam rentang tertutup 0.0 s.d. 100.0."""
    try:
        score = float(str(grade_input).strip())
    except (ValueError, TypeError):
        return False, "Nilai harus berupa angka numerik yang valid.", None

    if score < 0.0 or score > 100.0:
        return False, f"Nilai {score:.2f} di luar rentang valid (0.0 - 100.0).", None

    return True, "Nilai valid.", score
```

> [!TIP]
> **Pola Tuple Return `(status, message, data)`:**  
> Mengembalikan tuple status keberhasilan `bool` bersama pesan penjelasan `str` memberikan fleksibilitas tinggi bagi pemanggil fungsi untuk menampilkan pesan error yang ramah kepada pengguna tanpa memicu kegagalan fatal (*unhandled exception*).

---

## 4. Logika Bisnis Manipulasi Data (`student_manager.py`)

Modul `student_manager.py` mengelola operasi siklus hidup data mahasiswa.

### Operasi Penambahan Mahasiswa (Create)

```python
def add_student(
    students: list[dict[str, Any]],
    nim: str,
    name: str,
    grade_input: Any
) -> tuple[bool, str, dict[str, Any] | None]:
    # 1. Validasi NIM
    valid_nim, msg_nim = validate_nim(nim, students)
    if not valid_nim:
        return False, msg_nim, None

    # 2. Validasi Nama
    valid_name, msg_name = validate_name(name)
    if not valid_name:
        return False, msg_name, None

    # 3. Validasi Nilai
    valid_grade, msg_grade, grade_val = validate_grade(grade_input)
    if not valid_grade or grade_val is None:
        return False, msg_grade, None

    # 4. Konstruksi Rekaman
    new_record = {
        "nim": nim.strip(),
        "name": name.strip(),
        "grade": grade_val
    }
    students.append(new_record)
    return True, f"Mahasiswa '{new_record['name']}' berhasil ditambahkan.", new_record
```

---

## 5. Algoritma Pencarian Multi-Kriteria

Pengguna sering kali hanya mengingat sebagian nama atau beberapa digit terakhir NIM seorang mahasiswa. Fungsi `search_students()` menyediakan fasilitas pencarian fleksibel menggunakan pencocokan substring tanpa memperhatikan besar-kecil huruf (*case-insensitive*):

```python
def search_students(students: list[dict[str, Any]], query: str) -> list[dict[str, Any]]:
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
```

Kompleksitas waktu dari pencarian linier ini adalah $O(n)$, yang sangat cepat dan efisien untuk ukuran dataset memori hingga puluhan ribu entitas.

---

## 6. Pembaruan (Update) dan Penghapusan (Delete) Data

### Pembaruan Data Selektif

Operasi pembaruan memungkinkan perubahan nama atau nilai secara independen tanpa memaksa pengguna menginput ulang seluruh atribut yang tidak berubah:

```python
def update_student(
    students: list[dict[str, Any]],
    nim: str,
    new_name: str | None = None,
    new_grade: Any = None
) -> tuple[bool, str]:
    target = find_student_by_nim(students, nim)
    if target is None:
        return False, f"Mahasiswa dengan NIM '{nim}' tidak ditemukan."

    if new_name is not None and new_name.strip() != "":
        ok, msg = validate_name(new_name)
        if not ok:
            return False, f"Pembaruan nama gagal: {msg}"
        target["name"] = new_name.strip()

    if new_grade is not None and str(new_grade).strip() != "":
        ok, msg, val = validate_grade(new_grade)
        if not ok or val is None:
            return False, f"Pembaruan nilai gagal: {msg}"
        target["grade"] = val

    return True, f"Data mahasiswa NIM '{nim}' berhasil diperbarui."
```

### Penghapusan Berdasarkan NIM

```python
def delete_student(students: list[dict[str, Any]], nim: str) -> tuple[bool, str]:
    clean_nim = nim.strip() if isinstance(nim, str) else ""
    for idx, item in enumerate(students):
        if item.get("nim") == clean_nim:
            removed = students.pop(idx)
            return True, f"Mahasiswa '{removed['name']}' (NIM: {clean_nim}) berhasil dihapus."

    return False, f"Data mahasiswa dengan NIM '{clean_nim}' tidak ditemukan."
```

---

## 7. Analisis Statistik Akademik & Agregasi Nilai

Sistem manajemen data tidak lengkap tanpa kapabilitas analitik. Modul ini menghitung rata-rata kelas, mencari nilai batas ekstrem, dan mengelompokkan mahasiswa peraih nilai tertinggi:

```python
def calculate_statistics(students: list[dict[str, Any]]) -> dict[str, Any]:
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
    grades = [float(s["grade"]) for s in students]
    avg_val = round(sum(grades) / total_count, 2)
    max_val = max(grades)
    min_val = min(grades)

    return {
        "total_students": total_count,
        "average_grade": avg_val,
        "highest_grade": max_val,
        "lowest_grade": min_val,
        "top_students": [s for s in students if float(s["grade"]) == max_val],
        "lowest_students": [s for s in students if float(s["grade"]) == min_val]
    }
```

> [!NOTE]
> **Penanganan Pembagian Nol (*ZeroDivisionError*):**  
> Perhatikan pengecekan kondisi batas `if not students:`. Jika koleksi data kosong, fungsi mengembalikan nilai default yang aman dan mencegah kegagalan runtime akibat pembagian dengan nol.

---

## 8. Perancangan Antarmuka Pengguna CLI (`main.py`)

Modul `main.py` menghubungkan seluruh komponen logika bisnis dengan pengguna akhir melalui terminal interaktif.

### Format Tabel Konsol Berbasis F-String

Kerapian tampilan terminal dicapai dengan spesifikasi perataan teks dan lebar kolom:

```python
def print_table(students: list[dict[str, Any]], title: str = "DAFTAR DATA MAHASISWA") -> None:
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
        g = float(s["grade"])
        cat = get_grade_category(g)
        print(f"{idx:<4} | {s['nim']:<12} | {s['name']:<30} | {g:<7.2f} | {cat:<8}")

    print(separator)
    print(f"Total: {len(students)} mahasiswa terdaftar.\n")
```

---

## 9. Unit Testing Otomatis (*Automated Unit Testing*)

Keandalan perangkat lunak dijamin melalui *automated testing* menggunakan modul bawaan Python `unittest`. Dengan memisahkan logika dari `input()`, seluruh skenario dapat diuji secara otomatis dalam fraksi detik:

```bash
python -m unittest content/foundations/chapter-12/tests/test_student_manager.py
```

### Matriks Test Coverage & Pengujian

| Komponen Uji | Kasus Uji Normal | Kasus Uji Batas (*Boundary*) | Kasus Uji Negatif |
|:---|:---|:---|:---|
| **NIM** | Digit numerik valid 9 digit | Batas minimum (5) & maksimum (15) digit | Karakter non-digit, teks kosong, duplikat |
| **Nama** | Alfabet dengan spasi | Panjang minimal 2 karakter | String kosong, karakter simbol ilegal |
| **Nilai** | Nilai desimal (misal: 85.5) | Titik batas $0.0$ dan $100.0$ | Angka $< 0.0$, $> 100.0$, teks non-angka |
| **CRUD** | Tambah, perbarui, dan hapus | Operasi pada koleksi kosong | Update atau delete NIM tak terdaftar |
| **Statistik** | Rata-rata dan ekstrem kelas | Koleksi dengan 1 mahasiswa | Koleksi kosong tanpa rekaman |

---

## 10. Refleksi Fondasi & Menuju Level 2: Python Intermediate

Selamat atas pencapaian Anda menyelesaikan seluruh 12 bab pada **Level 1: Python Foundations**!

Dengan menyelesaikan proyek capstone ini, Anda telah membuktikan kemampuan:
- Berpikir algoritmik dalam memecahkan masalah komputasi nyata.
- Menulis kode Python prosedural yang modular, rapi, dan mematuhi konvensi PEP 8.
- Merancang struktur data majemuk yang fleksibel dan efisien di memori.
- Membangun perangkat lunak yang tangguh terhadap kesalahan masukan pengguna.

### Menuju Level 2: Python Intermediate
Di Level 2 mendatang, aplikasi **Student Data Management System** ini akan berevolusi lebih jauh:
1. **Pemrograman Berorientasi Objek (OOP — Ch 13):** Rekaman kamus (`dict`) akan ditransformasikan menjadi objek kelas `Student` dan `StudentRegistry` dengan enkapsulasi metode.
2. **File I/O & Serialisasi JSON (Ch 14):** Data tidak lagi hilang saat aplikasi ditutup, melainkan disimpan secara persisten ke dalam berkas disk permanen (`.json` / `.csv`).
3. **Advanced Packaging & Tooling (Ch 15–22):** Pengemasan proyek sebagai pustaka Python terdistribusi dengan dokumentasi dan otomatisasi modern.
