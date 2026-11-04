"""Contoh Praktik Terapan: CSV & JSON Data Manager
Python Learning Hub - Chapter 17: File Handling & Data Serialization
"""

import csv
import json
from pathlib import Path

# 1. Menyiapkan dataset sampel dalam CSV
csv_file = Path("nodes_telekomunikasi.csv")
json_file = Path("nodes_telekomunikasi.json")

data_awal = [
    ["node_id", "nama_lokasi", "kapasitas_gbps", "status"],
    ["N-01", "Gedung Kuliah Umum", "10.0", "ONLINE"],
    ["N-02", "Laboratorium Teknik", "40.0", "ONLINE"],
    ["N-03", "Asrama Mahasiswa", "5.0", "MAINTENANCE"],
]

with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data_awal)

print(f"1. Berkas CSV '{csv_file.name}' berhasil dibuat.")

# 2. Membaca CSV dan memvalidasi ke dictionary
daftar_node = []
with open(csv_file, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for baris in reader:
        node = {
            "node_id": baris["node_id"],
            "nama_lokasi": baris["nama_lokasi"],
            "kapasitas_gbps": float(baris["kapasitas_gbps"]),
            "status": baris["status"]
        }
        daftar_node.append(node)

print(f"2. Berhasil mem-parsing {len(daftar_node)} node dari CSV.")

# 3. Serialisasi ke berkas JSON
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(daftar_node, f, indent=2)

print(f"3. Data berhasil diserialisasi ke '{json_file.name}'.")

# 4. Deserialisasi ulang untuk membuktikan integritas
with open(json_file, "r", encoding="utf-8") as f:
    hasil_load = json.load(f)

print("4. Verifikasi isi JSON ter-deserialisasi:")
for n in hasil_load:
    print(f"   - Node [{n['node_id']}] {n['nama_lokasi']} ({n['kapasitas_gbps']} Gbps) -> {n['status']}")

# Pembersihan
if csv_file.exists():
    csv_file.unlink()
if json_file.exists():
    json_file.unlink()

