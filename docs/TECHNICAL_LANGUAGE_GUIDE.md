# Panduan Standar Bahasa Teknis & Kebijakan Terminologi Global
## Python Learning Hub — Official Technical Language Policy & Style Guide

> **Prioritas:** TERTINGGI (*HIGHEST*) — Berlaku untuk seluruh konten edukasi saat ini dan masa depan.  
> **Versi Panduan:** 2.0.0  
> **Tanggal Efektif:** 4 November 2026  
> **Ruang Lingkup:** Seluruh modul Python (Chapter 01–30), materi pembelajaran AI/ML masa depan, slide presentasi interaktif Reveal.js, tutorial setup lingkungan, penjelasan kode, latihan, tugas mandiri, serta dokumentasi kurikulum.  
> **Prinsip Fundamental:** *"Indonesian for explanations, English for established technical terminology."* (Bahasa Indonesia untuk narasi penjelasan, Bahasa Inggris untuk terminologi teknis yang telah mapan).

---

## 1. Prinsip Dasar & Kebijakan Bahasa

Dalam dunia rekayasa perangkat lunak dan komputasi, menerjemahkan istilah teknis bahasa Inggris secara harfiah (*literal translation*) hanya karena padanan bahasa Indonesia-nya ada sering kali menimbulkan kerancuan, kebingungan konseptual, dan ketidaksesuaian dengan dokumentasi resmi pemrograman.

Platform **Python Learning Hub** menetapkan kebijakan resmi:
1. **Bahasa Pengantar:** Tulis narasi penjelasan konsep, instruksi tutorial, deskripsi tugas, dan rubrik penilaian dalam **Bahasa Indonesia yang natural, lugas, baku, dan komunikatif**.
2. **Terminologi Teknis Standar:** Pertahankan terminologi teknis yang diakui secara internasional tetap dalam **Bahasa Inggris** (menggunakan format `code span` atau teks tegak/miring sesuai konteks).
3. **Larangan Terjemahan Harfiah Mesin:** Jangan menggunakan terjemahan harfiah kaku (misalnya: dilarang menerjemahkan `dictionary` menjadi "kamus", `virtual environment` menjadi "lingkungan virtual", atau `inheritance` menjadi "pewarisan").
4. **Preservasi Sintaksis & Identifier:** Pertahankan sintaksis Python, kata kunci bawaan (`def`, `class`, `yield`, `import`, dll.), nama modul/pustaka (`numpy`, `pytest`, `sqlite3`, dll.), dan nama framework tanpa modifikasi.
5. **Kebiasaan Profesional:** Gunakan terminologi Bahasa Inggris ketika istilah tersebut jauh lebih lazim dan standar dalam industri rekayasa perangkat lunak internasional.
6. **Penjelasan Istilah Baru:** Berikan penjelasan singkat atau definisi ketika sebuah istilah teknis baru pertama kali diperkenalkan kepada pembelajar.
7. **Konsistensi Lintas Media:** Terapkan standar terminologi yang seragam di seluruh modul bacaan, slide presentasi, penjelasan kode, latihan (*exercises*), tugas mandiri (*assignments*), dan tutorial.
8. **Preservasi Istilah Indonesia yang Tepat:** Jangan menulis ulang istilah Bahasa Indonesia yang memang sudah tepat dan lazim secara teknis tanpa alasan yang jelas.
9. **Kepatuhan Atribusi & Referensi:** Jangan mengubah judul asli karya referensi eksternal atau catatan atribusi lisensi yang diwajibkan secara hukum.
10. **Hindari Campuran Bahasa Berlebihan:** Hindari mencampuradukkan kata bahasa Inggris ke dalam kalimat narasi umum sehari-hari; gunakan istilah bahasa Inggris secara spesifik untuk konsep teknis yang telah mapan.

---

## 2. Tabel Standar Terminologi Baku (Avoid vs. Preferred)

Tabel berikut menetapkan terminologi yang **wajib digunakan (*Preferred*)** dan padanan harfiah yang **harus dihindari (*Avoid*)** di seluruh materi Python Learning Hub:

| Istilah yang DILARANG / DIHINDARI (*Avoid*) | Terminologi Baku yang WAJIB DIGUNAKAN (*Preferred*) | Catatan Kontekstual |
| :--- | :--- | :--- |
| Lingkungan pengembangan | **Development Environment** | Konteks konfigurasi IDE, compiler, dan tooling kerja |
| Lingkungan pemrograman | **Programming Environment** | Ekosistem eksekusi kode dan runtime |
| Lingkungan virtual | **Virtual Environment** | Isolasi dependensi paket via `.venv` |
| Penerjemah Python | **Python Interpreter** | Mesin eksekusi CPython / runtime Python |
| Penyunting kode | **Code Editor** | Perangkat lunak editor teks (misal: VS Code) |
| Kamus Python | **Python Dictionary** / **`dict`** | Struktur data hash map pasangan key-value |
| Daftar Python | **Python List** / **`list`** | Koleksi elemen berurutan yang mutable |
| Pewarisan | **Inheritance** | Relasi turunan class pada paradigma OOP |
| Pengkapsulan | **Encapsulation** | Penyembunyian state internal via private attribute |
| Polimorfisme | **Polymorphism** | Kemampuan antarmuka seragam (duck typing/overriding) |
| Pembelajaran mesin | **Machine Learning** | Disiplin dan algoritma pemodelan data |
| Pembelajaran mendalam | **Deep Learning** | Arsitektur neural network berlapis banyak |
| Jaringan saraf tiruan | **Artificial Neural Network** | Model jaringan komputasi terinspirasi biologis |
| Pelatihan model | **Model Training** / **Training** | Proses optimasi bobot model dengan data |
| Penyetelan halus | **Fine-Tuning** | Penyesuaian bobot pre-trained model |
| Penyebaran model | **Model Deployment** / **Deployment** | Penerbitan model/aplikasi ke server produksi |
| Penanganan pengecualian | **Exception Handling** | Blok proteksi `try-except-finally` |
| Penanganan kesalahan | **Error Handling** | Strategi defensif mitigasi galat runtime |
| Pengujian unit | **Unit Testing** | Validasi fungsional komponen via test suite |
| Cakupan pengujian | **Test Coverage** | Persentase eksekusi kode yang diuji |
| Pemanggilan balik | **Callback** | Fungsi yang diteruskan sebagai argumen |
| Pengulangan asinkron | **Asynchronous Execution** | Operasi non-blocking berbasis event loop |
| Manajemen dependensi | **Dependency Management** | Pengelolaan pustaka via pip/pyproject.toml |

