"""Contoh 20.5: Komposisi ("has-a") vs Pewarisan ("is-a")
Python Learning Hub - Level 2: Intermediate Python
"""

# Prinsip desain OOP: Utamakan Komposisi dibanding Pewarisan jika relasinya adalah "memiliki" bukan "adalah"

class PowerSupply:
    def __init__(self, watt: float, efisiensi_pct: float):
        self.watt = watt
        self.efisiensi_pct = efisiensi_pct

    def status_daya(self) -> str:
        return f"{self.watt}W ({self.efisiensi_pct}% efisiensi)"

class NetworkPort:
    def __init__(self, port_id: str, speed_mbps: int):
        self.port_id = port_id
        self.speed_mbps = speed_mbps
        self.is_up: bool = False

    def aktifkan(self) -> None:
        self.is_up = True

class ModularRouter:
    """Router MEMILIKI (has-a) PowerSupply dan MEMILIKI beberapa NetworkPort."""

    def __init__(self, hostname: str, psu_watt: float):
        self.hostname = hostname
        self.psu = PowerSupply(psu_watt, 92.5)  # Komposisi
        self.ports: list[NetworkPort] = []      # Komposisi koleksi port

    def tambah_port(self, port_id: str, speed_mbps: int) -> None:
        self.ports.append(NetworkPort(port_id, speed_mbps))

    def ringkasan_sistem(self) -> None:
        print(f"Router Hostname: {self.hostname}")
        print(f"Power Supply   : {self.psu.status_daya()}")
        print(f"Total Port     : {len(self.ports)}")
        for p in self.ports:
            status = "UP" if p.is_up else "DOWN"
            print(f"  - Port {p.port_id}: {p.speed_mbps} Mbps [{status}]")

router = ModularRouter("Edge-Router-01", 250.0)
router.tambah_port("eth0", 1000)
router.tambah_port("eth1", 10000)
router.tambah_port("eth2", 1000)

router.ports[0].aktifkan()
router.ports[1].aktifkan()

router.ringkasan_sistem()
