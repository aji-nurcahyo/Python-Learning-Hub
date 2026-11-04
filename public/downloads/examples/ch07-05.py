# Validasi Pengenal Perangkat (Device Identifier)
# File: ch07-05.py

def validasi_id_perangkat(device_id: str) -> tuple[bool, str]:
    """
    Kaidah ID Node IoT Telekomunikasi:
    1. Diawali dengan prefix 'NODE-'
    2. Panjang total tepat 10 karakter (contoh: 'NODE-A0123')
    3. 5 karakter terakhir harus alfanumerik (huruf/angka)
    """
    id_bersih = device_id.strip()

    if not id_bersih.startswith("NODE-"):
        return False, "Prefix harus diawali 'NODE-'"

    if len(id_bersih) != 10:
        return False, f"Panjang harus tepat 10 karakter (saat ini: {len(id_bersih)})"

    suffix = id_bersih[5:]
    if not suffix.isalnum():
        return False, f"Bagian akhir '{suffix}' harus berupa karakter alfanumerik"

    return True, "ID Perangkat Valid"

uji_id = ["NODE-A0123", "NODE-99", "HUB-12345", "NODE-B#421", "NODE-XYZ99"]

for id_str in uji_id:
    valid, alasan = validasi_id_perangkat(id_str)
    print(f"ID: '{id_str:<12}' -> Valid: {str(valid):<5} | Catatan: {alasan}")

