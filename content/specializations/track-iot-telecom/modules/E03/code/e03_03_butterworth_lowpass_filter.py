import numpy as np
from scipy.signal import butter, sosfiltfilt


def compute_snr_db(clean: np.ndarray, observed: np.ndarray) -> float:
    signal_power = float(np.sum(clean**2))
    noise_power = float(np.sum((observed - clean) ** 2))
    return 10.0 * float(np.log10(signal_power / max(noise_power, 1e-12)))


def butter_lowpass_zero_phase(signal: np.ndarray, fs: float, cutoff_hz: float, order: int = 4) -> np.ndarray:
    if cutoff_hz >= fs / 2.0:
        raise ValueError("Cutoff harus di bawah frekuensi Nyquist (fs / 2).")
    sos = butter(order, cutoff_hz, btype="low", fs=fs, output="sos")
    return sosfiltfilt(sos, signal)


if __name__ == "__main__":
    fs = 800.0
    t = np.linspace(0.0, 1.0, int(fs), endpoint=False)
    rng = np.random.default_rng(42)

    clean = 1.5 * np.sin(2 * np.pi * 40.0 * t)
    noisy = clean + 0.8 * np.sin(2 * np.pi * 180.0 * t) + rng.normal(0.0, 0.25, len(t))
    filtered = butter_lowpass_zero_phase(noisy, fs=fs, cutoff_hz=85.0, order=4)

    snr_before = compute_snr_db(clean, noisy)
    snr_after = compute_snr_db(clean, filtered)
    print(f"SNR sebelum filtering : {snr_before:.2f} dB")
    print(f"SNR sesudah filtering : {snr_after:.2f} dB")
    print(f"Perbaikan SNR         : +{snr_after - snr_before:.2f} dB")

