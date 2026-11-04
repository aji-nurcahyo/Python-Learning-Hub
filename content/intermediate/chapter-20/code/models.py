"""Modul Models: Hierarki Class Perangkat Telekomunikasi Berorientasi Objek.
Python Learning Hub - Chapter 20: Object-Oriented Programming II
"""

class Device:
    """Class induk (parent class) yang mendefinisikan atribut dan perilaku dasar."""

    def __init__(self, serial_id: str, hostname: str, ip_address: str, power_watts: float):
        self.serial_id = serial_id
        self.hostname = hostname
        self.ip_address = ip_address
        self.power_watts = float(power_watts)
        self.is_active: bool = True

    def diagnostics(self) -> dict:
        """Method diagnostik dasar yang akan di-override oleh class turunan."""
        status_str = "ACTIVE" if self.is_active else "INACTIVE"
        return {
            "serial_id": self.serial_id,
            "hostname": self.hostname,
            "type": "Generic Device",
            "status": status_str,
            "metric": f"Daya: {self.power_watts:.1f}W"
        }

    def __str__(self) -> str:
        """Representasi ramah pengguna (user-friendly)."""
        return f"{self.hostname} ({self.ip_address}) [{self.serial_id}]"

    def __repr__(self) -> str:
        """Representasi formal untuk developer dan debugging."""
        return f"Device(serial_id='{self.serial_id}', hostname='{self.hostname}', power_watts={self.power_watts})"

    def __eq__(self, other: object) -> bool:
        """Dua perangkat dianggap setara jika memiliki serial ID yang sama."""
        if not isinstance(other, Device):
            return NotImplemented
        return self.serial_id == other.serial_id

    def __hash__(self) -> int:
        """Memastikan objek tetap hashable untuk digunakan dalam set atau dictionary key."""
        return hash(self.serial_id)


class RouterDevice(Device):
    """Class turunan spesifik untuk Router jaringan."""

    def __init__(self, serial_id: str, hostname: str, ip_address: str, power_watts: float, throughput_gbps: float, protocol: str):
        super().__init__(serial_id, hostname, ip_address, power_watts)
        self.throughput_gbps = float(throughput_gbps)
        self.protocol = protocol

    def diagnostics(self) -> dict:
        # Override dan perluas diagnostik dasar
        diag = super().diagnostics()
        diag.update({
            "type": "Core Router",
            "metric": f"Throughput: {self.throughput_gbps:.1f} Gbps | Protokol: {self.protocol}"
        })
        return diag


class SwitchDevice(Device):
    """Class turunan spesifik untuk Switch distribusi / akses."""

    def __init__(self, serial_id: str, hostname: str, ip_address: str, power_watts: float, port_count: int, poe_enabled: bool = False):
        super().__init__(serial_id, hostname, ip_address, power_watts)
        self.port_count = int(port_count)
        self.poe_enabled = poe_enabled

    def diagnostics(self) -> dict:
        diag = super().diagnostics()
        poe_str = "PoE Supported" if self.poe_enabled else "Non-PoE"
        diag.update({
            "type": "Network Switch",
            "metric": f"Port: {self.port_count} ({poe_str})"
        })
        return diag


class SensorDevice(Device):
    """Class turunan spesifik untuk Sensor lingkungan IoT/BTS."""

    def __init__(self, serial_id: str, hostname: str, ip_address: str, power_watts: float, sensor_type: str, reading_value: float, unit: str):
        super().__init__(serial_id, hostname, ip_address, power_watts)
        self.sensor_type = sensor_type
        self.reading_value = float(reading_value)
        self.unit = unit

    def diagnostics(self) -> dict:
        diag = super().diagnostics()
        diag.update({
            "type": f"Sensor ({self.sensor_type})",
            "metric": f"Nilai Bacaan: {self.reading_value:.2f} {self.unit}"
        })
        return diag
