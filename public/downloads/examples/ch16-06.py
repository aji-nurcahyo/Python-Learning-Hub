"""Contoh 16.6: Kebenaran Algoritma vs Performa (Edge Cases & Boundaries)
Python Learning Hub - Level 2: Intermediate
"""

def temukan_maksimum_aman(koleksi: list[float]) -> float | None:
    """Algoritma pencarian nilai maksimum yang tangguh terhadap kasus batas."""
    if not koleksi:
        return None  # Edge case: list kosong tidak boleh memicu ValueError
    maks = koleksi[0]
    for x in koleksi[1:]:
        if x > maks:
            maks = x
    return maks

kasus_uji = [
    ("List Normal", [10.5, 45.2, 30.0, 8.4]),
    ("List Negatif Semua", [-25.0, -12.4, -80.0, -5.5]),
    ("List Satu Elemen", [42.0]),
    ("List Duplikat Semua", [7.0, 7.0, 7.0]),
    ("List Kosong", []),
]

print("Verifikasi Kebenaran Algoritma pada Kasus Batas:")
for label, data in kasus_uji:
    hasil = temukan_maksimum_aman(data)
    print(f"  - {label:<22} -> Maksimum: {hasil}")

