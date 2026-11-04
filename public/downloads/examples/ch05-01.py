# Deteksi Bilangan Positif, Negatif, atau Nol
# File: ch05-01.py

def cek_tanda_bilangan(nilai: float) -> str:
    """Mengidentifikasi tanda bilangan menggunakan struktur if-elif-else."""
    if nilai > 0:
        return "Positif"
    elif nilai < 0:
        return "Negatif"
    else:
        return "Nol"

# Kasus uji deterministik
daftar_uji = [15.5, -42.0, 0.0]

for bil in daftar_uji:
    kategori = cek_tanda_bilangan(bil)
    print(f"Bilangan {bil:>5} -> {kategori}")
