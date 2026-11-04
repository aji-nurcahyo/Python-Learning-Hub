"""Contoh Capstone 12.3: Operasi CRUD Data Mahasiswa
Python Learning Hub - Level 1: Foundations Capstone
"""

students = [
    {"nim": "121140001", "name": "Budi Santoso", "grade": 86.5},
    {"nim": "121140002", "name": "Siti Nurhaliza", "grade": 92.0},
]

# 1. CREATE: Tambah Mahasiswa
new_student = {"nim": "121140003", "name": "Ahmad Fauzi", "grade": 75.0}
students.append(new_student)
print(f"[CREATE] Mahasiswa '{new_student['name']}' berhasil ditambahkan.")

# 2. READ: Menampilkan semua data
print("\n[READ] Daftar Mahasiswa Saat Ini:")
for s in students:
    print(f"  {s['nim']} - {s['name']} (Nilai: {s['grade']})")

# 3. UPDATE: Perbarui nilai mahasiswa berdasarkan NIM
target_nim = "121140001"
for s in students:
    if s["nim"] == target_nim:
        s["grade"] = 89.0
        print(f"\n[UPDATE] Nilai NIM {target_nim} berhasil diperbarui menjadi {s['grade']}.")
        break

# 4. DELETE: Hapus mahasiswa berdasarkan NIM
delete_nim = "121140003"
for idx, s in enumerate(students):
    if s["nim"] == delete_nim:
        removed = students.pop(idx)
        print(f"\n[DELETE] Mahasiswa '{removed['name']}' berhasil dihapus.")
        break

print(f"\nTotal data akhir: {len(students)} mahasiswa.")
