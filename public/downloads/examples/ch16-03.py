"""Contoh 16.3: Pertumbuhan Kuadratik O(n^2) vs Linearitmik O(n log n)
Python Learning Hub - Level 2: Intermediate
"""

import math

def hitung_skala_pertumbuhan(n: int) -> tuple[int, int]:
    """Membandingkan pertumbuhan operasi O(n log n) vs O(n^2)."""
    ops_n_log_n = int(n * math.log2(n)) if n > 1 else 0
    ops_n2 = n ** 2
    return ops_n_log_n, ops_n2

skala = [10, 50, 100, 500, 1_000, 5_000]

print(f"{'Ukuran N':<10} | {'Timsort O(n log n)':<22} | {'Bubble/Selection O(n^2)':<25} | {'Rasio Penghematan':<18}")
print("-" * 80)
for n in skala:
    nlogn, n2 = hitung_skala_pertumbuhan(n)
    rasio = n2 / nlogn if nlogn > 0 else 1.0
    print(f"{n:<10,d} | {nlogn:<22,d} | {n2:<25,d} | {rasio:<18.1f}x lebih cepat")
