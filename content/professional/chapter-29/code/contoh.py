"""Chapter 29: Software Architecture & Deployment
Contoh Kode Terpadu: Clean Architecture, Config, DI Service & CLI
"""

from telecom_config import AppConfig
from telecom_repository import InMemoryNodeRepository
from telecom_service import NodeDeploymentService
from telecom_cli import run_cli_command


def main() -> None:
    print("=== DEMO CHAPTER 29: SOFTWARE ARCHITECTURE & DEPLOYMENT ===\n")

    # 1. Configuration Layer
    config = AppConfig.load()
    print("[1] Membaca Twelve-Factor App Configuration:")
    print(f" -> Aplikasi  : {config.app_name}")
    print(f" -> Lingkungan: {config.environment}")
    print(f" -> Port      : {config.service_port}\n")

    # 2. Dependency Injection
    print("[2] Menginisialisasi In-Memory Repository & Service (DI):")
    repo = InMemoryNodeRepository()
    service = NodeDeploymentService(repository=repo)
    print(" -> Repository dan Service terhubung secara longgar (loosely coupled).\n")

    # 3. CLI Presentation Layer
    print("[3] Menjalankan Perintah CLI 'status':")
    status_res = run_cli_command(service, ["status", "--cluster", "sumatera-selatan"])
    print(f" -> Hasil Status: {status_res}\n")

    print("[4] Menjalankan Perintah CLI 'deploy':")
    deploy_res = run_cli_command(
        service,
        ["deploy", "--version", "3.0.0", "--cluster", "sumatera-selatan", "--operator", "Aji Pamungkas"],
    )
    print(f" -> Hasil Deploy: {deploy_res}\n")

    print("Semua layer arsitektur berhasil berkolaborasi dengan pemisahan tanggung jawab yang bersih.")


if __name__ == "__main__":
    main()

