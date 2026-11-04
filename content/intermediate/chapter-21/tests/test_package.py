"""Unit Test Suite: Validasi Package telecom_toolkit
Python Learning Hub - Chapter 21: Packages, Environments & Testing
"""

import unittest
import sys
from pathlib import Path

# Memasukkan folder code ke sys.path
code_dir = Path(__file__).resolve().parent.parent / "code"
sys.path.insert(0, str(code_dir))

from telecom_toolkit import BaseStation, dbm_ke_mw, mw_ke_dbm, hitung_link_budget

class TestTelecomToolkit(unittest.TestCase):
    def setUp(self):
        """Pola Test Fixture: Menyiapkan objek awal sebelum tiap pengujian."""
        self.station = BaseStation("BTS-TEST-01", "Site Lab", tx_power_dbm=40.0, antenna_gain_dbi=15.0)

    def test_fixture_station_eirp(self):
        self.assertEqual(self.station.eirp_dbm, 55.0)
        self.assertEqual(self.station.station_id, "BTS-TEST-01")

    def test_parameterized_dbm_conversions(self):
        """Pola Parameterized Testing: Menguji serangkaian nilai konversi."""
        test_matrix = [
            (0.0, 1.0),
            (10.0, 10.0),
            (20.0, 100.0),
            (30.0, 1000.0),
        ]
        for dbm, expected_mw in test_matrix:
            with self.subTest(dbm=dbm, expected_mw=expected_mw):
                self.assertEqual(dbm_ke_mw(dbm), expected_mw)
                self.assertEqual(mw_ke_dbm(expected_mw), dbm)

    def test_exception_invalid_inputs(self):
        """Pola Exception Testing: Memastikan exception terlempar pada input ilegal."""
        # mw <= 0 harus memicu ValueError
        with self.assertRaises(ValueError):
            mw_ke_dbm(0.0)
        with self.assertRaises(ValueError):
            mw_ke_dbm(-15.0)

        # Daya BTS di luar rentang aman
        with self.assertRaises(ValueError):
            self.station.tx_power_dbm = 999.0

        # Path loss negatif pada link budget
        with self.assertRaises(ValueError):
            hitung_link_budget(40.0, 10.0, 2.0, -50.0)

    def test_link_budget_calculation(self):
        prx = hitung_link_budget(tx_power_dbm=43.0, tx_gain_dbi=18.0, rx_gain_dbi=2.0, path_loss_db=105.0)
        self.assertEqual(prx, -42.0)

if __name__ == "__main__":
    unittest.main()

