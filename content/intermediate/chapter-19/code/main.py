"""Main Runner: Eksekusi demonstrasi Device Inventory Manager.
Python Learning Hub - Chapter 19: Object-Oriented Programming I
"""

from device import Device
from inventory import DeviceInventory

def main():
    print("==================================================")
    print("     DEVICE INVENTORY MANAGER — CHAPTER 19        ")
    print("==================================================")

    # Inisialisasi inventaris site telekomunikasi
    site_inv = DeviceInventory("BTS ITERA Gedung C")

    # Mendaftarkan perangkat perangkat keras
    d1 = Device("RTR-01", "Core Gateway Router", "Network", 120.0)
    d2 = Device("SW-01", "Aggregation Switch 48P", "Network", 65.0)
    d3 = Device("SRV-01", "Telemetry Processor Node", "Server", 450.0)
    d4 = Device("SENS-01", "Ambient Temp & Humidity", "Sensor", 15.0)

    for d in [d1, d2, d3, d4]:
        site_inv.add_device(d)
        print(f"+ Terdaftar: {d.info()}")

    # Uji validasi setter @property
    print("\n--- Uji Proteksi Validasi Atribut @property ---")
    try:
        d1.power_watts = -50.0
    except ValueError as err:
        print(f"✓ Validasi daya negatif berhasil dicegah: {err}")

    try:
        d1.power_watts = 6000.0
    except ValueError as err:
        print(f"✓ Validasi daya melebihi kapasitas berhasil dicegah: {err}")

    # Menampilkan ringkasan inventaris
    s = site_inv.summary()
    print("\n--- Ringkasan Inventaris Site ---")
    print(f"Lokasi Site           : {s['site_name']}")
    print(f"Total Perangkat       : {s['total_devices']} unit")
    print(f"Perangkat Aktif       : {s['active_devices']} unit")
    print(f"Total Konsumsi Daya   : {s['total_power_active_w']:.1f} Watt")

    # Filter perangkat berdasarkan kategori
    print("\n--- Filter Kategori 'Network' ---")
    for net_dev in site_inv.filter_by_category("Network"):
        print(f"  * {net_dev.name} ({net_dev.device_id}) -> {net_dev.power_watts}W")

if __name__ == "__main__":
    main()
