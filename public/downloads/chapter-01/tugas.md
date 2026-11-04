# Tugas Praktik Chapter 01: Verifikasi Environment Node Telekomunikasi

## Deskripsi Tugas
Sebagai calon insinyur telekomunikasi atau pengembang perangkat lunak otomasi, langkah pertama saat melakukan konfigurasi sistem adalah memeriksa kesiapan lingkungan eksekusi (*runtime environment inspection*).

Anda diminta untuk membuat skrip Python mandiri bernama `tugas_01.py` yang membaca parameter lingkungan Python bawaan dan menampilkan status inisialisasi stasiun pemancar telekomunikasi.

---

## Petunjuk Pengerjaan

1. **Unduh Starter Code:** Ambil berkas `tugas_01.py` yang telah disediakan.
2. **Gunakan Modul Standar:**
   - Gunakan modul bawaan Python `sys` untuk membaca versi interpreter: `sys.version.split()[0]`.
   - Gunakan modul bawaan `platform` untuk membaca nama sistem operasi: `platform.system()`.
3. **Spesifikasi Output Terminal:**
   Skrip harus menampilkan laporan berformat kartu ringkas seperti berikut:
   ```text
   ==================================================
        SISTEM MONITORING NODE TELEKOMUNIKASI
   ==================================================
   Sistem Operasi      : <Nama OS>
   Versi CPython       : <Versi Python>
   ID Perangkat Node   : NODE-TELKOM-ITERA-01
   Frekuensi Dasar     : 1800.0 MHz
   Waktu Propagasi (1km): 3.33 mikrodetik
   Status Inisialisasi : OPERASIONAL / SIAP
   ==================================================
   ```
4. **Kaidah Penulisan:**
   - Gunakan indentasi konsisten 4 spasi standar PEP 8.
   - Sertakan docstring di awal berkas sesuai standar PEP 257.
   - Bungkus alur utama di dalam blok `if __name__ == '__main__':`.

---

## Rubrik Penilaian (Total Bobot: 100%)

| Kriteria Penilaian | Bobot | Deskripsi Capaian |
|:---|:---:|:---|
| **Kebenaran Fungsional** | 40% | Skrip berhasil membaca modul `sys` dan `platform`, menghitung waktu propagasi secara akurat, dan mencetak seluruh data yang diminta. |
| **Kepatuhan Gaya PEP 8** | 30% | Penamaan variabel menggunakan `snake_case`, penggunaan indentasi 4 spasi tanpa karakter tab, spasi di sekitar operator. |
| **Dokumentasi & Docstring** | 20% | Menyertakan modul docstring dan komentar yang menjelaskan tujuan setiap bagian kode secara logis. |
| **Struktur Eksekusi** | 10% | Menggunakan idiom `if __name__ == '__main__':` untuk menjaga modularitas program. |

