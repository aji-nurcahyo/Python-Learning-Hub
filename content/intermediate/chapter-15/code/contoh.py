"""Demonstrasi Deterministik: Data Search & Ranking System
Chapter 15: Searching & Sorting Algorithms — Python Learning Hub
Pengembang: Aji Pamungkas Tri Nurcahyo — Institut Teknologi Sumatera
"""

from search_sort import (
    binary_search,
    bubble_sort,
    insertion_sort,
    linear_search,
    rank_records,
    selection_sort,
)


def main() -> None:
    print("==========================================================")
    print("DEMONSTRASI CHAPTER 15: SEARCHING & SORTING ALGORITHMS")
    print("Python Learning Hub - Level 2: Intermediate")
    print("==========================================================")

    data = [42, 17, 89, 5, 23, 64, 11, 72]
    print(f"\n1. Data Awal: {data}")

    # 1. Linear Search
    idx_lin = linear_search(data, 23)
    print(f"2. Linear Search target 23: Indeks ke-{idx_lin}")

    # 2. Binary Search (Prasyarat: Terurut)
    sorted_data = sorted(data)
    idx_bin, steps = binary_search(sorted_data, 23)
    print(f"3. Binary Search target 23 pada {sorted_data}:")
    print(f"   -> Ditemukan di indeks {idx_bin} dalam {steps} perbandingan!")

    # 3. Pengujian Tiga Algoritma Pengurutan
    b_sort = bubble_sort(data)
    s_sort = selection_sort(data)
    i_sort = insertion_sort(data)
    print(f"\n4. Pengurutan Ascending:")
    print(f"   Bubble Sort    : {b_sort}")
    print(f"   Selection Sort : {s_sort}")
    print(f"   Insertion Sort : {i_sort}")

    # 4. Pengurutan Descending
    print(f"   Bubble (Desc)  : {bubble_sort(data, reverse=True)}")

    # 5. Pemeringkatan Rekaman dengan Timsort
    records = [
        {"host": "Server-Alpha", "latensi_ms": 12.4},
        {"host": "Server-Beta",  "latensi_ms": 4.1},
        {"host": "Server-Gamma", "latensi_ms": 8.7},
    ]
    ranked = rank_records(records, sort_key="latensi_ms", reverse=False)
    print("\n5. Ranking Server Latensi Terendah:")
    for r, s in enumerate(ranked, start=1):
        print(f"   #{r}: {s['host']} ({s['latensi_ms']} ms)")

    print("\nSemua demonstrasi Searching & Sorting Algorithms berhasil dijalankan.")


if __name__ == "__main__":
    main()

