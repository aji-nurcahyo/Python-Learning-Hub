"""Contoh 19.4: Perbedaan Instance Attributes vs Class Attributes
Python Learning Hub - Level 2: Intermediate Python
"""

class NetworkDevice:
    # Class Attribute: dibagi bersama oleh seluruh instance dari class ini
    vendor_default: str = "ITERA-Telecom"
    total_devices: int = 0

    def __init__(self, device_id: str, hostname: str, ip_address: str):
        # Instance Attributes: unik dan independen untuk setiap instance object
        self.device_id = device_id
        self.hostname = hostname
        self.ip_address = ip_address
        
        # Mengubah class attribute melalui nama class
        NetworkDevice.total_devices += 1

    def info(self) -> str:
        return f"Device #{self.device_id}: {self.hostname} ({self.ip_address}) [Vendor: {self.vendor_default}]"

print(f"Total awal perangkat: {NetworkDevice.total_devices}")

d1 = NetworkDevice("DEV-001", "Core-Router-A", "10.10.1.1")
d2 = NetworkDevice("DEV-002", "Distribution-Switch-B", "10.10.1.2")
d3 = NetworkDevice("DEV-003", "Access-Point-Floor1", "10.10.2.10")

print(d1.info())
print(d2.info())
print(d3.info())

print(f"Total akhir perangkat terdaftar: {NetworkDevice.total_devices}")
print(f"Akses class attribute lewat instance d1: {d1.vendor_default}")
