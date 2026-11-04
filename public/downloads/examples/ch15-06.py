"""Contoh 15.6: Pengurutan Bawaan Python (sorted vs .sort) & Timsort
Python Learning Hub - Level 2: Intermediate
"""

# Perbedaan: sorted() mengembalikan list baru, .sort() memutasi list in-place
nilai_asli = [78.5, 92.0, 64.0, 85.0]

# 1. Fungsi bawaan sorted() (Non-Destruktif)
hasil_sorted = sorted(nilai_asli)
print("List Asli (Tetap)    :", nilai_asli)
print("Hasil sorted() Baru  :", hasil_sorted)

# 2. Metode .sort() (In-Place Mutasi)
nilai_asli.sort(reverse=True)
print("Hasil .sort() In-Place (Descending):", nilai_asli)

# 3. Kinerja Timsort: Algoritma hibrida adaptif Merge Sort + Insertion Sort
# Menjamin stabilitas (Stable Sort) dan kompleksitas O(n log n) kasus terburuk.
kata_kunci = ["antena", "BTS", "Modem", "kabel", "Router"]
# Pengurutan case-insensitive menggunakan fungsi str.lower sebagai key
print("\nPengurutan Alfabetik Case-Insensitive:")
print(" ", sorted(kata_kunci, key=str.lower))

