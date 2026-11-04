# Pencarian Teks dalam Log Jaringan
# File: ch07-02.py

pesan_log = "[ERROR 2026-11-04] BTS-Lampung-01: Gagal menerima sinyal sinkronisasi dari UE-8821"

# 1. Operator keanggotaan 'in'
apakah_error = "ERROR" in pesan_log
apakah_sukses = "SUCCESS" in pesan_log

# 2. Metode find()
posisi_ue = pesan_log.find("UE-8821")

# 3. Metode startswith() dan endswith()
awalan_log = pesan_log.startswith("[ERROR")
akhiran_log = pesan_log.endswith("UE-8821")

print(f"Log: '{pesan_log}'")
print(f"Mengandung 'ERROR'   : {apakah_error}")
print(f"Mengandung 'SUCCESS' : {apakah_sukses}")
print(f"Posisi teks 'UE-8821': Indeks ke-{posisi_ue}")
print(f"Diawali '[ERROR'     : {awalan_log}")
print(f"Diakhiri 'UE-8821'   : {akhiran_log}")
