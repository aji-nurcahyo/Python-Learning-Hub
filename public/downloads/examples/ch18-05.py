"""Contoh 18.5: Pembuatan dan Pemanggilan Custom Exception (SignalRangeError)
Python Learning Hub - Level 2: Intermediate
"""

class TelecomException(Exception):
    """Kelas dasar exception untuk domain sistem telekomunikasi."""
    pass


class SignalRangeError(TelecomException):
    """Exception yang dipicu ketika level daya sinyal berada di luar rentang fisik."""
    def __init__(self, nilai_dbm: float, pesan: str = "Level daya sinyal melampaui batas batas normal") -> None:
        self.nilai_dbm = nilai_dbm
        super().__init__(f"{pesan} (Terukur: {nilai_dbm} dBm, Rentang: -140 s.d. 0 dBm)")


def validasi_level_sinyal(daya_dbm: float) -> str:
    """Memvalidasi level sinyal penerima (RSRP)."""
    if not (-140.0 <= daya_dbm <= 0.0):
        raise SignalRangeError(daya_dbm)
    return "VALID"

daftar_uji = [-85.0, -110.5, 15.0, -155.0]

print("Uji Penilaian Level Sinyal dengan Custom Exception:")
for nilai in daftar_uji:
    try:
        status = validasi_level_sinyal(nilai)
        print(f"  - Daya {nilai:>6.1f} dBm -> Status: {status}")
    except SignalRangeError as err:
        print(f"  - Daya {nilai:>6.1f} dBm -> TERTANGKAP: {err}")
