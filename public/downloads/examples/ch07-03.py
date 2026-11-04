# Penghitungan Karakter dan Frekuensi Huruf
# File: ch07-03.py

teks_telemetri = "PACKET_HEADER_DATA_CRC_OK_ACK_PACKET"

# Menghitung kemunculan substring dengan count()
jumlah_packet = teks_telemetri.count("PACKET")
jumlah_garis_bawah = teks_telemetri.count("_")

# Menghitung huruf vokal secara manual dengan loop
vokal = "AEIOU"
cacah_vokal = 0
for char in teks_telemetri:
    if char in vokal:
        cacah_vokal += 1

print(f"Teks Asli          : {teks_telemetri}")
print(f"Panjang Karakter   : {len(teks_telemetri)}")
print(f"Kata 'PACKET'      : {jumlah_packet} kali")
print(f"Karakter '_'       : {jumlah_garis_bawah} kali")
print(f"Total Huruf Vokal  : {cacah_vokal}")

