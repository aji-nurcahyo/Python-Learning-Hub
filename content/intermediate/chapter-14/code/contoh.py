"""Demonstrasi Deterministik: Dataset Transformation Toolkit
Chapter 14: Comprehensions & Iterators — Python Learning Hub
Pengembang: Aji Pamungkas Tri Nurcahyo — Institut Teknologi Sumatera
"""

from transform_toolkit import (
    build_index_map,
    extract_unique_categories,
    filter_and_transform,
    flatten_matrix,
    stream_transformed_data,
)


def main() -> None:
    print("==========================================================")
    print("DEMONSTRASI CHAPTER 14: COMPREHENSIONS & ITERATORS")
    print("Python Learning Hub - Level 2: Intermediate")
    print("==========================================================")

    data = [
        {"id": "ND-01", "name": "Sensor Alpha", "type": "suhu", "power": 45.0},
        {"id": "ND-02", "name": "Sensor Beta", "type": "daya", "power": 90.0},
        {"id": "ND-03", "name": "Sensor Gamma", "type": "suhu", "power": 30.0},
        {"id": "ND-04", "name": "Sensor Delta", "type": "daya", "power": 120.0},
    ]

    # 1. List Comprehension: Filter & Scale
    filtered = filter_and_transform(data, "power", threshold=50.0, multiplier=1.1)
    print("\n1. Hasil List Comprehension (Daya >= 50 + 10%):")
    for f in filtered:
        print(f"   {f['id']} - {f['name']}: {f['power']} mW")

    # 2. Dict Comprehension: Index Mapping
    peta = build_index_map(data, "id", "name")
    print(f"\n2. Peta Asosiatif (Dict Comprehension): {peta}")

    # 3. Set Comprehension: Deduplication
    kategori = extract_unique_categories(data, "type")
    print(f"\n3. Kategori Unik (Set Comprehension): {sorted(kategori)}")

    # 4. Nested Comprehension: Matrix Flattening
    matriks = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flat = flatten_matrix(matriks)
    print(f"\n4. Flattening Matriks 3x3: {flat}")

    # 5. Generator Expression: Lazy Stream
    raw_vals = [20.0, 55.0, 80.0, 15.0, 95.0]
    gen = stream_transformed_data(raw_vals, threshold=50.0)
    print(f"\n5. Generator Stream Hasil (Ambang 50.0): {list(gen)}")

    print("\nSemua demonstrasi Comprehensions & Iterators berhasil dijalankan.")


if __name__ == "__main__":
    main()

