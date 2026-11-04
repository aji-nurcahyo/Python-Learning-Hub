"""Contoh 17.8: Konversi Data CSV ke JSON Terstruktur & Validasi Rekaman
Python Learning Hub - Level 2: Intermediate
"""

import csv
import json
from pathlib import Path

csv_path = Path("perangkat.csv")
json_path = Path("perangkat.json")

csv_raw = (
    "id,nama,tipe,latensi_ms\n"
    "1,Core-Router-01,ROUTER,4.2\n"
    "2,Edge-Switch-02,SWITCH,8.5\n"
    "3,Tower-BTS-11,BTS,15.1\n"
)

try:
    # 1. Menulis CSV mentah
    csv_path.write_text(csv_raw, encoding="utf-8")

    # 2. Membaca CSV dan memvalidasi tipe data numerik
    daftar_perangkat = []
    with open(csv_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            record_valid = {
                "id": int(row["id"]),
                "nama": row["nama"].strip(),
                "tipe": row["tipe"].strip(),
                "latensi_ms": float(row["latensi_ms"])
            }
            daftar_perangkat.append(record_valid)

    # 3. Export ke format JSON
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(daftar_perangkat, f, indent=2)

    # 4. Verifikasi hasil konversi
    print(f"Berhasil mengonversi {len(daftar_perangkat)} rekaman dari CSV ke JSON:")
    for item in daftar_perangkat:
        print(f"  - [{item['id']}] {item['nama']} ({item['tipe']}) : {item['latensi_ms']} ms")
finally:
    if csv_path.exists():
        csv_path.unlink()
    if json_path.exists():
        json_path.unlink()
