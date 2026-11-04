"""Contoh 19.1: Paradigma Prosedural vs Object-Oriented Programming (OOP)
Python Learning Hub - Level 2: Intermediate Python
"""

# 1. Pendekatan Prosedural (Data dan fungsi terpisah)
student_dict = {"nim": "121140001", "name": "Budi Santoso", "ipk": 3.75}

def hitung_predikat_prosedural(mhs: dict) -> str:
    return "Cumlaude" if mhs["ipk"] >= 3.5 else "Sangat Memuaskan"

print("[Pendekatan Prosedural]")
print(f"Mahasiswa: {student_dict['name']} | IPK: {student_dict['ipk']} | Predikat: {hitung_predikat_prosedural(student_dict)}")

# 2. Pendekatan Object-Oriented (Data dan perilaku terenkapsulasi dalam satu unit)
class Student:
    def __init__(self, nim: str, name: str, ipk: float):
        self.nim = nim
        self.name = name
        self.ipk = ipk

    def hitung_predikat(self) -> str:
        return "Cumlaude" if self.ipk >= 3.5 else "Sangat Memuaskan"

    def ringkasan(self) -> str:
        return f"Student(NIM='{self.nim}', Name='{self.name}', IPK={self.ipk:.2f}, Predikat='{self.hitung_predikat()}')"

mhs_obj = Student("121140001", "Budi Santoso", 3.75)
print("\n[Pendekatan Object-Oriented]")
print(mhs_obj.ringkasan())
