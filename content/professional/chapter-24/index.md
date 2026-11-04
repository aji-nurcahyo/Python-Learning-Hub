# Chapter 24: Decorators, Generators & Context Managers
## Metaprogramming, `functools.wraps`, `yield` & `contextlib`

Selamat datang di **Chapter 24: Decorators, Generators & Context Managers** pada kurikulum **Python Learning Hub**. Bab ini merupakan gerbang utama menuju teknik *metaprogramming* dan optimasi alokasi memori di lingkungan Python profesional.

Ketika sistem perangkat lunak berkembang hingga mengolah ribuan transaksi per detik atau membaca file telemetri berukuran gigabyte, pendekatan konvensional yang memuat seluruh data ke memori RAM (*eager evaluation*) akan memicu masalah kehabisan memori (*Out Of Memory* / OOM). Selain itu, penyisipan kode lintas modul seperti logging, auditing, benchmarking, dan validasi izin akses (*cross-cutting concerns*) sering kali mengotori logika bisnis utama.

Modul ini membekali Anda dengan tiga instrumen Python paling elegan dan ekspresif untuk mengatasi persoalan tersebut.

---

## 1. Fondasi: First-Class Functions dan Closures

Di Python, fungsi diperlakukan sebagai **objek kelas pertama (*first-class citizens*)**:
1. Fungsi dapat disimpan dalam variabel atau struktur data.
2. Fungsi dapat dilewatkan sebagai parameter ke fungsi lain (*higher-order functions*).
3. Fungsi dapat didefinisikan di dalam tubuh fungsi lain (*nested functions*).
4. Fungsi dapat mengembalikan fungsi lain sebagai nilai kembaliannya.

### Konsep Closure
**Closure** adalah fungsi dalam (*inner function*) yang mempertahankan referensi ke variabel-variabel di lingkup sekitarnya (*enclosing scope*) bahkan setelah fungsi luar (*outer function*) selesai dieksekusi.

```python
def make_multiplier(factor: float):
    def multiplier(number: float) -> float:
        return number * factor  # 'factor' dipertahankan oleh closure
    return multiplier

double = make_multiplier(2.0)
print(double(15.0))  # Menghasilkan 30.0
```

---

## 2. Decorators dan Preservasi Metadata dengan `functools.wraps`

Decorator pada hakikatnya adalah fungsi yang menerima fungsi lain sebagai argumen, membungkusnya dengan logika tambahan, dan mengembalikan fungsi pembungkus (*wrapper*).

Sintaksis `@my_decorator` merupakan bentuk singkat (*syntactic sugar*) dari:
```python
target_func = my_decorator(target_func)
```

### Pentingnya `functools.wraps`
Ketika suatu fungsi dibungkus oleh wrapper decorator biasa, metadata bawaannya seperti `__name__`, `__doc__`, dan `__annotations__` akan tertimpa oleh identitas wrapper. Modul bawaan `functools` menyediakan decorator `@functools.wraps` untuk menyalin kembali seluruh metadata asli:

```python
import functools
import time
from typing import Callable, Any

def audit_logger(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"[LOG CALL] {func.__name__} dipanggil.")
        result = func(*args, **kwargs)
        print(f"[LOG RESULT] {func.__name__} selesai.")
        return result
    return wrapper
```

---

## 3. Parameterized Decorators (Decorator Berparameter)

Sering kali decorator membutuhkan parameter konfigurasi (misalnya batas retry maksimal, nama peran otorisasi, atau batas rentang numerik). Untuk mencapainya, kita membuat **decorator factory** yang memiliki tiga tingkatan fungsi bertingkat:

1. **Factory Function:** Menerima argumen konfigurasi.
2. **Decorator Function:** Menerima fungsi target yang akan di-wrap.
3. **Wrapper Function:** Menerima `*args` dan `**kwargs` saat pemanggilan runtime.

```python
def validate_range(min_val: float, max_val: float):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(val: float, *args, **kwargs):
            if not (min_val <= val <= max_val):
                raise ValueError(f"Nilai {val} di luar batas toleransi [{min_val}, {max_val}]")
            return func(val, *args, **kwargs)
        return wrapper
    return decorator

@validate_range(min_val=-120.0, max_val=-30.0)
def record_rssi(rssi_dbm: float):
    return f"RSSI diterima: {rssi_dbm} dBm"
```

---

## 4. Decorator Stacking (Penumpukan Decorator)

Satu fungsi dapat didekorasi oleh lebih dari satu decorator:
```python
@audit_logger
@measure_time
@validate_range(min_val=0, max_val=100)
def calculate_metric(value: float):
    ...
```

