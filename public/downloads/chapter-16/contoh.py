"""Demonstrasi Deterministik: Algorithm Performance Comparator
Chapter 16: Algorithm Analysis & Problem Solving — Python Learning Hub
Pengembang: Aji Pamungkas Tri Nurcahyo — Institut Teknologi Sumatera
"""

from benchmarker import (
    analyze_theoretical_growth,
    benchmark_function,
    compare_duplicate_detectors,
)


def main() -> None:
    print("==========================================================")
    print("DEMONSTRASI CHAPTER 16: ALGORITHM ANALYSIS")
    print("Python Learning Hub - Level 2: Intermediate")
    print("==========================================================")

    # 1. Analisis Teori Big-O
    n = 10_000
    ops = analyze_theoretical_growth(n)
    print(f"\n1. Analisis Teori Big-O untuk N = {n:,}:")
    print(f"   O(1)       : {ops['O(1)']:,} operasi")
    print(f"   O(log n)   : {ops['O(log_n)']:,} operasi")
    print(f"   O(n)       : {ops['O(n)']:,} operasi")
    print(f"   O(n log n) : {ops['O(n_log_n)']:,} operasi")
    print(f"   O(n^2)     : {ops['O(n2)']:,} operasi")

    # 2. Benchmarking Empiris Deteksi Duplikat (Space-Time Tradeoff)
    dataset = list(range(1000)) + [42]
    comp = compare_duplicate_detectors(dataset)
    print(f"\n2. Deteksi Duplikat Empiris (N = {comp['dataset_size']:,}):")
    print(f"   Brute Force O(n^2): {comp['brute_force_ms']:.4f} ms")
    print(f"   Hash Set O(n)     : {comp['hash_set_ms']:.4f} ms")
    print(f"   Duplikat Ditemukan: {comp['has_duplicates']}")

    # 3. Pengukuran Fungsi Standar
    test_arr = list(range(5000, 0, -1))
    res = benchmark_function(sorted, test_arr, repetitions=3)
    print(f"\n3. Benchmarking Timsort 5,000 Elemen:")
    print(f"   Rata-rata Durasi  : {res['average_duration_ms']:.4f} ms ({res['repetitions']} repetisi)")

    print("\nSemua demonstrasi Algorithm Analysis berhasil dijalankan.")


if __name__ == "__main__":
    main()
