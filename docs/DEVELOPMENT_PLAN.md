# Rencana Prioritas Pengembangan Konten (30 Chapter)
## Python Learning Hub — Phased Content Development Priority Plan

Dokumen ini memetakan urutan prioritas implementasi materi pembelajaran secara bertahap (*phased rollout*), terstruktur, dan realistis untuk menyelesaikan seluruh 30 chapter **Python Learning Hub**.

---

## 1. Strategi Peluncuran Bertahap (*Phased Strategy*)

Pengembangan materi tidak dilakukan secara acak, melainkan mengikuti **alur pedagogis linier berkesinambungan** (*scaffolded learning progression*):

```text
[FASE 1: Foundations Core]    Ch 01 – 07  ──► Menyambung ke Ch 08–11 (Aktif) ──► Ch 12 (Capstone L1)
                                                       │
                                                       ▼
[FASE 2: Intermediate Core]   Ch 13 – 18  ──► Algoritma, File I/O & Exception Lanjut
                                                       │
                                                       ▼
[FASE 3: Intermediate OOP]    Ch 19 – 22  ──► OOP I, OOP II, Packaging & Ch 22 (Capstone L2)
                                                       │
                                                       ▼
[FASE 4: Professional Eng.]   Ch 23 – 30  ──► Arsitektur, Async, FastAPI & Ch 30 (Capstone L3)
```

Setiap fase memiliki gerbang kualitas (*quality gates*) yang harus dipenuhi sebelum materi dipublikasikan sebagai modul siap belajar (`"available": true`).

---

## 2. Rincian Fase Pengembangan

### FASE 1: Melengkapi Fondasi Inti Level 1 (Prioritas Tertinggi / P1)
*Target: Menjadikan Level 1 Python Foundations 100% lengkap dan siap dipelajari dari awal bagi pemula.*

| Chapter | Judul & Fokus Materi | Estimasi Beban | Sumber Rujukan Utama | Status & Keluaran yang Dihasilkan |
|:---|:---|:---:|:---|:---|
| **Ch 01** | `01-introduction` — Ekosistem, Interpreter & Skrip Pertama | 4 Jam | [DOCS] Sec 1-2, [THINK] Ch 1 | **SELESAI (100%)**: `index.md`, 16 slide, 5 contoh kode, 3 latihan, 1 tugas |
| **Ch 02** | `02-variables-data-types` — Variabel, Tipe Skalar & Memory | 4 Jam | [THINK] Ch 2, [30DAY] Day 02 | **SELESAI (100%)**: `index.md`, 17 slide, 5 contoh kode, 3 latihan, 1 tugas |
| **Ch 03** | `03-operators-expressions` — Operator Aritmatika & Logika | 4 Jam | [DOCS] Sec 3, [30DAY] Day 03 | **SELESAI (100%)**: `index.md`, 16 slide, 5 contoh kode, 3 latihan, 1 tugas |
| **Ch 04** | `04-input-output` — Masukan Pengguna & Formatted f-Strings | 4 Jam | [DOCS] Sec 7.1, [CS50P] Wk 0 | **SELESAI (100%)**: `index.md`, 17 slide, 5 contoh kode, 3 latihan, 1 tugas |
| **Ch 05** | `05-conditionals` — Percabangan If-Elif-Else & Alur Logika | 5 Jam | [DOCS] Sec 4.1, [CS50P] Wk 1 | **SELESAI (100%)**: `index.md`, 18 slide, 6 contoh kode, 3 latihan, 1 tugas |
| **Ch 06** | `06-loops-iteration` — Perulangan While, For & Range | 5 Jam | [DOCS] Sec 4.2-4.3, [SWCARP] Ep 2 | **SELESAI (100%)**: `index.md`, 18 slide, 7 contoh kode, 3 latihan, 1 tugas |
| **Ch 07** | `07-strings-processing` — Slicing & Metode String | 4 Jam | [DOCS] Sec 3.1.2, [30DAY] Day 04 | **SELESAI (100%)**: `index.md`, 18 slide, 7 contoh kode, 3 latihan, 1 tugas |
| **Ch 08–11**| *Pengayaan Narasi Konsep Bacaan pada Modul yang Sudah Aktif* | 4 Jam | [DOCS], [THINK], ITERA upstream | **AKTIF (100%)**: Memperkaya `index.md` dan menambah daftar referensi |
| **Ch 12** | `12-foundations-capstone` — Foundations Capstone Project | 6 Jam | [CS50P] Projects, Telecom specs | Panduan proyek capstone CLI, starter code, rubrik 100% (Batch 3) |

