# Tabel Perkalian Sederhana Menggunakan For Loop
# File: ch06-02.py

pengali = 8
print(f"=== TABEL PERKALIAN {pengali} ===")

for i in range(1, 11):
    hasil = pengali * i
    print(f"{pengali} x {i:2d} = {hasil:2d}")
