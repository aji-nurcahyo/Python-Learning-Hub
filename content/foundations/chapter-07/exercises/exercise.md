# Latihan Terarah — Chapter 07: Strings & Text Processing

Kerjakan latihan berikut untuk menguji kemampuan Anda dalam memanfaatkan metode-metode string, slicing, pencarian teks, dan validasi karakter di Python.

---

### Latihan 1: Ekstraktor Protokol & Port URL Jaringan
**Tujuan:** Menggunakan `.find()`, `.split()`, dan slicing.

1. Diberikan string URL endpoint gateway:
   `url = "https://192.168.1.100:8443/telemetry/v1"`
2. Ekstrak:
   - Protokol (misal: `"https"` menggunakan pemisah `"://"`).
   - Alamat IP host (misal: `"192.168.1.100"`).
   - Nomor Port (misal: `"8443"`).
3. Cetak ketiga informasi tersebut dalam format kartu ringkas.

---

### Latihan 2: Penyensoran Data Sensitif / Masking
**Tujuan:** Menerapkan string slicing dan perataan string.

1. Sebuah ID perangkat transmisi memiliki nomor seri:
   `serial_number = "SN-2026-ITERA-88492"`
2. Buat string tersensor (*masked string*) di mana 5 digit angka terakhir disembunyikan dengan karakter bintang `*****`:
   `"SN-2026-ITERA-*****"`
3. Lakukan operasi ini dengan memanfaatkan pemotongan slicing `serial_number[:-5]` dan penggabungan string `+ "*****"`.

---

### Latihan 3: Pemeriksaan Kesesuaian Alamat MAC Nirkabel
**Tujuan:** Menggunakan `.split()`, `len()`, dan `.isalnum()`.

1. Alamat MAC standar terdiri dari 6 pasang karakter heksadesimal dipisahkan titik dua:
   `mac = "00:1A:2B:3C:4D:5E"`
2. Buat fungsi `validasi_mac(mac_str: str) -> bool` yang memeriksa:
   - Apakah terdapat tepat 6 segmen saat dipecah dengan `.split(":")`.
   - Apakah setiap segmen memiliki panjang tepat 2 karakter.
   - Apakah setiap segmen merupakan karakter alfanumerik.
3. Uji dengan `"00:1A:2B:3C:4D:5E"`, `"00:1A:2B:3C:4D"`, dan `"00:1A:2B:3C:4D:ZZZ"`.
