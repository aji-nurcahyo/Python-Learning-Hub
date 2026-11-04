# Argumen Pemisah (sep) dan Akhiran (end) pada print()
# File: ch04-01.py

# Argumen sep menentukan karakter di antara argumen
print("Node-A", "Node-B", "Node-C", sep=" -> ")
print("2026", "11", "04", sep="-")
print("192", "168", "1", "1", sep=".")

# Argumen end menentukan karakter penutup (default adalah newline '\n')
print("Menghubungkan ke pemancar", end="...")
print(" [TERHUBUNG]")

# Kombinasi sep dan end
print("STATUS", "READY", sep=": ", end=" | ID: BTS-01\n")

