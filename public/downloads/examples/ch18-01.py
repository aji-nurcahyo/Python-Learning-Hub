"""Contoh 18.1: Blok try-except Dasar & Penanganan ZeroDivisionError (Safe Division)
Python Learning Hub - Level 2: Intermediate
"""

def pembagian_aman(pembilang: float, penyebut: float) -> float | None:
    """Melakukan pembagian dua angka dengan penanganan ZeroDivisionError."""
    try:
        hasil = pembilang / penyebut
        return hasil
    except ZeroDivisionError:
        print(f"Peringatan: Terjadi pembagian dengan nol ({pembilang} / {penyebut})!")
        return None

kasus_uji = [(100.0, 4.0), (45.0, 0.0), (0.0, 5.0), (-30.0, -2.0)]

print("Uji Operasi Pembagian Aman:")
for a, b in kasus_uji:
    res = pembagian_aman(a, b)
    print(f"  - {a:>5.1f} / {b:>4.1f} = {res}")
