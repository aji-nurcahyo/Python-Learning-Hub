"""Contoh 13.7: Rekursi vs Iterasi dan Inspeksi Anotasi Fungsi
Python Learning Hub - Level 2: Intermediate
"""

# 1. Faktorial Rekursif dengan Base Case
def faktorial_rekursif(n: int) -> int:
    """Menghitung n! secara rekursif: n * (n - 1)! dengan base case n <= 1."""
    if n <= 1:
        return 1  # Base Case: Menghentikan rekursi
    return n * faktorial_rekursif(n - 1)  # Recursive Step

# 2. Faktorial Iteratif (Membandingkan efisiensi alokasi stack frame)
def faktorial_iteratif(n: int) -> int:
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil

# Uji keselarasan hasil
print("Hasil Faktorial 5!:")
print(f"  - Rekursif: {faktorial_rekursif(5)}")
print(f"  - Iteratif: {faktorial_iteratif(5)}")

# 3. Inspeksi Anotasi Fungsi (Function Annotations)
def hitung_redaman(jarak_km: float, frekuensi_ghz: float) -> float:
    """Estimasi redaman propagasi sinyal pada ruang bebas (Free Space Path Loss)."""
    return round(92.45 + 20 * 0.477 + 20 * 0.38, 2)

print("\nInspeksi Metadata Anotasi (Tipe Data):")
for param, tipe in hitung_redaman.__annotations__.items():
    print(f"  - Parameter '{param}': {tipe}")