**Aturan Urutan Stacking:**
- **Pembungkusan (*wrapping*):** Dijalankan dari **bawah ke atas** (`calculate_metric = audit_logger(measure_time(validate_range(calculate_metric)))`).
- **Eksekusi (*execution*):** Dijalankan dari **atas ke bawah** (`audit_logger` wrapper dieksekusi terlebih dahulu, lalu memanggil `measure_time` wrapper, dan seterusnya).

---

## 5. Generator Functions dan Evaluasi Lazy (`yield`)

Fungsi konvensional mengeksekusi instruksi dan mengembalikan seluruh hasil sekaligus melalui `return`. Sebaliknya, **generator function** memuat setidaknya satu pernyataan **`yield`**.

Ketika generator function dipanggil, kode di dalamnya tidak langsung dieksekusi, melainkan mengembalikan sebuah **generator iterator object**.

### Karakteristik Eksekusi Generator
1. **Lazy Evaluation:** Nilai baru hanya dihitung ketika pemanggil secara eksplisit meminta elemen berikutnya via `next()` atau perulangan `for`.
2. **Efisiensi Memori O(1):** Generator hanya menyimpan status eksekusi lokal dan satu elemen aktif di memori RAM, terlepas dari apakah data berjumlah 10 elemen atau 10 miliar elemen.
3. **Generator Exhaustion:** Generator hanya dapat diiterasi **satu kali**. Setelah mencapai akhir data, generator akan melempar `StopIteration`. Untuk membaca ulang data, generator harus dibuat kembali.

```python
def fibonacci_sequence():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci_sequence()
first_5 = [next(fib) for _ in range(5)]  # [0, 1, 1, 2, 3]
```

---

## 6. Generator Pipelines (Rantai Pengolahan Data)

Salah satu pola arsitektur data paling powerful di Python adalah menyambungkan beberapa generator menjadi **pipa pemrosesan data (*generator pipeline*)**. Setiap generator berperan sebagai tahap independen (sumber data -> penyaring -> transformator):

```python
def data_source():
    for val in [10, 45, 80, 120, 25]:
        yield val

def filter_threshold(stream, min_val):
    for item in stream:
        if item >= min_val:
            yield item

def amplify(stream, factor):
    for item in stream:
        yield item * factor

# Merakit pipeline secara deklaratif
pipeline = amplify(filter_threshold(data_source(), min_val=50), factor=1.5)
```

Elemen data mengalir satu demi satu melewati setiap tahap pipa tanpa pernah memerlukan array atau list perantara yang membebani memori.

---

## 7. Protokol Context Manager dan Pernyataan `with`

Pernyataan `with` menjamin pembersihan sumber daya sistem (*resource cleanup*) seperti koneksi soket jaringan, penguncian mutex (*thread lock*), atau penanganan file berkas.

### Protokol Dua Metode (`__enter__` dan `__exit__`)
Suatu class dapat menjadi context manager dengan mengimplementasikan dua method khusus:
1. **`__enter__(self)`:** Mengalokasikan sumber daya dan mengembalikan objek yang diikat ke variabel di belakang kata kunci `as`.
2. **`__exit__(self, exc_type, exc_val, exc_tb)`:** Dipanggil secara otomatis ketika alur keluar dari blok `with`, baik keluar secara normal maupun akibat terjadinya *unhandled exception*.

```python
class NetworkSession:
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    def __enter__(self):
        print(f"Membuka koneksi ke {self.endpoint}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Menutup koneksi dari {self.endpoint}")
        return False  # Propagate exception jika terjadi
```

---

## 8. Context Manager Berbasis Generator (`contextlib.contextmanager`)

Untuk skenario yang tidak memerlukan class berukuran penuh, modul `contextlib` menyediakan decorator `@contextmanager` yang mengubah fungsi generator menjadi context manager yang ringkas:

```python
from contextlib import contextmanager

@contextmanager
def temporary_channel(channel_id: int):
    print(f"Alokasi kanal #{channel_id}")
    try:
        yield f"CH-{channel_id}"
    finally:
        print(f"Pelepasan kanal #{channel_id}")
```
Kode sebelum `yield` bertindak sebagai `__enter__`, nilai yang di-`yield` menjadi target `as`, dan blok `finally` bertindak sebagai `__exit__`.

---

## 9. Rangkuman & Langkah Selanjutnya

- **Decorators** memisahkan *cross-cutting concerns* (logging, timing, validasi) dari logika bisnis utama.
- **`functools.wraps`** wajib digunakan untuk mempertahankan identitas fungsi asli.
- **Generators (`yield`)** memungkinkan pengolahan data streaming dengan konsumsi memori konstan O(1).
- **Context Managers (`with`)** memastikan dealokasi sumber daya sistem secara deterministik dan tahan terhadap crash.

Pada modul berikutnya di **Chapter 25**, kita akan mempelajari bagaimana menjamin keandalan sistem berskala enterprise menggunakan **Type Hints, Protocol, Mypy, dan Linter Ruff**.
