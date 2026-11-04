"""Contoh 14.5: Protokol Iterator (iter & next) dan Penanganan StopIteration
Python Learning Hub - Level 2: Intermediate
"""

koleksi_kanal = ["CH-01", "CH-06", "CH-11"]

# 1. Mendapatkan iterator dari iterable menggunakan iter()
iterator_kanal = iter(koleksi_kanal)
print(f"Tipe objek asli    : {type(koleksi_kanal).__name__}")
print(f"Tipe objek iterator: {type(iterator_kanal).__name__}")

# 2. Mengambil elemen satu per satu secara lazy menggunakan next()
print("\nPengambilan Elemen Manual:")
print("next(1):", next(iterator_kanal))
print("next(2):", next(iterator_kanal))
print("next(3):", next(iterator_kanal))

# 3. Pemanggilan saat iterator habis: memicu StopIteration atau nilai sentinel
try:
    next(iterator_kanal)
except StopIteration:
    print("\n[INFO] Iterator telah habis: StopIteration berhasil ditangkap!")

# Pengambilan aman dengan argumen default sentinel
print("next aman:", next(iterator_kanal, "TIDAK_ADA_DATA_LAGI"))

