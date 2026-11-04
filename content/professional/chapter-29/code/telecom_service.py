"""Chapter 29: Software Architecture & Deployment
Application / Service Layer: Logika Orkestrasi dengan Dependency Injection
"""

from typing import Any

try:
    from telecom_models import DeploymentRelease, NetworkNode, NodeStatus
    from telecom_repository import NodeRepository
except ImportError:
    from .telecom_models import DeploymentRelease, NetworkNode, NodeStatus
    from .telecom_repository import NodeRepository


class NodeDeploymentService:
    """Service bisnis yang bergantung pada abstraksi NodeRepository via Dependency Injection."""

    def __init__(self, repository: NodeRepository) -> None:
        self.repository = repository
        self.deployment_history: list[DeploymentRelease] = []

    def deploy_release(
        self,
        cluster_zone: str,
        version: str,
        deployed_by: str,
        commit_hash: str = "a1b2c3d",
    ) -> dict[str, Any]:
        """Melakukan simulasi deployment rilis baru ke seluruh simpul operasional pada klaster."""
        nodes = self.repository.list_by_cluster(cluster_zone)
        if not nodes:
            raise ValueError(f"Klaster '{cluster_zone}' tidak memiliki simpul terdaftar.")

        operational_nodes = [n for n in nodes if n.is_operational]
        release = DeploymentRelease(
            version=version,
            environment="production",
            commit_hash=commit_hash,
            deployed_by=deployed_by,
        )
        self.deployment_history.append(release)

        return {
            "status": "SUCCESS",
            "version": version,
            "cluster": cluster_zone,
            "total_nodes": len(nodes),
            "updated_nodes": len(operational_nodes),
            "skipped_maintenance": len(nodes) - len(operational_nodes),
        }

    def get_cluster_status(self, cluster_zone: str) -> dict[str, Any]:
        nodes = self.repository.list_by_cluster(cluster_zone)
        active_count = sum(1 for n in nodes if n.status == NodeStatus.ACTIVE)
        return {
            "cluster": cluster_zone,
            "total_nodes": len(nodes),
            "active_nodes": active_count,
            "health_score": round((active_count / len(nodes)) * 100.0, 1) if nodes else 0.0,
        }

