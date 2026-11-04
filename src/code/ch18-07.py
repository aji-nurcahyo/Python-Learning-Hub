"""Contoh 18.7: Teknik Debugging Logis Menggunakan Assertion & Defensive Checks
Python Learning Hub - Level 2: Intermediate
"""

def hitung_redaman_kabel(daya_masuk_dbm: float, daya_keluar_dbm: float) -> float:
    """Menghitung redaman (loss) kabel transmisi dalam satuan dB."""
    # Debugging assertion untuk memvalidasi invarian logika
    assert daya_masuk_dbm >= daya_keluar_dbm, (
        f"Invarian Gagal: Daya keluar ({daya_keluar_dbm} dBm) tidak boleh lebih besar "
        f"daripada daya masuk ({daya_masuk_dbm} dBm) pada kabel pasif!"
    )
    return round(daya_masuk_dbm - daya_keluar_dbm, 2)

print("Uji Debugging Redaman Kabel:")
# Kasus 1: Perhitungan logis normal
loss_normal = hitung_redaman_kabel(20.0, 16.5)
print(f"  - Kasus Normal : Daya In 20 dBm, Out 16.5 dBm -> Redaman: {loss_normal} dB")

# Kasus 2: Bug logis terdeteksi oleh Assertion
try:
    loss_anomali = hitung_redaman_kabel(10.0, 25.0)
except AssertionError as bug:
    print(f"  - Bug Terdeteksi: {bug}")

