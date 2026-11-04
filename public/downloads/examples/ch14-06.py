"""Contoh 14.6: Perkakas Iterasi Tingkat Lanjut (enumerate & zip)
Python Learning Hub - Level 2: Intermediate
"""

stasiun_id = ["BTS-Pusat", "BTS-Utara", "BTS-Selatan"]
daya_mw = [450.0, 320.0, 580.0]
frekuensi_mhz = [1800, 2100, 900]

# 1. enumerate(): Menghasilkan pasangan (indeks, elemen) dengan awalan kustom
print("Daftar Stasiun (enumerate start=1):")
for nomor, nama in enumerate(stasiun_id, start=1):
    print(f"  {nomor}. {nama}")

# 2. zip(): Menggabungkan beberapa koleksi paralel secara bersamaan
print("\nPenggabungan Data Paralel (zip):")
for nama, pwr, freq in zip(stasiun_id, daya_mw, frekuensi_mhz):
    print(f"  {nama:<12} | Daya: {pwr:>5.1f} mW | Frekuensi: {freq} MHz")

# 3. zip untuk pembuatan kamus cepat (Dict Pairing)
kamus_daya = dict(zip(stasiun_id, daya_mw))
print("\nKamus Hasil zip():", kamus_daya)

