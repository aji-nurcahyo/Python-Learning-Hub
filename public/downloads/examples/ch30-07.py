"""Chapter 30 Example 07: Capstone Unified CLI Controller & Dispatcher
Python Learning Hub - Professional Capstone Project
"""


class UnifiedPlatformCli:
    """Pengendali antarmuka baris perintah terpadu untuk platform telemetri."""

    def dispatch(self, command: str) -> str:
        if command == "ingest":
            return "[CLI] Memulai proses penyerapan data telemetri..."
        elif command == "analyze":
            return "[CLI] Menjalankan kalkulasi agregasi dan metrik SLA..."
        elif command == "report":
            return "[CLI] Menyintesis berkas laporan performa Markdown..."
        return f"[CLI] Perintah '{command}' tidak valid. Gunakan: ingest | analyze | report"


def main() -> None:
    print("Mendemonstrasikan Dispatcher CLI Platform (Capstone Layer 7):\n")
    cli = UnifiedPlatformCli()

    print(" ->", cli.dispatch("ingest"))
    print(" ->", cli.dispatch("analyze"))
    print(" ->", cli.dispatch("report"))


if __name__ == "__main__":
    main()
