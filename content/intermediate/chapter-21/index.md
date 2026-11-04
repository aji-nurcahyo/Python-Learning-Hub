# Chapter 21: Packages, Environments & Testing
## PyPI, Virtual Environment, pip, `pyproject.toml` & Automated Testing

Selamat datang di **Chapter 21: Packages, Environments & Testing** pada kurikulum **Python Learning Hub**. Modul ini menandai transisi penting dari sekadar menulis skrip program menjadi membangun **perangkat lunak terdistribusi yang terstandar, terisolasi, dan teruji secara otomatis**.

Dalam dunia rekayasa perangkat lunak profesional dan riset teknologi informasi, mengelola dependensi pihak ketiga, menjaga kebersihan sistem operasi, dan memastikan keandalan kode melalui pengujian terotomasi (*automated testing*) adalah kompetensi inti yang wajib dikuasai oleh setiap pengembang Python.

---

## 1. Modul vs Package dalam Ekosistem Python

### Perbedaan Konseptual
- **Modul**: Berkas kode Python tunggal dengan ekstensi `.py` yang mendefinisikan variabel, fungsi, atau class.
- **Package**: Direktori yang memuat satu atau lebih modul Python serta berkas inisialisasi bernama `__init__.py`. Package mendefinisikan *namespace* bertingkat untuk mengelompokkan fungsionalitas yang saling berhubungan.

### Berkas `__init__.py` dan Variabel `__all__`
Ketika Python mengimpor sebuah package, isi berkas `__init__.py` akan dieksekusi terlebih dahulu. Kita dapat mengontrol simbol apa saja yang dapat diimpor oleh pengguna dengan mendefinisikan variabel daftar `__all__`:

```python
# telecom_toolkit/__init__.py
from .models import BaseStation
from .calculators import hitung_link_budget

__version__ = "1.0.0"
__all__ = ["BaseStation", "hitung_link_budget"]
```

### Impor Absolut vs Impor Relatif
- **Absolute Import**: Menentukan path lengkap dari root proyek:
  ```python
  from telecom_toolkit.models import BaseStation
  ```
- **Relative Import**: Menggunakan tanda titik (`.`) untuk merujuk pada direktori modul saat ini:
  ```python
  from .calculators import dbm_ke_mw
  ```

---

## 2. Tata Kelola Virtual Environment (`.venv`)

### Mengapa Virtual Environment Bersifat Wajib?
Menginstal pustaka pihak ketiga secara global menggunakan `pip install` langsung ke sistem operasi sangat berbahaya:
1. **Konflik Versi (*Dependency Hell*)**: Proyek A membutuhkan `pydantic==1.10`, sedangkan Proyek B membutuhkan `pydantic==2.5`. Instalasi global akan merusak salah satu proyek.
2. **Korupsi Paket Sistem**: Pada sistem Linux/macOS, Python bawaan OS dapat mengalami malfungsi jika pustaka sistem tertimpa oleh versi pip yang berbeda.

### Perintah Pembuatan dan Aktivasi Multi-Platform
Python menyediakan modul bawaan `venv` untuk membuat lingkungan virtual terisolasi:

```powershell
# 1. Membuat virtual environment baru di dalam folder .venv
python -m venv .venv
```

**Cara Aktivasi Sesuai Sistem Operasi:**
- **Windows (PowerShell)**:
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
- **Windows (Command Prompt / CMD)**:
  ```cmd
  .\.venv\Scripts\activate.bat
  ```
- **Linux / macOS (Bash/Zsh)**:
  ```bash
  source .venv/bin/activate
  ```

Setelah aktif, prompt terminal akan menampilkan prefiks `(.venv)`. Untuk keluar dari lingkungan virtual, cukup jalankan perintah `deactivate`.

---

## 3. Konfigurasi Proyek Modern dengan `pyproject.toml` (PEP 621)

