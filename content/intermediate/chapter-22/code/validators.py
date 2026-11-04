"""Modul Validators: Fungsi-fungsi validasi input dan integritas data.
Python Learning Hub - Chapter 22: Intermediate Capstone Project
"""

import re
from exceptions import ValidationError

VALID_CATEGORIES = {"Network", "Server", "Sensor", "Storage", "Power"}

def validate_serial_id(serial_id: str) -> str:
    """Memvalidasi format nomor seri (misal: RTR-001, SW-10, SENS-99)."""
    s = str(serial_id).strip().upper()
    if not re.match(r"^[A-Z0-9]{2,8}-[A-Z0-9]{2,8}$", s):
        raise ValidationError(f"Format serial ID '{serial_id}' tidak valid! Contoh format valid: 'RTR-01' atau 'SENS-99'.")
    return s

def validate_positive_number(val: float, field_name: str) -> float:
    try:
        num = float(val)
    except (ValueError, TypeError):
        raise ValidationError(f"Field '{field_name}' harus berupa angka numerik!")
    if num <= 0:
        raise ValidationError(f"Field '{field_name}' harus bernilai positif lebih besar dari nol!")
    return num

def validate_category(category: str) -> str:
    cat = str(category).strip().title()
    if cat not in VALID_CATEGORIES:
        raise ValidationError(f"Kategori '{category}' tidak dikenali! Pilihan valid: {sorted(VALID_CATEGORIES)}.")
    return cat

def validate_ip_address(ip: str) -> str:
    parts = ip.strip().split(".")
    if len(parts) != 4:
        raise ValidationError(f"Format IP '{ip}' tidak valid (harus 4 oktet)!")
    for p in parts:
        if not p.isdigit() or not (0 <= int(p) <= 255):
            raise ValidationError(f"Oktet '{p}' pada IP '{ip}' di luar batas [0-255]!")
    return ip.strip()

