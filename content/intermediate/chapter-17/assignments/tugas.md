# Tugas Praktik 17: Telecom Gateway Data Pipeline & Serialization Suite
## Python Learning Hub — Level 2: Intermediate

---

### Deskripsi Tugas

Dalam industri telekomunikasi modern, gateway transmisi menerima aliran data dari berbagai stasiun pemancar (*Base Transceiver Station* / BTS) yang tersimpan dalam format file CSV lokal. Sebagai Network Software Engineer, Anda diminta untuk merancang dan membangun modul data pipeline yang tangguh untuk:

1. Membaca dan memvalidasi berkas CSV telemetri node jaringan.
2. Menyaring rekaman anomali (*invalid records*) dan mencatat jumlah baris yang berhasil/gagal dimuat.
3. Mengizinkan penambahan (*insert*) dan pembaruan (*update*) rekaman stasiun BTS secara in-memory.
4. Menghasilkan ringkasan statistik (rata-rata kapasitas, total stasiun aktif, stasiun offline).
5. Mengekspor basis data terstruktur ke format JSON dengan struktur yang siap dikonsumsi oleh dashboard web.
6. Menggunakan library `pathlib.Path` untuk mengelola path berkas dan membuat folder arsip secara otomatis.

---

### Persyaratan Fungsional & Teknis

1. **Penggunaan Context Manager `with`:**
   - Seluruh operasi berkas I/O (baca, tulis, tambah) wajib menggunakan context manager `with` dan menyertakan parameter `encoding="utf-8"`.
   - Untuk berkas CSV, wajib menyertakan `newline=""` pada saat membuka file.
2. **Validasi Data Defensif:**
   - Field wajib: `id`, `lokasi`, `frekuensi_mhz`, `kapasitas_gbps`, `status`.
   - Konversi nilai `frekuensi_mhz` dan `kapasitas_gbps` ke tipe `float`. Jika gagal, lewati baris tersebut tanpa menghentikan eksekusi program.
3. **Penyimpanan & Export JSON:**
   - Gunakan `json.dump()` dengan format rapi (`indent=2` atau `indent=4`) untuk mengekspor data yang lolos validasi.
4. **Penanganan Kasus Hilang (*Missing Files*):**
   - Tangani `FileNotFoundError` secara eksplisit apabila berkas CSV yang dituju tidak ada pada sistem.

---

### Rubrik Penilaian (Total: 100 Poin)

| Kriteria Penilaian | Bobot | Deskripsi Kualitas |
| :--- | :---: | :--- |
| **1. Penguasaan File I/O & Context Manager** | 25 Poin | Menggunakan `with open()` secara konsisten, menyertakan `encoding="utf-8"`, dan `newline=""` pada CSV. |
| **2. Parsing & Manipulasi CSV Tabular** | 25 Poin | Memanfaatkan `csv.DictReader` dan `csv.DictWriter` secara tepat dengan pemetaan header yang valid. |
| **3. Serialisasi & Deserialisasi JSON** | 25 Poin | Mampu mengonversi data dictionary ke JSON terstruktur dengan `json.dump()`/`json.load()` secara rapi. |
| **4. Validasi Data & Penanganan Error `pathlib`** | 25 Poin | Penanganan `FileNotFoundError`, validasi tipe numerik, dan integrasi modul modern `pathlib.Path`. |

---

### Berkas Pengumpulan

- `tugas_17.py`: Skrip mandiri implementasi solusi yang mematuhi standar PEP 8, memiliki type hints, dan docstring lengkap.
