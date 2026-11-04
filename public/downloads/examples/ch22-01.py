"""Contoh 22.1: Model Data Capstone (Hierarki Class Perangkat Inventaris)
Python Learning Hub - Level 2: Intermediate Capstone Project
"""

class Device:
    """Class dasar untuk seluruh jenis perangkat telekomunikasi & TI."""

    def __init__(self, device_id: str, name: str, category: str, price: float):
        self.device_id = device_id
        self.name = name
        self.category = category
        self.price = float(price)
        self.status = "ACTIVE"

    def to_dict(self) -> dict:
        return {
            "device_id": self.device_id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "status": self.status
        }

    def __repr__(self) -> str:
        return f"Device(id='{self.device_id}', name='{self.name}', price={self.price})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Device):
            return NotImplemented
        return self.device_id == other.device_id

class RouterDevice(Device):
    """Subclass perangkat jaringan perutean paket."""

    def __init__(self, device_id: str, name: str, price: float, ports: int, routing_proto: str):
        super().__init__(device_id, name, "Network", price)
        self.ports = ports
        self.routing_proto = routing_proto

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({"ports": self.ports, "routing_proto": self.routing_proto})
        return data

print("=== Inisialisasi Model Domain Capstone ===")
dev1 = Device("DEV-001", "Unmanaged Switch 8P", "Hardware", 450000.0)
rtr1 = RouterDevice("RTR-001", "Core Gateway BGP", 12500000.0, 16, "BGP/OSPF")

print("Device Base :", dev1.to_dict())
print("Router Child:", rtr1.to_dict())
print("Equality Check (dev1 == rtr1):", dev1 == rtr1)
