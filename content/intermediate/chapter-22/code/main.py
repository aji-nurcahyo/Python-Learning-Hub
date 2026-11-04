"""CLI Main Runner: Terminal-based Inventory Management System.
Python Learning Hub - Chapter 22: Intermediate Capstone Project
"""

import sys
from pathlib import Path
from exceptions import InventoryException
from domain_models import NetworkDevice, ServerDevice, SensorDevice
from storage import JSONStorageHandler
from inventory_manager import InventoryManager

def print_menu():
    print("\n" + "=" * 50)
    print("      INVENTORY MANAGEMENT SYSTEM (CAPSTONE)      ")
    print("=" * 50)
    print("1. Tampilkan Semua Perangkat (List All)")
    print("2. Tambah Perangkat Jaringan (Network Device)")
    print("3. Tambah Server Node (Server Device)")
    print("4. Tambah Sensor Telemetri (Sensor Device)")
    print("5. Cari Perangkat (Keyword Search)")
    print("6. Urutkan Perangkat (Sort by Price/Name)")
    print("7. Hapus Perangkat (Delete)")
    print("8. Tampilkan Laporan Ringkasan Aset")
    print("0. Keluar (Exit)")
    print("=" * 50)

def main():
    db_file = Path(__file__).resolve().parent / "data" / "inventory_db.json"
    storage = JSONStorageHandler(db_file)
    manager = InventoryManager("Data Center Kampus ITERA", storage)

    # Inisialisasi data awal jika penyimpanan masih kosong
    if len(manager.list_all()) == 0:
        manager.create_device(NetworkDevice("RTR-01", "Core Gateway BGP", 14500000.0, 150.0, 16, "BGP/OSPF"))
        manager.create_device(ServerDevice("SRV-01", "Database Cluster Blade", 38000000.0, 450.0, 32, 128))
        manager.create_device(SensorDevice("SN-01", "Rack Humidity & Temp", 450000.0, 12.0, "Climate", "°C / %RH"))

    print(f"Sistem aktif. Terhubung ke basis data: {db_file.name}")
    print(f"Total perangkat tersimpan saat ini: {len(manager.list_all())} unit.")

    # Menampilkan ringkasan awal
    s = manager.calculate_summary()
    print(f"Site: {s['site_name']} | Total Aset: Rp {s['total_valuation_idr']:,.0f} | Daya: {s['total_power_active_w']:.1f}W")

if __name__ == "__main__":
    main()
