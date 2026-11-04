"""Chapter 30: Professional Capstone Project
Contoh Terpadu: Python Data Monitoring & Automation Platform
"""

from platform_config import PlatformConfig
from platform_engine import TelemetryProcessingEngine
from platform_reporter import TelemetryReportGenerator
from platform_sources import LocalCsvTelemetrySource, MockApiTelemetrySource
from platform_storage import LocalTelemetryStorage


SAMPLE_CSV = """device_id,timestamp,rssi_dbm,packet_loss_pct,cpu_load_pct,temperature_c,status
BTS-SUMSEL-01,1700000000,-68.0,0.05,45.2,52.1,HEALTHY
BTS-SUMSEL-02,1700000010,-82.4,1.10,62.0,61.4,HEALTHY
BTS-SUMSEL-03,1700000020,-104.5,8.90,92.5,82.0,CRITICAL
"""


def main() -> None:
    print("=== CAPSTONE: PYTHON DATA MONITORING & AUTOMATION PLATFORM ===\n")

    # 1. Config Layer
    config = PlatformConfig.load()
    print(f"[1] Konfigurasi Sistem: App={config.app_name} | Env={config.environment}")

    # 2. Ingestion & Storage Layer
    storage = LocalTelemetryStorage()
    engine = TelemetryProcessingEngine(storage=storage)

    csv_source = LocalCsvTelemetrySource(SAMPLE_CSV)
    api_source = MockApiTelemetrySource()
    total = engine.ingest_from_sources([csv_source, api_source])
    print(f"\n[2] Ingesti Data: Berhasil mengumpulkan {total} entri telemetri dari file lokal & API.")

    # 3. Processing & Anomaly Detection Layer
    summary = engine.analyze_cluster("Sumatera-Core")
    anomalies = engine.detect_anomalies(
        loss_threshold=config.alert_loss_threshold,
        temp_threshold=config.alert_temp_threshold,
    )
    print(f"\n[3] Analisis Klaster {summary.cluster_name}:")
    print(f" -> Total Simpul : {summary.total_records}")
    print(f" -> Simpul Sehat : {summary.healthy_count} ({summary.health_rate}%)")
    print(f" -> Rerata Loss  : {summary.avg_packet_loss}%")
    print(f" -> Anomali SLA  : {len(anomalies)} insiden terdeteksi")

    # 4. Reporter Layer
    print("\n[4] Laporan Eksekutif:")
    md = TelemetryReportGenerator.generate_markdown(summary, len(anomalies))
    print(md)

    print("Platform berhasil menjalankan seluruh siklus hidup observabilitas dan otomasi.")


if __name__ == "__main__":
    main()

