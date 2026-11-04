# Pemrosesan Aliran Data Sensor dengan break dan continue
# File: ch06-05.py

# Data deret telemetri suhu stasiun (Celsius)
# -999.0 menandakan sensor error/glitch (harus dilewati dengan continue)
# 100.0 menandakan kondisi bahaya panas ekstrem (harus dihentikan dengan break)
telemetri_suhu = [28.5, 31.0, -999.0, 34.2, 29.8, 102.5, 30.0]

print("=== MEMULAI MONITORING TELEMETRI SUHU RUANG RAK ===")
for detik, suhu in enumerate(telemetri_suhu, start=1):
    if suhu == -999.0:
        print(f"Detik {detik:2d}: Glitch sinyal sensor terdeteksi (-999.0 C). Lewati pembacaan.")
        continue

    if suhu > 75.0:
        print(f"Detik {detik:2d}: [ALARM KRITIS] Suhu melonjak mencapai {suhu} C! Hentikan loop pemantauan.")
        break

    print(f"Detik {detik:2d}: Suhu normal terukur = {suhu:5.1f} C")

print("Monitoring selesai dengan aman.")
