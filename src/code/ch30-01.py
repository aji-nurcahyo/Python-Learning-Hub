"""Chapter 30 Example 01: Capstone Ingestion Pipeline - Structured Telemetry
Python Learning Hub - Professional Capstone Project
"""

import csv
import io
from typing import Any


CSV_DATA_STREAM = """device_id,timestamp,rssi_dbm,packet_loss_pct,status
BTS-LAMPUNG-01,1700000000,-68.5,0.02,HEALTHY
BTS-LAMPUNG-02,1700000010,-88.2,1.45,DEGRADED
BTS-LAMPUNG-03,1700000020,-112.0,12.80,CRITICAL
"""


def ingest_telemetry_csv(raw_csv_text: str) -> list[dict[str, Any]]:
    """Membaca dan mem-parsing aliran data CSV mentah menjadi record terstruktur."""
    stream = io.StringIO(raw_csv_text.strip())
    reader = csv.DictReader(stream)
    records = []
    for row in reader:
        records.append({
            "device_id": row["device_id"],
            "timestamp": int(row["timestamp"]),
            "rssi_dbm": float(row["rssi_dbm"]),
            "packet_loss_pct": float(row["packet_loss_pct"]),
            "status": row["status"],
        })
    return records


def main() -> None:
    print("Mengeksekusi Pipeline Ingesti Data Telemetri Mentah (Capstone Layer 1):\n")
    records = ingest_telemetry_csv(CSV_DATA_STREAM)
    for rec in records:
        print(f" -> [{rec['device_id']}] RSSI: {rec['rssi_dbm']} dBm | Loss: {rec['packet_loss_pct']}% | Status: {rec['status']}")
    print(f"\nTotal entri berhasil di-ingest: {len(records)} records.")


if __name__ == "__main__":
    main()

