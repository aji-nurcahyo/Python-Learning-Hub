"""Contoh 15.2: Algoritma Pencarian Biner (Binary Search)
Python Learning Hub - Level 2: Intermediate
"""

def pencarian_biner(koleksi_terurut: list[int], target: int) -> tuple[int | None, int]:
    """Mencari target pada list TERURUT menggunakan strategi divide and conquer.
    Mengembalikan (indeks_ditemukan, jumlah_langkah).
    Kompleksitas Waktu: O(log n)
    """
    kiri = 0
    kanan = len(koleksi_terurut) - 1
    langkah = 0

    while kiri <= kanan:
        langkah += 1
        tengah = (kiri + kanan) // 2
        nilai_tengah = koleksi_terurut[tengah]

        if nilai_tengah == target:
            return tengah, langkah
        elif nilai_tengah < target:
            kiri = tengah + 1  # Target berada di paruh kanan
        else:
            kanan = tengah - 1  # Target berada di paruh kiri

    return None, langkah

# Prasyarat MUTLAK: Data harus sudah terurut secara menaik
frekuensi_khz = [100, 250, 450, 800, 900, 1800, 2100, 2600, 3500, 5200]
print("Koleksi Frekuensi Terurut:", frekuensi_khz)

idx, steps = pencarian_biner(frekuensi_khz, 2600)
print(f"Cari 2600: Ditemukan di indeks {idx} (Hanya butuh {steps} perbandingan)")

idx_missing, steps_m = pencarian_biner(frekuensi_khz, 1500)
print(f"Cari 1500: Hasil {idx_missing} (Selesai dalam {steps_m} perbandingan)")

