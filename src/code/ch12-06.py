"""Contoh Capstone 12.6: Pengurutan Ranking & Predikat Nilai
Python Learning Hub - Level 1: Foundations Capstone
"""

def get_grade_category(score: float) -> str:
    if score >= 80.0:
        return "A"
    if score >= 70.0:
        return "B"
    if score >= 60.0:
        return "C"
    if score >= 50.0:
        return "D"
    return "E"

students = [
    {"nim": "121140001", "name": "Budi Santoso", "grade": 86.5},
    {"nim": "121140002", "name": "Siti Nurhaliza", "grade": 92.0},
    {"nim": "121140003", "name": "Ahmad Fauzi", "grade": 74.25},
    {"nim": "121140004", "name": "Dewi Lestari", "grade": 81.0},
]

# Mengurutkan mahasiswa berdasarkan nilai tertinggi (ranking)
ranked = sorted(students, key=lambda s: float(s["grade"]), reverse=True)

print(f"{'Rank':<5} | {'NIM':<10} | {'Nama':<18} | {'Nilai':<6} | {'Predikat':<8}")
print("-" * 55)
for rank, s in enumerate(ranked, start=1):
    score = float(s["grade"])
    predikat = get_grade_category(score)
    print(f"{rank:<5} | {s['nim']:<10} | {s['name']:<18} | {score:<6.2f} | {predikat:<8}")
