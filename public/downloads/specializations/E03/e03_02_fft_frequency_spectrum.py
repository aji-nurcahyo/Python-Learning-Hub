import numpy as np
from scipy.fft import rfft, rfftfreq


def analyze_top_frequencies(signal: np.ndarray, fs: float, top_k: int = 3) -> list[tuple[float, float]]:
    n = len(signal)
    freqs = rfftfreq(n, d=1.0 / fs)
    amps = (2.0 / n) * np.abs(rfft(signal))
    amps[0] /= 2.0  # Koreksi komponen DC
    top_indices = np.argsort(amps)[::-1][:top_k]
    return [(round(float(freqs[i]), 2), round(float(amps[i]), 3)) for i in top_indices]


if __name__ == "__main__":
    fs = 800.0
    t = np.linspace(0.0, 1.0, int(fs), endpoint=False)
    rng = np.random.default_rng(42)
    sig = 1.5 * np.sin(2 * np.pi * 40.0 * t) + 0.8 * np.sin(2 * np.pi * 180.0 * t) + rng.normal(0.0, 0.2, len(t))

    peaks = analyze_top_frequencies(sig, fs, top_k=3)
    print("Puncak Spektrum Terdeteksi (Hz, Amplitudo):")
    for freq_hz, amp in peaks:
        print(f" - {freq_hz:6.2f} Hz -> amplitudo ~ {amp:.3f}")

