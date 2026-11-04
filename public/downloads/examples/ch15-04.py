"""Contoh 15.4: Algoritma Pengurutan Seleksi (Selection Sort)
Python Learning Hub - Level 2: Intermediate
"""

def selection_sort(data: list[int]) -> list[int]:
    """Mengurutkan data dengan mencari nilai terkecil pada setiap iterasi.
    Kompleksitas: O(n²) pada semua kasus.
    """
    arr = list(data)
    n = len(arr)

    for i in range(n):
        indeks_min = i
        for j in range(i + 1, n):
            if arr[j] < arr[indeks_min]:
                indeks_min = j

        # Tukar elemen minimum ke posisi i saat ini
        if indeks_min != i:
            arr[i], arr[indeks_min] = arr[indeks_min], arr[i]

    return arr

slot_kanal = [11, 1, 6, 9, 3, 5]
print("Slot Sebelum Selection Sort:", slot_kanal)
print("Slot Setelah Selection Sort:", selection_sort(slot_kanal))

