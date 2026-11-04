# Validasi Berulang dengan While Loop (Simulasi Input Teruji)
# File: ch06-04.py

# Mensimulasikan antrean ketikan pengguna: dua input salah, lalu satu input benar
simulasi_input_pengguna = ["-15.0", "999.0", "43.5"]
indeks = 0
daya_tervalidasi = None

print("Memulai proses validasi input daya pemancar (rentang aman: 1.0 - 100.0 W)...")

while indeks < len(simulasi_input_pengguna):
    masukan = simulasi_input_pengguna[indeks]
    indeks += 1
    nilai = float(masukan)
    print(f"Percobaan input #{indeks}: Membaca '{masukan}'")

    if 1.0 <= nilai <= 100.0:
        daya_tervalidasi = nilai
        print(f"-> Sukses: Nilai {nilai} W diterima dan valid.")
        break
    else:
        print(f"-> Gagal: Nilai {nilai} di luar batas aman. Ulangi masukan.")

print(f"Hasil akhir proses validasi: Daya Terdaftar = {daya_tervalidasi} W")

