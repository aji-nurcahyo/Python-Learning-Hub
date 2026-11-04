"""Chapter 29 Example 07: Command-Line Entry Points with Subcommands
Python Learning Hub - Professional Python Engineering
"""

import argparse


def build_cli_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="telecom-ops",
        description="Perangkat Baris Perintah Pemeliharaan Jaringan & Deployment",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subcommand: status
    parser_status = subparsers.add_parser("status", help="Menampilkan status simpul")
    parser_status.add_argument("--cluster", default="lampung-core", help="Nama klaster jaringan")

    # Subcommand: deploy
    parser_deploy = subparsers.add_parser("deploy", help="Menjalankan deployment versi baru")
    parser_deploy.add_argument("--version", required=True, help="Tag versi rilis (misal 1.2.0)")
    parser_deploy.add_argument("--dry-run", action="store_true", help="Simulasi tanpa menerapkan mutasi")

    return parser


def run_cli(args_list: list[str]) -> str:
    parser = build_cli_parser()
    parsed = parser.parse_args(args_list)

    if parsed.command == "status":
        return f"[STATUS] Klaster {parsed.cluster} beroperasi normal (Uptime: 99.98%)."
    elif parsed.command == "deploy":
        mode = "SIMULASI (DRY-RUN)" if parsed.dry_run else "PRODUKSI LANGSUNG"
        return f"[DEPLOY] Versi {parsed.version} dieksekusi dalam mode {mode}."
    return "Perintah tidak dikenali."


def main() -> None:
    print("Mendemonstrasikan CLI Entry Point Tingkat Produksi dengan argparse:\n")

    res_1 = run_cli(["status", "--cluster", "sumatera-selatan"])
    print("1. Pemanggilan Perintah Status:")
    print("   ", res_1)

    res_2 = run_cli(["deploy", "--version", "2.1.0", "--dry-run"])
    print("\n2. Pemanggilan Perintah Deploy:")
    print("   ", res_2)


if __name__ == "__main__":
    main()
