"""Contoh 16.4: Kompleksitas Ruang Memori (Space Complexity) O(1) vs O(n)
Python Learning Hub - Level 2: Intermediate
"""

import sys

N = 50_000

# 1. Algoritma dengan Space Complexity O(1) [Konstan]
# Menghitung total kumulatif secara in-place / generator tanpa membuat list kedua
total_o1 = sum(i for i in range(N))
memori_generator = sys.getsizeof((i for i in range(N)))

# 2. Algoritma dengan Space Complexity O(n) [Linier]
# Menduplikasi data ke dalam struktur baru di memori RAM
duplikasi_list = [i * 2 for i in range(N)]
memori_list = sys.getsizeof(duplikasi_list)

print(f"Dataset Ukuran        : {N:,} elemen")
print(f"Total Akumulasi       : {total_o1:,}")
print(f"Alokasi Memori O(1)   : {memori_generator:,} byte (Ruang Konstan)")
print(f"Alokasi Memori O(n)   : {memori_list:,} byte (Ruang Linier terhadap N)")

