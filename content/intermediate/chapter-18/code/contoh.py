"""Contoh Praktik Terapan: Robust Data Validator
Python Learning Hub - Chapter 18: Exception Handling & Debugging
"""

class ValidationException(Exception):
    """Custom exception untuk kesalahan validasi data."""
    pass


def validasi_stasiun(node: dict) -> dict:
    """Memvalidasi dan membersihkan data node telekomunikasi."""
    if "node_id" not in node:
        raise ValidationException("Field 'node_id' wajib disertakan.")

    try:
        frek = float(node["frekuensi"])
    except (KeyError, ValueError) as err:
        raise ValidationException(f"Frekuensi tidak valid: {err}") from err

    if frek <= 0:
        raise ValidationException(f"Frekuensi harus bernilai positif ({frek} MHz)")

    return {
        "node_id": str(node["node_id"]),
        "frekuensi": frek,
        "status": node.get("status", "ACTIVE")
    }


# Uji eksekusi terhadap beberapa sampel data
sampel_data = [
    {"node_id": "N-101", "frekuensi": 2412.0},
    {"node_id": "N-102", "frekuensi": -50.0},
    {"frekuensi": 1800.0},
    {"node_id": "N-104", "frekuensi": "RUSAK"},
]

valid = []
invalid = []

print("Memulai Validasi Dataset Node:")
for d in sampel_data:
    try:
        bersih = validasi_stasiun(d)
        valid.append(bersih)
        print(f"  [OK] Node {bersih['node_id']} berhasil divalidasi ({bersih['frekuensi']} MHz)")
    except ValidationException as e:
        invalid.append({"data": d, "error": str(e)})
        print(f"  [GAGAL] Data ditolak: {e}")

print(f"\nSelesai: {len(valid)} valid, {len(invalid)} ditolak.")

