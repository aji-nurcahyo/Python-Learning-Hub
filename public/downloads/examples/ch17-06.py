"""Contoh 17.6: Deserialisasi Payload JSON ke Objek Python (json.loads & load)
Python Learning Hub - Level 2: Intermediate
"""

import json
import os

nama_file_temp = "paket_transmisi.json"

payload_json_mentah = """
{
  "transmisi_id": "TX-99012",
  "frekuensi_ghz": 5.8,
  "antrean_paket": [128, 256, 512, 1024],
  "enkripsi_aktif": true,
  "metrik": {
    "snr_db": 28.5,
    "packet_loss_pct": 0.02
  }
}
"""

try:
    # 1. Menulis string sampel ke berkas sementara
    with open(nama_file_temp, "w", encoding="utf-8") as f:
        f.write(payload_json_mentah.strip())

    # 2. Deserialisasi dari file stream (json.load)
    with open(nama_file_temp, "r", encoding="utf-8") as f:
        objek_data = json.load(f)

    # 3. Mengakses data Python terstruktur
    print("Hasil Deserialisasi JSON:")
    print("Tipe Objek Hasil :", type(objek_data).__name__)
    print("ID Transmisi     :", objek_data["transmisi_id"])
    print("Frekuensi        :", objek_data["frekuensi_ghz"], "GHz")
    print("Total Paket      :", len(objek_data["antrean_paket"]))
    print("SNR Penerima     :", objek_data["metrik"]["snr_db"], "dB")
finally:
    if os.path.exists(nama_file_temp):
        os.remove(nama_file_temp)

