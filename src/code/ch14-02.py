"""Contoh 14.2: Nested List Comprehensions (Matriks & Grid Koordinat)
Python Learning Hub - Level 2: Intermediate
"""

# 1. Pembangkitan matriks 2D (Grid Node Jaringan 3x3)
grid_node = [[f"Node({baris},{kolom})" for kolom in range(3)] for baris in range(3)]
print("Matriks Grid 3x3:")
for b in grid_node:
    print(" ", b)

# 2. Meratakan matriks bersarang menjadi list 1D (Matrix Flattening)
matriks_daya = [
    [12.5, 14.0, 15.2],
    [22.1, 24.5, 26.0],
    [31.0, 33.2, 35.5]
]
semua_daya = [nilai for baris in matriks_daya for nilai in baris]
print("\nHasil Flattening Matriks 2D:", semua_daya)

# 3. Flattening dengan pemfilteran nilai
daya_tinggi = [x for baris in matriks_daya for x in baris if x >= 25.0]
print("Elemen Daya Tinggi (>= 25.0):", daya_tinggi)

