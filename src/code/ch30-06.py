"""Chapter 30 Example 06: Capstone Automated Analytics & Report Generator
Python Learning Hub - Professional Capstone Project
"""


class MarkdownReportGenerator:
    """Generator laporan performa otomatis berformat Markdown untuk stakeholder operasional."""

    @staticmethod
    def generate_summary_report(
        cluster_name: str,
        total_nodes: int,
        healthy_nodes: int,
        avg_packet_loss: float,
    ) -> str:
        health_pct = round((healthy_nodes / total_nodes) * 100.0, 1) if total_nodes > 0 else 0.0
        lines = [
            f"# Laporan Telemetri Klaster: {cluster_name}",
            "",
            "## Ringkasan Performa Sistem",
            f"- Total Simpul Terpantau : {total_nodes}",
            f"- Simpul Berstatus Sehat : {healthy_nodes} ({health_pct}%)",
            f"- Rata-rata Packet Loss : {avg_packet_loss:.2f}%",
            "",
            f"**Kesimpulan SLA:** {'MEMENUHI STANDAR' if health_pct >= 90.0 else 'PERLU PERBAIKAN'}",
        ]
        return "\n".join(lines)


def main() -> None:
    print("Menghasilkan Ringkasan Laporan Otomatis (Capstone Layer 6):\n")
    report = MarkdownReportGenerator.generate_summary_report(
        cluster_name="Lampung Metropolitan Core",
        total_nodes=40,
        healthy_nodes=38,
        avg_packet_loss=0.42,
    )
    print(report)


if __name__ == "__main__":
    main()

