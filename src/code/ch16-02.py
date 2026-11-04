"""Contoh 16.2: Analisis Pertumbuhan Waktu Linier O(n) vs Logaritmik O(log n)
Python Learning Hub - Level 2: Intermediate
"""

import math

def estimasi_operasi(n: int) -> tuple[int, int]:
    """Menghitung jumlah operasi maksimal: Linear O(n) vs Binary Search O(log n)."""
    ops_linear = n
    ops_binary = math.ceil(math.log2(n)) if n > 0 else 0
    return ops_linear, ops_binary

skala_data = [10, 100, 1_000, 10_000, 100_000, 1_000_000]

print(f"{'Ukuran Data (N)':<18} | {'Operasi Linear O(n)':<22} | {'Operasi Binary O(log n)':<25}")
print("-" * 72)
for n in skala_data:
    lin, bin_ops = estimasi_operasi(n)
    print(f"{n:<18,d} | {lin:<22,d} | {bin_ops:<25d}")

