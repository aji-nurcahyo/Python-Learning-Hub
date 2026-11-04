"""Contoh 19.5: Enkapsulasi & Validasi Data Menggunakan @property dan @setter
Python Learning Hub - Level 2: Intermediate Python
"""

class SignalTransmitter:
    """Pemancar sinyal dengan proteksi rentang daya transmisi (dBm)."""

    def __init__(self, transmitter_id: str, power_dbm: float):
        self.transmitter_id = transmitter_id
        # Inisialisasi melalui property setter agar validasi langsung aktif
        self.power_dbm = power_dbm

    @property
    def power_dbm(self) -> float:
        """Getter untuk membaca nilai private atribut _power_dbm."""
        return self._power_dbm

    @power_dbm.setter
    def power_dbm(self, value: float) -> None:
        """Setter dengan validasi batas aman operasional pemancar."""
        val = float(value)
        if not (-30.0 <= val <= 50.0):
            raise ValueError(f"Daya transmisi {val} dBm di luar batas aman [-30.0 s/d 50.0 dBm]!")
        self._power_dbm = val

    def get_status(self) -> str:
        return f"Transmitter '{self.transmitter_id}' operasional pada daya {self._power_dbm:.1f} dBm"

tx = SignalTransmitter("TX-LAMPUNG-01", 33.5)
print(tx.get_status())

# Mengubah nilai lewat setter property
tx.power_dbm = 42.0
print(f"Daya diperbarui: {tx.power_dbm:.1f} dBm")

# Menguji proteksi validasi terhadap nilai di luar rentang
try:
    tx.power_dbm = 75.0
except ValueError as err:
    print(f"Validasi berhasil menangkap error: {err}")
