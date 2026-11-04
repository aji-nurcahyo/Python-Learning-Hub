"""Contoh 13.5: Ekspresi Lambda untuk Transformasi Ringkas & Pengurutan Data
Python Learning Hub - Level 2: Intermediate
"""

# 1. Lambda dasar: fungsi anonim satu baris
kuadrat = lambda x: x ** 2
print(f"5 kuadrat = {kuadrat(5)}")

# 2. Pengurutan data kompleks (list of dicts) dengan custom key lambda
stasiun_bts = [
    {"id": "BTS-01", "frekuensi_mhz": 1800, "daya_w": 40.0, "klien": 120},
    {"id": "BTS-02", "frekuensi_mhz": 900,  "daya_w": 20.0, "klien": 45},
    {"id": "BTS-03", "frekuensi_mhz": 2100, "daya_w": 60.0, "klien": 310},
    {"id": "BTS-04", "frekuensi_mhz": 1800, "daya_w": 35.0, "klien": 88},
]

# Urutkan berdasarkan beban klien terbanyak (descending)
terurut_klien = sorted(stasiun_bts, key=lambda bts: bts["klien"], reverse=True)
print("\nStasiun Terurut Beban Klien Terbanyak:")
for b in terurut_klien:
    print(f"  {b['id']} -> {b['klien']} klien (Daya: {b['daya_w']} W)")

# 3. Penggunaan lambda bersama map() dan filter()
nilai_mentah = [45.0, 78.5, 92.0, 58.0, 84.0]
lulus = list(filter(lambda x: x >= 70.0, nilai_mentah))
dinormalisasi = list(map(lambda x: round(x / 100.0, 2), lulus))

print(f"\nNilai Lulus (>= 70): {lulus}")
print(f"Normalisasi Skala 0-1: {dinormalisasi}")

