# Kalkulasi Waktu Propagasi Sinyal Gelombang Elektromagnetik
# File: ch01-05.py

jarak_meter = 1500.0  # Jarak stasiun pemancar ke penerima dalam meter
kecepatan_cahaya = 3e8  # Kecepatan cahaya dalam ruang hampa (3 x 10^8 m/s)

# Rumus fisika: waktu = jarak / kecepatan
waktu_propagasi_detik = jarak_meter / kecepatan_cahaya
waktu_propagasi_mikrodetik = waktu_propagasi_detik * 1e6

print("Jarak Transmisi:", jarak_meter, "meter")
print("Kecepatan Gelombang:", kecepatan_cahaya, "m/s")
print("Waktu Tempuh Propagasi:", waktu_propagasi_mikrodetik, "mikrodetik")

