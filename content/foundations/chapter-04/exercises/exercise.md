# Latihan Terarah — Chapter 04: Input & Output

Kerjakan latihan berikut untuk melatih kemampuan Anda dalam menyusun antarmuka teks interaktif dan memformat keluaran konsol secara rapi menggunakan f-strings.

---

### Latihan 1: Prompt Interaktif Pengukuran Sinyal
**Tujuan:** Menggunakan fungsi `input()`, pembersihan spasi, dan konversi ke float.

1. Tulis skrip interaktif yang meminta pengguna memasukkan:
   - Nama Stasiun Pemancar (teks).
   - Nilai daya terima RSRP dalam satuan dBm (angka desimal).
2. Bersihkan input nama menggunakan `.strip()`.
3. Konversikan nilai RSRP menjadi `float`.
4. Cetak pesan konfirmasi: `"Data RSRP untuk stasiun [NAMA] tercatat sebesar [NILAI] dBm."`

---

### Latihan 2: Pemformatan Angka Rasio & Notasi Ilmiah
**Tujuan:** Menguasai format specifier `:.2f`, `:.2e`, dan `:.1%`.

1. Diberikan data variabel:
   ```python
   kecepatan_bit = 1000000000  # 1 Gbps (10^9 bps)
   rugi_paket = 0.00245        # 0.245% packet loss
   sensitivitas = 0.0000000012 # 1.2 x 10^-9 Watt
   ```
2. Gunakan satu blok f-string untuk menampilkan:
   - Kecepatan bit dalam pemisah ribuan koma (`:,`).
   - Rasio rugi paket dalam format persentase dua angka desimal (`:.2%`).
   - Sensitivitas penerima dalam format notasi ilmiah eksponensial (`:.2e`).

---

### Latihan 3: Generator Laporan Tabel Inventaris Frekuensi
**Tujuan:** Merancang tata letak tabel dengan perataan kolom `<` (kiri), `>` (kanan), dan `^` (tengah).

1. Tampilkan tabel inventaris spektrum frekuensi dengan header:
   `BAND` (lebar 8, rata kiri), `RENTANG FREKUENSI` (lebar 20, rata tengah), dan `ALOKASI OPERATOR` (lebar 18, rata kanan).
2. Cetak minimal 3 baris data alokasi operator seluler dengan batas garis horizontal di atas dan di bawah tabel.

