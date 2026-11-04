"""Chapter 30: Professional Capstone Project
Main Application Entry Point: Python Data Monitoring & Automation Platform
"""

from platform_cli import run_platform_cli
from platform_engine import TelemetryProcessingEngine
from platform_storage import LocalTelemetryStorage

DEFAULT_STREAM = """device_id,timestamp,rssi_dbm,packet_loss_pct,cpu_load_pct,temperature_c,status
BTS-01,1700000000,-70.0,0.1,50.0,55.0,HEALTHY
BTS-02,1700000010,-85.0,1.5,65.0,62.0,HEALTHY
BTS-03,1700000020,-110.0,9.0,91.0,81.0,CRITICAL
"""


def run_platform() -> None:
    storage = LocalTelemetryStorage()
    engine = TelemetryProcessingEngine(storage=storage)
    res = run_platform_cli(engine, ["--run", "--report", "--cluster", "Lampung-Metropolitan"], DEFAULT_STREAM)
    print("Eksekusi Capstone Selesai:")
    print(f" -> Total Data Terkelola : {res.get('total_nodes')} entri")
    print(f" -> Rasio Kesehatan      : {res.get('health_rate')}%")
    print(f" -> Anomali Terdeteksi   : {res.get('anomalies_count')} unit")


if __name__ == "__main__":
    run_platform()

