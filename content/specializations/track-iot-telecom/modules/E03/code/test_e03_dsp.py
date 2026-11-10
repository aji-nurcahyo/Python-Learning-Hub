import sys
from pathlib import Path
import numpy as np

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from e03_02_fft_frequency_spectrum import analyze_top_frequencies
from e03_03_butterworth_lowpass_filter import butter_lowpass_zero_phase, compute_snr_db


def test_fft_identifies_expected_signal_and_interference_peaks() -> None:
    fs = 800.0
    t = np.linspace(0.0, 1.0, int(fs), endpoint=False)
    sig = 1.5 * np.sin(2 * np.pi * 40.0 * t) + 0.8 * np.sin(2 * np.pi * 180.0 * t)
    peaks = analyze_top_frequencies(sig, fs, top_k=2)
    detected_freqs = {p[0] for p in peaks}
    assert detected_freqs == {40.0, 180.0}


def test_butterworth_improves_snr_significantly() -> None:
    fs = 800.0
    t = np.linspace(0.0, 1.0, int(fs), endpoint=False)
    rng = np.random.default_rng(42)
    clean = 1.5 * np.sin(2 * np.pi * 40.0 * t)
    noisy = clean + 0.8 * np.sin(2 * np.pi * 180.0 * t) + rng.normal(0.0, 0.25, len(t))
    filtered = butter_lowpass_zero_phase(noisy, fs=fs, cutoff_hz=85.0, order=4)
    assert compute_snr_db(clean, filtered) - compute_snr_db(clean, noisy) > 10.0

