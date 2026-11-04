"""Chapter 29: Software Architecture & Deployment
Data Access Layer (Ports & Adapters / Repository Pattern)
"""

from typing import Optional, Protocol

try:
    from telecom_models import NetworkNode, NodeStatus
except ImportError:
    from .telecom_models import NetworkNode, NodeStatus


class NodeRepository(Protocol):
    """Kontrak abstraksi untuk penyimpanan dan pengambilan entitas NetworkNode."""

    def get_by_id(self, node_id: str) -> Optional[NetworkNode]:
        ...

    def list_by_cluster(self, cluster_zone: str) -> list[NetworkNode]:
        ...

    def save(self, node: NetworkNode) -> None:
        ...


class InMemoryNodeRepository:
    """Implementasi in-memory repository untuk pengujian lokal dan simulasi deployment."""

    def __init__(self) -> None:
        self._nodes: dict[str, NetworkNode] = {
            "ND-01": NetworkNode("ND-01", "edge-router-lampung", "10.0.1.1", "sumatera-selatan", NodeStatus.ACTIVE),
            "ND-02": NetworkNode("ND-02", "core-gateway-itera", "10.0.1.2", "sumatera-selatan", NodeStatus.ACTIVE),
            "ND-03": NetworkNode("ND-03", "bts-antena-kalianda", "10.0.2.1", "sumatera-selatan", NodeStatus.MAINTENANCE),
        }

    def get_by_id(self, node_id: str) -> Optional[NetworkNode]:
        return self._nodes.get(node_id)

    def list_by_cluster(self, cluster_zone: str) -> list[NetworkNode]:
        return [n for n in self._nodes.values() if n.cluster_zone == cluster_zone]

    def save(self, node: NetworkNode) -> None:
        self._nodes[node.node_id] = node

