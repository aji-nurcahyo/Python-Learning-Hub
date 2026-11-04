"""Modul InventoryManager: Service layer manajemen inventaris perangkat.
Python Learning Hub - Chapter 22: Intermediate Capstone Project
"""

from exceptions import DuplicateDeviceError, DeviceNotFoundError
from domain_models import Device
from storage import JSONStorageHandler

class InventoryManager:
    """Pengelola repositori inventaris perangkat dengan dukungan persistensi dan analitik."""

    def __init__(self, site_name: str, storage_handler: JSONStorageHandler | None = None):
        self.site_name = site_name
        self.storage = storage_handler
        self._devices: dict[str, Device] = {}

        if self.storage:
            self.reload_from_storage()

    def reload_from_storage(self) -> None:
        """Memuat ulang seluruh data dari storage handler."""
        if self.storage:
            loaded = self.storage.load()
            self._devices = {dev.serial_id: dev for dev in loaded}

    def save_to_storage(self) -> None:
        """Menyimpan keadaan memori saat ini ke storage handler."""
        if self.storage:
            self.storage.save(list(self._devices.values()))

    # --- Operasi CRUD Dasar ---

    def create_device(self, device: Device) -> None:
        """CREATE: Mendaftarkan perangkat baru."""
        if device.serial_id in self._devices:
            raise DuplicateDeviceError(f"Perangkat dengan serial ID '{device.serial_id}' sudah terdaftar!")
        self._devices[device.serial_id] = device
        self.save_to_storage()

    def get_device(self, serial_id: str) -> Device:
        """READ: Mengambil satu perangkat berdasarkan serial ID."""
        s = serial_id.strip().upper()
        if s not in self._devices:
            raise DeviceNotFoundError(f"Perangkat ID '{serial_id}' tidak ditemukan!")
        return self._devices[s]

    def update_price(self, serial_id: str, new_price: float) -> Device:
        """UPDATE: Memperbarui harga perangkat."""
        dev = self.get_device(serial_id)
        dev.price = float(new_price)
        self.save_to_storage()
        return dev

    def toggle_status(self, serial_id: str) -> Device:
        """UPDATE: Mengubah status aktif / non-aktif perangkat."""
        dev = self.get_device(serial_id)
        dev.is_active = not dev.is_active
        self.save_to_storage()
        return dev

    def delete_device(self, serial_id: str) -> Device:
        """DELETE: Menghapus perangkat dari sistem."""
        dev = self.get_device(serial_id)
        del self._devices[dev.serial_id]
        self.save_to_storage()
        return dev

    # --- Operasi Pencarian, Filter & Pengurutan ---

    def list_all(self) -> list[Device]:
        return list(self._devices.values())

    def search_by_keyword(self, keyword: str) -> list[Device]:
        """Pencarian substring pada nama atau serial ID (case-insensitive)."""
        kw = keyword.strip().lower()
        return [
            d for d in self._devices.values()
            if kw in d.name.lower() or kw in d.serial_id.lower()
        ]

    def filter_by_category(self, category: str) -> list[Device]:
        cat_lower = category.strip().lower()
        return [d for d in self._devices.values() if d.category.lower() == cat_lower]

    def sort_devices(self, key: str = "price", descending: bool = False) -> list[Device]:
        """Mengurutkan perangkat berdasarkan: 'price', 'name', 'power', atau 'serial'."""
        key_map = {
            "price": lambda d: d.price,
            "name": lambda d: d.name.lower(),
            "power": lambda d: d.power_watts,
            "serial": lambda d: d.serial_id,
        }
        sort_fn = key_map.get(key, lambda d: d.price)
        return sorted(self._devices.values(), key=sort_fn, reverse=descending)

    # --- Ringkasan & Analitik Portofolio ---

    def calculate_summary(self) -> dict:
        devices = list(self._devices.values())
        total_val = sum(d.price for d in devices)
        total_pwr = sum(d.power_watts for d in devices if d.is_active)
        
        cat_dist = {}
        for d in devices:
            cat_dist[d.category] = cat_dist.get(d.category, 0) + 1

        return {
            "site_name": self.site_name,
            "total_count": len(devices),
            "active_count": sum(1 for d in devices if d.is_active),
            "total_valuation_idr": total_val,
            "total_power_active_w": total_pwr,
            "category_distribution": cat_dist
        }

