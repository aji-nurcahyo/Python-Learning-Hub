"""Contoh 19.7: Interaksi Antar Object (Device Inventory Manager)
Python Learning Hub - Level 2: Intermediate Python
"""

class Device:
    def __init__(self, serial: str, tipe: str, konsumsi_daya: float):
        self.serial = serial
        self.tipe = tipe
        self.konsumsi_daya = float(konsumsi_daya)

    def deskripsi(self) -> str:
        return f"[{self.serial}] {self.tipe} ({self.konsumsi_daya:.1f}W)"

class DeviceInventory:
    def __init__(self, lokasi: str):
        self.lokasi = lokasi
        self._daftar_device: list[Device] = []

    def tambah_device(self, dev: Device) -> None:
        self._daftar_device.append(dev)

    def total_konsumsi(self) -> float:
        return sum(d.konsumsi_daya for d in self._daftar_device)

    def cari_berdasarkan_tipe(self, tipe: str) -> list[Device]:
        return [d for d in self._daftar_device if d.tipe.lower() == tipe.lower()]

    def cetak_laporan(self) -> None:
        print(f"=== Laporan Inventaris Ruang Server: {self.lokasi} ===")
        print(f"Total Perangkat : {len(self._daftar_device)}")
        print(f"Total Konsumsi  : {self.total_konsumsi():.1f} Watt")
        for dev in self._daftar_device:
            print(f"- {dev.deskripsi()}")

inv = DeviceInventory("Data Center ITERA Gd. C")
inv.tambah_device(Device("RTR-01", "Router", 65.0))
inv.tambah_device(Device("SW-01", "Switch", 40.0))
inv.tambah_device(Device("SRV-01", "Server", 350.0))
inv.tambah_device(Device("SW-02", "Switch", 45.0))

inv.cetak_laporan()

switches = inv.cari_berdasarkan_tipe("Switch")
print(f"\nDitemukan {len(switches)} perangkat bertipe 'Switch':")
for sw in switches:
    print(f"* {sw.serial} konsumsi daya {sw.konsumsi_daya}W")
