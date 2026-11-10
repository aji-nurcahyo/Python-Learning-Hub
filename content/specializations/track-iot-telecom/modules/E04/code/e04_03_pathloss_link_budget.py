import numpy as np


def compute_fspl_db(distance_km: float, freq_mhz: float) -> float:
    if distance_km <= 0 or freq_mhz <= 0:
        raise ValueError("Jarak dan frekuensi wajib bernilai positif.")
    return float(32.44 + 20.0 * np.log10(distance_km) + 20.0 * np.log10(freq_mhz))


def received_power_dbm(tx_power_dbm: float, tx_gain_dbi: float, rx_gain_dbi: float, path_loss_db: float) -> float:
    return round(tx_power_dbm + tx_gain_dbi + rx_gain_dbi - path_loss_db, 2)


if __name__ == "__main__":
    tx_dbm, g_tx, g_rx = 43.0, 17.0, 0.0
    freq = 1800.0
    print(f"Simulasi Link Budget Frekuensi {freq:.0f} MHz (Tx={tx_dbm} dBm, Gain={g_tx} dBi):")
    for d in [0.5, 1.0, 2.0, 4.0]:
        fspl = compute_fspl_db(d, freq)
        rx = received_power_dbm(tx_dbm, g_tx, g_rx, fspl)
        print(f" - Jarak {d:4.1f} km | FSPL = {fspl:6.2f} dB | Rx Power = {rx:6.2f} dBm")

