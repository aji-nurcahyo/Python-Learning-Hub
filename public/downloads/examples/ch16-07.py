"""Contoh 16.7: Rekayasa Pemecahan Masalah & Space-Time Tradeoff
Python Learning Hub - Level 2: Intermediate
"""

# Masalah: Mencari apakah ada elemen duplikat di dalam data jaringan
# Pendekatan 1: Brute Force O(n^2) waktu, O(1) ruang (Nested Loops)
def ada_duplikat_brute_force(data: list[int]) -> bool:
    n = len(data)
    for i in range(n):
        for j in range(i + 1, n):
            if data[i] == data[j]:
                return True
    return False

# Pendekatan 2: Hash Set O(n) waktu, O(n) ruang (Space-Time Tradeoff)
def ada_duplikat_hash_set(data: list[int]) -> bool:
    diketahui = set()
    for item in data:
        if item in diketahui:
            return True
        diketahui.add(item)
    return False

sampel_unik = list(range(1000))
sampel_duplikat = list(range(1000)) + [42]

print("Uji Pendekatan 1 (Brute Force O(n^2)):")
print("  - Sampel Unik      :", ada_duplikat_brute_force(sampel_unik))
print("  - Sampel Duplikat  :", ada_duplikat_brute_force(sampel_duplikat))

print("\nUji Pendekatan 2 (Hash Set O(n) - Space-Time Tradeoff):")
print("  - Sampel Unik      :", ada_duplikat_hash_set(sampel_unik))
print("  - Sampel Duplikat  :", ada_duplikat_hash_set(sampel_duplikat))
print("\nPendekatan 2 menukar sedikit memori RAM tambahan demi penghematan drastis waktu CPU.")
