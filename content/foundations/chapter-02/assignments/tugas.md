# Tugas Praktik Chapter 02: Validasi Parameter Transceiver BTS

## Deskripsi Tugas
Dalam stasiun pemancar seluler (BTS), paket konfigurasi sering kali diterima dalam bentuk teks mentah dari file konfigurasi atau antarmuka jaringan. Sebelum transceiver diaktifkan, sistem otomasi harus melakukan validasi tipe data dan konversi nilai agar tidak menyebabkan kegagalan sistem.

Anda diminta membuat modul `tugas_02.py` yang memproses parameter stasiun pemancar, mengonversinya ke tipe data yang sesuai, dan memvalidasi keabsahan nilai-nilai tersebut.

---

## Petunjuk Pengerjaan

1. **Unduh Starter Code:** Gunakan berkas `tugas_02.py`.
2. **Spesifikasi Input Mentah:**
   ```python
   raw_bts_name = "  BTS-LampungSelatan-02  "
   raw_frequency_mhz = "2100.5"
   raw_tx_power_watt = "40"
   raw_is_operational = "1"
   ```
3. **Tahap Pemrosesan & Konversi:**
   - Bersihkan spasi pada nama BTS menggunakan metode bawaan `.strip()`.
   - Konversikan frekuensi ke tipe `float`.
   - Konversikan daya pancar ke tipe `int`.
   - Konversikan status operasional ke tipe `bool` (dari integer `1` &rarr; `True`, `0` &rarr; `False`).
4. **Validasi Nilai Parameter:**
   - Nama BTS harus bertipe `str` dan panjang karakter $> 5$.
   - Frekuensi harus bertipe numerik (`float`/`int`) dan berada di rentang 700.0 s.d. 3500.0 MHz.
   - Daya pancar harus bertipe `int` dan bernilai antara 1 s.d. 100 Watt.
   - Status operasional harus bertipe `bool`.
5. **Format Laporan Output Terminal:**
   ```text
   ==================================================
           VALIDASI KONFIGURASI TRANSCEIVER BTS
   ==================================================
   Nama Stasiun      : BTS-LampungSelatan-02 (str, 21 karakter)
   Frekuensi Operasi : 2100.5 MHz (float)
   Daya Pancar       : 40 W (int)
   Status Aktif      : True (bool)
   --------------------------------------------------
   Status Validasi   : SEMUA PARAMETER VALID (SIAP TRANSMISI)
   ==================================================
   ```

---

## Rubrik Penilaian (Total Bobot: 100%)

| Kriteria Penilaian | Bobot | Deskripsi Capaian |
|:---|:---:|:---|
| **Kebenaran Type Casting** | 40% | Mengonversi keempat nilai string mentah ke tipe data target (`str`, `float`, `int`, `bool`) secara akurat tanpa galat. |
| **Logika Validasi Parameter** | 30% | Memvalidasi tipe data dengan `isinstance()` dan memeriksa batasan nilai numerik (frekuensi dan daya). |
| **Kepatuhan Gaya PEP 8** | 20% | Penamaan variabel deskriptif snake_case, kerapian spasi, dan struktur kode bersih. |
| **Pengujian Kasus Uji** | 10% | Menyertakan kasus uji tambahan dengan input valid dan input di luar batas toleransi. |
