"""Contoh 16.1: Operasi Waktu Konstan O(1) vs Waktu Linier O(n)
Python Learning Hub - Level 2: Intermediate
"""

import time

# 1. Menyiapkan dataset pencarian berukuran 100.000 elemen
N = 100_000
daftar_elemen = list(range(N))
himpunan_elemen = set(range(N))

target = N - 1  # Target di posisi paling ujung (kasus terburuk untuk list)

# 2. Uji Pencarian Linier O(n) pada List
t0 = time.perf_counter()
ada_di_list = target in daftar_elemen
waktu_list = (time.perf_counter() - t0) * 1000

# 3. Uji Pencarian Hash O(1) pada Set
t0 = time.perf_counter()
ada_di_set = target in himpunan_elemen
waktu_set = (time.perf_counter() - t0) * 1000

# Validasi empiris bahwa Set O(1) selalu lebih cepat dari List O(n)
lebih_cepat = waktu_set <= waktu_list

print(f"Dataset Ukuran: {N:,} elemen | Target: {target:,}")
print(f"Pencarian List [O(n)] : Selesai (Ada: {ada_di_list})")
print(f"Pencarian Set  [O(1)] : Selesai (Ada: {ada_di_set})")
print(f"Pencarian Set O(1) lebih cepat dari List O(n): {lebih_cepat}")
print("Pencarian Set O(1) jauh lebih kencang daripada Linear Search O(n)!")
