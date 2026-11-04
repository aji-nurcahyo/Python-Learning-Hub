"""Contoh Kode Chapter 21: Packages, Environments & Testing
Python Learning Hub - Level 2: Intermediate Python

Menyajikan modul mandiri dengan fungsionalitas murni dan rangkaian pengujian assertif.
"""

import math

def dbm_ke_mw(dbm: float) -> float:
    return round(10.0 ** (float(dbm) / 10.0), 4)

def mw_ke_dbm(mw: float) -> float:
    if mw <= 0:
        raise ValueError("Daya harus lebih besar dari nol!")
    return round(10.0 * math.log10(float(mw)), 2)

def hitung_link_budget(tx_power_dbm: float, tx_gain_dbi: float, rx_gain_dbi: float, path_loss_db: float) -> float:
    if path_loss_db < 0:
        raise ValueError("Path loss tidak boleh negatif!")
    return round(float(tx_power_dbm) + float(tx_gain_dbi) + float(rx_gain_dbi) - float(path_loss_db), 2)

if __name__ == "__main__":
    print("=== Menjalankan Verifikasi Matematis Sinyal ===")
    assert dbm_ke_mw(30.0) == 1000.0, "30 dBm harus setara dengan 1000 mW (1 Watt)"
    assert mw_ke_dbm(1000.0) == 30.0, "1000 mW harus setara dengan 30 dBm"
    
    prx = hitung_link_budget(43.0, 15.0, 2.0, 120.0)
    assert prx == -60.0, "Link budget harus menghasilkan -60.0 dBm"
    
    print(f"30 dBm  -> {dbm_ke_mw(30.0)} mW")
    print(f"1000 mW -> {mw_ke_dbm(1000.0)} dBm")
    print(f"Prx     -> {prx} dBm")
    print("Seluruh assertion pengujian berhasil diverifikasi!")

