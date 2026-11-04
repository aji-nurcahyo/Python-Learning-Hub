"""Modul MultiDeviceManager: Pengelola koleksi multi-perangkat polimorfik.
Python Learning Hub - Chapter 20: Object-Oriented Programming II
"""

from models import Device

class MultiDeviceManager:
    """Class sistem yang mengelola berbagai jenis perangkat turunan secara polimorfik."""

    def __init__(self, datacenter_name: str):
        self.datacenter_name = datacenter_name
        self._devices: dict[str, Device] = {}

    def register_device(self, device: Device) -> None:
        """Mendaftarkan perangkat apa pun yang merupakan turunan dari Device."""
        if not isinstance(device, Device):
            raise TypeError("Objek yang didaftarkan harus merupakan instance atau turunan dari Device!")
        if device.serial_id in self._devices:
            raise KeyError(f"Perangkat dengan serial ID '{device.serial_id}' sudah terdaftar!")
        self._devices[device.serial_id] = device

    def run_all_diagnostics(self) -> list[dict]:
        """Eksekusi polimorfik: Memanggil diagnostics() seragam pada objek yang berbeda kelas."""
        return [dev.diagnostics() for dev in self._devices.values()]

    def calculate_total_power(self) -> float:
        return sum(dev.power_watts for dev in self._devices.values())

    def filter_by_class(self, device_class: type) -> list[Device]:
        """Mengambil perangkat berdasarkan tipe class spesifik."""
        return [dev for dev in self._devices.values() if isinstance(dev, device_class)]

    def generate_report(self) -> None:
        print(f"==================================================")
        print(f"  LAPORAN DIAGNOSTIK MULTI-PERANGKAT: {self.datacenter_name}  ")
        print(f"==================================================")
        print(f"Total Perangkat : {len(self._devices)} unit")
        print(f"Konsumsi Daya   : {self.calculate_total_power():.1f} Watt\n")
        
        for diag in self.run_all_diagnostics():
            print(f"[{diag['type']:<18}] {diag['hostname']:<24} | {diag['metric']} ({diag['status']})")
        print(f"==================================================")
