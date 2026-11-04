"""Contoh 17.3: Pemrosesan Berkas CSV dengan csv.reader dan csv.writer
Python Learning Hub - Level 2: Intermediate
"""

import csv
import os

nama_csv = "data_bts.csv"

# Baris data sampel: header + baris nilai
rekaman_bts = [
    ["id_bts", "lokasi", "frekuensi_mhz", "daya_dbm"],
    ["BTS-001", "Bandar Lampung", "1800", "43.0"],
    ["BTS-002", "Kalianda", "2100", "40.5"],
    ["BTS-003", "Natar", "900", "46.0"]
]

try:
    # 1. Menulis data menggunakan csv.writer
    with open(nama_csv, "w", newline="", encoding="utf-8") as f:
        penulis = csv.writer(f)
        penulis.writerows(rekaman_bts)

    # 2. Membaca data menggunakan csv.reader
    print("Daftar Stasiun BTS yang Terbaca dari CSV:")
    with open(nama_csv, "r", newline="", encoding="utf-8") as f:
        pembaca = csv.reader(f)
        header = next(pembaca)  # Memisahkan baris judul
        print(f"Header: {', '.join(header)}")
        for baris in pembaca:
            id_bts, kota, freq, daya = baris
            print(f"- {id_bts:<8} | Lokasi: {kota:<15} | Frek: {freq:>4} MHz | Daya: {daya} dBm")
finally:
    if os.path.exists(nama_csv):
        os.remove(nama_csv)

