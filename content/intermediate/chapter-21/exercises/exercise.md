# Latihan Terarah Chapter 21: Packages, Environments & Testing

Latihan ini dirancang untuk melatih pemahaman tata kelola paket Python (`__init__.py`), pengelolaan *virtual environment*, pembuatan *test cases*, penggunaan pola *fixture*, parameterisasi, serta pengujian *exception*.

---

### Latihan 1: Merancang Struktur Package Python Sederhana
1. Rancang direktori package `network_metrics/` dengan berkas `__init__.py`, `ping.py`, dan `throughput.py`.
2. Di dalam `__init__.py`, definisikan list `__all__ = ["hitung_latency_rata_rata", "hitung_jitter"]`.
3. Tulis fungsi `hitung_latency_rata_rata(latencies: list[float]) -> float` yang mengembalikan rata-rata waktu respons, dan melempar `ValueError` jika list kosong.

---

### Latihan 2: Pengujian Assertif Mandiri
1. Tulis fungsi `validasi_port_number(port: int) -> bool` yang memeriksa apakah nomor port berada dalam rentang valid TCP/UDP ($1 \le \text{port} \le 65535$).
2. Buat skrip pengujian berbasis `assert` yang memverifikasi:
   - Port 80 dan 443 adalah `True`.
   - Port 0, -1, dan 70000 adalah `False`.

---

### Latihan 3: Pengujian Parameterisasi (Parameterized Testing)
1. Tulis fungsi `kategori_kualitas_sinyal(rsrp_dbm: float) -> str`:
   - $\text{RSRP} \ge -80 \to \text{"EXCELLENT"}$
   - $-90 \le \text{RSRP} < -80 \to \text{"GOOD"}$
   - $-100 \le \text{RSRP} < -90 \to \text{"MID_CELL"}$
   - $\text{RSRP} < -100 \to \text{"CELL_EDGE"}$
2. Buat tabel pengujian parameterisasi dengan minimal 5 pasangan data uji (input RSRP vs expected output) dan uji menggunakan loop assertion atau `unittest.subTest`.

---

### Latihan 4: Pengujian Exception (Exception Testing)
1. Buat class exception kustom `BufferOverflowError(Exception)`.
2. Tulis fungsi `tambah_paket_buffer(buffer: list, paket: str, maks_ukuran: int = 5)`. Jika panjang buffer $\ge \text{maks\_ukuran}$, lempar `BufferOverflowError`.
3. Buat fungsi tes yang memverifikasi bahwa penambahan paket ke-6 pada buffer berkapasitas 5 berhasil memicu `BufferOverflowError`.

