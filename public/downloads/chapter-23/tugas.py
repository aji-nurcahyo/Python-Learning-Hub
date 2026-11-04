"""Template Tugas Mahasiswa: Chapter 23 - Advanced OOP & Design Patterns
Topik: Extensible Network Controller System
Platform: Python Learning Hub
Pengembang: Aji Pamungkas Tri Nurcahyo
Institusi: Institut Teknologi Sumatera (ITERA)
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Type


# 1. Konfigurasi Node (Gunakan Dataclass Frozen)
@dataclass(frozen=True)
class NodeConfig:
    node_id: str
    hostname: str
    capacity_gbps: float


# 2. Antarmuka Abstrak Node Jaringan
class AbstractNode(ABC):
    def __init__(self, config: NodeConfig, mgmt_ip: str) -> None:
        self.config = config
        self._mgmt_ip = ""
        self.mgmt_ip = mgmt_ip  # Memanggil property setter

    @property
    def mgmt_ip(self) -> str:
        return self._mgmt_ip

    @mgmt_ip.setter
    def mgmt_ip(self, ip: str) -> None:
        parts = ip.split(".")
        if len(parts) != 4 or not all(p.isdigit() and 0 <= int(p) <= 255 for p in parts):
            raise ValueError(f"Format alamat IP tidak valid: '{ip}'")
        self._mgmt_ip = ip

    @abstractmethod
    def get_operational_state(self) -> dict[str, Any]:
        """Mengembalikan metrik operasional perangkat."""
        pass

    @abstractmethod
    def process_traffic(self, packets: int) -> int:
        """Memproses paket data dan mengembalikan jumlah paket yang sukses diteruskan."""
        pass


# 3. Implementasi Node Konkret
class EdgeRouter(AbstractNode):
    def get_operational_state(self) -> dict[str, Any]:
        return {"node_id": self.config.node_id, "type": "EdgeRouter", "ip": self.mgmt_ip, "status": "UP"}

    def process_traffic(self, packets: int) -> int:
        # Edge router memproses paket dengan efisiensi 98%
        return int(packets * 0.98)


class AggregationSwitch(AbstractNode):
    def get_operational_state(self) -> dict[str, Any]:
        return {"node_id": self.config.node_id, "type": "AggregationSwitch", "ip": self.mgmt_ip, "status": "UP"}

    def process_traffic(self, packets: int) -> int:
        # Switch memproses paket tanpa kehilangan jika dalam batas kapasitas
        return packets


# 4. Factory Pattern untuk Pembuatan Node
class NodeFactory:
    _registry: dict[str, Type[AbstractNode]] = {
        "router": EdgeRouter,
        "switch": AggregationSwitch,
    }

    @classmethod
    def create_node(cls, kind: str, node_id: str, hostname: str, capacity: float, ip: str) -> AbstractNode:
        target_cls = cls._registry.get(kind.lower())
        if not target_cls:
            raise ValueError(f"Jenis node '{kind}' tidak dikenal.")
        config = NodeConfig(node_id=node_id, hostname=hostname, capacity_gbps=capacity)
        return target_cls(config=config, mgmt_ip=ip)


# 5. Strategy Pattern untuk Perutean Lalu Lintas
class TrafficRoutingStrategy(ABC):
    @abstractmethod
    def route_packets(self, node: AbstractNode, total_packets: int) -> str:
        pass


class PriorityRoutingStrategy(TrafficRoutingStrategy):
    def route_packets(self, node: AbstractNode, total_packets: int) -> str:
        processed = node.process_traffic(total_packets)
        return f"[PRIORITY ROUTE] {node.config.node_id} meneruskan {processed}/{total_packets} paket berprioritas tinggi."


class RoundRobinRoutingStrategy(TrafficRoutingStrategy):
    def route_packets(self, node: AbstractNode, total_packets: int) -> str:
        processed = node.process_traffic(total_packets)
        return f"[ROUND ROBIN] {node.config.node_id} meneruskan {processed}/{total_packets} paket secara bergiliran."


# 6. Komposisi: Network Controller
class NetworkController:
    def __init__(self, name: str, routing_strategy: TrafficRoutingStrategy) -> None:
        self.name = name
        self.routing_strategy = routing_strategy
        self._nodes: dict[str, AbstractNode] = {}

    def attach_node(self, node: AbstractNode) -> None:
        self._nodes[node.config.node_id] = node

    def execute_routing(self, packets_per_node: int) -> list[str]:
        results: list[str] = []
        for node in self._nodes.values():
            report = self.routing_strategy.route_packets(node, packets_per_node)
            results.append(report)
        return results


def main() -> None:
    print("=== PENGUJIAN EXTENSIBLE NETWORK CONTROLLER ===")
    r1 = NodeFactory.create_node("router", "RTR-01", "gw-edge.telco.net", 10.0, "192.168.1.1")
    s1 = NodeFactory.create_node("switch", "SW-01", "dist-sw.telco.net", 40.0, "192.168.1.2")

    controller = NetworkController("Pusat Kendali Regional", PriorityRoutingStrategy())
    controller.attach_node(r1)
    controller.attach_node(s1)

    print("\n--- Eksekusi Perutean Prioritas ---")
    for log in controller.execute_routing(1000):
        print(f" * {log}")

    # Ganti strategi runtime
    controller.routing_strategy = RoundRobinRoutingStrategy()
    print("\n--- Eksekusi Perutean Round Robin ---")
    for log in controller.execute_routing(500):
        print(f" * {log}")


if __name__ == "__main__":
    main()
