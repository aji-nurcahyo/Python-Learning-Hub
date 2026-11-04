"""Starter Code Tugas Mandiri: Hierarchical Telecom Infrastructure Management
Python Learning Hub - Chapter 20: Object-Oriented Programming II

Nama Mahasiswa : ____________________
NIM            : ____________________
Institusi      : Institut Teknologi Sumatera (ITERA)
"""

class TransceiverNode:
    """Class induk dasar untuk simpul pemancar/penerima telekomunikasi."""

    def __init__(self, node_id: str, site_name: str, power_consumption_w: float):
        self.node_id = node_id
        self.site_name = site_name
        self.power_consumption_w = float(power_consumption_w)
        self.status = "OPERATIONAL"

    def run_diagnostics(self) -> dict:
        """Diagnostik dasar."""
        return {
            "node_id": self.node_id,
            "site": self.site_name,
            "type": "Generic Transceiver",
            "power_w": self.power_consumption_w,
            "status": self.status
        }

    def __str__(self) -> str:
        return f"{self.node_id} ({self.site_name}) - {self.status}"

    def __repr__(self) -> str:
        return f"TransceiverNode('{self.node_id}', '{self.site_name}', {self.power_consumption_w})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TransceiverNode):
            return NotImplemented
        return self.node_id == other.node_id

    def __hash__(self) -> int:
        return hash(self.node_id)


class CellularAntenna(TransceiverNode):
    """Subclass untuk antena pemancar seluler (4G/5G)."""

    def __init__(self, node_id: str, site_name: str, power_consumption_w: float, mimo_config: str, azimuth_deg: float):
        super().__init__(node_id, site_name, power_consumption_w)
        self.mimo_config = mimo_config
        self.azimuth_deg = float(azimuth_deg)

    def run_diagnostics(self) -> dict:
        diag = super().run_diagnostics()
        diag.update({
            "type": "Cellular Antenna",
            "details": f"MIMO: {self.mimo_config} | Azimuth: {self.azimuth_deg:.1f}°"
        })
        return diag


class MicrowaveLink(TransceiverNode):
    """Subclass untuk tautan transmisi gelombang mikro point-to-point."""

    def __init__(self, node_id: str, site_name: str, power_consumption_w: float, frequency_ghz: float, capacity_mbps: float):
        super().__init__(node_id, site_name, power_consumption_w)
        self.frequency_ghz = float(frequency_ghz)
        self.capacity_mbps = float(capacity_mbps)

    def run_diagnostics(self) -> dict:
        diag = super().run_diagnostics()
        diag.update({
            "type": "Microwave Link",
            "details": f"Frekuensi: {self.frequency_ghz:.2f} GHz | Kapasitas: {self.capacity_mbps:.0f} Mbps"
        })
        return diag


class FiberOpticNode(TransceiverNode):
    """Subclass untuk simpul terminasi kabel optik."""

    def __init__(self, node_id: str, site_name: str, power_consumption_w: float, core_count: int, rx_optical_power_dbm: float):
        super().__init__(node_id, site_name, power_consumption_w)
        self.core_count = int(core_count)
        self.rx_optical_power_dbm = float(rx_optical_power_dbm)

    def run_diagnostics(self) -> dict:
        diag = super().run_diagnostics()
        diag.update({
            "type": "Fiber Optic Node",
            "details": f"Cores: {self.core_count} | Rx Power: {self.rx_optical_power_dbm:.2f} dBm"
        })
        return diag


class TelecomInfrastructureManager:
    """Manajer sistem yang mengelola berbagai simpul transceiver secara polimorfik."""

    def __init__(self, region_name: str):
        self.region_name = region_name
        self._nodes: dict[str, TransceiverNode] = {}

    def register_node(self, node: TransceiverNode) -> None:
        if not isinstance(node, TransceiverNode):
            raise TypeError("Objek harus merupakan instance dari TransceiverNode!")
        if node.node_id in self._nodes:
            raise KeyError(f"Simpul ID '{node.node_id}' sudah terdaftar!")
        self._nodes[node.node_id] = node

    def execute_system_diagnostics(self) -> None:
        print(f"==================================================")
        print(f"  DIAGNOSTIK INFRASTRUKTUR TELEKOMUNIKASI: {self.region_name}  ")
        print(f"==================================================")
        for node in self._nodes.values():
            d = node.run_diagnostics()
            print(f"[{d['type']:<18}] Node {d['node_id']:<10} | {d['details']} ({d['status']})")
        print(f"Total Konsumsi Daya: {self.total_power_load():.1f} Watt")
        print(f"==================================================")

    def total_power_load(self) -> float:
        return sum(n.power_consumption_w for n in self._nodes.values())


if __name__ == "__main__":
    mgr = TelecomInfrastructureManager("Wilayah Lampung Selatan")

    ant1 = CellularAntenna("ANT-01", "Tower ITERA 1", 240.0, "64x64 Massive MIMO", 120.0)
    mw1 = MicrowaveLink("MW-01", "Tower ITERA 1", 65.0, 15.2, 1200.0)
    fib1 = FiberOpticNode("FIB-01", "ODC ITERA Gd. C", 30.0, 96, -14.2)

    mgr.register_node(ant1)
    mgr.register_node(mw1)
    mgr.register_node(fib1)

    mgr.execute_system_diagnostics()

    # Uji kesetaraan dan deduplikasi set
    ant_clone = CellularAntenna("ANT-01", "Tower Berbeda", 300.0, "4x4 MIMO", 0.0)
    print("\nUji Kesetaraan (ant1 == ant_clone):", ant1 == ant_clone)
    nodes_set = {ant1, ant_clone}
    print(f"Jumlah elemen unik dalam set: {len(nodes_set)}")

