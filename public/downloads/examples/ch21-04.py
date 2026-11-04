"""Contoh 21.4: Pola Dasar Automated Testing Menggunakan Assertion
Python Learning Hub - Level 2: Intermediate Python
"""

def konversi_dbm_ke_milliwatt(dbm: float) -> float:
    """Mengonversi daya dBm ke mW: P(mW) = 10^(dBm / 10)."""
    return round(10 ** (dbm / 10), 4)

def konversi_milliwatt_ke_dbm(mw: float) -> float:
    """Mengonversi daya mW ke dBm: P(dBm) = 10 * log10(mW)."""
    import math
    if mw <= 0:
        raise ValueError("Daya mW harus bernilai positif!")
    return round(10 * math.log10(mw), 2)

# Menjalankan pengujian berbasis assertion
print("=== Menjalankan Test Assertions ===")

# Test 1: 0 dBm harus setara dengan 1.0 mW
assert konversi_dbm_ke_milliwatt(0.0) == 1.0, "Gagal: 0 dBm harus = 1.0 mW"
print("✓ Test 1 LULUS: 0 dBm == 1.0 mW")

# Test 2: 10 dBm harus setara dengan 10.0 mW
assert konversi_dbm_ke_milliwatt(10.0) == 10.0, "Gagal: 10 dBm harus = 10.0 mW"
print("✓ Test 2 LULUS: 10 dBm == 10.0 mW")

# Test 3: 20 dBm harus setara dengan 100.0 mW
assert konversi_dbm_ke_milliwatt(20.0) == 100.0, "Gagal: 20 dBm harus = 100.0 mW"
print("✓ Test 3 LULUS: 20 dBm == 100.0 mW")

# Test 4: 100 mW dikonversi balik ke dBm harus 20.0 dBm
assert konversi_milliwatt_ke_dbm(100.0) == 20.0, "Gagal: 100 mW harus = 20.0 dBm"
print("✓ Test 4 LULUS: 100.0 mW == 20.0 dBm")

print("\nSemua 4 test assertion berhasil dieksekusi tanpa error!")
