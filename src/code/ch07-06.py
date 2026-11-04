# Parsing Pesan Telemetri Sensor Terstruktur
# File: ch07-06.py

raw_payload = "ID=BTS-04;FREQ=1800.5;PWR=40.0;STAT=ACTIVE"

# 1. Pisahkan setiap field berdasarkan delimiter titik-koma ';'
pasangan_field = raw_payload.split(";")

data_terurai = {}

for pair in pasangan_field:
    # 2. Pisahkan key dan value berdasarkan tanda '='
    kunci, nilai = pair.split("=")
    data_terurai[kunci] = nilai

print(f"Payload Mentah: '{raw_payload}'")
print("Hasil Parsing Field:")
for k, v in data_terurai.items():
    print(f"  {k:<6} -> {v}")

# 3. Rekonstruksi string format laporan baru
laporan_baru = f"Perangkat {data_terurai['ID']} aktif pada {data_terurai['FREQ']} MHz dengan daya {data_terurai['PWR']} W."
print("\nRekonstruksi Laporan:")
print(laporan_baru)

