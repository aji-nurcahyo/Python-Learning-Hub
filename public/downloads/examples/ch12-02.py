"""Contoh Capstone 12.2: Validasi Masukan Data Mahasiswa
Python Learning Hub - Level 1: Foundations Capstone
"""

def validate_nim(nim: str, existing_list: list[dict]) -> tuple[bool, str]:
    cleaned = nim.strip()
    if not cleaned:
        return False, "NIM tidak boleh kosong."
    if not cleaned.isdigit():
        return False, "NIM harus berupa karakter digit angka."
    if not (5 <= len(cleaned) <= 15):
        return False, "Panjang NIM harus antara 5 hingga 15 digit."
    for item in existing_list:
        if item.get("nim") == cleaned:
            return False, f"NIM '{cleaned}' sudah terdaftar."
    return True, "NIM valid."

def validate_grade(val: object) -> tuple[bool, str, float | None]:
    try:
        score = float(str(val).strip())
    except (ValueError, TypeError):
        return False, "Nilai harus berupa angka numerik.", None
    if score < 0.0 or score > 100.0:
        return False, "Nilai harus berada dalam rentang 0.0 s.d. 100.0.", None
    return True, "Nilai valid.", score

# Pengujian validasi
database = [{"nim": "121140001", "name": "Budi", "grade": 85.0}]
test_cases_nim = ["121140001", "121140002", "12AB5", ""]
test_cases_grade = [88.5, "95.0", 105.0, -10.0, "abc"]

print("Hasil Uji Validasi NIM:")
for n in test_cases_nim:
    ok, msg = validate_nim(n, database)
    print(f"  NIM '{n}': {'VALID' if ok else 'INVALID'} -> {msg}")

print("\nHasil Uji Validasi Nilai:")
for g in test_cases_grade:
    ok, msg, res = validate_grade(g)
    print(f"  Nilai '{g}': {'VALID' if ok else 'INVALID'} -> {msg}")
