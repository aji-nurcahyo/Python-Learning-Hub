nilai = 10  # global

def hitung():
    nilai = 20  # lokal
    return nilai + 5

print(hitung())  # 25
print(nilai)     # 10
