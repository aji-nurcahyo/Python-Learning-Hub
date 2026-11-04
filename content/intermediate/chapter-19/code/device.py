"""Modul Device: Representasi entitas perangkat telekomunikasi mandiri.
Python Learning Hub - Chapter 19: Object-Oriented Programming I
"""

class Device:
    """Class entitas perangkat keras telekomunikasi.
    
    Menggunakan enkapsulasi berbasis @property untuk validasi parameter teknis
    seperti konsumsi daya dan tegangan operasional.
    """

    def __init__(self, device_id: str, name: str, category: str, power_watts: float):
        self.device_id = device_id
        self.name = name
        self.category = category
        self.power_watts = power_watts  # Menggunakan setter property
        self._is_active: bool = True

    @property
    def power_watts(self) -> float:
        """Getter untuk atribut privat konsumsi daya."""
        return self._power_watts

    @power_watts.setter
    def power_watts(self, value: float) -> None:
        """Setter dengan validasi batas fisik daya (0 s/d 5000 Watt)."""
        val = float(value)
        if val < 0:
            raise ValueError(f"Konsumsi daya tidak boleh negatif ({val} W)!")
        if val > 5000.0:
            raise ValueError(f"Konsumsi daya {val} W melebihi kapasitas rak standar (maks 5000 W)!")
        self._power_watts = val

    @property
    def is_active(self) -> bool:
        return self._is_active

    def activate(self) -> None:
        self._is_active = True

    def deactivate(self) -> None:
        self._is_active = False

    def info(self) -> str:
        status_str = "AKTIF" if self._is_active else "NON-AKTIF"
        return f"[{self.device_id}] {self.name} ({self.category}) - {self._power_watts:.1f}W [{status_str}]"

    def to_dict(self) -> dict:
        return {
            "device_id": self.device_id,
            "name": self.name,
            "category": self.category,
            "power_watts": self._power_watts,
            "is_active": self._is_active
        }
