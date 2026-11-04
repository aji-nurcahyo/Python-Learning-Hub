# Pengolahan Masukan Pengguna dan Type Casting
# File: ch04-02.py

# Pada sesi interaktif: input_teks = input("Masukkan frekuensi (MHz): ")
# Fungsi input() selalu menghasilkan tipe string (str)
input_simulasi = "2100.5"

# Konversi string masukan menjadi numerik float
frekuensi_mhz = float(input_simulasi)
frekuensi_khz = frekuensi_mhz * 1000

print("Nilai teks asli:", input_simulasi, "| Tipe:", type(input_simulasi).__name__)
print("Frekuensi (MHz):", frekuensi_mhz, "| Tipe:", type(frekuensi_mhz).__name__)
print("Frekuensi (kHz):", frekuensi_khz, "| Tipe:", type(frekuensi_khz).__name__)

