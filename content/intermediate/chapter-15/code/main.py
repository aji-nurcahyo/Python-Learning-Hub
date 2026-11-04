"""Aplikasi CLI: Data Search & Ranking System (main.py)
Chapter 15: Searching & Sorting Algorithms — Python Learning Hub
Pengembang: Aji Pamungkas Tri Nurcahyo — Institut Teknologi Sumatera
"""

import sys
from search_sort import (
    binary_search,
    bubble_sort,
    insertion_sort,
    linear_search,
    rank_records,
    selection_sort,
)


def print_menu() -> None:
    print("\n========================================================")
    print("      DATA SEARCH & RANKING SYSTEM - CHAPTER 15 (CLI)")
    print("========================================================")
    print("1. Tampilkan Dataset Nilai Numerik & Rekaman")
    print("2. Uji Pencarian Linier vs Biner")
    print("3. Uji Algoritma Pengurutan (Bubble, Selection, Insertion)")
    print("4. Urutkan Rekaman Klien Menggunakan Timsort Bawaan")
    print("5. Keluar")
    print("========================================================")


def main() -> None:
    numbers = [42, 17, 89, 5, 23, 64, 11, 72]
    clients = [
        {"id": "CL-01", "name": "Budi Santoso", "bandwidth": 100, "ping": 12.5},
        {"id": "CL-02", "name": "Siti Nurhaliza", "bandwidth": 250, "ping": 8.0},
        {"id": "CL-03", "name": "Ahmad Fauzi", "bandwidth": 50, "ping": 25.0},
        {"id": "CL-04", "name": "Dewi Lestari", "bandwidth": 500, "ping": 5.2},
    ]

    while True:
        print_menu()
        choice = input("Pilih menu [1-5]: ").strip()

        if choice == "1":
            print(f"\n[DATASET NUMERIK]: {numbers}")
            print("\n[REKAMAN KLIEN JARINGAN]:")
            for c in clients:
                print(f"  {c['id']} | {c['name']:<18} | Bandwidth: {c['bandwidth']} Mbps | Ping: {c['ping']} ms")

        elif choice == "2":
            target_str = input("Masukkan angka target yang ingin dicari: ").strip()
            try:
                target = int(target_str)
                # Linear search pada list asli tak terurut
                idx_lin = linear_search(numbers, target)
                print(f"[LINEAR SEARCH] Target {target}: Indeks ke-{idx_lin}")

                # Binary search pada list terurut
                sorted_nums = sorted(numbers)
                idx_bin, steps = binary_search(sorted_nums, target)
                print(f"[BINARY SEARCH] List Terurut: {sorted_nums}")
                print(f"  Target {target}: Indeks ke-{idx_bin} (Selesai dalam {steps} perbandingan)")
            except ValueError:
                print("[ERROR] Masukan harus berupa bilangan bulat.")

        elif choice == "3":
            print("\n--- PERBANDINGAN PENGURUTAN (ASCENDING) ---")
            print("Data Mentah     :", numbers)
            print("Bubble Sort     :", bubble_sort(numbers))
            print("Selection Sort  :", selection_sort(numbers))
            print("Insertion Sort  :", insertion_sort(numbers))

        elif choice == "4":
            print("\n--- PEMERINGKATAN KLIEN TERCEPAT (TIMSORT) ---")
            ranked = rank_records(clients, sort_key="bandwidth", reverse=True)
            for r, c in enumerate(ranked, start=1):
                print(f"  Peringkat #{r}: {c['name']:<18} -> {c['bandwidth']} Mbps (Ping: {c['ping']} ms)")

        elif choice == "5":
            print("\nTerima kasih telah menggunakan Data Search & Ranking System. Sampai jumpa!")
            break
        else:
            print("[PERINGATAN] Pilihan tidak valid. Silakan pilih menu 1-5.")


if __name__ == "__main__":
    main()

