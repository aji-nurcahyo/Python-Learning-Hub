"""Contoh Capstone 12.1: Model Data Mahasiswa (In-Memory List of Dictionaries)
Python Learning Hub - Level 1: Foundations Capstone
"""

# Inisialisasi basis data mahasiswa menggunakan struktur data list of dicts
mahasiswa: list[dict[str, object]] = [
    {"nim": "121140001", "name": "Budi Santoso", "grade": 86.50},
    {"nim": "121140002", "name": "Siti Nurhaliza", "grade": 92.00},
    {"nim": "121140003", "name": "Ahmad Fauzi", "grade": 74.25},
]

print(f"Total mahasiswa terdaftar: {len(mahasiswa)}")
for mhs in mahasiswa:
    print(f"- NIM: {mhs['nim']} | Nama: {mhs['name']:<18} | Nilai: {mhs['grade']}")
