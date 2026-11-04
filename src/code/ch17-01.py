"""Contoh 17.1: Membaca File Teks dengan Context Manager with & UTF-8
Python Learning Hub - Level 2: Intermediate
"""

import os

nama_file = "sampel_log.txt"

# Persiapan file sampel sementara
konten_awal = (
    "2026-11-04 08:00:01 INFO [Node-01] Daya transmisi normal: 23 dBm\n"
    "2026-11-04 08:00:05 WARN [Node-02] Suhu pemancar meningkat: 48 C\n"
    "2026-11-04 08:00:10 INFO [Node-03] Latensi transmisi paket: 12 ms\n"
)
with open(nama_file, "w", encoding="utf-8") as f:
    f.write(konten_awal)

try:
    # Membaca seluruh konten baris per baris secara efisien
    print("Membaca Baris File Teks:")
    with open(nama_file, "r", encoding="utf-8") as file_in:
        for nomor, baris in enumerate(file_in, 1):
            print(f"Baris {nomor}: {baris.strip()}")
finally:
    if os.path.exists(nama_file):
        os.remove(nama_file)