*Status Kemajuan Fase 1:*
- **Batch 1 (Chapter 01 s.d. 04):** **100% Selesai & Terverifikasi** (CPython 3, Slide Deck, Typecheck, Build, Routes).
- **Batch 2 (Chapter 05 s.d. 07):** **100% Selesai & Terverifikasi** (CPython 3, Slide Deck, Typecheck, Build, Routes).
- **Existing Active (Chapter 08 s.d. 11):** **100% Aktif & Terintegrasi**.
- **Batch 3 (Chapter 12 Capstone):** Siap dikerjakan pada iterasi berikutnya untuk menuntaskan 100% Level 1 Foundations.

*Milestone Fase 1:* Seluruh 12 Chapter di Level 1 Foundations berstatus **Tersedia Penuh (100% Active)**. Pengguna pemula dapat mempelajari dasar Python secara mandiri dari awal hingga akhir level.

---

### FASE 2: Tingkat Menengah — Algoritma & Pemrosesan Data (Prioritas P2)
*Target: Menguasai teknik fungsi tingkat tinggi, pemrosesan sequence efisien, algoritma klasik, dan penyimpanan data lokal.*

| Chapter | Judul & Fokus Materi | Estimasi Beban | Sumber Rujukan Utama | Keluaran yang Dihasilkan |
|:---|:---|:---:|:---|:---|
| **Ch 13** | `13-advanced-functions` — *args, **kwargs, Lambda, Closures | 5 Jam | [DOCS] Sec 4.8, [30DAY] Day 14 | `index.md`, 18 slide, 6 contoh kode, 4 latihan, 1 tugas |
| **Ch 14** | `14-comprehensions-iterators` — List/Dict/Set Comprehension | 5 Jam | [DOCS] Sec 5.1.3, [30DAY] Day 13 | `index.md`, 18 slide, 6 contoh kode, 4 latihan, 1 tugas |
| **Ch 15** | `15-searching-sorting-algorithms` — Linear, Binary Search, Sort | 6 Jam | [THINK] Ch 10, [LEARN] `algorithms/` | `index.md`, 22 slide, 8 contoh kode, 4 latihan, 1 tugas |
| **Ch 16** | `16-algorithm-analysis-problem-solving` — Kompleksitas Big-O | 5 Jam | [THINK] App B, Python TimeWiki | `index.md`, 18 slide, 5 contoh kode, 3 latihan, 1 tugas |
| **Ch 17** | `17-file-handling-serialization` — Context Manager, CSV, JSON | 5 Jam | [DOCS] Sec 7.2, [CS50P] Wk 6 | `index.md`, 20 slide, 6 contoh kode, 4 latihan, 1 tugas |
| **Ch 18** | `18-exception-handling-debugging` — Custom Exception, pdb | 5 Jam | [DOCS] Sec 8, [CS50P] Wk 3 | `index.md`, 18 slide, 5 contoh kode, 3 latihan, 1 tugas |

*Milestone Fase 2:* Kemampuan algoritmik dan pemrosesan berkas data terapan telah terbangun secara komprehensif.

---

### FASE 3: Tingkat Menengah — OOP & Packaging Standar (Prioritas P3)
*Target: Menguasai rekayasa berorientasi objek murni, manajemen dependensi, dan pengujian otomatis.*

| Chapter | Judul & Fokus Materi | Estimasi Beban | Sumber Rujukan Utama | Keluaran yang Dihasilkan |
|:---|:---|:---:|:---|:---|
| **Ch 19** | `19-oop-fundamentals` — Class, Instance, Constructor, self | 5 Jam | [DOCS] Sec 9, [THINK] Ch 15 | `index.md`, 20 slide, 6 contoh kode, 4 latihan, 1 tugas |
| **Ch 20** | `20-oop-advanced` — Inheritance, Super, Dunder, Property | 6 Jam | [DOCS] Sec 9.5, [CS50P] Wk 8 | `index.md`, 22 slide, 7 contoh kode, 4 latihan, 1 tugas |
| **Ch 21** | `21-packaging-environments-testing` — venv, pip, pytest | 5 Jam | [PYPA], [PYTEST], [CS50P] Wk 5 | `index.md`, 20 slide, 6 contoh kode, 4 latihan, 1 tugas |
| **Ch 22** | `22-intermediate-capstone` — Intermediate Capstone Project | 7 Jam | [CS50P] Final Projects | Panduan proyek paket OOP ber-unit-test `pytest` |

*Milestone Fase 3:* Level 2 Intermediate Development **100% Lengkap**. Pembaca memiliki kapabilitas setara sertifikasi PCAP industri.

---

