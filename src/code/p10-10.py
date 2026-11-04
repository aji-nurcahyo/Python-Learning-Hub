def cari_sensor(data, id_sensor):
    for sensor in data:
        if sensor["id"] == id_sensor:
            return sensor
    return None

print(cari_sensor([{ "id": "S01", "rsrp": -82 }], "S01"))
print(cari_sensor([], "S99"))
