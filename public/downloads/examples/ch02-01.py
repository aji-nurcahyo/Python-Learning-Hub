# Variabel sebagai Referensi Objek di Memori
# File: ch02-01.py

# Memberikan label variabel pada nilai objek
nama_stasiun = "BTS-Sukarame-01"
id_transceiver = 1042
kapasitas_kanal = 64

print("Nama Stasiun:", nama_stasiun)
print("ID Transceiver:", id_transceiver)
print("Kapasitas Kanal:", kapasitas_kanal)

# Referensi variabel lain ke objek yang sama
salinan_id = id_transceiver
print("Apakah referensi menunjuk objek yang sama?", salinan_id is id_transceiver)

