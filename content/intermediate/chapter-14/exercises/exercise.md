# Latihan Terarah — Chapter 14: Comprehensions & Iterators

Uji kecakapan Anda dalam menulis transformasi data yang ekspresif menggunakan list, dict, set comprehension, generator expression, serta protokol iterator.

---

### Latihan 1: Ekstraksi Log Frekuensi Radio (List Comprehension & Ternary)
**Tujuan:** Menggunakan list comprehension dengan kondisi `if` dan ekspresi bersyarat `if-else`.

1. Diberikan data pengukuran SNR (*Signal-to-Noise Ratio*) dalam dB:
   ```python
   snr_log = [14.2, 8.5, 22.0, 4.1, 18.7, 9.9, 27.5]
   ```
2. Buat list `snr_lulus` yang hanya memuat nilai SNR $\ge 10.0\text{ dB}$.
3. Buat list `status_kualitas` yang mengubah setiap nilai menjadi `"MEMENUHI"` jika $\ge 15.0\text{ dB}$, dan `"MARGINAL"` jika di bawahnya.
4. Tuliskan masing-masing dalam satu baris ekspresi list comprehension.

---

### Latihan 2: Inversi & Normalisasi Dictionary IP Host (Dict Comprehension)
**Tujuan:** Membalik pasangan `key-value` (*inversion*) dan membersihkan teks pada `dictionary`.

1. Diberikan pemetaan nama node ke alamat IP:
   ```python
   node_ip = {
       "  Router-Inti ": "192.168.1.1",
       "Switch-Akses-01": "192.168.1.10",
       " Switch-Akses-02 ": "192.168.1.20"
   }
   ```
2. Buat dictionary baru `ip_ke_node` di mana alamat IP menjadi `key`, dan nama node yang sudah dibersihkan spasinya (`.strip()`) menjadi `value`.
3. Hanya sertakan node yang memiliki akhiran `"Akses-01"` atau `"Akses-02"`.

---

### Latihan 3: Penggabungan Paralel Dua Aliran Sensor (zip & enumerate)
**Tujuan:** Mengombinasikan data pengukuran multi-kanal menggunakan fungsi bawaan `zip()` dan `enumerate()`.

1. Diberikan dua deret data sensor:
   ```python
   suhu_celsius = [26.5, 28.0, 31.2, 35.4]
   kelembaban_rh = [65.0, 60.5, 52.0, 45.0]
   ```
2. Gunakan `enumerate()` dan `zip()` untuk mencetak laporan berformat:
   ```text
   Detik 1 -> Suhu: 26.5 C | Kelembaban: 65.0 %
   Detik 2 -> Suhu: 28.0 C | Kelembaban: 60.5 %
   ...
   ```

---

### Latihan 4: Generator Pemrosesan Deret Bilangan Prima
**Tujuan:** Menerapkan evaluasi *lazy* dengan generator expression untuk menghemat konsumsi memori.

1. Buat fungsi helper `apakah_prima(n: int) -> bool`.
2. Gunakan generator expression `(p for p in range(2, 1000) if apakah_prima(p))` untuk menghasilkan bilangan prima.
3. Gunakan `next()` untuk mengambil 5 bilangan prima pertama secara bertahap tanpa membangkitkan seluruh list ke dalam RAM.