> **Catatan Penting:** Tabel di atas menetapkan terminologi preferensi resmi untuk Python Learning Hub, bukan menyatakan bahwa setiap padanan bahasa Indonesia salah secara inheren. Istilah Bahasa Indonesia yang telah mapan seperti **algoritma**, **variabel**, **parameter**, **perulangan**, **percabangan**, **pengujian**, dan **evaluasi** tetap digunakan secara wajar dan natural.

---

## 3. Contoh Penulisan Kalimat yang Benar (*BAD vs. GOOD*)

### Contoh 1: Konfigurasi Tooling
- ❌ **SALAH (BAD):**  
  *"Pada bab ini kita akan menyiapkan lingkungan pengembangan Python dan memasang penerjemah Python."*
- ✔️ **BENAR (GOOD):**  
  *"Pada bab ini kita akan menyiapkan Python Development Environment dan menginstal Python Interpreter."*

### Contoh 2: Struktur Data
- ❌ **SALAH (BAD):**  
  *"Buat kamus yang berisi pasangan kunci dan nilai."*
- ✔️ **BENAR (GOOD):**  
  *"Buat dictionary yang menyimpan pasangan key-value."*

### Contoh 3: Machine Learning & Pemodelan
- ❌ **SALAH (BAD):**  
  *"Kita akan melakukan pelatihan model pembelajaran mesin."*
- ✔️ **BENAR (GOOD):**  
  *"Kita akan melakukan training pada model Machine Learning."*

### Contoh 4: Isolasi Proyek & Dependensi
- ❌ **SALAH (BAD):**  
  *"Aktifkan lingkungan virtual sebelum menginstal paket agar tidak mencemari lingkungan global."*
- ✔️ **BENAR (GOOD):**  
  *"Aktifkan Virtual Environment sebelum menginstal paket agar tidak mencemari Python environment global."*

### Contoh 5: Paradigma Berorientasi Objek (OOP)
- ❌ **SALAH (BAD):**  
  *"Pewarisan dan pengkapsulan memungkinkan kelas anak mewarisi atribut kelas induk."*
- ✔️ **BENAR (GOOD):**  
  *"Prinsip Inheritance dan Encapsulation memungkinkan subclass mewarisi atribut dari superclass."*

### Contoh 6: Robustness & Testing
- ❌ **SALAH (BAD):**  
  *"Gunakan penanganan pengecualian dan lakukan pengujian unit dengan cakupan pengujian tinggi."*
- ✔️ **BENAR (GOOD):**  
  *"Terapkan Exception Handling dan lakukan Unit Testing dengan target Test Coverage yang tinggi."*

---

## 4. Panduan Tipografi & Format Teks

### A. Format Kode Inline (`code span`)
Gunakan backtick (`` `...` ``) untuk:
- Tipe data bawaan: `int`, `float`, `str`, `bool`, `list`, `dict`, `set`, `tuple`.
- Kata kunci Python: `def`, `class`, `return`, `with`, `try`, `except`, `raise`, `import`, `yield`.
- Variabel, fungsi, class, argumen: `hitung_snr()`, `node_id`, `NetworkNode`.
- File, direktori, ekstensi: `pyproject.toml`, `.venv`, `requirements.txt`, `main.py`.
- Perintah terminal / CLI: `python3 -m venv .venv`, `py -m pip install -r requirements.txt`.

### B. Format Teks Penjelasan
- **Huruf Tebal (**teks**)**: Digunakan untuk penekanan konsep penting saat pertama kali dikenalkan.
- **Huruf Miring (*teks*)**: Digunakan untuk istilah asing non-kode, misalnya *lazy evaluation*, *type coercion*, *race condition*.
- **KaTeX / LaTeX Math**: Digunakan untuk formula matematis atau notasi asimtotik komputasi ($O(1)$, $O(\log n)$, $O(n)$, $O(n \log n)$).

---

## 5. Komentar Kode & Docstring

Komentar di dalam skrip Python (`# komentar`) dan docstring (`"""docstring"""`) mematuhi kaidah:
1. Narasi menggunakan Bahasa Indonesia yang ringkas dan komunikatif.
2. Identifier dan nama fungsi menggunakan konvensi PEP 8.
3. Istilah teknis tetap dalam Bahasa Inggris.

```python
# Inisialisasi Virtual Environment dan konfigurasi Dependency Management
# Memuat data telemetri ke dalam dictionary dengan skema key-value terstruktur
telemetry_data: dict[str, float] = {
    "latency_ms": 24.5,
    "packet_loss_pct": 0.02
}
```

---

## 6. Integrasi dengan Aturan AI Agent (Antigravity Workspace Rule)

Kebijakan ini dienkapsulasi ke dalam berkas aturan workspace agent:
- `.agent/rules/technical-terminology.md`
- Berlaku otomatis bagi seluruh asisten AI pemrograman untuk memvalidasi setiap generasi modul, slide, latihan, dan tutorial baru.
