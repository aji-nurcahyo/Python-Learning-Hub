"""Chapter 29: Software Architecture & Deployment
Main Application Entry Point: Production-Ready Python Application
"""

import sys
from telecom_repository import InMemoryNodeRepository
from telecom_service import NodeDeploymentService
from telecom_cli import run_cli_command


def run_app() -> None:
    repo = InMemoryNodeRepository()
    service = NodeDeploymentService(repository=repo)
    args = sys.argv[1:] if len(sys.argv) > 1 else ["status", "--cluster", "sumatera-selatan"]

    print("Memulai Production-Ready Python Application...")
    output = run_cli_command(service, args)
    print("Keluaran Eksekusi:", output)


if __name__ == "__main__":
    run_app()

