"""Contoh 14.4: Set Comprehensions & Deduplikasi Dinamis
Python Learning Hub - Level 2: Intermediate
"""

# Log pembacaan sensor dengan data kembar (duplikat) dan variasi spasi
log_aliran_mac = [
    "  00:1A:2B:3C:4D:5E  ",
    "00:1a:2b:3c:4d:5e",
    "  08:00:27:12:34:56",
    "08:00:27:12:34:56 ",
    "AA:BB:CC:DD:EE:FF",
    "00:1a:2b:3c:4d:5e",
]

# Set comprehension: Normalisasi huruf kapital, pembersihan spasi, dan deduplikasi instan
alamat_unik = {mac.strip().upper() for mac in log_aliran_mac}

print("Total log mentah   :", len(log_aliran_mac))
print("Total alamat unik  :", len(alamat_unik))
print("Himpunan Alamat MAC:")
for mac in sorted(alamat_unik):
    print(f"  - {mac}")
