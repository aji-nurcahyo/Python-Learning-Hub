"""Chapter 29: Software Architecture & Deployment
Presentation / CLI Layer: Antarmuka Baris Perintah Terstruktur
"""

import argparse
from typing import Optional

try:
    from telecom_repository import InMemoryNodeRepository
    from telecom_service import NodeDeploymentService
except ImportError:
    from .telecom_repository import InMemoryNodeRepository
    from .telecom_service import NodeDeploymentService


def create_cli_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="telecom-deploy",
        description="CLI Manajemen Deployment & Observabilitas Klaster Telekomunikasi",
    )
    subparsers = parser.add_subparsers(dest="subcommand", required=True)

    # Subcommand: status
    status_parser = subparsers.add_parser("status", help="Menampilkan ringkasan kesehatan klaster")
    status_parser.add_argument("--cluster", default="sumatera-selatan", help="Zona klaster target")

    # Subcommand: deploy
    deploy_parser = subparsers.add_parser("deploy", help="Menerapkan rilis perangkat lunak baru")
    deploy_parser.add_argument("--version", required=True, help="Tag versi (misal 2.0.0)")
    deploy_parser.add_argument("--cluster", default="sumatera-selatan", help="Zona klaster target")
    deploy_parser.add_argument("--operator", default="DevOps Engineer", help="Identitas operator")

    return parser


def run_cli_command(
    service: NodeDeploymentService,
    args_list: list[str],
) -> dict[str, str | int | float]:
    parser = create_cli_parser()
    parsed = parser.parse_args(args_list)

    if parsed.subcommand == "status":
        return service.get_cluster_status(parsed.cluster)
    elif parsed.subcommand == "deploy":
        return service.deploy_release(
            cluster_zone=parsed.cluster,
            version=parsed.version,
            deployed_by=parsed.operator,
        )
    return {"error": "Subcommand tidak valid"}

