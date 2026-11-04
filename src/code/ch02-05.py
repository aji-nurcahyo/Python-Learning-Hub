# Validasi Parameter BTS dengan isinstance()
# File: ch02-05.py

node_id = "BTS-BandarLampung-04"
frekuensi_mhz = 1800.0
daya_tx = 40
operasional = True

# Memeriksa kesesuaian tipe data spesifikasi
valid_id = isinstance(node_id, str)
valid_frekuensi = isinstance(frekuensi_mhz, (int, float))
valid_daya = isinstance(daya_tx, int)
valid_status = isinstance(operasional, bool)

print("Validasi Node ID (str):", valid_id)
print("Validasi Frekuensi (int/float):", valid_frekuensi)
print("Validasi Daya TX (int):", valid_daya)
print("Validasi Status (bool):", valid_status)
print("Semua parameter valid:", valid_id and valid_frekuensi and valid_daya and valid_status)
