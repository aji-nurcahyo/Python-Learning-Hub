"""Chapter 29: Software Architecture & Deployment
Domain Layer: Model Entitas Jaringan & Rilis Perangkat Lunak
"""

from dataclasses import dataclass
from enum import Enum


class NodeStatus(str, Enum):
    ACTIVE = "ACTIVE"
    STANDBY = "STANDBY"
    MAINTENANCE = "MAINTENANCE"
    OFFLINE = "OFFLINE"


@dataclass(frozen=True)
class NetworkNode:
    """Entitas bisnis murni yang merepresentasikan simpul infrastruktur telekomunikasi."""
    node_id: str
    hostname: str
    ip_address: str
    cluster_zone: str
    status: NodeStatus = NodeStatus.ACTIVE

    @property
    def is_operational(self) -> bool:
        return self.status in (NodeStatus.ACTIVE, NodeStatus.STANDBY)


@dataclass(frozen=True)
class DeploymentRelease:
    """Informasi versi rilis perangkat lunak dan metadata deployment."""
    version: str
    environment: str  # 'development' | 'staging' | 'production'
    commit_hash: str
    deployed_by: str

