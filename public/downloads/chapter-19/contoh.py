"""Contoh Kode Chapter 19: Object-Oriented Programming I
Python Learning Hub - Level 2: Intermediate Python

Menyajikan implementasi lengkap class Device dan DeviceInventory dalam satu berkas mandiri.
"""

class Device:
    def __init__(self, device_id: str, name: str, category: str, power_watts: float):
        self.device_id = device_id
        self.name = name
        self.category = category
        self.power_watts = power_watts
        self._is_active: bool = True

    @property
    def power_watts(self) -> float:
        return self._power_watts

    @power_watts.setter
    def power_watts(self, value: float) -> None:
        val = float(value)
        if val < 0 or val > 5000:
            raise ValueError(f"Konsumsi daya {val}W di luar batas valid [0 s/d 5000 W]!")
        self._power_watts = val

    @property
    def is_active(self) -> bool:
        return self._is_active

    def activate(self) -> None:
        self._is_active = True

    def deactivate(self) -> None:
        self._is_active = False

    def info(self) -> str:
        st = "AKTIF" if self._is_active else "NON-AKTIF"
        return f"[{self.device_id}] {self.name} ({self.category}) - {self._power_watts:.1f}W [{st}]"

class DeviceInventory:
    def __init__(self, site_name: str):
        self.site_name = site_name
        self._devices: dict[str, Device] = {}

    def add_device(self, dev: Device) -> None:
        if dev.device_id in self._devices:
            raise KeyError(f"ID '{dev.device_id}' sudah terdaftar!")
        self._devices[dev.device_id] = dev

    def total_power(self) -> float:
        return sum(d.power_watts for d in self._devices.values() if d.is_active)

    def summary(self) -> None:
        print(f"=== Inventaris {self.site_name} ===")
        print(f"Total Unit : {len(self._devices)}")
        print(f"Total Daya : {self.total_power():.1f} Watt")
        for d in self._devices.values():
            print(f"- {d.info()}")

if __name__ == "__main__":
    inv = DeviceInventory("BTS ITERA Gedung C")
    inv.add_device(Device("RTR-01", "Core Gateway Router", "Network", 120.0))
    inv.add_device(Device("SW-01", "Aggregation Switch 48P", "Network", 65.0))
    inv.add_device(Device("SRV-01", "Telemetry Processor Node", "Server", 450.0))
    inv.summary()
