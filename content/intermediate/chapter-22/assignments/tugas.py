"""Starter Code Tugas Mandiri: Intermediate Capstone Project — Inventory Management System
Python Learning Hub - Chapter 22: Intermediate Capstone Project

Nama Mahasiswa : ____________________
NIM            : ____________________
Institusi      : Institut Teknologi Sumatera (ITERA)
"""

import json
from pathlib import Path
from typing import Optional

# =====================================================================
# BAGIAN 1: Hierarki Custom Exceptions
# =====================================================================

class InventoryException(Exception):
    """Base exception untuk domain sistem inventaris."""
    pass

class DeviceNotFoundError(InventoryException):
    """Dilempar saat ID perangkat tidak ditemukan."""
    pass

class DuplicateDeviceError(InventoryException):
    """Dilempar saat registrasi ID perangkat yang sudah ada."""
    pass

class ValidationError(InventoryException):
    """Dilempar saat data input tidak valid."""
    pass


# =====================================================================
# BAGIAN 2: Model Domain OOP (Device & Subclasses)
# =====================================================================

class Device:
    """Class induk perangkat inventaris."""

    def __init__(self, serial_id: str, name: str, category: str, price: float, power_watts: float):
        self.serial_id = str(serial_id).strip().upper()
        self.name = str(name).strip()
        self.category = str(category).strip().title()
        self.price = float(price)
        self.power_watts = float(power_watts)
        self.is_active = True

        if self.price <= 0:
            raise ValidationError("Harga perangkat harus bernilai positif lebih besar dari nol!")
        if self.power_watts <= 0:
            raise ValidationError("Konsumsi daya harus bernilai lebih besar dari nol!")

    def to_dict(self) -> dict:
        return {
            "device_type": "Device",
            "serial_id": self.serial_id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "power_watts": self.power_watts,
            "is_active": self.is_active
        }

    @classmethod
    def from_dict(cls, data: dict):
        dev = cls(
            serial_id=data["serial_id"],
            name=data["name"],
            category=data["category"],
            price=data["price"],
            power_watts=data["power_watts"]
        )
        dev.is_active = data.get("is_active", True)
        return dev

    def __str__(self) -> str:
        st = "ACTIVE" if self.is_active else "INACTIVE"
        return f"[{self.serial_id}] {self.name} ({self.category}) - Rp {self.price:,.0f} [{st}]"

    def __repr__(self) -> str:
        return f"Device('{self.serial_id}', '{self.name}', {self.price})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Device):
            return NotImplemented
        return self.serial_id == other.serial_id

    def __hash__(self) -> int:
        return hash(self.serial_id)


class NetworkDevice(Device):
    """Subclass perangkat jaringan (Router, Switch)."""

    def __init__(self, serial_id: str, name: str, price: float, power_watts: float, ports: int, routing_protocol: str):
        super().__init__(serial_id, name, "Network", price, power_watts)
        self.ports = int(ports)
        self.routing_protocol = routing_protocol.strip()

    def to_dict(self) -> dict:
        d = super().to_dict()
        d.update({
            "device_type": "NetworkDevice",
            "ports": self.ports,
            "routing_protocol": self.routing_protocol
        })
        return d

    @classmethod
    def from_dict(cls, data: dict):
        dev = cls(
            serial_id=data["serial_id"],
            name=data["name"],
            price=data["price"],
            power_watts=data["power_watts"],
            ports=data["ports"],
            routing_protocol=data["routing_protocol"]
        )
        dev.is_active = data.get("is_active", True)
        return dev


# =====================================================================
# BAGIAN 3: Manajer Inventaris & Persistensi
# =====================================================================

class InventoryManager:
    def __init__(self, site_name: str, file_path: Optional[Path] = None):
        self.site_name = site_name
        self.file_path = file_path
        self._devices: dict[str, Device] = {}

    def create(self, dev: Device) -> None:
        """TODO: Tambahkan perangkat ke _devices, cegah ID duplikat."""
        if dev.serial_id in self._devices:
            raise DuplicateDeviceError(f"Serial ID '{dev.serial_id}' sudah terdaftar!")
        self._devices[dev.serial_id] = dev

    def read(self, serial_id: str) -> Device:
        """TODO: Ambil perangkat berdasarkan ID, lempar DeviceNotFoundError jika tidak ada."""
        s = serial_id.strip().upper()
        if s not in self._devices:
            raise DeviceNotFoundError(f"Perangkat ID '{serial_id}' tidak ditemukan!")
        return self._devices[s]

    def update_price(self, serial_id: str, new_price: float) -> None:
        dev = self.read(serial_id)
        if new_price <= 0:
            raise ValidationError("Harga baru harus bernilai positif!")
        dev.price = float(new_price)

    def delete(self, serial_id: str) -> Device:
        dev = self.read(serial_id)
        return self._devices.pop(dev.serial_id)

    def list_all(self) -> list[Device]:
        return list(self._devices.values())

    def sort_by_price(self, descending: bool = False) -> list[Device]:
        return sorted(self._devices.values(), key=lambda d: d.price, reverse=descending)

    def calculate_summary(self) -> dict:
        devs = list(self._devices.values())
        return {
            "site_name": self.site_name,
            "total_count": len(devs),
            "total_valuation": sum(d.price for d in devs)
        }


# =====================================================================
# BAGIAN 4: Demonstrasi & Eksekusi Proyek
# =====================================================================

if __name__ == "__main__":
    print("Menginisialisasi Inventory Management System Capstone...")
    mgr = InventoryManager("NOC ITERA Kampus")

    d1 = Device("SENS-01", "Sensor Suhu Lingkungan", "Sensor", 350000.0, 10.0)
    d2 = NetworkDevice("RTR-01", "Core Gateway BGP", 14500000.0, 150.0, 16, "BGP")

    mgr.create(d1)
    mgr.create(d2)

    print("\n--- Daftar Inventaris Terurut Berdasarkan Harga ---")
    for d in mgr.sort_by_price():
        print(f"  {d}")

    summary = mgr.calculate_summary()
    print(f"\nTotal Perangkat: {summary['total_count']}")
    print(f"Total Nilai Aset: Rp {summary['total_valuation']:,.0f}")

