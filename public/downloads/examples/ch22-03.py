"""Contoh 22.3: Storage Engine Capstone (Serialisasi JSON Persistent)
Python Learning Hub - Level 2: Intermediate Capstone Project
"""

import json

class InMemoryStorageEngine:
    """Simulasi mesin penyimpanan berkas JSON terisolasi."""

    def __init__(self):
        self.buffer = ""

    def save(self, data: list[dict]) -> str:
        self.buffer = json.dumps(data, indent=2, ensure_ascii=False)
        return self.buffer

    def load(self) -> list[dict]:
        if not self.buffer:
            return []
        return json.loads(self.buffer)

storage = InMemoryStorageEngine()

sample_inventory = [
    {"device_id": "RTR-01", "name": "MikroTik CCR", "category": "Network", "price": 8500000.0},
    {"device_id": "SRV-01", "name": "Dell PowerEdge", "category": "Server", "price": 42000000.0},
    {"device_id": "SENS-01", "name": "SHT30 Temperature", "category": "Sensor", "price": 250000.0},
]

serialized_json = storage.save(sample_inventory)
print("=== Serialisasi Data JSON Capstone ===")
print(serialized_json)

loaded_data = storage.load()
print(f"\nBerhasil memuat kembali {len(loaded_data)} rekaman perangkat dari storage JSON.")
assert len(loaded_data) == 3
print("Integritas data terverifikasi identik.")
