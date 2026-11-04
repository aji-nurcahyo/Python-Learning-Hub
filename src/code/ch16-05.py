"""Contoh 16.5: Pengukuran Empiris dengan time.perf_counter()
Python Learning Hub - Level 2: Intermediate
"""

import time

def ukur_durasi(fungsi, *args, repetisi: int = 5) -> float:
    """Mengukur rata-rata durasi eksekusi fungsi menggunakan time.perf_counter()."""
    waktu_total = 0.0
    for _ in range(repetisi):
        t0 = time.perf_counter()
        fungsi(*args)
        t1 = time.perf_counter()
        waktu_total += (t1 - t0)
    return waktu_total / repetisi

def sorting_python_terurut(data: list[int]) -> list[int]:
    return sorted(data)

def sorting_python_terbalik(data: list[int]) -> list[int]:
    return sorted(data, reverse=True)

data_sampel = list(range(10_000, 0, -1))

durasi_asc = ukur_durasi(sorting_python_terurut, data_sampel, repetisi=5)
durasi_desc = ukur_durasi(sorting_python_terbalik, data_sampel, repetisi=5)

valid_pengukuran = durasi_asc > 0 and durasi_desc > 0

print("Hasil Benchmarking Empiris (10,000 Elemen Terbalik):")
print(f"  - Timsort Ascending  : Selesai (Valid: {durasi_asc > 0})")
print(f"  - Timsort Descending : Selesai (Valid: {durasi_desc > 0})")
print(f"Benchmarking time.perf_counter() berjalan presisi: {valid_pengukuran}")
print("Catatan: Pengukuran empiris dipengaruhi oleh beban CPU dan caching memori.")
