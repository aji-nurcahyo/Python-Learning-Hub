from contoh import PENGUKURAN as pengukuran, cari_sensor

hasil = cari_sensor(pengukuran, "S02")
if hasil is None:
    print("Sensor tidak ditemukan")
else:
    print(hasil["lokasi"], hasil["rsrp"])
