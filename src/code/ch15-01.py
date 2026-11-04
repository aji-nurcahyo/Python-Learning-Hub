"""Contoh 15.1: Algoritma Pencarian Linier (Linear Search)
Python Learning Hub - Level 2: Intermediate
"""

def pencarian_linier(koleksi: list[object], target: object) -> int | None:
    """Mencari target secara sekuensial dari awal hingga akhir list.
    Mengembalikan indeks pertama yang cocok atau None jika tidak ditemukan.
    Kompleksitas Waktu: O(n)
    """
    for indeks, elemen in enumerate(koleksi):
        if elemen == target:
            return indeks
    return None

data_node = ["Router-A", "Switch-B", "Gateway-C", "AccessPoint-D", "Server-E"]

print("Data Koleksi:", data_node)
print("Cari 'Gateway-C'   : Indeks ke-", pencarian_linier(data_node, "Gateway-C"))
print("Cari 'Router-A'    : Indeks ke-", pencarian_linier(data_node, "Router-A"))
print("Cari 'Firewall-X'  : Hasil ->", pencarian_linier(data_node, "Firewall-X"))
