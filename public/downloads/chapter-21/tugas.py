"""Starter Code Tugas Mandiri: Telecom Quality Metric Toolkit
Python Learning Hub - Chapter 21: Packages, Environments & Testing

Nama Mahasiswa : ____________________
NIM            : ____________________
Institusi      : Institut Teknologi Sumatera (ITERA)
"""

import math
import unittest

# =====================================================================
# BAGIAN 1: Modul Inti Pustaka (telecom_metrics/analyzer.py)
# =====================================================================

def hitung_snr_db(signal_power_w: float, noise_power_w: float) -> float:
    """Menghitung SNR dalam skala desibel (dB).
    Formula: 10 * log10(P_signal / P_noise)
    """
    p_sig = float(signal_power_w)
    p_noise = float(noise_power_w)
    if p_sig <= 0 or p_noise <= 0:
        raise ValueError("Daya sinyal dan daya derau (noise) harus bernilai positif lebih besar dari nol!")
    return round(10.0 * math.log10(p_sig / p_noise), 2)


def hitung_kapasitas_shannon(bandwidth_hz: float, snr_linier: float) -> float:
    """Menghitung batas kapasitas kanal transmisi teoritis (Shannon-Hartley).
    Formula: C = B * log2(1 + SNR)
    """
    bw = float(bandwidth_hz)
    snr = float(snr_linier)
    if bw <= 0:
        raise ValueError("Bandwidth harus bernilai lebih besar dari nol!")
    if snr < 0:
        raise ValueError("SNR linier tidak boleh bernilai negatif!")
    return round(bw * math.log2(1.0 + snr), 2)


def evaluasi_kelayakan_link(ber: float) -> str:
    """Mengevaluasi kelayakan tautan transmisi berdasarkan Bit Error Rate."""
    b = float(ber)
    if not (0.0 <= b <= 1.0):
        raise ValueError("Nilai BER harus berada dalam rentang probabilitas [0.0 s/d 1.0]!")
    return "LAYAK" if b <= 1e-6 else "TIDAK LAYAK"


# =====================================================================
# BAGIAN 2: Suite Pengujian Otomatis (tests/test_analyzer.py)
# =====================================================================

class TestTelecomMetrics(unittest.TestCase):
    def setUp(self):
        """Pola Test Fixture: Menyiapkan variabel kanal pengujian standar."""
        self.standard_bandwidth = 20_000_000.0  # 20 MHz Kanal LTE
        self.test_noise_w = 0.001

    def test_parameterized_snr_calculation(self):
        """Pola Parameterized Testing: Menguji tabel rasio daya dan dB."""
        test_cases = [
            (0.001, 0.001, 0.0),      # P_sig == P_noise -> 0 dB
            (0.010, 0.001, 10.0),     # P_sig 10x -> 10 dB
            (0.100, 0.001, 20.0),     # P_sig 100x -> 20 dB
            (1.000, 0.001, 30.0),     # P_sig 1000x -> 30 dB
        ]
        for p_sig, p_noise, expected_db in test_cases:
            with self.subTest(p_sig=p_sig, expected_db=expected_db):
                self.assertEqual(hitung_snr_db(p_sig, p_noise), expected_db)

    def test_exception_invalid_inputs(self):
        """Pola Exception Testing: Memastikan input ilegal ditolak."""
        with self.assertRaises(ValueError):
            hitung_snr_db(1.0, 0.0)  # Noise nol harus memicu ValueError
        with self.assertRaises(ValueError):
            hitung_snr_db(-5.0, 0.001)

        with self.assertRaises(ValueError):
            hitung_kapasitas_shannon(-100.0, 10.0)

        with self.assertRaises(ValueError):
            evaluasi_kelayakan_link(1.5)  # BER > 1.0 ilegal

    def test_shannon_capacity(self):
        # 10 MHz dengan SNR linier 3 -> log2(4) = 2 -> 20 Mbps
        cap = hitung_kapasitas_shannon(10_000_000.0, 3.0)
        self.assertEqual(cap, 20_000_000.0)

    def test_evaluasi_ber(self):
        self.assertEqual(evaluasi_kelayakan_link(1e-7), "LAYAK")
        self.assertEqual(evaluasi_kelayakan_link(1e-4), "TIDAK LAYAK")


if __name__ == "__main__":
    print("Menjalankan test suite otomatis...")
    unittest.main()
