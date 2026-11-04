data = [
    {"id": "S01", "lokasi": "A", "rsrp": -82},
    {"id": "S02", "lokasi": "B", "rsrp": -107},
]
lokasi_unik = {x["lokasi"] for x in data}
rsrp_per_id = {x["id"]: x["rsrp"] for x in data}
print(lokasi_unik)
print(rsrp_per_id)
