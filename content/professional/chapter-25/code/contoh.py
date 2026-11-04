"""Chapter 25: Mini Project Demonstrator
Typed Python Library
Python Learning Hub - Professional Python Engineering
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from domain_types import TelemetryRecord
from protocols import RadioSensor
from containers import EntityRepository
from telemetry_service import TelemetryService


def run_demonstration() -> None:
    print("=" * 65)
    print("DEMO: TYPED PYTHON LIBRARY (CHAPTER 25)")
    print("=" * 65)

    # 1. Repositori Generik Tipe Aman
    repo: EntityRepository[TelemetryRecord] = EntityRepository()
    service = TelemetryService(repo)

    # 2. Ingest TypedDict Records
    rec1: TelemetryRecord = {
        "node_id": "NODE-SBY-01",
        "frequency_mhz": 2100.0,
        "rsrp_dbm": -79.5,
        "snr_db": 19.2,
        "is_active": True,
        "description": "Sektor Utama Utara",
    }
    rec2: TelemetryRecord = {
        "node_id": "NODE-SBY-02",
        "frequency_mhz": 1800.0,
        "rsrp_dbm": -108.0,
        "snr_db": 5.4,
        "is_active": False,
    }

    service.ingest_record(rec1)
    service.ingest_record(rec2)
    print(f"Total rekaman berhasil di-ingest: {repo.count()}")

    # 3. Filter dengan Callable Type Annotation
    active_nodes = service.filter_records(lambda r: r["is_active"] and r["rsrp_dbm"] >= -90.0)
    print(f"\nSimpul Aktif & Kualitas Prima (RSRP >= -90 dBm):")
    for r in active_nodes:
        print(f" * {r['node_id']} | Freq: {r['frequency_mhz']} MHz | RSRP: {r['rsrp_dbm']} dBm")

    # 4. Transmisi Objek Berbasis Protocol
    sensor = RadioSensor("SENS-CHASSIS-04", temperature_c=48.5)
    print(f"\nStatus Sensor: Suhu Sehat = {sensor.check_health()}")
    print(f"Hasil Transmisi Protocol: {service.transmit(sensor)}")


if __name__ == "__main__":
    run_demonstration()
