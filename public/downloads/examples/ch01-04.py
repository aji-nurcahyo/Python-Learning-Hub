# Struktur Indentasi dan Blok Kode Python
# File: ch01-04.py

daya_dbm = -75

# Python menggunakan indentasi 4 spasi (bukan kurung kurawal)
if daya_dbm >= -85:
    status = "Sinyal Bagus"
    print(f"Level Daya: {daya_dbm} dBm -> {status}")
else:
    status = "Sinyal Lemah"
    print(f"Level Daya: {daya_dbm} dBm -> {status}")

print("Blok percabangan selesai dieksekusi secara terurut.")

