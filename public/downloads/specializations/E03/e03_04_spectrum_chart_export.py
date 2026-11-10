import sys
import tempfile
from pathlib import Path
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import rfft, rfftfreq

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from e03_03_butterworth_lowpass_filter import butter_lowpass_zero_phase

fs = 800.0
t = np.linspace(0.0, 1.0, int(fs), endpoint=False)
rng = np.random.default_rng(42)
clean = 1.5 * np.sin(2 * np.pi * 40.0 * t)
noisy = clean + 0.8 * np.sin(2 * np.pi * 180.0 * t) + rng.normal(0.0, 0.25, len(t))
filtered = butter_lowpass_zero_phase(noisy, fs=fs, cutoff_hz=85.0, order=4)

freqs = rfftfreq(len(t), d=1.0 / fs)
mag_before = (2.0 / len(t)) * np.abs(rfft(noisy))
mag_after = (2.0 / len(t)) * np.abs(rfft(filtered))

fig, axes = plt.subplots(2, 1, figsize=(10, 6.5), dpi=150)
axes[0].plot(t[:120], noisy[:120], alpha=0.5, label="Sinyal Berderau")
axes[0].plot(t[:120], filtered[:120], linewidth=2.0, label="Hasil Butterworth LPF")
axes[0].set_title("Domain Waktu (150 ms Pertama)")
axes[0].set_xlabel("Waktu (detik)")
axes[0].set_ylabel("Amplitudo")
axes[0].legend()

axes[1].plot(freqs, mag_before, alpha=0.55, label="Spektrum Sebelum Filter")
axes[1].plot(freqs, mag_after, linewidth=2.0, label="Spektrum Sesudah Filter")
axes[1].set_xlim(0, 260)
axes[1].set_title("Spektrum Frekuensi (rfft)")
axes[1].set_xlabel("Frekuensi (Hz)")
axes[1].set_ylabel("Magnitudo")
axes[1].legend()

with tempfile.TemporaryDirectory() as td:
    out_png = Path(td) / "e03_spectrum_comparison.png"
    fig.tight_layout()
    fig.savefig(out_png, dpi=150)
    plt.close(fig)
    print("Grafik waktu & spektrum dirender :", out_png.name)
    print("Magnitudo 180 Hz sebelum/sesudah :", round(float(mag_before[180]), 3), "->", round(float(mag_after[180]), 4))

