# Operator Logika dan Evaluasi Short-Circuit
# File: ch03-03.py

daya_aktif = True
suhu_normal = True
gangguan = False

# Evaluasi ekspresi logika
status_operasional = daya_aktif and suhu_normal and not gangguan
print("Status Operasional Node:", status_operasional)

# Evaluasi kondisi siaga (alert)
perlu_inspeksi = (not suhu_normal) or gangguan
print("Perlu Inspeksi Lapangan:", perlu_inspeksi)

# Pembuktian short-circuit logic:
# Pada 'False and ...', operan kedua tidak akan pernah dievaluasi
print("Short-circuit AND:", False and (10 / 0 == 0))  # Tidak memicu ZeroDivisionError
# Pada 'True or ...', operan kedua tidak akan pernah dievaluasi
print("Short-circuit OR:", True or (10 / 0 == 0))   # Tidak memicu ZeroDivisionError

