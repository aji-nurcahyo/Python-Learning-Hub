# Latihan Terarah: Chapter 18 — Exception Handling & Debugging

Selamat datang di lembar latihan terarah **Chapter 18**. Selesaikan 4 latihan bertahap berikut untuk menguasai pertahanan program terhadap error runtime, perancangan custom exception, dan debugging sistematis.

---

### Latihan 1: Validasi Pembagian Daya Terdistribusi (ZeroDivisionError)
**Tujuan:** Menggunakan blok `try-except` untuk mencegah terminasi paksa program saat pembagian nol.

1. Tulis fungsi `distribusi_daya(total_daya_watt: float, jumlah_antena: int) -> float | None`.
2. Hitung alokasi daya per antena: `total_daya_watt / jumlah_antena`.
3. Tangani kasus `jumlah_antena == 0` dengan menangkap `ZeroDivisionError` dan mencetak pesan peringatan informatif tanpa membiarkan program crash.

---

### Latihan 2: Konversi Parameter Jaringan Multi-Exception
**Tujuan:** Menangani beberapa tipe exception secara spesifik dalam satu blok proteksi.

1. Diberikan dictionary konfigurasi:
   ```python
   config = {"ip": "192.168.1.1", "port": "8080", "timeout": "dua_detik"}
   ```
2. Buat fungsi `baca_timeout(konfigurasi: dict) -> int | None` yang mencoba membaca kunci `"timeout"` dan mengonversinya ke integer.
3. Tangkap `KeyError` jika kunci `"timeout"` tidak ada, dan tangkap `ValueError` jika nilai string tidak dapat diubah menjadi integer.

---

### Latihan 3: Perancangan Custom Exception `BandwidthExceededError`
**Tujuan:** Membuat class exception turunan dari `Exception` untuk aturan domain bisnis.

1. Definisikan class `BandwidthExceededError(Exception)` yang menerima argumen `permintaan_mbps: float` dan `batas_mbps: float`.
2. Buat fungsi `alokasi_bandwidth(permintaan_mbps: float, batas_mbps: float = 100.0) -> str`.
3. Jika `permintaan_mbps > batas_mbps`, lemparkan exception menggunakan statement `raise BandwidthExceededError(...)`.
4. Uji pemanggilan fungsi tersebut di dalam blok `try-except` dan cetak pesan kesalahannya.

---

### Latihan 4: Audit Alur Eksekusi dengan Modul `logging`
**Tujuan:** Menggantikan statement `print()` sementara dengan pencatatan log terstruktur.

1. Impor modul bawaan `logging`.
2. Konfigurasikan logger dengan `logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")`.
3. Tulis fungsi `kirim_paket(id_tujuan: str, ukuran_kb: int) -> bool` yang mencatat:
   - `logging.info(...)` saat pengiriman dimulai.
   - `logging.warning(...)` jika ukuran paket melebihi ambang batas (misal > 1024 KB).
   - `logging.error(...)` jika ID tujuan berupa string kosong.

