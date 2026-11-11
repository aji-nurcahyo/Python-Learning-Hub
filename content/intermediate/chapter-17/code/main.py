"""Aplikasi CLI Demonstrasi CSV & JSON Data Manager
Python Learning Hub - Chapter 17: File Handling & Data Serialization
"""

import sys
from pathlib import Path

# Pastikan folder modul dapat diimpor
sys.path.insert(0, str(Path(__file__).parent))

from data_manager import TelemetryDataManager


def jalankan_demo() -> None:
    print("==================================================")
    print("   TELEMETRY CSV & JSON DATA MANAGER (CH 17)")
    print("==================================================")

    manager = TelemetryDataManager()
    sampel_csv = Path(__file__).parent / "stasiun_bts.csv"
    output_json = Path(__file__).parent / "stasiun_bts.json"

    # 1. Menyiapkan data sampel CSV lokal
    konten_csv = (
        "id,lokasi,frekuensi_mhz,daya_dbm,status\n"
        "BTS-01,Bandar Lampung,1800,43.5,ACTIVE\n"
        "BTS-02,Kotabumi,2100,41.0,ACTIVE\n"
        "BTS-03,Kalianda,900,46.2,MAINTENANCE\n"
    )
    sampel_csv.write_text(konten_csv, encoding="utf-8", newline="\n")

    try:
        # 2. Memuat dan memvalidasi data CSV
        total = manager.load_from_csv(sampel_csv)
        print(f"\n[1] Berhasil memuat {total} rekaman dari CSV:")
        for r in manager.records:
            print(f"    - [{r['id']}] {r['lokasi']:<16} | Frek: {r['frekuensi_mhz']:>4} MHz | Daya: {r['daya_dbm']:>4.1f} dBm | {r['status']}")

        # 3. Menambahkan rekaman baru
        print("\n[2] Menambahkan rekaman BTS baru...")
        status_aksi = manager.add_or_update_record({
            "id": "BTS-04",
            "lokasi": "Metro",
            "frekuensi_mhz": 2300.0,
            "daya_dbm": 44.0,
            "status": "ACTIVE"
        })
        print(f"    Status operasi: {status_aksi}")

        # 4. Ringkasan statistik
        ringkasan = manager.calculate_summary()
        print("\n[3] Ringkasan Metrik Telemetri:")
        print(f"    - Total Stasiun : {ringkasan['total_records']}")
        print(f"    - Rata-rata Daya: {ringkasan['avg_power_dbm']} dBm")
        print(f"    - Stasiun Aktif : {ringkasan['active_count']}")

        # 5. Ekspor ke JSON
        manager.export_to_json(output_json)
        print(f"\n[4] Data berhasil diekspor ke: {output_json.name}")
        print(f"    Ukuran file JSON: {output_json.stat().st_size} byte")

    finally:
        # Bersihkan file pengujian jika diperlukan
        if sampel_csv.exists():
            sampel_csv.unlink()
        if output_json.exists():
            output_json.unlink()

    print("\nEksekusi Data Manager selesai dengan sukses.")


if __name__ == "__main__":
    jalankan_demo()

