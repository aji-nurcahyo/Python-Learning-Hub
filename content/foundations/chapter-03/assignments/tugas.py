"""
Tugas Praktik 03: Kalkulator Anggaran Daya Tautan (Link Budget)
Mata Kuliah: Algoritma & Pemrograman / Python Learning Hub
Program Studi: Teknik Telekomunikasi - ITERA
Nama Mahasiswa: [Isi Nama Anda]
NIM           : [Isi NIM Anda]
"""

def hitung_link_budget(
    p_tx_dbm: float,
    g_tx_dbi: float,
    g_rx_dbi: float,
    l_fspl_db: float,
    l_misc_db: float,
    sensitivitas_rx_dbm: float = -95.0,
    ambang_margin_db: float = 10.0
) -> dict:
    """Menghitung daya terima, fade margin, dan kelayakan tautan komunikasi radio."""
    # 1. Hitung daya sinyal terima P_rx
    p_rx_dbm = p_tx_dbm + g_tx_dbi + g_rx_dbi - l_fspl_db - l_misc_db
    
    # 2. Hitung fade margin tautan
    margin_db = p_rx_dbm - sensitivitas_rx_dbm
    
    # 3. Evaluasi kelayakan dengan operator relasional
    layak = margin_db >= ambang_margin_db
    
    return {
        "p_tx": p_tx_dbm,
        "g_tx": g_tx_dbi,
        "g_rx": g_rx_dbi,
        "l_total": l_fspl_db + l_misc_db,
        "p_rx": p_rx_dbm,
        "margin": margin_db,
        "layak": layak
    }

def tampilkan_laporan_link_budget(data: dict) -> None:
    """Mencetak kartu laporan link budget radio ke layar terminal."""
    print("=" * 50)
    print("        ANALISIS LINK BUDGET TAUTAN RADIO")
    print("=" * 50)
    print(f"Daya Pemancar (P_tx)        : {data['p_tx']:.1f} dBm")
    print(f"Penguatan Total Antena      : {data['g_tx'] + data['g_rx']:.1f} dBi (Tx: {data['g_tx']:.1f} dBi, Rx: {data['g_rx']:.1f} dBi)")
    print(f"Total Redaman Lintasan      : {data['l_total']:.1f} dB")
    print("-" * 50)
    print(f"Daya Sinyal Terima (P_rx)   : {data['p_rx']:.1f} dBm")
    print(f"Fade Margin                 : {data['margin']:.1f} dB")
    print("-" * 50)
    status_teks = "MEMENUHI SYARAT (MARGIN >= 10 dB)" if data["layak"] else "TIDAK LAYAK (MARGIN DI BAWAH 10 dB)"
    print(f"Kelayakan Tautan            : {status_teks}")
    print("=" * 50)

if __name__ == "__main__":
    hasil = hitung_link_budget(
        p_tx_dbm=43.0,
        g_tx_dbi=18.0,
        g_rx_dbi=14.0,
        l_fspl_db=142.5,
        l_misc_db=3.0,
        sensitivitas_rx_dbm=-95.0
    )
    tampilkan_laporan_link_budget(hasil)

