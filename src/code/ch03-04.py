# Presedensi Operator dan Compound Assignment
# File: ch03-04.py

# Presedensi: Tanda kurung () > Eksponen ** > Perkalian/Pembagian > Penjumlahan/Pengurangan
nilai_a = 5 + 3 * 2 ** 3
nilai_b = (5 + 3) * (2 ** 3)

print("Hasil tanpa kurung (5 + 3 * 2 ** 3):", nilai_a)
print("Hasil dengan kurung ((5 + 3) * (2 ** 3)):", nilai_b)

# Compound assignment
total_antena = 4
print("Awal:", total_antena)

total_antena += 2  # total_antena = total_antena + 2
print("Setelah += 2:", total_antena)

total_antena *= 3  # total_antena = total_antena * 3
print("Setelah *= 3:", total_antena)

total_antena //= 2 # total_antena = total_antena // 2
print("Setelah //= 2:", total_antena)
