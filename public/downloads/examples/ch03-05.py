# Perhitungan Panjang Gelombang Elektromagnetik & Konversi Daya
# File: ch03-05.py

import math

# Parameter gelombang radio
c = 3e8              # Kecepatan cahaya dalam m/s
frekuensi_hz = 1.8e9  # 1.8 GHz (LTE Band 3) dalam Hz

# Rumus: lambda = c / f
panjang_gelombang = c / frekuensi_hz

# Konversi daya pemancar dari miliwatt (mW) ke dBm: P_dBm = 10 * log10(P_mW)
daya_mw = 40000  # 40 Watt = 40,000 mW
daya_dbm = 10 * math.log10(daya_mw)

print("Frekuensi Pembawa:", frekuensi_hz / 1e6, "MHz")
print("Panjang Gelombang (lambda):", round(panjang_gelombang, 4), "meter")
print("Panjang Gelombang (cm):", round(panjang_gelombang * 100, 2), "cm")
print("Daya Pemancar (mW):", daya_mw, "mW")
print("Daya Pemancar (dBm):", round(daya_dbm, 2), "dBm")
