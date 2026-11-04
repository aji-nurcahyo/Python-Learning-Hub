"""Chapter 24: Mini Project Demonstrator
Data Processing Pipeline with Decorators, Generators & Context Managers
Python Learning Hub - Professional Python Engineering
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from pipeline import execute_pipeline


def run_demonstration() -> None:
    print("=" * 65)
    print("DEMO: DATA PROCESSING PIPELINE (CHAPTER 24)")
    print("=" * 65)

    sample_dataset = [
        {"cell_id": "BTS-JKT-01", "rsrp_dbm": -78.5, "snr_db": 18.2},
        {"cell_id": "BTS-JKT-02", "rsrp_dbm": -102.0, "snr_db": 8.5},   # filtered out (< 12 dB)
        {"cell_id": "BTS-JKT-03", "rsrp_dbm": -84.0, "snr_db": 14.1},
        {"cell_id": "BTS-JKT-04", "rsrp_dbm": -110.5, "snr_db": 6.0},   # filtered out (< 12 dB)
        {"cell_id": "BTS-JKT-05", "rsrp_dbm": -72.0, "snr_db": 22.4},
    ]

    print(f"Total data input : {len(sample_dataset)} rekaman mentah")
    output = execute_pipeline(sample_dataset, min_snr=12.0)

    print(f"\nHasil Pemrosesan Pipeline:")
    print(f"Total lolos filter  : {output['processed_count']} rekaman")
    print(f"Status Timer Context: {output['timer']['label']} (Success: {output['timer']['success']})")

    print("\nRincian Rekaman Terverifikasi:")
    for res in output["results"]:
        print(f" * {res['cell_id']} | RSRP: {res['rsrp_dbm']} dBm | SNR: {res['snr_db']} dB")


if __name__ == "__main__":
    run_demonstration()

