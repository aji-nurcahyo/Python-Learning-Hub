# Konversi Tipe Data Eksplisit (Type Casting)
# File: ch02-03.py

# Konversi string ke angka
teks_frekuensi = "1800"
frekuensi_int = int(teks_frekuensi)
frekuensi_float = float(teks_frekuensi)

# Konversi angka ke teks
daya_mw = 250
teks_daya = str(daya_mw) + " mW"

# Konversi ke boolean (Truthy & Falsy)
print("Konversi int:", frekuensi_int, type(frekuensi_int).__name__)
print("Konversi float:", frekuensi_float, type(frekuensi_float).__name__)
print("Konversi string:", teks_daya, type(teks_daya).__name__)
print("bool(0):", bool(0))
print("bool(100):", bool(100))
print("bool(''):", bool(""))
print("bool('Aktif'):", bool("Aktif"))

