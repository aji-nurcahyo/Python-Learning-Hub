"""Contoh 15.3: Algoritma Pengurutan Gelembung (Bubble Sort Teroptimasi)
Python Learning Hub - Level 2: Intermediate
"""

def bubble_sort(data: list[float]) -> list[float]:
    """Mengurutkan data menggunakan algoritma Bubble Sort dengan deteksi pertukaran.
    Kompleksitas: Kasus Buruk O(n²), Kasus Terbaik O(n).
    """
    arr = list(data)  # Bekerja pada salinan list (non-destruktif)
    n = len(arr)

    for i in range(n):
        ada_pertukaran = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Pertukaran nilai (swap)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                ada_pertukaran = True

        # Jika satu putaran penuh tidak ada swap, data sudah terurut sempurna!
        if not ada_pertukaran:
            break

    return arr

daya_sampel = [45.2, 12.0, 88.5, 32.1, 10.4, 60.0]
print("Data Sebelum Bubble Sort:", daya_sampel)
print("Data Setelah Bubble Sort:", bubble_sort(daya_sampel))

