"""Modul Calculators: Fungsi murni kalkulasi matematis daya & link budget.
Python Learning Hub - Chapter 21: Packages, Environments & Testing
"""

import math

def dbm_ke_mw(dbm: float) -> float:
    """Mengonversi nilai daya dari skala logaritmik (dBm) ke linier (mW)."""
    return round(10.0 ** (float(dbm) / 10.0), 4)

def mw_ke_dbm(mw: float) -> float:
    """Mengonversi nilai daya dari linier (mW) ke logaritmik (dBm)."""
    val = float(mw)
    if val <= 0:
        raise ValueError("Daya dalam skala milliwatt harus lebih besar dari nol!")
    return round(10.0 * math.log10(val), 2)

def hitung_link_budget(tx_power_dbm: float, tx_gain_dbi: float, rx_gain_dbi: float, path_loss_db: float) -> float:
    """Menghitung daya terima sinyal (Prx):
    Prx = Ptx + Gtx + Grx - PathLoss
    """
    if path_loss_db < 0:
        raise ValueError("Redaman lintasan (path loss) tidak boleh bernilai negatif!")
    return round(float(tx_power_dbm) + float(tx_gain_dbi) + float(rx_gain_dbi) - float(path_loss_db), 2)