Standar pengemasan Python modern telah beralih dari skrip lama seperti `setup.py` menuju berkas deklaratif terpadu bernama **`pyproject.toml`**. Format ini menjadi sumber kebenaran tunggal (*single source of truth*) untuk seluruh metadata proyek:

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "telecom-toolkit"
version = "1.0.0"
authors = [{ name = "Aji Pamungkas Tri Nurcahyo" }]
description = "Pustaka metrik sinyal dan manajemen transmisi telekomunikasi"
requires-python = ">=3.10"
dependencies = []

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "pytest-cov>=4.0.0",
]
```

### Instalasi Mode Editable (`pip install -e .`)
Dengan `pyproject.toml`, pengembang dapat menginstal paket buatannya sendiri dalam mode editable:
```powershell
pip install -e .
```
Mode ini membuat tautan langsung ke folder kode sumber lokal, sehingga setiap perubahan pada kode Python akan langsung aktif tanpa perlu menginstal ulang paket.

---

## 4. Fondasi Automated Testing

Pengujian manual melalui terminal tidak lagi memadai saat kompleksitas perangkat lunak bertambah. *Automated Testing* memberikan jaminan bahwa:
- Setiap fungsi menghasilkan output yang presisi sesuai spesifikasi matematis.
- Penambahan fitur baru tidak menyebabkan kerusakan tak terduga pada fitur lama (*regression prevention*).

### Pola-Pola Pengujian Standar

#### A. Basic Assertion
Menggunakan kata kunci `assert` untuk memvalidasi kondisi bernilai `True`:
```python
assert hitung_link_budget(43.0, 15.0, 2.0, 100.0) == -40.0
```

#### B. Pola Fixture (Setup & Teardown)
Fixture menyiapkan data uji awal atau objek simulasi sebelum pengujian dijalankan:
```python
def setUp(self):
    self.station = BaseStation("BTS-01", "Lab ITERA", 40.0, 15.0)
```

#### C. Parameterized Testing
Menjalankan puluhan skenario uji menggunakan tabel data input-output tanpa perlu menulis fungsi duplikat:
```python
test_matrix = [
    (0.0, 1.0),
    (10.0, 10.0),
    (20.0, 100.0),
]
for dbm, expected_mw in test_matrix:
    assert dbm_ke_mw(dbm) == expected_mw
```

#### D. Exception Testing
Memastikan bahwa fungsi secara tangguh menolak nilai ilegal dan melempar exception yang sesuai:
```python
with self.assertRaises(ValueError):
    mw_ke_dbm(-10.0)
```

---

## 5. Mini Proyek: Tested Python Package (`telecom_toolkit`)

Pada bab ini, kita membangun paket teruji **`telecom_toolkit`** yang memuat:
1. Struktur paket standar dengan `__init__.py` dan konfigurasi `pyproject.toml`.
2. Modul matematis `calculators.py` untuk konversi daya dBm-mW dan kalkulasi *link budget* nirkabel.
3. Modul model `models.py` yang memodelkan stasiun pemancar `BaseStation` dengan properti radiasi `eirp_dbm`.
4. Test suite komprehensif pada `tests/test_package.py` yang menguji fixture, kasus parameterisasi, dan batas exception.

---

## 6. Ringkasan Bab
- Modul adalah satu berkas `.py`, sedangkan package adalah direktori yang memuat `__init__.py`.
- Selalu gunakan *virtual environment* (`.venv`) untuk mengisolasi dependensi proyek agar tidak mencemari lingkungan komputasi global.
- `pyproject.toml` standar PEP 621 adalah format deklaratif resmi untuk mengelola metadata, versi Python, dan dependensi proyek.
- Mode instalasi *editable* (`pip install -e .`) mempermudah pengembangan paket internal secara langsung.
- Automated testing menjamin keandalan sistem melalui kombinasi *basic assertions*, *fixtures*, *parameterized tests*, dan *exception testing*.
- Pada bab penutup Level 2 (**Chapter 22: Intermediate Capstone Project**), Anda akan mengintegrasikan seluruh keahlian dari Chapter 13 hingga 21 untuk membangun sistem aplikasi inventaris terdistribusi yang komprehensif.
