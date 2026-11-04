"""Aplikasi CLI: Flexible Data Processor (main.py)
Chapter 13: Advanced Functions — Python Learning Hub
Pengembang: Aji Pamungkas Tri Nurcahyo — Institut Teknologi Sumatera
"""

import sys
from typing import Callable

from data_processor import apply_pipeline, make_scaler, make_threshold_filter, summarize_dataset


def print_menu() -> None:
    print("\n========================================================")
    print("      FLEXIBLE DATA PROCESSOR - CHAPTER 13 (CLI)")
    print("========================================================")
    print("1. Tampilkan Dataset Saat Ini")
    print("2. Terapkan Pipeline Skalar (Faktor Pengali & Offset)")
    print("3. Terapkan Filter Ambang Batas (Min & Max)")
    print("4. Ringkas Statistik Dataset (*args & **kwargs)")
    print("5. Reset Dataset ke Nilai Awal")
    print("6. Keluar")
    print("========================================================")


def main() -> None:
    initial_data = [12.5, 24.0, 18.2, 35.8, 42.0, 8.4, 50.1]
    current_data = list(initial_data)

    while True:
        print_menu()
        choice = input("Pilih menu [1-6]: ").strip()

        if choice == "1":
            print(f"\n[DATASET]: {current_data}")
            print(f"Total elemen: {len(current_data)}")

        elif choice == "2":
            try:
                factor_str = input("Masukkan faktor pengali (misal: 2.0): ").strip()
                factor = float(factor_str)
                offset_str = input("Masukkan offset penjumlahan (misal: 1.5): ").strip()
                offset = float(offset_str) if offset_str else 0.0

                scaler = make_scaler(factor, offset)
                current_data = apply_pipeline(current_data, scaler)
                print(f"[SUKSES] Dataset berhasil diskala: {current_data}")
            except ValueError:
                print("[ERROR] Masukan harus berupa angka numerik valid.")

        elif choice == "3":
            try:
                min_str = input("Batas minimum (kosongkan jika tanpa batas): ").strip()
                max_str = input("Batas maksimum (kosongkan jika tanpa batas): ").strip()
                min_val = float(min_str) if min_str else None
                max_val = float(max_str) if max_str else None

                t_filter = make_threshold_filter(min_val, max_val)
                current_data = apply_pipeline(current_data, filter_func=t_filter)
                print(f"[SUKSES] Dataset setelah pemfilteran: {current_data}")
            except ValueError:
                print("[ERROR] Batas harus berupa nilai numerik.")

        elif choice == "4":
            # Demonstrasi *args (pilihan metrik) & **kwargs (kustom rentang)
            summary = summarize_dataset(
                current_data,
                "count", "avg", "min", "max", "sum",
                prefix="Statistik",
                rentang=lambda d: max(d) - min(d) if d else 0.0
            )
            print("\n--- RINGKASAN DATASET ---")
            for k, v in summary.items():
                print(f"  {k:<22}: {v}")

        elif choice == "5":
            current_data = list(initial_data)
            print("[INFO] Dataset telah dikembalikan ke kondisi awal.")

        elif choice == "6":
            print("\nTerima kasih telah menggunakan Flexible Data Processor. Sampai jumpa!")
            break
        else:
            print("[PERINGATAN] Pilihan tidak valid. Silakan pilih menu 1-6.")


if __name__ == "__main__":
    main()
