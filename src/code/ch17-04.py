"""Contoh 17.4: Pengolahan CSV Tabular dengan csv.DictReader & DictWriter
Python Learning Hub - Level 2: Intermediate
"""

import csv
import os

nama_file = "sensor_telemetri.csv"
fieldnames = ["sensor_id", "tegangan", "arus", "status"]

data_sensor = [
    {"sensor_id": "V-101", "tegangan": 220.4, "arus": 4.5, "status": "NORMAL"},
    {"sensor_id": "V-102", "tegangan": 218.1, "arus": 5.2, "status": "NORMAL"},
    {"sensor_id": "V-103", "tegangan": 195.0, "arus": 7.8, "status": "WARNING"},
]

try:
    # 1. Menulis dictionary ke CSV dengan DictWriter
    with open(nama_file, "w", newline="", encoding="utf-8") as f:
        penulis = csv.DictWriter(f, fieldnames=fieldnames)
        penulis.writeheader()
        penulis.writerows(data_sensor)

    # 2. Membaca kembali CSV ke dalam bentuk dictionary dengan DictReader
    print("Membaca Rekaman Telemetri Menggunakan DictReader:")
    with open(nama_file, "r", newline="", encoding="utf-8") as f:
        pembaca = csv.DictReader(f)
        for row in pembaca:
            s_id = row["sensor_id"]
            teg = float(row["tegangan"])
            stat = row["status"]
            print(f"Sensor [{s_id}] -> Tegangan: {teg:.1f} V | Status: {stat}")
finally:
    if os.path.exists(nama_file):
        os.remove(nama_file)
