# Pembangkitan Pola Matriks Antena dengan Nested Loop
# File: ch06-07.py

baris = 4
kolom = 6

print(f"=== KISI MATRIKS ANTENA MIMO ({baris}x{kolom}) ===")
for r in range(1, baris + 1):
    for c in range(1, kolom + 1):
        print(f"[A{r}{c}]", end=" ")
    print()  # Pindah baris baru setelah setiap baris selesai

print("\n=== POLA SEGITIGA TINGKAT SINYAL ===")
for i in range(1, 6):
    for _ in range(i):
        print("*", end="")
    print()
