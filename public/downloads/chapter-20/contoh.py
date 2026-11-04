"""Contoh Kode Chapter 20: Object-Oriented Programming II
Python Learning Hub - Level 2: Intermediate Python

Menyajikan implementasi hierarki inheritance, method overriding, super(),
polimorfisme, dan special methods dunder (__str__, __repr__, __eq__, __hash__).
"""

class Device:
    def __init__(self, serial_id: str, hostname: str, power_watts: float):
        self.serial_id = serial_id
        self.hostname = hostname
        self.power_watts = float(power_watts)

    def diagnostics(self) -> str:
        return f"Device {self.hostname}: Daya {self.power_watts}W"

    def __str__(self) -> str:
        return f"{self.hostname} [{self.serial_id}]"

    def __repr__(self) -> str:
        return f"Device('{self.serial_id}', '{self.hostname}', {self.power_watts})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Device):
            return NotImplemented
        return self.serial_id == other.serial_id

    def __hash__(self) -> int:
        return hash(self.serial_id)

class RouterDevice(Device):
    def __init__(self, serial_id: str, hostname: str, power_watts: float, throughput_gbps: float):
        super().__init__(serial_id, hostname, power_watts)
        self.throughput_gbps = float(throughput_gbps)

    def diagnostics(self) -> str:
        # Override method parent dengan memanggil super()
        parent_diag = super().diagnostics()
        return f"[Router] {parent_diag} | Throughput: {self.throughput_gbps} Gbps"

class SwitchDevice(Device):
    def __init__(self, serial_id: str, hostname: str, power_watts: float, ports: int):
        super().__init__(serial_id, hostname, power_watts)
        self.ports = ports

    def diagnostics(self) -> str:
        parent_diag = super().diagnostics()
        return f"[Switch] {parent_diag} | Kapasitas: {self.ports} Port"

if __name__ == "__main__":
    devices: list[Device] = [
        RouterDevice("RT-01", "Core-Router", 150.0, 40.0),
        SwitchDevice("SW-01", "Dist-Switch", 60.0, 48),
    ]

    print("=== Eksekusi Polimorfik Diagnostik ===")
    for dev in devices:
        print(dev.diagnostics())
