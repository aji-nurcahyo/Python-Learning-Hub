sensor = {"id": "S01", "lokasi": "Gedung A", "rsrp": -82}
print(sensor["id"])
print(sensor.get("rsrq", "tidak tersedia"))
sensor["rsrp"] = -80
print(sensor.items())
