# Pemformatan Nama dan Teks Pengguna
# File: ch07-01.py

nama_mentah = "   aji pamungkas tri nurcahyo   "

# 1. Menghapus spasi di awal dan akhir
nama_bersih = nama_mentah.strip()

# 2. Mengubah menjadi format Title Case
nama_kapital = nama_bersih.title()

# 3. Memecah nama menjadi daftar kata
bagian_nama = nama_kapital.split()
nama_depan = bagian_nama[0]
nama_belakang = bagian_nama[-1]

print(f"Nama Asli Mentah : '{nama_mentah}'")
print(f"Setelah strip()  : '{nama_bersih}'")
print(f"Format Judul     : '{nama_kapital}'")
print(f"Nama Depan       : {nama_depan}")
print(f"Nama Belakang    : {nama_belakang}")

