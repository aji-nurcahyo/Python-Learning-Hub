"""Aplikasi CLI Demonstrasi Robust Data Validator
Python Learning Hub - Chapter 18: Exception Handling & Debugging
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from validator import TelecomRecordValidator


def demonstrasi_validasi() -> None:
    print("==================================================")
    print("      ROBUST DATA VALIDATOR SUITE (CH 18)         ")
    print("==================================================")

    validator = TelecomRecordValidator()

    # Sekumpulan rekaman uji dengan variasi galat nyata
    dataset_uji = [
        {"id": "BTS-01", "lokasi": "Lampung", "frekuensi_mhz": 1800.0, "daya_dbm": 43.0},
        {"id": "BTS-02", "lokasi": "Metro", "frekuensi_mhz": "dua ribu", "daya_dbm": 40.0},     # ValueError
        {"id": "BTS-03", "lokasi": "Kalianda", "daya_dbm": 45.0},                                # MissingFieldError (frekuensi)
        {"id": "BTS-04", "lokasi": "Kotabumi", "frekuensi_mhz": 900.0, "daya_dbm": 999.0},      # InvalidRangeError (daya)
        {"id": "BTS-05", "lokasi": "Natar", "frekuensi_mhz": 2100.0, "daya_dbm": 42.5},         # Valid
    ]

    print(f"\nMemulai validasi terhadap {len(dataset_uji)} rekaman data telemetri...")
    ringkasan = validator.process_batch(dataset_uji)

    print("\n--- Ringkasan Hasil Validasi ---")
    print(f"Total Rekaman Diproses : {ringkasan['total_diproses']}")
    print(f"Rekaman Lolos Validasi : {ringkasan['total_valid']}")
    print(f"Rekaman Gagal / Ditolak: {ringkasan['total_invalid']}")
    print(f"Tingkat Keberhasilan   : {ringkasan['valid_ratio_pct']}%")

    print("\nRincian Rekaman Ditolak:")
    for err_item in validator.invalid_records:
        rec_id = err_item["data"].get("id", "UNKNOWN")
        print(f"  - [{rec_id}] Alasan: {err_item['alasan']}")


if __name__ == "__main__":
    demonstrasi_validasi()
