# Normalisasi dan Pembersihan Teks
# File: ch07-07.py

teks_kotor = "  [PENTING]   Sinyal  Transmisi   TERPUTUS  sementara...!!   "

# 1. Hapus tanda kurung siku dan tanda seru/titik yang berlebihan
teks_buang_simbol = teks_kotor.replace("[", "").replace("]", "").replace("!", "").replace(".", "")

# 2. Hapus spasi berlebih antar kata dengan split dan join
kata_kata = teks_buang_simbol.split()
teks_rapi = " ".join(kata_kata)

# 3. Ubah menjadi huruf kecil seragam
teks_normal = teks_rapi.lower()

print(f"Teks Asli   : '{teks_kotor}'")
print(f"Tanpa Simbol: '{teks_buang_simbol.strip()}'")
print(f"Spasi Rapi  : '{teks_rapi}'")
print(f"Terkalibrasi: '{teks_normal}'")

