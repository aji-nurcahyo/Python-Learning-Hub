"""Contoh 21.6: Parameterized Testing (Tabel Kasus Uji Otomatis)
Python Learning Hub - Level 2: Intermediate Python
"""

# Dalam pytest, pola ini diimplementasikan via:
# @pytest.mark.parametrize("ip_input, expected_valid", [...])

def validasi_format_ipv4(ip: str) -> bool:
    """Memeriksa validitas format alamat IPv4 (4 oktet angka 0-255)."""
    parts = ip.strip().split(".")
    if len(parts) != 4:
        return False
    for p in parts:
        if not p.isdigit() or not (0 <= int(p) <= 255):
            return False
        # Mencegah leading zero seperti "01"
        if len(p) > 1 and p.startswith("0"):
            return False
    return True

# Tabel kasus uji parameterisasi
test_matrix = [
    ("192.168.1.1", True, "Alamat IP privat standar"),
    ("10.0.0.254", True, "Alamat IP kelas A valid"),
    ("256.100.0.1", False, "Oktet melebihi batas 255"),
    ("192.168.1", False, "Kurang dari 4 oktet"),
    ("192.168.1.01", False, "Memiliki leading zero"),
    ("10.a.0.1", False, "Karakter non-numerik"),
]

print("=== Menjalankan Parameterized Test Suite ===")
passed_count = 0
for idx, (ip_str, expected, reason) in enumerate(test_matrix, start=1):
    actual = validasi_format_ipv4(ip_str)
    assert actual == expected, f"Gagal pada kasus {idx}: {ip_str}"
    status_str = "VALID" if actual else "INVALID"
    print(f"Kasus {idx:02d}: {ip_str:<15} -> {status_str:<7} [LULUS] ({reason})")
    passed_count += 1

print(f"\nHasil: {passed_count}/{len(test_matrix)} kasus parameterisasi LULUS.")
