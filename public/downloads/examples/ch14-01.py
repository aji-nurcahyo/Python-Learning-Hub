"""Contoh 14.1: List Comprehension Dasar dan Pemfilteran Kondisional
Python Learning Hub - Level 2: Intermediate
"""

# 1. Transformasi data skalar dengan list comprehension
sinyal_mentah_dbm = [-115.0, -98.2, -84.0, -70.5, -62.0]
# Konversi ke miliwatt: 10^(dBm / 10)
daya_mw = [round(10 ** (p / 10), 6) for p in sinyal_mentah_dbm]

print("Daya Mentah (dBm) :", sinyal_mentah_dbm)
print("Konversi Daya (mW):", daya_mw)

# 2. Pemfilteran data menggunakan klausa if (kondisional)
# Ambil sinyal kuat saja (>= -90.0 dBm)
sinyal_kuat = [s for s in sinyal_mentah_dbm if s >= -90.0]
print("Sinyal Kuat (>= -90 dBm):", sinyal_kuat)

# 3. Transformasi dengan percabangan if-else (ternary)
# Klasifikasi status sinyal: "BAIK" jika >= -85 dBm, selain itu "LEMAH"
status_sinyal = ["BAIK" if s >= -85.0 else "LEMAH" for s in sinyal_mentah_dbm]
print("Label Status Sinyal     :", status_sinyal)

