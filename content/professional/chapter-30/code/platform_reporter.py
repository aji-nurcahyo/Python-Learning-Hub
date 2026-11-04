"""Chapter 30: Professional Capstone Project
Reporter Layer: Generator Laporan Analitik Otomatis
"""

try:
    from platform_models import ClusterMetricSummary
except ImportError:
    from .platform_models import ClusterMetricSummary


class TelemetryReportGenerator:
    """Generator laporan performa operasional dalam format Markdown dan ringkasan eksekutif."""

    @staticmethod
    def generate_markdown(summary: ClusterMetricSummary, anomaly_count: int) -> str:
        sla_status = "MEMENUHI STANDAR (SLA COMPLIANT)" if summary.health_rate >= 80.0 else "KRITIS (SLA BREACH)"
        return f"""# Laporan Eksekutif: Data Monitoring & Automation Platform
**Klaster:** {summary.cluster_name} | **Status SLA:** {sla_status}

## Metrik Kinerja Klaster
- **Total Simpul Terpantau :** {summary.total_records} unit
- **Simpul Berstatus Sehat :** {summary.healthy_count} unit ({summary.health_rate}%)
- **Rata-rata Packet Loss :** {summary.avg_packet_loss}%
- **Rata-rata Beban CPU   :** {summary.avg_cpu_load}%
- **Jumlah Anomali Aktif  :** {anomaly_count} insiden
"""

