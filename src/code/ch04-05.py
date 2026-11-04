# Format Tabel Terstruktur dengan Perataan Teks (Alignment)
# File: ch04-05.py

# Header tabel
print("=" * 45)
print(f"{'KODE BTS':<12} | {'FREKUENSI':^14} | {'STATUS':>12}")
print("=" * 45)

# Baris data dengan perataan kiri (<), tengah (^), kanan (>)
data_bts = [
    ("BTS-01", 900.0, "ONLINE"),
    ("BTS-02", 1800.5, "ONLINE"),
    ("BTS-03", 2100.0, "MAINTENANCE"),
    ("BTS-04", 2600.0, "OFFLINE"),
]

for kode, frek, status in data_bts:
    print(f"{kode:<12} | {frek:^10.1f} MHz | {status:>12}")

print("=" * 45)

