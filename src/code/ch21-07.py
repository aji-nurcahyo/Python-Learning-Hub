"""Contoh 21.7: Pola Pengujian Exception (Testing Errors dengan Assert)
Python Learning Hub - Level 2: Intermediate Python
"""

# Dalam pytest, pengujian exception ditulis dengan:
# with pytest.raises(ExpectedException):
#     fungsi_yang_gagal()

class InvalidFrequencyError(ValueError):
    """Exception kustom untuk frekuensi di luar spektrum operasional."""
    pass

def set_frekuensi_carrier(freq_mhz: float) -> str:
    if not (700.0 <= freq_mhz <= 3800.0):
        raise InvalidFrequencyError(f"Frekuensi {freq_mhz} MHz di luar batas alokasi seluler [700-3800 MHz]!")
    return f"Carrier aktif pada {freq_mhz:.1f} MHz"

print("=== Menjalankan Exception Testing Suite ===")

# Kasus 1: Input valid harus berhasil tanpa exception
hasil = set_frekuensi_carrier(1800.0)
assert "1800.0 MHz" in hasil
print("✓ Kasus 1: Input frekuensi valid (1800 MHz) berjalan normal.")

# Kasus 2: Input frekuensi terlalu rendah (400 MHz) harus memicu InvalidFrequencyError
terpemicu = False
try:
    set_frekuensi_carrier(400.0)
except InvalidFrequencyError as exc:
    terpemicu = True
    print(f"✓ Kasus 2: Exception berhasil tertangkap: '{exc}'")
assert terpemicu, "Gagal: InvalidFrequencyError seharusnya terpicu!"

# Kasus 3: Input frekuensi terlalu tinggi (5000 MHz) harus memicu InvalidFrequencyError
terpemicu = False
try:
    set_frekuensi_carrier(5000.0)
except InvalidFrequencyError as exc:
    terpemicu = True
    print(f"✓ Kasus 3: Exception berhasil tertangkap: '{exc}'")
assert terpemicu, "Gagal: InvalidFrequencyError seharusnya terpicu!"

print("\nSeluruh pengujian assertion exception berhasil diverifikasi!")
