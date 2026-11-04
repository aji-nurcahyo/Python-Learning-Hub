"""Modul Domain Models: Hierarki Domain Model Perangkat untuk Capstone Inventory.
Python Learning Hub - Chapter 22: Intermediate Capstone Project
"""

from validators import validate_serial_id, validate_positive_number, validate_category

class Device:
    """Class induk dasar untuk seluruh perangkat keras inventaris."""

    def __init__(self, serial_id: str, name: str, category: str, price: float, power_watts: float):
        self.serial_id = validate_serial_id(serial_id)
        self.name = str(name).strip()
        self.category = validate_category(category)
        self.price = validate_positive_number(price, "price")
        self.power_watts = validate_positive_number(power_watts, "power_watts")
        self.is_active: bool = True

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
        status_str = "ACTIVE" if self.is_active else "INACTIVE"
        return f"[{self.serial_id}] {self.name} ({self.category}) - Rp {self.price:,.0f} [{status_str}]"

    def __repr__(self) -> str:
        return f"Device('{self.serial_id}', '{self.name}', '{self.category}', {self.price}, {self.power_watts})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Device):
            return NotImplemented
        return self.serial_id == other.serial_id

    def __hash__(self) -> int:
        return hash(self.serial_id)


class NetworkDevice(Device):
    """Subclass perangkat jaringan (Router, Switch, Gateway)."""

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


class SensorDevice(Device):
    """Subclass sensor pemantauan IoT & telemetri fasilitas."""

    def __init__(self, serial_id: str, name: str, price: float, power_watts: float, metric_type: str, reading_unit: str):
        super().__init__(serial_id, name, "Sensor", price, power_watts)
        self.metric_type = metric_type.strip()
        self.reading_unit = reading_unit.strip()

    def to_dict(self) -> dict:
        d = super().to_dict()
        d.update({
            "device_type": "SensorDevice",
            "metric_type": self.metric_type,
            "reading_unit": self.reading_unit
        })
        return d

    @classmethod
    def from_dict(cls, data: dict):
        dev = cls(
            serial_id=data["serial_id"],
            name=data["name"],
            price=data["price"],
            power_watts=data["power_watts"],
            metric_type=data["metric_type"],
            reading_unit=data["reading_unit"]
        )
        dev.is_active = data.get("is_active", True)
        return dev


class ServerDevice(Device):
    """Subclass server komputasi & node virtualisasi."""

    def __init__(self, serial_id: str, name: str, price: float, power_watts: float, cpu_cores: int, ram_gb: int):
        super().__init__(serial_id, name, "Server", price, power_watts)
        self.cpu_cores = int(cpu_cores)
        self.ram_gb = int(ram_gb)

    def to_dict(self) -> dict:
        d = super().to_dict()
        d.update({
            "device_type": "ServerDevice",
            "cpu_cores": self.cpu_cores,
            "ram_gb": self.ram_gb
        })
        return d

    @classmethod
    def from_dict(cls, data: dict):
        dev = cls(
            serial_id=data["serial_id"],
            name=data["name"],
            price=data["price"],
            power_watts=data["power_watts"],
            cpu_cores=data["cpu_cores"],
            ram_gb=data["ram_gb"]
        )
        dev.is_active = data.get("is_active", True)
        return dev

