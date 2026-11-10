import numpy as np

# Matriks pengukuran 4 stasiun sensor (baris) x 3 metrik: [suhu_C, kelembapan_pct, latensi_ms]
sensor_readings = np.array(
    [
        [28.4, 62.0, 18.2],
        [29.1, 60.5, 19.5],
        [36.5, 48.0, 45.2],
        [27.9, 64.1, 16.8],
    ],
    dtype=np.float64,
)

print("Shape matriks :", sensor_readings.shape)
print("Jumlah dimensi:", sensor_readings.ndim)
print("Total elemen  :", sensor_readings.size)
print("Tipe data     :", sensor_readings.dtype)

# Slicing: ambil seluruh baris untuk kolom latensi (indeks 2)
latensi_col = sensor_readings[:, 2]
print("Kolom latensi :", latensi_col)

# Agregasi per kolom (axis=0)
rata_per_metrik = np.mean(sensor_readings, axis=0)
maks_per_metrik = np.max(sensor_readings, axis=0)
print("Rata-rata [suhu, lembap, latensi]:", np.round(rata_per_metrik, 2))
print("Maksimum  [suhu, lembap, latensi]:", np.round(maks_per_metrik, 2))

