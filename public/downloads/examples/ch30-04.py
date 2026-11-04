"""Chapter 30 Example 04: Capstone Concurrent Stream Processing Pipeline
Python Learning Hub - Professional Capstone Project
"""

from concurrent.futures import ThreadPoolExecutor
import time
from typing import Any


def process_telemetry_batch(batch_id: int) -> dict[str, Any]:
    """Memproses satu partisi batch telemetri secara terisolasi."""
    time.sleep(0.01)  # Simulasi kalkulasi agregasi
    return {
        "batch_id": batch_id,
        "records_processed": 500,
        "status": "COMPLETED",
    }


def main() -> None:
    print("Memproses Stream Telemetri Skala Tinggi via Thread Pool (Capstone Layer 4):\n")
    batch_ids = [101, 102, 103, 104]

    with ThreadPoolExecutor(max_workers=2) as executor:
        results = list(executor.map(process_telemetry_batch, batch_ids))

    total_records = sum(r["records_processed"] for r in results)
    for r in results:
        print(f" -> Batch #{r['batch_id']}: {r['records_processed']} entri terproses | Status: {r['status']}")

    print(f"\nAgregasi Selesai: {total_records} data berhasil diproses secara paralel.")


if __name__ == "__main__":
    main()
