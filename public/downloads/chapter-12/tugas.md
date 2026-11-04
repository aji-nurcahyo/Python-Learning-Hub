# Proyek Akhir Terpadu — Chapter 12: Student Data Management System

## Deskripsi Proyek Capstone
Proyek Akhir Terpadu (*Foundations Capstone Project*) merupakan modul kulminasi dari **Level 1: Python Foundations** pada platform **Python Learning Hub**. 

Tujuan proyek ini adalah merancang, mengimplementasikan, dan menguji aplikasi Command-Line Interface (CLI) berskala utuh bernama **Student Data Management System** (Sistem Manajemen Data Mahasiswa). Aplikasi ini mengintegrasikan seluruh kompetensi pemrograman prosedural dan modular yang telah dipelajari sepanjang Chapter 01 hingga Chapter 11:
- Variabel, tipe data skalar, dan penataan string (Ch 02, 07)
- Ekspresi aritmatika, logika, dan operator perbandingan (Ch 03)
- Pemformatan input dan output konsol berbasis tabel rapi (Ch 04)
- Percabangan kondisional bertingkat untuk validasi aturan bisnis (Ch 05)
- Perulangan iteratif untuk navigasi menu dan manipulasi data (Ch 06)
- Struktur data koleksi majemuk *list of dictionaries* (Ch 08, 09)
- Modularitas fungsi, parameterisasi, dan pemisahan *pure business logic* (Ch 10)
- Pengorganisasian modul multi-berkas dan penanganan eksepsi kokoh (Ch 11)

---

## Persyaratan Fungsional (10 Fitur Wajib)

Aplikasi harus mengimplementasikan 10 kapabilitas fungsional berikut:
1. **Menu Interaktif Utama:** Menampilkan antarmuka navigasi konsol dengan opsi menu bernomor yang berulang terus hingga pengguna memilih keluar secara sadar.
2. **Pencatatan Mahasiswa Baru (Create):** Menerima masukan NIM, Nama Lengkap, dan Nilai Akhir, lalu menyimpannya ke dalam koleksi basis data in-memory.
3. **Penyajian Data Keseluruhan (Read):** Menampilkan seluruh data mahasiswa terdaftar dalam format tabel konsol yang rapi dengan nomor urut, NIM, Nama, Nilai (2 desimal), dan Predikat Huruf.
4. **Pencarian Multi-Kriteria (Search):** Mencari mahasiswa berdasarkan kecocokan NIM atau bagian dari nama (*substring search*, *case-insensitive*).
5. **Pembaruan Data (Update):** Memperbarui nama dan/atau nilai mahasiswa berdasarkan NIM target, tanpa mengubah identitas NIM itu sendiri.
6. **Penghapusan Rekaman (Delete):** Menghapus data mahasiswa dari basis data in-memory berdasarkan NIM dengan konfirmasi keamanan.
7. **Kalkulasi Rata-Rata Kelas (Statistics - Average):** Menghitung rata-rata nilai akademik seluruh kelas secara akurat.
8. **Identifikasi Nilai Ekstrem (Statistics - Min/Max):** Menemukan nilai tertinggi dan nilai terendah beserta daftar nama mahasiswa peraih nilai tersebut.
9. **Validasi Masukan Kokoh (Input Validation & Error Handling):**
   - NIM: Wajib digit angka, panjang 5–15 karakter, dan tidak boleh duplikat (*unique primary key*).
   - Nama: Tidak boleh kosong/hanya spasi, minimal 2 karakter alfabet.
   - Nilai: Angka numerik (float/int) valid dalam rentang tertutup $[0.0, 100.0]$.
   - Menu: Masukan opsi tidak valid tidak boleh menyebabkan program *crash*.
10. **Terminasi Aman (Safe Exit):** Menyediakan opsi keluar dari sistem dengan pesan penutup yang ramah dan membersihkan memori kerja secara terkontrol.

---

## Arsitektur Teknis & Batasan Implementasi

