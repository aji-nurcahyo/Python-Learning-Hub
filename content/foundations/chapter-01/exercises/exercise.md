# Latihan Terarah — Chapter 01: Introduction to Python

Kerjakan serangkaian latihan berikut untuk memperkuat pemahaman fundamental Anda tentang eksekusi skrip, penulisan fungsi `print()`, dan penanganan galat.

---

### Latihan 1: Kartu Identitas Node Telekomunikasi
**Tujuan:** Memahami fungsi `print()`, penulisan teks, angka, dan pemisah baris.

1. Buat berkas baru bernama `latihan_01_identitas.py`.
2. Tulis skrip yang mencetak identitas node BTS dengan spesifikasi berikut:
   - Nama Node: `BTS-Sukarame-BandarLampung`
   - Frekuensi Kerja: `1800 MHz`
   - Saluran Aktif: `32 Saluran`
   - Status Operasional: `ONLINE`
3. Gunakan pemisah tanda hubung panjang atau garis pembatas untuk membuat tampilan rapi seperti kartu laporan konsol.

---

### Latihan 2: Eksperimen Indentasi dan Sintaks
**Tujuan:** Mengamati pesan galat dari interpreter CPython.

1. Tulis kode sengaja yang melanggar kaidah sintaks:
   ```python
   print("Uji coba pesan tanpa kurung penutup"
   ```
2. Jalankan skrip dan cermati pesan error `SyntaxError` yang muncul di terminal.
3. Perbaiki kesalahan tersebut dengan menutup tanda kurung.
4. Buat blok percabangan sederhana tanpa memberi spasi indentasi:
   ```python
   nilai = 10
   if nilai > 5:
   print("Nilai lebih besar dari lima")
   ```
5. Perhatikan munculnya `IndentationError: expected an indented block`. Perbaiki dengan menambahkan 4 spasi pada baris `print()`.

---

### Latihan 3: Kalkulasi Jarak Perambatan Sinyal
**Tujuan:** Melakukan perhitungan aritmatika sederhana dan mencetak hasilnya.

1. Diketahui waktu propagasi sinyal optik atau radio adalah $5 \times 10^{-6}$ detik (5 mikrodetik).
2. Dengan kecepatan gelombang $c = 3 \times 10^8\text{ m/s}$, hitung jarak tempuh gelombang menggunakan rumus:
   $$\text{jarak} = \text{kecepatan} \times \text{waktu}$$
3. Tampilkan hasil perhitungan jarak dalam satuan meter dan kilometer ke layar terminal.
