import numpy as np
from scipy.fft import rfft, rfftfreq
from scipy.signal import butter, sosfiltfilt


def analyze_and_denoise_vibration(fs: float = 600.0, cutoff_hz: float = 75.0) -> dict:
    t = np.linspace(0.0, 1.0, int(fs), endpoint=False)
    rng = np.random.default_rng(42)

    clean = 1.2 * np.sin(2 * np.pi * 25.0 * t)
    noise_150hz = 0.75 * np.sin(2 * np.pi * 150.0 * t) + rng.normal(0.0, 0.2, len(t))
    raw = clean + noise_150hz

    sos = butter(4, cutoff_hz, btype="low", fs=fs, output="sos")
    denoised = sosfiltfilt(sos, raw)

    snr_raw = 10.0 * np.log10(np.sum(clean**2) / np.sum((raw - clean) ** 2))
    snr_clean = 10.0 * np.log10(np.sum(clean**2) / np.sum((denoised - clean) ** 2))

    freqs = rfftfreq(len(t), d=1.0 / fs)
    mag_after = (2.0 / len(t)) * np.abs(rfft(denoised))
    dom_freq = float(freqs[int(np.argmax(mag_after))])

    return {
        "t": t,
        "raw": raw,
        "denoised": denoised,
        "dominant_hz_after": round(dom_freq, 2),
        "snr_before_db": round(float(snr_raw), 2),
        "snr_after_db": round(float(snr_clean), 2),
        "snr_gain_db": round(float(snr_clean - snr_raw), 2),
    }


if __name__ == "__main__":
    res = analyze_and_denoise_vibration()
    print("Frekuensi dominan pasca filter:", res["dominant_hz_after"], "Hz")
    print("SNR sebelum -> sesudah        :", res["snr_before_db"], "dB ->", res["snr_after_db"], "dB")
    print("Perbaikan SNR DSP             : +", res["snr_gain_db"], "dB")