### FASE 4: Tingkat Profesional — Rekayasa Sistem Perangkat Lunak (Prioritas P4)
*Target: Standar software engineering industri modern: pattern, static typing, asinkron, REST API, dan kontainerisasi.*

| Chapter | Judul & Fokus Materi | Estimasi Beban | Sumber Rujukan Utama | Keluaran yang Dihasilkan |
|:---|:---|:---:|:---|:---|
| **Ch 23** | `23-advanced-oop-patterns` — ABC, Design Patterns (GoF) | 6 Jam | Python Docs `abc`, [LEARN] | `index.md`, 20 slide, 6 contoh kode, 4 latihan, 1 tugas |
| **Ch 24** | `24-decorators-generators-context` — Yield, Custom Decorator | 6 Jam | [DOCS] Sec 9.9, [CS50P] Wk 9 | `index.md`, 20 slide, 6 contoh kode, 4 latihan, 1 tugas |
| **Ch 25** | `25-type-hints-quality` — Type Annotations, mypy, Pydantic | 5 Jam | PEP 484, PEP 8, mypy docs | `index.md`, 18 slide, 6 contoh kode, 4 latihan, 1 tugas |
| **Ch 26** | `26-advanced-testing-logging` — Fixtures, Mock, Production Logs | 6 Jam | [PYTEST], Python Docs `logging` | `index.md`, 20 slide, 6 contoh kode, 4 latihan, 1 tugas |
| **Ch 27** | `27-concurrency-async` — Threading, Multiprocessing, asyncio | 7 Jam | Python Docs `asyncio` | `index.md`, 22 slide, 7 contoh kode, 4 latihan, 1 tugas |
| **Ch 28** | `28-networking-apis` — Sockets, HTTP, FastAPI Microservices | 7 Jam | FastAPI Docs, Python `socket` | `index.md`, 22 slide, 7 contoh kode, 4 latihan, 1 tugas |
| **Ch 29** | `29-architecture-deployment` — Clean Arch, Docker, CI/CD | 7 Jam | 12-Factor App, Docker Docs | `index.md`, 20 slide, 6 contoh kode, 4 latihan, 1 tugas |
| **Ch 30** | `30-professional-capstone` — Enterprise Cloud-Native Capstone | 8 Jam | Enterprise Production Specs | Panduan arsitektur REST API Dockerized CI/CD |

*Milestone Fase 4:* Seluruh kurikulum 30 Chapter **100% Lengkap (Level 1, Level 2, Level 3)**.

---

## 3. Gerbang Kualitas Konten (*Quality Gates & Acceptance Criteria*)

Sebelum suatu chapter diubah statusnya menjadi `"available": true`, modul tersebut **wajib** lolos dari 7 kriteria verifikasi berikut:

1. **Kelengkapan Berkas Modul:**
   - Memiliki `metadata.json` valid sesuai schema.
   - Memiliki `index.md` dengan narasi konsep minimal 800 kata.
   - Memiliki `slides/deck.json` dengan 15–25 slide terstruktur.
   - Memiliki skrip `code/contoh.py` yang dapat dijalankan mandiri.
   - Memiliki berkas panduan tugas `assignments/tugas.md` dengan rubrik penilaian berbobot 100%.
2. **Kesesuaian Tata Bahasa & Pedagogi:**
   - Penjelasan ditulis dalam bahasa Indonesia yang baku, jelas, dan santun.
   - Menggunakan istilah teknis komputasi yang tepat (misal *mutabilitas*, *ruang lingkup*, *tipe data terurut*).
   - Memuat analogi model mental dan diagram ASCII/KaTeX yang relevan.
3. **Verifikasi Interpreter CPython 3 Nyata:**
   - Seluruh contoh program dieksekusi melalui `python scripts/run_examples.py`.
   - Output terminal terverifikasi tanpa error di `outputs.json` dan lolos `npm run check:outputs`.
4. **Verifikasi Sumber Daya Fisik:**
   - Lolos validasi `node scripts/check_resources.mjs`.
   - Tidak ada link rusak (*no 404 broken links*) baik lokal maupun di subpath GitHub Pages.
5. **Kepatuhan Tipe Data & Linting:**
   - `npm run typecheck` menghasilkan 0 error TypeScript.
   - `npm run lint` menghasilkan 0 peringatan/error ESLint.
6. **Kepatuhan Atribusi Lisensi:**
   - Menyertakan daftar referensi resmi di bagian penutup modul dengan pernyataan lisensi asal.
7. **Integritas Build Produksi:**
   - `npm run build` sukses 100% dan lolos seluruh pengujian rute statis di `dist/`.

