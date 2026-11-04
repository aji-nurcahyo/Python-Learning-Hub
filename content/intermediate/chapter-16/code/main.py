"""Aplikasi CLI: Algorithm Performance Comparator (main.py)
Chapter 16: Algorithm Analysis & Problem Solving — Python Learning Hub
Pengembang: Aji Pamungkas Tri Nurcahyo — Institut Teknologi Sumatera
"""

import sys
from benchmarker import (
    analyze_theoretical_growth,
    benchmark_function,
    compare_duplicate_detectors,
)


def print_menu() -> None:
    print("\n========================================================")
    print("   ALGORITHM PERFORMANCE COMPARATOR - CHAPTER 16 (CLI)")
    print("========================================================")
    print("1. Analisis Teori Pertumbuhan Big-O (Skala Input N)")
    print("2. Uji Empiris Space-Time Tradeoff (Brute Force vs Hash Set)")
    print("3. Uji Kecepatan Sorting (Built-in Timsort Empiris)")
    print("4. Keluar")
    print("========================================================")


def main() -> None:
    while True:
        print_menu()
        choice = input("Pilih menu [1-4]: ").strip()

        if choice == "1":
            try:
                n_str = input("Masukkan ukuran input N (misal: 1000): ").strip()
                n_val = int(n_str) if n_str else 1000
                growth = analyze_theoretical_growth(n_val)
                print(f"\n--- ESTIMASI OPERASI TEORITIS UNTUK N = {n_val:,} ---")
                print(f"  - O(1) konstan     : {growth['O(1)']:,} operasi")
                print(f"  - O(log n) biner   : {growth['O(log_n)']:,} operasi")
                print(f"  - O(n) linier      : {growth['O(n)']:,} operasi")
                print(f"  - O(n log n) timsort: {growth['O(n_log_n)']:,} operasi")
                print(f"  - O(n²) kuadratik  : {growth['O(n2)']:,} operasi")
            except ValueError:
                print("[ERROR] Masukan harus berupa bilangan bulat positif.")

        elif choice == "2":
            try:
                size_str = input("Ukuran sampel data uji (misal: 2000): ").strip()
                size = int(size_str) if size_str else 2000
                test_data = list(range(size)) + [size // 2]  # Memuat duplikat
                comp = compare_duplicate_detectors(test_data)
                print(f"\n--- HASIL BENCHMARK EMPIRIS (N = {size:,}) ---")
                print(f"  - Pendekatan Brute Force O(n²): {comp['brute_force_ms']:.4f} ms")
                print(f"  - Pendekatan Hash Set O(n)    : {comp['hash_set_ms']:.4f} ms")
                ratio = (comp['brute_force_ms'] / comp['hash_set_ms']) if comp['hash_set_ms'] > 0 else 1.0
                print(f"  -> Hash Set {ratio:.1f}x lebih cepat berkat Space-Time Tradeoff!")
            except ValueError:
                print("[ERROR] Masukan ukuran harus berupa bilangan bulat.")

        elif choice == "3":
            sample_list = list(range(20_000, 0, -1))
            res = benchmark_function(sorted, sample_list, repetitions=5)
            print(f"\n--- BENCHMARK TIMSORT CPYTHON (20,000 Elemen Terbalik) ---")
            print(f"  - Rata-rata durasi: {res['average_duration_ms']:.4f} ms (5 repetisi)")

        elif choice == "4":
            print("\nTerima kasih telah menggunakan Algorithm Performance Comparator. Sampai jumpa!")
            break
        else:
            print("[PERINGATAN] Pilihan tidak valid. Silakan pilih menu 1-4.")


if __name__ == "__main__":
    main()
