# Tugas Mini Project: Concurrent Task Processing System

**Chapter 27: Concurrent & Asynchronous Programming**  
**Tingkat:** Level 3 — Professional Python Engineering  
**Platform:** Python Learning Hub  
**Institusi:** Institut Teknologi Sumatera (ITERA)  

---

## 1. Deskripsi Tugas

Dalam sistem telekomunikasi dan komputasi awan modern, volume pemrosesan data sensor dan telemetri perangkat jaringan melampaui batas kecepatan eksekusi sequential berskala tunggal.

Tugas Anda adalah merancang dan mengimplementasikan modul **`ConcurrentTaskProcessor`** yang mampu:
1. Membagi beban kerja ke dalam model konkurensi yang tepat (I/O-bound menggunakan thread pool, CPU-bound menggunakan multiprocessing/multitasking computation).
2. Mengeksekusi kumpulan coroutine asinkron secara non-blocking dengan batas waktu *timeout* menggunakan `asyncio`.
3. Menjamin integritas metrik pemrosesan (*task counters*, *failure logs*) bebas dari *race condition* dengan mekanisme sinkronisasi `threading.Lock`.
4. Mengembalikan ringkasan eksekusi yang komprehensif (jumlah task sukses, gagal, timeout, dan total durasi pemrosesan).

---

## 2. Diagram Arsitektur Pemrosesan Konkuren

```
                     ┌───────────────────────────┐
                     │   Incoming Task Stream    │
                     └─────────────┬─────────────┘
                                   │
                 ┌─────────────────┴─────────────────┐
                 │                                   │
          [I/O-Bound Workload]               [Asyncio Coroutines]
                 │                                   │
      ┌──────────▼──────────┐             ┌──────────▼──────────┐
      │ ThreadPoolExecutor  │             │   asyncio.gather()  │
      │  (max_workers = N)  │             │   with wait_for()   │
      └──────────┬──────────┘             └──────────┬──────────┘
                 │                                   │
                 └─────────────────┬─────────────────┘
                                   │
                      ┌────────────▼────────────┐
                      │   SynchronizedCounter   │
                      │  (threading.Lock safe)  │
                      └────────────┬────────────┘
                                   │
                      ┌────────────▼────────────┐
                      │ ExecutionSummary Report │
                      └─────────────────────────┘
```

---

## 3. Persyaratan Fungsional Modul

Modul wajib diimplementasikan di dalam file `tugas.py` dengan komponen berikut:

1. **`SafeMetricsTracker` Class:**
   - Menyimpan metrik `success_count`, `failure_count`, dan `timeout_count`.
   - Menggunakan `threading.Lock` dengan context manager (`with self._lock:`) untuk setiap operasi mutasi counter.
   - Menyediakan method `record_success()`, `record_failure()`, dan `record_timeout()`.

2. **`ConcurrentTaskProcessor` Class:**
   - **`process_io_batch(task_list: list[str], max_workers: int = 4) -> list[dict]`**:
     - Mengirimkan setiap task ke `ThreadPoolExecutor`.
     - Memperbarui counter keberhasilan pada `SafeMetricsTracker`.
   - **`process_async_batch(endpoints: list[str], timeout_sec: float = 0.5) -> list[dict]`**:
     - Mengambil data dari daftar endpoint menggunakan `asyncio.gather()`.
     - Jika salah satu task melebihi `timeout_sec`, tangkap `asyncio.TimeoutError` dan catat ke `SafeMetricsTracker`.
   - **`get_summary() -> dict`**:
     - Mengembalikan ringkasan status operasional secara terstruktur.

---

## 4. Rubrik Penilaian (Total: 100 Poin)

| Kriteria Penilaian | Bobot | Deskripsi |
| :--- | :---: | :--- |
| **Arsitektur Thread-Safe (Lock)** | 25 Poin | Implementasi `SafeMetricsTracker` menggunakan `threading.Lock` context manager secara tepat tanpa race condition atau deadlock. |
| **Integrasi ThreadPoolExecutor** | 25 Poin | Eksekusi task I/O-bound secara paralel menggunakan pool worker dengan penanganan hasil via `as_completed` atau `executor.map`. |
| **Eksekusi Asyncio & Timeout** | 25 Poin | Pemanfaatan coroutine `async/await`, pengelompokan dengan `asyncio.gather`, dan proteksi `asyncio.wait_for`. |
| **Penanganan Error & Determinisme** | 15 Poin | Exception pada salah satu worker tidak meruntuhkan aplikasi utama; output terurut dan deterministik. |
| **Kerapian Kode & Type Hints** | 10 Poin | Mengikuti PEP 8, memiliki type annotations lengkap, dan docstrings yang jelas dalam Bahasa Indonesia. |

---

## 5. Cara Pengujian

Jalankan test mandiri pada terminal:
```bash
python tugas.py
```
Pastikan seluruh asersi dan log laporan status menunjukkan nilai 100% lulus tanpa adanya `RaceConditionError` maupun *deadlock*.
