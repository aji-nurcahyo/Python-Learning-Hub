"""Contoh Capstone 12.5: Analisis Statistik Nilai Akademik
Python Learning Hub - Level 1: Foundations Capstone
"""

def compute_stats(students: list[dict]) -> dict:
    if not students:
        return {"total": 0, "avg": 0.0, "max": None, "min": None, "top": [], "bottom": []}
    grades = [float(s["grade"]) for s in students]
    avg_score = round(sum(grades) / len(grades), 2)
    max_score = max(grades)
    min_score = min(grades)
    top_students = [s["name"] for s in students if float(s["grade"]) == max_score]
    bottom_students = [s["name"] for s in students if float(s["grade"]) == min_score]
    return {
        "total": len(students),
        "avg": avg_score,
        "max": max_score,
        "min": min_score,
        "top": top_students,
        "bottom": bottom_students
    }

data = [
    {"nim": "121140001", "name": "Budi Santoso", "grade": 86.5},
    {"nim": "121140002", "name": "Siti Nurhaliza", "grade": 92.0},
    {"nim": "121140003", "name": "Ahmad Fauzi", "grade": 74.25},
    {"nim": "121140004", "name": "Dewi Lestari", "grade": 92.0},
]

stats = compute_stats(data)
print("=== RINGKASAN STATISTIK KELAS ===")
print(f"Total Mahasiswa : {stats['total']}")
print(f"Rata-rata Nilai : {stats['avg']:.2f}")
print(f"Nilai Tertinggi : {stats['max']:.2f} ({', '.join(stats['top'])})")
print(f"Nilai Terendah  : {stats['min']:.2f} ({', '.join(stats['bottom'])})")
