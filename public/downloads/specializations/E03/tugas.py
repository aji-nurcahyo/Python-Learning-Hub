"""Starter code Tugas E03: Spectral Analyzer & Digital Denoising Engine."""

from __future__ import annotations

import numpy as np


def extract_dominant_frequencies(signal: np.ndarray, fs: float, top_k: int = 2) -> list[tuple[float, float]]:
    """Mengekstrak top-k frekuensi dominan dan amplitudonya memakai scipy.fft.rfft."""
    # TODO: Gunakan rfft, rfftfreq, dan normalisasi magnitudo (2.0 / len(signal))
    raise NotImplementedError("Implementasikan extract_dominant_frequencies")


def apply_butter_lowpass(signal: np.ndarray, fs: float, cutoff_hz: float, order: int = 4) -> np.ndarray:
    """Merancang low-pass Butterworth SOS dan menyaring sinyal tanpa distorsi fasa."""
    # TODO: Validasi Nyquist (cutoff_hz < fs / 2), gunakan butter(..., output='sos') dan sosfiltfilt
    raise NotImplementedError("Implementasikan apply_butter_lowpass")


def compute_snr_db(clean_ref: np.ndarray, observed: np.ndarray) -> float:
    """Menghitung Signal-to-Noise Ratio (dB)."""
    # TODO: 10 * log10(sum(clean^2) / sum((observed - clean)^2))
    raise NotImplementedError("Implementasikan compute_snr_db")


if __name__ == "__main__":
    print("Starter E03 siap diuji memakai NumPy, SciPy, dan pytest.")

