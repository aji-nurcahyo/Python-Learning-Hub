"""Contoh 15.5: Algoritma Pengurutan Sisip (Insertion Sort)
Python Learning Hub - Level 2: Intermediate
"""

def insertion_sort(data: list[float]) -> list[float]:
    """Mengurutkan data dengan menyisipkan elemen ke bagian prefix yang sudah terurut.
    Sangat efisien untuk data yang hampir terurut (Nearly Sorted): O(n).
    """
    arr = list(data)
    for i in range(1, len(arr)):
        kunci = arr[i]
        j = i - 1
        # Geser elemen yang lebih besar dari kunci ke kanan
        while j >= 0 and arr[j] > kunci:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = kunci
    return arr

latensi_ms = [4.2, 12.5, 3.1, 8.4, 25.0, 6.7]
print("Latensi Sebelum Insertion Sort:", latensi_ms)
print("Latensi Setelah Insertion Sort:", insertion_sort(latensi_ms))

