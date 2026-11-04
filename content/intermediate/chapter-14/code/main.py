"""Aplikasi CLI: Dataset Transformation Toolkit (main.py)
Chapter 14: Comprehensions & Iterators — Python Learning Hub
Pengembang: Aji Pamungkas Tri Nurcahyo — Institut Teknologi Sumatera
"""

import sys
from transform_toolkit import (
    build_index_map,
    extract_unique_categories,
    filter_and_transform,
    flatten_matrix,
    stream_transformed_data,
)


def print_menu() -> None:
    print("\n========================================================")
    print("    DATASET TRANSFORMATION TOOLKIT - CHAPTER 14 (CLI)")
    print("========================================================")
    print("1. Tampilkan Dataset Rekaman Sampel")
    print("2. Filter & Transformasi Nilai (List Comprehension)")
    print("3. Buat Peta Indeks ID -> Nilai (Dict Comprehension)")
    print("4. Ekstrak Kategori Unik (Set Comprehension)")
    print("5. Ratakan Matriks Grid Sensor 2D (Nested Comprehension)")
    print("6. Streaming Generator Data Hemat Memori")
    print("7. Keluar")
    print("========================================================")


def main() -> None:
    raw_nodes = [
        {"id": "ND-01", "name": "Sensor Labtek 1", "type": "suhu", "power": 45.2},
        {"id": "ND-02", "name": "Sensor Labtek 2", "type": "daya", "power": 88.0},
        {"id": "ND-03", "name": "Sensor Menara A", "type": "suhu", "power": 120.5},
        {"id": "ND-04", "name": "Sensor Menara B", "type": "getaran", "power": 32.1},
        {"id": "ND-05", "name": "Sensor Labtek 3", "type": "daya", "power": 94.4},
    ]

    while True:
        print_menu()
        choice = input("Pilih menu [1-7]: ").strip()

        if choice == "1":
            print("\n--- REKAMAN DATASET SAMPEL ---")
            for r in raw_nodes:
                print(f"  {r['id']} | {r['name']:<18} | Tipe: {r['type']:<8} | Daya: {r['power']} mW")

        elif choice == "2":
            try:
                t_str = input("Masukkan ambang batas daya minimum (misal: 50.0): ").strip()
                t_val = float(t_str) if t_str else 50.0
                filtered = filter_and_transform(raw_nodes, "power", t_val, multiplier=1.1)
                print(f"\nHasil Filter (Power >= {t_val}) + Kenaikan 10%:")
                for item in filtered:
                    print(f"  {item['id']} -> {item['name']}: {item['power']} mW")
            except ValueError:
                print("[ERROR] Masukan ambang batas harus berupa angka numerik.")

        elif choice == "3":
            idx_map = build_index_map(raw_nodes, "id", "name")
            print("\nPeta Indeks Asosiatif (Dict Comprehension):")
            for k, v in idx_map.items():
                print(f"  {k} => {v}")

        elif choice == "4":
            cats = extract_unique_categories(raw_nodes, "type")
            print(f"\nKategori Unik Terdeteksi (Set Comprehension): {cats}")

        elif choice == "5":
            sample_matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
            flat = flatten_matrix(sample_matrix)
            print(f"\nMatriks Awal: {sample_matrix}")
            print(f"Hasil Flattening (1D List): {flat}")

        elif choice == "6":
            powers = [r["power"] for r in raw_nodes]
            gen = stream_transformed_data(powers, threshold=40.0)
            print(f"\nAliran Generator Lazy (Ambang 40.0):")
            for idx, val in enumerate(gen, start=1):
                print(f"  Item #{idx} dikonsumsi dari stream: {val}")

        elif choice == "7":
            print("\nTerima kasih telah menggunakan Dataset Transformation Toolkit. Sampai jumpa!")
            break
        else:
            print("[PERINGATAN] Pilihan tidak valid. Silakan pilih menu 1-7.")


if __name__ == "__main__":
    main()

