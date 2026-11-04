"""Modul DeviceInventory: Manajemen koleksi dan operasi inventaris perangkat.
Python Learning Hub - Chapter 19: Object-Oriented Programming I
"""

from device import Device

class DeviceInventory:
    """Class pengelola koleksi perangkat telekomunikasi dalam satu site/lokasi."""

    def __init__(self, site_name: str):
        self.site_name = site_name
        self._devices: dict[str, Device] = {}

    def add_device(self, device: Device) -> None:
        """Menambahkan perangkat baru ke dalam inventaris."""
        if device.device_id in self._devices:
            raise KeyError(f"Perangkat dengan ID '{device.device_id}' sudah terdaftar di {self.site_name}!")
        self._devices[device.device_id] = device

    def remove_device(self, device_id: str) -> Device:
        """Menghapus perangkat berdasarkan ID dan mengembalikan objek yang dihapus."""
        if device_id not in self._devices:
            raise KeyError(f"Perangkat ID '{device_id}' tidak ditemukan!")
        return self._devices.pop(device_id)

    def get_device(self, device_id: str) -> Device:
        """Mengambil instance perangkat berdasarkan ID."""
        if device_id not in self._devices:
            raise KeyError(f"Perangkat ID '{device_id}' tidak ditemukan!")
        return self._devices[device_id]

    def list_all(self) -> list[Device]:
        return list(self._devices.values())

    def filter_by_category(self, category: str) -> list[Device]:
        cat_lower = category.lower()
        return [dev for dev in self._devices.values() if dev.category.lower() == cat_lower]

    def total_power_consumption(self, active_only: bool = True) -> float:
        """Menghitung total daya konsumsi seluruh perangkat."""
        if active_only:
            return sum(dev.power_watts for dev in self._devices.values() if dev.is_active)
        return sum(dev.power_watts for dev in self._devices.values())

    def summary(self) -> dict:
        devices = list(self._devices.values())
        active_count = sum(1 for d in devices if d.is_active)
        return {
            "site_name": self.site_name,
            "total_devices": len(devices),
            "active_devices": active_count,
            "total_power_active_w": self.total_power_consumption(active_only=True)
        }
