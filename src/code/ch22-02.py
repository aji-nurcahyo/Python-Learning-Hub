"""Contoh 22.2: Validasi Input & Hierarki Exception Kustom Capstone
Python Learning Hub - Level 2: Intermediate Capstone Project
"""

class InventoryException(Exception):
    """Base exception untuk seluruh domain sistem inventaris."""
    pass

class DeviceNotFoundError(InventoryException):
    """Dilempar saat ID perangkat tidak ditemukan dalam repositori."""
    pass

class DuplicateDeviceError(InventoryException):
    """Dilempar saat registrasi ID perangkat yang sudah ada."""
    pass

class ValidationError(InventoryException):
    """Dilempar saat format data atau nilai atribut tidak valid."""
    pass

def validasi_device_payload(payload: dict) -> None:
    required_keys = ["device_id", "name", "price"]
    for k in required_keys:
        if k not in payload:
            raise ValidationError(f"Field wajib '{k}' tidak ditemukan!")
    if not isinstance(payload["price"], (int, float)) or payload["price"] <= 0:
        raise ValidationError("Harga perangkat ('price') harus berupa angka positif!")

print("=== Pengujian Sistem Validasi & Exception Capstone ===")

valid_data = {"device_id": "SRV-10", "name": "Compute Blade", "price": 45000000.0}
validasi_device_payload(valid_data)
print("✓ Validasi data valid: BERHASIL")

# Uji error 1: Harga negatif
try:
    validasi_device_payload({"device_id": "SRV-10", "name": "Compute Blade", "price": -500})
except ValidationError as exc:
    print(f"✓ Error berhasil ditangkap: {exc}")

# Uji error 2: Key hilang
try:
    validasi_device_payload({"device_id": "SRV-10"})
except ValidationError as exc:
    print(f"✓ Error berhasil ditangkap: {exc}")
