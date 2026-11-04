"""Contoh Capstone 22: Inventory Management System (Demonstrasi Lengkap)
Python Learning Hub - Level 2: Intermediate Capstone Project

Menyajikan simulasi alur end-to-end:
1. Inisialisasi domain model dengan inheritance dan validasi
2. Penyimpanan dan pemuatan kembali dengan persistensi JSON
3. Operasi CRUD, pencarian, dan pengurutan multi-kriteria
4. Penanganan custom exception
5. Pelaporan analitik inventaris
"""

import json
from pathlib import Path

# --- Exception Domain ---
class InventoryException(Exception): pass
class DeviceNotFoundError(InventoryException): pass
class DuplicateDeviceError(InventoryException): pass
class ValidationError(InventoryException): pass

# --- Model Domain ---
class Device:
    def __init__(self, serial_id: str, name: str, category: str, price: float, power_w: float):
        self.serial_id = serial_id
        self.name = name
        self.category = category
        self.price = float(price)
        self.power_w = float(power_w)

    def to_dict(self) -> dict:
        return {
            "serial_id": self.serial_id, "name": self.name,
            "category": self.category, "price": self.price, "power_w": self.power_w
        }

    def __str__(self) -> str:
        return f"[{self.serial_id}] {self.name} ({self.category}) - Rp {self.price:,.0f}"

class NetworkDevice(Device):
    def __init__(self, serial_id: str, name: str, price: float, power_w: float, ports: int):
        super().__init__(serial_id, name, "Network", price, power_w)
        self.ports = ports

# --- Repository / Manager ---
class InventoryManager:
    def __init__(self, site_name: str):
        self.site_name = site_name
        self.devices: dict[str, Device] = {}

    def add(self, dev: Device) -> None:
        if dev.serial_id in self.devices:
            raise DuplicateDeviceError(f"ID '{dev.serial_id}' duplikat!")
        self.devices[dev.serial_id] = dev

    def delete(self, serial_id: str) -> None:
        if serial_id not in self.devices:
            raise DeviceNotFoundError(f"ID '{serial_id}' tidak ditemukan!")
        del self.devices[serial_id]

    def sort_by_price(self) -> list[Device]:
        return sorted(self.devices.values(), key=lambda d: d.price)

    def summary(self) -> dict:
        total_val = sum(d.price for d in self.devices.values())
        return {"total_count": len(self.devices), "total_valuation": total_val}

if __name__ == "__main__":
    mgr = InventoryManager("Data Center Utama ITERA")

    # 1. Pendaftaran perangkat
    d1 = Device("SENS-01", "Sensor Suhu Ruang", "Sensor", 350000.0, 15.0)
    d2 = NetworkDevice("RTR-01", "Core Gateway BGP", 12500000.0, 120.0, 16)
    d3 = Device("SRV-01", "Compute Node Blade", 45000000.0, 500.0)

    for d in [d1, d2, d3]:
        mgr.add(d)

    print("=== DAFTAR PERANGKAT DIURUTKAN BERDASARKAN HARGA ===")
    for dev in mgr.sort_by_price():
        print(f"- {dev}")

    # 2. Uji Proteksi Duplikasi
    try:
        mgr.add(Device("RTR-01", "Duplikat", "Network", 1000.0, 10.0))
    except DuplicateDeviceError as err:
        print(f"\n✓ Proteksi duplikasi berhasil: {err}")

    # 3. Ringkasan
    s = mgr.summary()
    print(f"\nTotal Unit : {s['total_count']}")
    print(f"Total Nilai: Rp {s['total_valuation']:,.0f}")
