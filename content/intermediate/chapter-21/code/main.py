"""Main Runner: Demonstrasi penggunaan package telecom_toolkit.
Python Learning Hub - Chapter 21: Packages, Environments & Testing
"""

from telecom_toolkit import BaseStation, dbm_ke_mw, mw_ke_dbm, hitung_link_budget

def main():
    print("==================================================")
    print("      DEMONSTRASI PACKAGE: TELECOM TOOLKIT        ")
    print("==================================================")

    # 1. Menggunakan entitas model BaseStation
    bts = BaseStation("BTS-01", "Tower Lab ITERA", tx_power_dbm=43.0, antenna_gain_dbi=17.5)
    print(f"Perangkat Terdaftar: {bts}")
    print(f"Daya Transmisi (Linier) : {dbm_ke_mw(bts.tx_power_dbm):.1f} mW ({dbm_ke_mw(bts.tx_power_dbm)/1000:.1f} Watt)")
    print(f"Total Radiasi EIRP      : {bts.eirp_dbm:.1f} dBm")

    # 2. Menggunakan fungsi kalkulator link budget
    print("\n--- Kalkulasi Link Budget Transmisi Nirkabel ---")
    rx_power = hitung_link_budget(
        tx_power_dbm=bts.tx_power_dbm,
        tx_gain_dbi=bts.antenna_gain_dbi,
        rx_gain_dbi=3.0,
        path_loss_db=110.0
    )
    print(f"Daya Terima Penerima (Prx) : {rx_power:.2f} dBm")
    print(f"Daya Terima (Linier)       : {dbm_ke_mw(rx_power):.6f} mW")

if __name__ == "__main__":
    main()

