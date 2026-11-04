# Interpolasi String Modern dengan f-Strings (PEP 498)
# File: ch04-03.py

nama_stasiun = "BTS-Gedung-A"
frekuensi_mhz = 1800.0
daya_tx = 43.5

# Menyisipkan variabel langsung ke dalam string
laporan = f"Stasiun: {nama_stasiun} beroperasi pada {frekuensi_mhz} MHz dengan daya {daya_tx} dBm."
print(laporan)

# Mengevaluasi ekspresi matematika langsung di dalam kurung kurawal {}
print(f"Daya dua kali lipat: {daya_tx * 2} dBm")
print(f"Status uppercase: {nama_stasiun.upper()}")
print(f"Kondisi daya aman: {'YA' if daya_tx <= 50 else 'TIDAK'}")
