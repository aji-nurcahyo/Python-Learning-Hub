"""Contoh 14.7: Generator Expression vs List Comprehension (Efisiensi Memori)
Python Learning Hub - Level 2: Intermediate
"""

import sys

N = 100_000

# 1. List Comprehension: Mengevaluasi seluruh elemen langsung dan disimpan di RAM
daftar_kuadrat = [x ** 2 for x in range(N)]
memori_list = sys.getsizeof(daftar_kuadrat)

# 2. Generator Expression: Evaluasi lazy (on-demand), hanya menyimpan generator iterator
gen_kuadrat = (x ** 2 for x in range(N))
memori_gen = sys.getsizeof(gen_kuadrat)

print(f"Dataset Ukuran: {N:,} elemen")
print(f"Ukuran Memori List      : {memori_list:,} byte")
print(f"Ukuran Memori Generator : {memori_gen:,} byte")
print(f"Rasio Penghematan RAM   : {memori_list / memori_gen:.1f}x lebih hemat memori!")

# 3. Konsumsi nilai dari generator secara langsung
print(f"\nNilai pertama dari generator: {next(gen_kuadrat)}")
print(f"Nilai kedua dari generator  : {next(gen_kuadrat)}")
print(f"Penjumlahan 3 nilai berikutnya: {sum(next(gen_kuadrat) for _ in range(3))}")
