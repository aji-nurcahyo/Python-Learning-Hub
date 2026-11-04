"""Contoh 13.6: Closure, Lexical Scope, dan Pembangkit Fungsi Berstatus
Python Learning Hub - Level 2: Intermediate
"""

from typing import Callable

# Closure: Fungsi bersarang yang mengingat variabel lingkungan bebasnya (enclosing scope)
def buat_pencacah(awalan: int = 0) -> Callable[[], int]:
    hitungan = awalan  # Variabel enclosing scope yang ditangkap oleh closure

    def langkah_berikutnya() -> int:
        nonlocal hitungan  # Menandai modifikasi variabel pada lingkup luar
        hitungan += 1
        return hitungan

    return langkah_berikutnya

# Menguji dua instansi closure independen
pencacah_paket = buat_pencacah(100)
pencacah_antrean = buat_pencacah(0)

print(f"Paket #1: {pencacah_paket()}")
print(f"Paket #2: {pencacah_paket()}")
print(f"Antrean #1: {pencacah_antrean()}")
print(f"Paket #3: {pencacah_paket()}")

# Pembangkit fungsi faktor pengali (Multiplier Factory)
def buat_pengali_daya(faktor: float) -> Callable[[float], float]:
    return lambda daya_masukan: round(daya_masukan * faktor, 3)

penguat_3db = buat_pengali_daya(2.0)     # Penguatan ~3 dB menggandakan daya
pelemahan_3db = buat_pengali_daya(0.5)   # Redaman ~3 dB mengurangi daya separuhnya

print(f"\nDaya 10 W dikuatkan 3dB: {penguat_3db(10.0)} W")
print(f"Daya 10 W dilemahkan 3dB: {pelemahan_3db(10.0)} W")
