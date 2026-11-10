# Latihan Mandiri A01 — Numerical Computing with NumPy

## Latihan 1: Eksplorasi Dataset Sensor
1. Muat berkas `datasets/sensor_matrix.csv` memakai `np.genfromtxt(..., delimiter=",", skip_header=1)`.
2. Pisahkan kolom ID node (`[:, 0]`) dan matriks fitur (`[:, 1:]`).
3. Hitung nilai minimum, median, rata-rata, dan maksimum per kolom menggunakan `axis=0`.

## Latihan 2: Normalisasi Z-Score via Broadcasting
1. Hitung rata-rata (`mean`) dan standar deviasi (`std`) per fitur dengan `keepdims=True`.
2. Lindungi pembagian nol memakai `np.where(std == 0, 1.0, std)`.
3. Identifikasi indeks baris yang memiliki setidaknya satu fitur dengan `abs(z_score) > 1.8`.

## Checklist Refleksi
- Apakah Anda sudah menghindari loop `for` untuk menghitung norma atau normalisasi?
- Apakah bentuk (`shape`) dari setiap array intermediate sesuai aturan broadcasting?

