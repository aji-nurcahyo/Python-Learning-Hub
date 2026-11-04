"""Contoh 17.5: Serialisasi Objek Python ke Format JSON (json.dumps & dump)
Python Learning Hub - Level 2: Intermediate
"""

import json
import os

konfigurasi_gateway = {
    "gateway_id": "GW-SUMATERA-01",
    "ip_address": "10.120.4.1",
    "aktif": True,
    "kapasitas_kanal": 64,
    "protokol_didukung": ["TCP", "UDP", "MQTT"],
    "koordinat": {
        "latitude": -5.3582,
        "longitude": 105.3149
    }
}

nama_file_json = "gateway_config.json"

try:
    # 1. Serialisasi dictionary ke JSON string di memori (json.dumps)
    json_string = json.dumps(konfigurasi_gateway, indent=2)
    print("Hasil Serialisasi String JSON:")
    print(json_string)

    # 2. Serialisasi langsung ke file penyimpanan lokal (json.dump)
    with open(nama_file_json, "w", encoding="utf-8") as f:
        json.dump(konfigurasi_gateway, f, indent=4)

    print(f"\nKonfigurasi berhasil disimpan ke berkas: {nama_file_json}")
finally:
    if os.path.exists(nama_file_json):
        os.remove(nama_file_json)

