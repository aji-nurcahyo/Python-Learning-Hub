"""Starter code Tugas E04: Drive-Test RF Quality Auditor & Blindspot Locator."""

from __future__ import annotations

from pathlib import Path
import pandas as pd


def classify_rsrp(rsrp_dbm: float) -> str:
    """Mengklasifikasikan kekuatan RSRP (dBm) menjadi Excellent, Good, Mid-Cell, atau Cell-Edge."""
    # TODO: Implementasikan klasifikasi berdasarkan ambang -80, -90, dan -105 dBm
    raise NotImplementedError("Implementasikan classify_rsrp")


def diagnose_rf_issue(rsrp_dbm: float, sinr_db: float) -> str:
    """Membedakan COVERAGE_BLINDSPOT, HIGH_INTERFERENCE, CRITICAL_EDGE, dan HEALTHY."""
    # TODO: Terapkan kombinasi ambang batas RSRP dan SINR
    raise NotImplementedError("Implementasikan diagnose_rf_issue")


def compute_fspl_db(distance_km: float, freq_mhz: float) -> float:
    """Menghitung Free-Space Path Loss (dB) dengan validasi jarak & frekuensi positif."""
    # TODO: Gunakan np.log10 dan validasi input > 0
    raise NotImplementedError("Implementasikan compute_fspl_db")


if __name__ == "__main__":
    csv_path = Path(__file__).resolve().parent.parent / "datasets" / "drive_test_lte_measurements.csv"
    print(f"Dataset drive test E04 siap dimuat dari: {csv_path}")

