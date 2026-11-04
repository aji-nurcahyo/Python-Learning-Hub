# Pemeriksaan Tahun Kabisat (Leap Year)
# File: ch05-03.py

def cek_tahun_kabisat(tahun: int) -> bool:
    """
    Aturan kalender Gregorian:
    Tahun kabisat jika habis dibagi 4, TETAPI tidak habis dibagi 100,
    KECUALI habis dibagi 400.
    """
    if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
        return True
    return False

daftar_tahun = [2000, 2024, 2026, 1900, 2028]

for th in daftar_tahun:
    status = "Kabisat" if cek_tahun_kabisat(th) else "Bukan Kabisat"
    print(f"Tahun {th}: {status}")

