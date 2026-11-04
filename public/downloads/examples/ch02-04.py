# Sifat Pengetikan Dinamis (Dynamic Typing)
# File: ch02-04.py

# Variabel dapat menunjuk ke tipe objek yang berbeda pada runtime
sinyal = "Tidak Ada Sinyal"
print("Nilai awal:", sinyal, "| Tipe:", type(sinyal).__name__)

sinyal = -95
print("Setelah re-assignment integer:", sinyal, "| Tipe:", type(sinyal).__name__)

sinyal = -95.5
print("Setelah re-assignment float:", sinyal, "| Tipe:", type(sinyal).__name__)

sinyal = True
print("Setelah re-assignment boolean:", sinyal, "| Tipe:", type(sinyal).__name__)

