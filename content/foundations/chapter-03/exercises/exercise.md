# Latihan Terarah — Chapter 03: Operators & Expressions

Kerjakan latihan berikut untuk memperdalam penguasaan Anda terhadap operator aritmatika, presedensi pengerjaan, dan ekspresi logika boolean di Python.

---

### Latihan 1: Pembagian Waktu Transmisi Time-Slot (Modulo & Floor Division)
**Tujuan:** Menggunakan operator `//` dan `%` dalam penjadwalan frame telekomunikasi.

1. Dalam standar seluler TDMA/TDD, waktu transmisi dibagi menjadi frame yang terdiri dari sejumlah *time-slot*.
2. Diketahui total ada `147` paket data yang harus dikirim. Setiap frame mampu menampung tepat `16` paket.
3. Hitung:
   - Jumlah frame penuh yang dibutuhkan menggunakan pembagian bulat (`//`).
   - Sisa paket data pada frame terakhir yang belum penuh menggunakan operator modulo (`%`).
4. Cetak hasilnya ke layar terminal dengan format deskriptif.

---

### Latihan 2: Evaluasi Status Siaga Multi-Kondisi (Logika Boolean)
**Tujuan:** Menggabungkan operator relasional dan logika `and`, `or`, `not`.

1. Sebuah node telekomunikasi memiliki 3 sensor dengan nilai berikut:
   - `suhu_celsius = 42.5` (Batas normal: $\le 45.0$)
   - `beban_cpu_persen = 88.0` (Batas normal: $\le 80.0$)
   - `koneksi_redundansi = True`
2. Buat ekspresi logika untuk:
   - `kondisi_bahaya`: jika suhu $> 45.0$ **atau** beban CPU $> 90.0$.
   - `perlu_optimasi`: jika beban CPU $> 80.0$ **dan tidak ada** bahaya.
   - `status_aman`: jika tidak dalam kondisi bahaya **dan** memiliki koneksi redundansi.
3. Cetak nilai boolean dari masing-masing status.

---

### Latihan 3: Perhitungan Panjang Gelombang Nirkabel Wi-Fi
**Tujuan:** Mengimplementasikan formula fisika $\lambda = c / f$ dengan presedensi matematika yang tepat.

1. Diketahui kecepatan cahaya $c = 3 \times 10^8\text{ m/s}$.
2. Hitung panjang gelombang (dalam satuan sentimeter) untuk dua pita frekuensi Wi-Fi:
   - Wi-Fi 2.4 GHz ($f_1 = 2.4 \times 10^9\text{ Hz}$)
   - Wi-Fi 5.0 GHz ($f_2 = 5.0 \times 10^9\text{ Hz}$)
3. Tampilkan perbandingan panjang gelombang kedua frekuensi tersebut dan simpulkan frekuensi mana yang memiliki perambatan gelombang lebih pendek.

