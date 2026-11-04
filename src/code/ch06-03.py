# Akumulasi Penjumlahan dan Perhitungan Nilai Rata-Rata
# File: ch06-03.py

daftar_daya_mw = [25.0, 32.5, 40.0, 18.5, 50.0]

total_daya = 0.0
jumlah_data = 0

for daya in daftar_daya_mw:
    total_daya += daya      # Pola akumulator
    jumlah_data += 1       # Pola pencacah (counter)

rata_rata = total_daya / jumlah_data if jumlah_data > 0 else 0.0

print(f"Data Daya Transmisi : {daftar_daya_mw}")
print(f"Jumlah Sampel       : {jumlah_data}")
print(f"Total Akumulasi     : {total_daya:.1f} mW")
print(f"Nilai Rata-Rata     : {rata_rata:.2f} mW")

