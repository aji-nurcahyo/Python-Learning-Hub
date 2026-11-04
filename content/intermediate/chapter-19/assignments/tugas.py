"""Starter Code Tugas Mandiri: Telecommunications Station Inventory Manager
Python Learning Hub - Chapter 19: Object-Oriented Programming I

Nama Mahasiswa : ____________________
NIM            : ____________________
Institusi      : Institut Teknologi Sumatera (ITERA)
"""

class StationDevice:
    """Class representasi perangkat keras stasiun pemancar telekomunikasi."""

    def __init__(self, serial_id: str, device_name: str, vendor: str, operating_freq_mhz: float, power_watts: float):
        self.serial_id = serial_id
        self.device_name = device_name
        self.vendor = vendor
        # Inisialisasi melalui property setter
        self.operating_freq_mhz = operating_freq_mhz
        self.power_watts = power_watts

    @property
    def operating_freq_mhz(self) -> float:
        return self._operating_freq_mhz

    @operating_freq_mhz.setter
    def operating_freq_mhz(self, value: float) -> None:
        val = float(value)
        # TODO: Validasi batas rentang 700.0 s/d 6000.0 MHz
        if not (700.0 <= val <= 6000.0):
            raise ValueError(f"Frekuensi {val} MHz di luar batas [700 - 6000 MHz]!")
        self._operating_freq_mhz = val

    @property
    def power_watts(self) -> float:
        return self._power_watts

    @power_watts.setter
    def power_watts(self, value: float) -> None:
        val = float(value)
        # TODO: Validasi batas daya 0.0 s/d 2000.0 Watt
        if not (0.0 <= val <= 2000.0):
            raise ValueError(f"Daya {val} W di luar batas aman [0 - 2000 W]!")
        self._power_watts = val

    def info(self) -> str:
        return f"[{self.serial_id}] {self.device_name} ({self.vendor}) | {self._operating_freq_mhz:.1f} MHz | {self._power_watts:.1f} W"

    def to_dict(self) -> dict:
        return {
            "serial_id": self.serial_id,
            "device_name": self.device_name,
            "vendor": self.vendor,
            "operating_freq_mhz": self._operating_freq_mhz,
            "power_watts": self._power_watts
        }


class StationInventory:
    """Pengelola koleksi perangkat pada stasiun pemancar."""

    def __init__(self, station_id: str, location_name: str):
        self.station_id = station_id
        self.location_name = location_name
        self._devices: dict[str, StationDevice] = {}

    def add_device(self, dev: StationDevice) -> None:
        """Menambahkan perangkat dengan proteksi ID duplikat."""
        if dev.serial_id in self._devices:
            raise KeyError(f"Perangkat dengan serial ID '{dev.serial_id}' sudah terdaftar!")
        self._devices[dev.serial_id] = dev

    def remove_device(self, serial_id: str) -> StationDevice:
        """Menghapus perangkat berdasarkan ID."""
        if serial_id not in self._devices:
            raise KeyError(f"Perangkat ID '{serial_id}' tidak ditemukan!")
        return self._devices.pop(serial_id)

    def search_by_vendor(self, vendor: str) -> list[StationDevice]:
        v_low = vendor.lower()
        return [dev for dev in self._devices.values() if dev.vendor.lower() == v_low]

    def calculate_total_power(self) -> float:
        return sum(dev.power_watts for dev in self._devices.values())

    def summary_report(self) -> None:
        print(f"=== LAPORAN STASIUN TRANSMISI: {self.station_id} ({self.location_name}) ===")
        print(f"Total Perangkat Terpasang : {len(self._devices)}")
        print(f"Total Konsumsi Daya       : {self.calculate_total_power():.1f} Watt")
        for dev in self._devices.values():
            print(f"- {dev.info()}")


if __name__ == "__main__":
    # Demonstrasi Penggunaan & Pengujian
    print("Menginisialisasi stasiun inventaris...")
    stn = StationInventory("BTS-ITERA-01", "Kawasan Kampus ITERA")

    d1 = StationDevice("TX-001", "Radio Unit 4G", "Ericsson", 1800.0, 160.0)
    d2 = StationDevice("TX-002", "Radio Unit 5G NR", "Huawei", 3500.0, 320.0)
    d3 = StationDevice("MW-001", "Microwave Dish Link", "Ericsson", 5800.0, 45.0)

    stn.add_device(d1)
    stn.add_device(d2)
    stn.add_device(d3)

    stn.summary_report()