1. **Struktur Multi-Berkas:**
   Proyek harus dibagi menjadi minimal 3 modul Python yang saling terpisah sesuai tanggung jawabnya (*Separation of Concerns*):
   - `validators.py`: Modul fungsi murni untuk memvalidasi masukan pengguna.
   - `student_manager.py`: Modul logika bisnis inti pemrosesan data (independen dari panggilan `input()` atau `print()`).
   - `main.py`: Modul antarmuka pengguna CLI interaktif yang mengelola loop menu utama dan format tampilan terminal.
2. **Model Data:**
   Menggunakan koleksi majemuk murni Python: *list of dictionaries*:
   ```python
   students = [
       {"nim": "121140001", "name": "Budi Santoso", "grade": 86.5},
       {"nim": "121140002", "name": "Siti Nurhaliza", "grade": 92.0},
   ]
   ```
3. **Pustaka Standar Saja:** Dilarang menggunakan dependensi eksternal pihak ketiga (misalnya `pandas`, `tabulate`, `rich`, atau basis data eksternal `sqlite3`). Gunakan fitur bawaan CPython murni.
4. **Type Hints & Docstrings:** Setiap fungsi wajib menyertakan anotasi tipe data (*type hints*) dan dokumentasi fungsi (*docstring*) yang informatif.

---

## Format Tampilan Menu & Tabel Konsol

```text
==========================================================
        SISTEM MANAJEMEN DATA MAHASISWA (CLI)
==========================================================
1. Tampilkan Semua Mahasiswa
2. Tambah Mahasiswa Baru
3. Cari Mahasiswa (NIM / Nama)
4. Perbarui Data Mahasiswa
5. Hapus Data Mahasiswa
6. Statistik Nilai Akademik
7. Tampilkan Peringkat Nilai (Ranking)
8. Keluar dari Aplikasi
==========================================================
Pilih menu [1-8]: 1

=== DAFTAR DATA MAHASISWA ===
----------------------------------------------------------------------
No   | NIM          | Nama Lengkap                   | Nilai   | Predikat
----------------------------------------------------------------------
1    | 121140001    | Budi Santoso                   | 86.50   | A       
2    | 121140002    | Siti Nurhaliza                 | 92.00   | A       
3    | 121140003    | Ahmad Fauzi                    | 74.25   | B       
----------------------------------------------------------------------
Total: 3 mahasiswa terdaftar.
```

---

## Rubrik Penilaian Proyek Capstone (Total Bobot: 100%)

| Komponen Penilaian | Bobot | Kriteria Evaluasi dan Standar Capaian |
|:---|:---:|:---|
| **1. Arsitektur Modular & Desain Sistem** | 15% | Kode terpisah secara modular (`validators.py`, `student_manager.py`, `main.py`). Logika bisnis tidak tercampur aduk dengan fungsi I/O konsol (`input`/`print`). |
| **2. Logika CRUD & Pencarian** | 25% | Operasi penambahan, pembacaan tabel, pembaruan data, penghapusan, dan algoritma pencarian multi-kriteria berjalan sempurna tanpa *bug*. |
| **3. Validasi Masukan & Ketahanan Sistem** | 20% | Pencegahan duplikasi NIM, validasi tipe nilai dan rentang numerik 0–100, penanganan masukan kosong atau salah format, dan ketahanan terhadap potensi *runtime error*. |
| **4. Analisis Statistik & Fitur Analitik** | 20% | Perhitungan nilai rata-rata, deteksi nilai ekstrem (tertinggi/terendah), identifikasi mahasiswa peraih skor tertinggi, serta pemetaan predikat huruf (A, B, C, D, E) tepat. |
| **5. Kerapian Kode, Type Hints & Format CLI** | 20% | Mematuhi konvensi PEP 8, memiliki type hints lengkap pada parameter dan return value, docstrings jelas, dan tampilan antarmuka CLI rapi terstruktur. |
