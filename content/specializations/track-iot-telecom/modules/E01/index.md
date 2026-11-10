# Modul E01: Sensor Telemetry, Serial Framing & Checksums

## 1. Realita Komunikasi Perangkat Keras & UART/Serial
Saat membaca data dari mikrokontroler (ESP32, Arduino, STM32) lewat kabel USB-Serial atau modul RF, data tidak datang rapi seperti tabel CSV di disk. Pengembang IoT sering menghadapi:
- **Sisa Buffer Saat Koneksi Baru Terbuka:** Baris pertama terpotong di tengah (`58.0,3.79`).
- **Bit Flip Akibat Derau Elektromagnetik:** Karakter berubah menjadi angka mustahil.

Oleh sebab itu, protokol serial baku selalu membungkus setiap pesan dalam **framing** (awalan `$` dan akhiran `*CHECKSUM`).

---

## 2. Verifikasi Integritas dengan XOR Checksum
Pada protokol berformat `$TELEM,101,28.4,62.0,3.85*7F`:
1. Ambil substring isi pesan (*payload*) di antara `$` dan `*`.
2. Lakukan operasi bitwise XOR (`^`) pada nilai kode ASCII (`ord(ch)`) seluruh karakter di dalam *payload*.
3. Ubah hasil 8-bit menjadi dua digit heksadesimal (`f"{val:02X}"`) lalu cocokkan dengan digit checksum setelah `*`. Jika berbeda, **buang frame segera**.

---

## 3. Pengemasan Biner Hemat Bandwidth Memakai `struct`
Mengirim teks `"$TELEM,101,28.4,62.0,3.85*7F\n"` menghabiskan **29 byte**. Dengan modul standar Python **`struct`**, `(node_id uint16, temp float32, humidity float32)` dikemas ke **10 byte biner tepat (`<Hff`)** — sangat krusial untuk jaringan daya rendah seperti LoRaWAN dan NB-IoT.

---

## 4. Kalibrasi & Smoothing Sinyal Sensor
Pembacaan ADC mentah sering berfluktuasi cepat (*jitter*). Menggunakan **Exponential Moving Average (EMA)**: `y_t = alpha * x_t + (1 - alpha) * y_{t-1}` menghaluskan sinyal berderau dalam memori $O(1)$ tanpa menyimpan buffer panjang.

