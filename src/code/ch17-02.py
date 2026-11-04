"""Contoh 17.2: Menulis (w) dan Menambahkan (a) Baris pada File Teks
Python Learning Hub - Level 2: Intermediate
"""

import os

nama_file = "laporan_harian.txt"

try:
    # 1. Menulis data baru (mode 'w' menimpa jika file sudah ada)
    with open(nama_file, "w", encoding="utf-8") as f:
        f.write("=== LAPORAN HARIAN TELEMETRI ===\n")
        f.write("Status: Sistem Berjalan Normal\n")

    # 2. Menambahkan baris log tambahan (mode 'a')
    catatan_tambahan = [
        "Pemeriksaan Kanal Frekuensi 2.4 GHz: OK\n",
        "Pemeriksaan Catu Daya Backup: Terisi 100%\n"
    ]
    with open(nama_file, "a", encoding="utf-8") as f:
        f.writelines(catatan_tambahan)

    # 3. Verifikasi hasil akhir
    with open(nama_file, "r", encoding="utf-8") as f:
        print("Isi Berkas Setelah Penambahan:")
        print(f.read().strip())
finally:
    if os.path.exists(nama_file):
        os.remove(nama_file)
