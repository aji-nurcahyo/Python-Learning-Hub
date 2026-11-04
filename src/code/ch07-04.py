# Pemeriksaan Palindrom dengan Slicing [::-1]
# File: ch07-04.py

def cek_palindrom(kata: str) -> bool:
    """Memeriksa apakah sebuah string dibaca sama dari depan maupun belakang."""
    # Bersihkan spasi dan normalkan ke huruf kecil
    kata_bersih = kata.replace(" ", "").lower()
    # Pembalikan string menggunakan slicing dengan langkah negatif -1
    kata_terbalik = kata_bersih[::-1]
    return kata_bersih == kata_terbalik

daftar_kata = ["Radar", "Level", "Transmisi", "Kasur ini rusak", "Python"]

for item in daftar_kata:
    hasil = cek_palindrom(item)
    print(f"'{item:<16}' -> Palindrom: {hasil}")

