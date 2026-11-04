# Validasi Masukan dengan Pernyataan Kondisional
# File: ch05-06.py

def validasi_dan_proses_frekuensi(input_str: str) -> tuple[bool, float | None, str]:
    """Memvalidasi apakah string masukan berupa angka dan berada dalam rentang valid."""
    teks_bersih = input_str.strip()
    
    # 1. Validasi string tidak kosong
    if not teks_bersih:
        return False, None, "Galat: Masukan kosong."
    
    # 2. Validasi apakah format numerik valid (mengizinkan titik desimal)
    try:
        nilai = float(teks_bersih)
    except ValueError:
        return False, None, f"Galat: '{teks_bersih}' bukan format angka desimal yang valid."
    
    # 3. Validasi rentang spektrum seluler (700 MHz - 3500 MHz)
    if nilai < 700.0 or nilai > 3500.0:
        return False, None, f"Peringatan: Frekuensi {nilai} MHz di luar rentang alokasi (700-3500 MHz)."
    
    return True, nilai, f"Sukses: Frekuensi {nilai:.1f} MHz valid dan siap dialokasikan."

sampel_masukan = [" 1800.5 ", "2100", "", "abc_mhz", "500.0", "4000.0"]

for item in sampel_masukan:
    valid, angka, pesan = validasi_dan_proses_frekuensi(item)
    print(f"Input: '{item:<10}' | Valid: {str(valid):<5} | Status: {pesan}")
