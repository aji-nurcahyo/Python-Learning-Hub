"""Contoh 20.1: Single Inheritance (Pewarisan Class Induk & Class Turunan)
Python Learning Hub - Level 2: Intermediate Python
"""

class BaseDevice:
    """Class induk (parent class) yang mendefinisikan atribut dasar perangkat."""

    def __init__(self, serial_number: str, hostname: str, lokasi: str):
        self.serial_number = serial_number
        self.hostname = hostname
        self.lokasi = lokasi
        self.is_active: bool = True

    def deskripsi_dasar(self) -> str:
        status = "AKTIF" if self.is_active else "NON-AKTIF"
        return f"[{self.serial_number}] {self.hostname} ({self.lokasi}) - {status}"

class NetworkRouter(BaseDevice):
    """Class turunan (child class) yang mewarisi sifat BaseDevice."""

    def __init__(self, serial_number: str, hostname: str, lokasi: str, throughput_gbps: float):
        # Memanggil constructor class induk menggunakan super()
        super().__init__(serial_number, hostname, lokasi)
        self.throughput_gbps = float(throughput_gbps)

    def info_spesifik(self) -> str:
        return f"{self.deskripsi_dasar()} | Throughput: {self.throughput_gbps:.1f} Gbps"

router = NetworkRouter("RT-9901", "Core-Router-Lampung", "Ruang NOC Lt.2", 40.0)

# Memanggil method warisan dari class induk
print("Method warisan :", router.deskripsi_dasar())
# Memanggil method spesifik class turunan
print("Method turunan :", router.info_spesifik())
# Memeriksa relasi tipe objek dengan isinstance dan issubclass
print("isinstance(router, BaseDevice)   :", isinstance(router, BaseDevice))
print("issubclass(NetworkRouter, BaseDevice):", issubclass(NetworkRouter, BaseDevice))
