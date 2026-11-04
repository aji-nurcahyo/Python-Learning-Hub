"""Contoh Capstone 12.4: Algoritma Pencarian Multi-Kriteria
Python Learning Hub - Level 1: Foundations Capstone
"""

def search_students(students: list[dict], query: str) -> list[dict]:
    q = query.strip().lower()
    if not q:
        return []
    results = []
    for s in students:
        if q in s["nim"].lower() or q in s["name"].lower():
            results.append(s)
    return results

data = [
    {"nim": "121140001", "name": "Budi Santoso", "grade": 86.5},
    {"nim": "121140002", "name": "Siti Nurhaliza", "grade": 92.0},
    {"nim": "121140003", "name": "Ahmad Fauzi", "grade": 74.25},
    {"nim": "121140004", "name": "Dewi Lestari", "grade": 81.0},
]

queries = ["siti", "0003", "budi", "xyz"]
for query in queries:
    matched = search_students(data, query)
    print(f"Pencarian '{query}': ditemukan {len(matched)} mahasiswa")
    for m in matched:
        print(f"  -> NIM: {m['nim']} | Nama: {m['name']} | Nilai: {m['grade']}")
