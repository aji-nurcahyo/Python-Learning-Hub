# Pencarian Nilai Minimum dan Maksimum Menggunakan Loop Manual
# File: ch06-06.py

sampel_rsrp = [-88.0, -95.5, -74.0, -102.0, -81.5]

# Inisialisasi awal menggunakan elemen pertama
nilai_min = sampel_rsrp[0]
nilai_max = sampel_rsrp[0]

for s in sampel_rsrp[1:]:
    if s < nilai_min:
        nilai_min = s
    if s > nilai_max:
        nilai_max = s

print(f"Data Pengukuran RSRP (dBm) : {sampel_rsrp}")
print(f"Nilai Terendah (Sinyal Terlemah)  : {nilai_min} dBm")
print(f"Nilai Tertinggi (Sinyal Terkuat)  : {nilai_max} dBm")
