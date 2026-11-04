"""Contoh 15.7: Pemeringkatan Rekaman Kompleks & Pengurutan Stabil (Stable Sort)
Python Learning Hub - Level 2: Intermediate
"""

klien_jaringan = [
    {"user": "Alice",   "kuota_gb": 40, "prioritas": 2, "kecepatan_mbps": 100},
    {"user": "Bob",     "kuota_gb": 10, "prioritas": 1, "kecepatan_mbps": 50},
    {"user": "Charlie", "kuota_gb": 40, "prioritas": 1, "kecepatan_mbps": 150},
    {"user": "David",   "kuota_gb": 25, "prioritas": 2, "kecepatan_mbps": 75},
]

# Pengurutan Multi-Kriteria:
# Kriteria 1: Prioritas tertinggi (angka 1 sebelum 2) -> ascending
# Kriteria 2: Kecepatan tertinggi -> descending (gunakan tanda minus untuk angka numerik)
pemeringkatan = sorted(
    klien_jaringan,
    key=lambda k: (k["prioritas"], -k["kecepatan_mbps"])
)

print(f"{'Peringkat':<10} | {'Pengguna':<10} | {'Prioritas':<10} | {'Kecepatan':<15}")
print("-" * 55)
for rank, k in enumerate(pemeringkatan, start=1):
    print(f"{rank:<10} | {k['user']:<10} | {k['prioritas']:<10} | {k['kecepatan_mbps']:>5} Mbps")

