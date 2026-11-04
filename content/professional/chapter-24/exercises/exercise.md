# Latihan Mandiri: Decorators, Generators & Context Managers (Chapter 24)

Selamat datang di latihan mandiri Chapter 24. Pada bab ini, Anda akan mempraktikkan metaprogramming tingkat lanjut: merancang decorator dengan parameter, membangun generator pipeline untuk efisiensi memori, serta mengelola siklus hidup resource dengan context manager.

---

## Latihan 1: Parameterized Retry Decorator
Buatlah decorator factory `@retry(max_attempts=3, delay_sec=0.1)` yang:
1. Menerima jumlah percobaan maksimal (`max_attempts`).
2. Jika fungsi yang di-wrap melempar exception, ulangi pemanggilan hingga batas maksimal tercapai.
3. Jika tetap gagal setelah `max_attempts`, lemparkan exception terakhir ke pemanggil.
4. Pastikan menggunakan `@functools.wraps(func)` agar nama dan docstring fungsi tidak hilang.

---

## Latihan 2: Prime Number Generator dengan Lazy Evaluation
Buatlah fungsi generator `prime_number_generator()` yang menghasilkan deret bilangan prima tanpa batas secara lazy (`yield`):
- Panggil generator menggunakan fungsi bawaan `next()`.
- Ambil 15 bilangan prima pertama menggunakan list comprehension: `[next(primes) for _ in range(15)]`.
- Buktikan bahwa generator tidak menghitung seluruh bilangan prima di awal, melainkan hanya saat diminta.

---

## Latihan 3: Generator Pipeline untuk Pemrosesan Log Jaringan
Diberikan sekumpulan baris log teks:
```python
raw_logs = [
    "2026-11-04 [INFO] System boot completed",
    "2026-11-04 [WARNING] High memory usage: 85%",
    "2026-11-04 [ERROR] Optical link loss detected on Port 4",
    "2026-11-04 [INFO] Heartbeat received",
    "2026-11-04 [ERROR] BGP neighbor session dropped",
]
```
Bangunlah rantai generator 3-tahap:
1. `stream_lines(logs)`: Mengalirkan baris log satu per satu.
2. `filter_errors(stream)`: Hanya melewatkan baris yang memuat substring `"[ERROR]"`.
3. `format_alert(stream)`: Mengubah setiap baris error menjadi format notifikasi: `"[CRITICAL ALERT] <pesan>"`.

---

## Latihan 4: Context Manager Berbasis Generator (`@contextmanager`)
Gunakan dekorator `@contextlib.contextmanager` untuk membuat context manager `temporary_file_lock(lock_id: str)`:
- Pada blok masuk (sebelum `yield`): Cetak `"[LOCK] Kunci {lock_id} diperoleh"`.
- Berikan objek token lock ke dalam blok `with`.
- Pada blok `finally` (setelah `yield`): Cetak `"[UNLOCK] Kunci {lock_id} dilepaskan"`.
- Buktikan bahwa pembersihan selalu dijalankan meskipun terjadi exception di dalam blok `with`.

