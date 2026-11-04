"""Contoh 13.4: Fungsi Sebagai First-Class Citizen & Higher-Order Functions
Python Learning Hub - Level 2: Intermediate
"""

from typing import Callable

# Fungsi skalar sederhana
def konversi_watt(dbm: float) -> float:
    return round(10 ** (dbm / 10) / 1000, 6)

def konversi_mwatt(dbm: float) -> float:
    return round(10 ** (dbm / 10), 4)

# Higher-order function: Menerima fungsi transformasi sebagai parameter
def proses_aliran_daya(
    daftar_dbm: list[float],
    transformasi: Callable[[float], float]
) -> list[float]:
    """Menerapkan fungsi transformasi pada setiap elemen koleksi data."""
    hasil: list[float] = []
    for nilai in daftar_dbm:
        hasil.append(transformasi(nilai))
    return hasil

sampel_sinyal = [10.0, 20.0, 30.0]

# Mempassing fungsi konversi_watt sebagai argumen
hasil_watt = proses_aliran_daya(sampel_sinyal, konversi_watt)
print("Konversi ke Watt :", hasil_watt)

# Mempassing fungsi konversi_mwatt sebagai argumen
hasil_mwatt = proses_aliran_daya(sampel_sinyal, konversi_mwatt)
print("Konversi ke mWatt:", hasil_mwatt)
