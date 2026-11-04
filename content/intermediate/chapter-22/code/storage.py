"""Modul Storage: Persistensi berkas JSON untuk Inventory Management System.
Python Learning Hub - Chapter 22: Intermediate Capstone Project
"""

import json
from pathlib import Path
from exceptions import StorageError
from domain_models import Device, NetworkDevice, SensorDevice, ServerDevice

TYPE_REGISTRY = {
    "Device": Device,
    "NetworkDevice": NetworkDevice,
    "SensorDevice": SensorDevice,
    "ServerDevice": ServerDevice,
}

class JSONStorageHandler:
    """Pengelola serialisasi dan deserialisasi berkas data JSON terisolasi."""

    def __init__(self, file_path: str | Path):
        self.file_path = Path(file_path)

    def save(self, devices: list[Device]) -> None:
        """Menyimpan daftar perangkat ke berkas JSON dengan encoding UTF-8."""
        try:
            self.file_path.parent.mkdir(parents=True, exist_ok=True)
            data = [dev.to_dict() for dev in devices]
            
            temp_file = self.file_path.with_suffix(".tmp")
            with open(temp_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            temp_file.replace(self.file_path)
        except Exception as err:
            raise StorageError(f"Gagal menyimpan data ke '{self.file_path}': {err}") from err

    def load(self) -> list[Device]:
        """Memuat daftar perangkat dari berkas JSON dan menginstansiasi class aslinya."""
        if not self.file_path.exists():
            return []

        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            devices: list[Device] = []
            for item in data:
                dtype = item.get("device_type", "Device")
                cls = TYPE_REGISTRY.get(dtype, Device)
                devices.append(cls.from_dict(item))
            return devices
        except Exception as err:
            raise StorageError(f"Gagal membaca data dari '{self.file_path}': {err}") from err
