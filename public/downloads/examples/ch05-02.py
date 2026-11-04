# Klasifikasi Nilai Akademik Mahasiswa
# File: ch05-02.py

def konversi_skor_ke_huruf(skor: float) -> str:
    """Mengonversi skor numerik 0-100 ke huruf mutu akademik."""
    if skor >= 80.0:
        return "A"
    elif skor >= 70.0:
        return "B"
    elif skor >= 60.0:
        return "C"
    elif skor >= 50.0:
        return "D"
    else:
        return "E"

daftar_skor = [85.5, 72.0, 64.0, 53.0, 41.5]

for s in daftar_skor:
    huruf = konversi_skor_ke_huruf(s)
    print(f"Skor: {s:5.1f} -> Huruf Mutu: {huruf}")
