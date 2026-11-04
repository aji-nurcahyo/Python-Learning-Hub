# Latihan Terarah — Chapter 02: Variables & Data Types

Kerjakan latihan berikut untuk menguji pemahaman Anda mengenai variabel, tipe data skalar, konversi tipe eksplisit, dan validasi tipe objek.

---

### Latihan 1: Deklarasi Parameter Jaringan Seluler
**Tujuan:** Mendeklarasikan variabel dengan tipe skalar yang sesuai standar PEP 8.

1. Buat berkas `latihan_02_parameter.py`.
2. Deklarasikan variabel-variabel berikut dengan tipe data yang tepat:
   - `nama_operator` (string): `"Telkomsel-ITERA"`
   - `alokasi_bandwidth_mhz` (float): `20.0`
   - `jumlah_pelanggan_aktif` (integer): `1425`
   - `mimo_didukung` (boolean): `True`
3. Gunakan fungsi `type()` untuk menampilkan tipe data masing-masing variabel ke layar konsol.

---

### Latihan 2: Pengolahan Data Telemetri Mentah (Type Casting)
**Tujuan:** Mengonversi data string dari sensor menjadi tipe numerik yang siap dihitung.

1. Diberikan data string hasil pembacaan telemetri sensor:
   ```python
   raw_temperature = "37.8"
   raw_channel_count = "16"
   raw_alarm_flag = "0"
   ```
2. Konversikan:
   - `raw_temperature` menjadi `float`.
   - `raw_channel_count` menjadi `int`.
   - `raw_alarm_flag` menjadi `bool` (ingat: `"0"` sebagai string bernilai `True`, perhatikan konversi terlebih dahulu ke integer `int("0")` sebelum ke `bool`!).
3. Tampilkan nilai setelah dikonversi beserta tipe datanya.

---

### Latihan 3: Pemeriksaan Kesesuaian Tipe Data (isinstance)
**Tujuan:** Menulis fungsi validator untuk mencegah terjadinya TypeError saat runtime.

1. Tulis fungsi `validasi_transmisi(frekuensi, daya)` yang memeriksa:
   - `frekuensi` harus bertipe `int` atau `float` dan nilainya harus $> 0$.
   - `daya` harus bertipe `int` atau `float` dan nilainya harus $\ge 0$.
2. Fungsi mengembalikan `True` jika valid, dan `False` jika terdapat tipe yang tidak sesuai atau nilai di luar batas.
3. Uji fungsi dengan input: `(1800.5, 20)`, `("1800", 20)`, dan `(-900, 10)`.

