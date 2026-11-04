"""Tugas Mini Project Chapter 29: Production-Ready Python Application
Platform: Python Learning Hub
Institusi: Institut Teknologi Sumatera (ITERA)

Petunjuk:
Lengkapi implementasi arsitektur berlapis (Clean Architecture) di bawah ini.
Pastikan kode memenuhi prinsip Separation of Concerns, Dependency Injection, dan Twelve-Factor App.
"""

from dataclasses import dataclass
from enum import Enum
import os
from typing import Any, Optional, Protocol


# ==============================================================================
# 1. DOMAIN LAYER (Entitas Bisnis Murni)
# ==============================================================================

class NodeStatus(str, Enum):
    ACTIVE = "ACTIVE"
    STANDBY = "STANDBY"
    MAINTENANCE = "MAINTENANCE"


@dataclass(frozen=True)
class NetworkNode:
    node_id: str
    hostname: str
    ip_address: str
    cluster: str
    status: NodeStatus = NodeStatus.ACTIVE

    @property
    def is_operational(self) -> bool:
        return self.status != NodeStatus.MAINTENANCE


# ==============================================================================
# 2. CONFIGURATION LAYER (Twelve-Factor App)
# ==============================================================================

@dataclass(frozen=True)
class AppConfig:
    app_name: str
    environment: str
    service_port: int
    log_level: str

    @classmethod
    def from_env(cls) -> "AppConfig":
        env = os.environ.get("DEPLOY_ENV", "production").lower()
        port_raw = os.environ.get("SERVICE_PORT", "8000")
        try:
            port = int(port_raw)
        except ValueError:
            port = 8000
        log_lvl = os.environ.get("LOG_LEVEL", "INFO").upper()

        return cls(
            app_name="TelecomProductionApp",
            environment=env,
            service_port=port,
            log_level=log_lvl,
        )


# ==============================================================================
# 3. REPOSITORY / PORTS & ADAPTERS LAYER
# ==============================================================================

class NodeRepository(Protocol):
    def get_by_id(self, node_id: str) -> Optional[NetworkNode]: ...
    def list_by_cluster(self, cluster: str) -> list[NetworkNode]: ...
    def save(self, node: NetworkNode) -> None: ...


class InMemoryNodeRepository:
    def __init__(self) -> None:
        self._nodes: dict[str, NetworkNode] = {
            "ND-01": NetworkNode("ND-01", "edge-router-01", "10.0.1.1", "lampung-core", NodeStatus.ACTIVE),
            "ND-02": NetworkNode("ND-02", "gateway-core-02", "10.0.1.2", "lampung-core", NodeStatus.ACTIVE),
            "ND-03": NetworkNode("ND-03", "bts-antena-03", "10.0.2.1", "lampung-core", NodeStatus.MAINTENANCE),
        }

    def get_by_id(self, node_id: str) -> Optional[NetworkNode]:
        return self._nodes.get(node_id)

    def list_by_cluster(self, cluster: str) -> list[NetworkNode]:
        return [n for n in self._nodes.values() if n.cluster == cluster]

    def save(self, node: NetworkNode) -> None:
        self._nodes[node.node_id] = node


# ==============================================================================
# 4. APPLICATION / SERVICE LAYER (Dependency Injection)
# ==============================================================================

class DeploymentService:
    def __init__(self, repository: NodeRepository) -> None:
        self.repository = repository
        self.history: list[dict[str, Any]] = []

    def deploy(self, cluster: str, version: str, operator: str) -> dict[str, Any]:
        nodes = self.repository.list_by_cluster(cluster)
        if not nodes:
            raise ValueError(f"Klaster '{cluster}' tidak ditemukan.")

        operational = [n for n in nodes if n.is_operational]
        record = {
            "version": version,
            "cluster": cluster,
            "operator": operator,
            "updated": len(operational),
            "skipped": len(nodes) - len(operational),
        }
        self.history.append(record)
        return {"status": "SUCCESS", "details": record}

    def get_health(self, cluster: str) -> dict[str, Any]:
        nodes = self.repository.list_by_cluster(cluster)
        active = sum(1 for n in nodes if n.status == NodeStatus.ACTIVE)
        total = len(nodes)
        score = round((active / total) * 100.0, 1) if total > 0 else 0.0
        return {"cluster": cluster, "total": total, "active": active, "health_pct": score}


# ==============================================================================
# 5. CLI DISPATCHER
# ==============================================================================

def execute_cli(service: DeploymentService, args: list[str]) -> dict[str, Any]:
    if not args:
        return {"error": "Argumen tidak boleh kosong."}

    cmd = args[0]
    if cmd == "status":
        cluster = args[1] if len(args) > 1 else "lampung-core"
        return service.get_health(cluster)
    elif cmd == "deploy":
        version = args[1] if len(args) > 1 else "1.0.0"
        cluster = args[2] if len(args) > 2 else "lampung-core"
        return service.deploy(cluster=cluster, version=version, operator="DevOps")
    return {"error": f"Perintah '{cmd}' tidak dikenal."}


def main() -> None:
    print("=== PENGUJIAN MANDIRI: PRODUCTION-READY PYTHON APPLICATION ===")

    # 1. Verifikasi Konfigurasi
    config = AppConfig.from_env()
    print(f"\n[1] Konfigurasi: App={config.app_name} | Env={config.environment} | Port={config.service_port}")
    assert config.app_name == "TelecomProductionApp", "Nama aplikasi harus cocok"

    # 2. Verifikasi Repository & Dependency Injection
    repo = InMemoryNodeRepository()
    service = DeploymentService(repository=repo)
    health = service.get_health("lampung-core")
    print(f"\n[2] Status Klaster Awal: Total={health['total']} | Sehat={health['active']} ({health['health_pct']}%)")
    assert health["total"] == 3
    assert health["active"] == 2
    assert health["health_pct"] == 66.7

    # 3. Verifikasi Deployment Service
    deploy_res = service.deploy(cluster="lampung-core", version="2.0.0", operator="Aji Pamungkas")
    print(f"\n[3] Hasil Deploy: {deploy_res['details']}")
    assert deploy_res["status"] == "SUCCESS"
    assert deploy_res["details"]["updated"] == 2
    assert deploy_res["details"]["skipped"] == 1

    # 4. Verifikasi CLI Dispatcher
    cli_out = execute_cli(service, ["status", "lampung-core"])
    print(f"\n[4] Pemanggilan via CLI: {cli_out}")
    assert cli_out["cluster"] == "lampung-core"

    print("\n[OK] SELURUH ARSITEKTUR BERLAPIS & DEPENDENCY INJECTION LULUS 100%!")


if __name__ == "__main__":
    main()

