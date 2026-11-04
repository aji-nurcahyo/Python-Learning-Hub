"""Unit Test Suite untuk Chapter 29: Software Architecture & Deployment
Memvalidasi Domain Model, Config Loading, Repository, Dependency Injection, dan CLI.
"""

import os
import sys
import unittest

# Menambahkan direktori code ke sys.path agar modul dapat diimpor
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CODE_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "code")
if CODE_DIR not in sys.path:
    sys.path.insert(0, CODE_DIR)

from telecom_config import AppConfig
from telecom_models import NetworkNode, NodeStatus
from telecom_repository import InMemoryNodeRepository
from telecom_service import NodeDeploymentService
from telecom_cli import run_cli_command


class TestSoftwareArchitecture(unittest.TestCase):
    """Test suite untuk memvalidasi pemisahan layer arsitektur dan perilaku sistem."""

    def setUp(self) -> None:
        self.repo = InMemoryNodeRepository()
        self.service = NodeDeploymentService(repository=self.repo)

    def test_domain_node_model_operational_state(self) -> None:
        """Memvalidasi bahwa domain model NetworkNode mengevaluasi status operasional dengan benar."""
        active_node = NetworkNode("N-1", "host-1", "10.0.0.1", "zone-a", NodeStatus.ACTIVE)
        maint_node = NetworkNode("N-2", "host-2", "10.0.0.2", "zone-a", NodeStatus.MAINTENANCE)

        self.assertTrue(active_node.is_operational)
        self.assertFalse(maint_node.is_operational)

    def test_config_loading_from_environment(self) -> None:
        """Memvalidasi konfigurasi memuat environment variables secara akurat."""
        os.environ["DEPLOY_ENV"] = "staging"
        os.environ["SERVICE_PORT"] = "9090"
        config = AppConfig.load()

        self.assertEqual(config.environment, "staging")
        self.assertEqual(config.service_port, 9090)

    def test_repository_crud_operations(self) -> None:
        """Memvalidasi operasi pengambilan dan penyimpanan pada implementasi repository."""
        new_node = NetworkNode("N-99", "new-gateway", "10.0.99.1", "sumatera-selatan", NodeStatus.STANDBY)
        self.repo.save(new_node)

        retrieved = self.repo.get_by_id("N-99")
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved.hostname, "new-gateway")

    def test_service_deployment_logic_with_di(self) -> None:
        """Memvalidasi deployment service mengupdate simpul operasional dan melewati maintenance node."""
        res = self.service.deploy_release(
            cluster_zone="sumatera-selatan",
            version="2.5.0",
            deployed_by="Aji Pamungkas",
        )
        self.assertEqual(res["status"], "SUCCESS")
        self.assertEqual(res["version"], "2.5.0")
        self.assertEqual(res["updated_nodes"], 2)
        self.assertEqual(res["skipped_maintenance"], 1)
        self.assertEqual(len(self.service.deployment_history), 1)

    def test_service_invalid_cluster_raises_error(self) -> None:
        """Memvalidasi bahwa klaster yang tidak terdaftar melempar ValueError."""
        with self.assertRaises(ValueError):
            self.service.deploy_release(cluster_zone="klaster-fiktif", version="1.0.0", deployed_by="tester")

    def test_cli_dispatch_and_execution(self) -> None:
        """Memvalidasi presentation layer CLI menerjemahkan argumen ke method service dengan benar."""
        output = run_cli_command(self.service, ["status", "--cluster", "sumatera-selatan"])
        self.assertEqual(output["cluster"], "sumatera-selatan")
        self.assertEqual(output["total_nodes"], 3)
        self.assertIn("health_score", output)


if __name__ == "__main__":
    unittest.main()

