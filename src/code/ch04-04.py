# Format Penentu (Format Specifiers) pada f-Strings
# File: ch04-04.py

nilai_pi = 3.14159265359
kecepatan_cahaya = 299792458
rasio_keberhasilan = 0.9875
id_antena = 7

# Format angka desimal tertentu (:.2f)
print(f"Nilai pi (2 desimal): {nilai_pi:.2f}")

# Format notasi ilmiah eksponensial (:.3e)
print(f"Kecepatan gelombang: {kecepatan_cahaya:.3e} m/s")

# Format persentase (:.1%)
print(f"Keberhasilan transmisi: {rasio_keberhasilan:.1%}")

# Zero-padding pada bilangan bulat ({:04d})
print(f"ID Antena terformat: ANT-{id_antena:04d}")

# Pemisah ribuan dengan koma ({:,})
print(f"Jarak total: {1500000:,} meter")
