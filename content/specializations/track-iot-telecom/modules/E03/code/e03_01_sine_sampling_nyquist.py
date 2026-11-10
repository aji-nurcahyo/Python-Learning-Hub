import numpy as np

fs = 800.0
duration_s = 1.0
n_samples = int(fs * duration_s)
t = np.linspace(0.0, duration_s, n_samples, endpoint=False)

rng = np.random.default_rng(42)
clean_signal = 1.5 * np.sin(2.0 * np.pi * 40.0 * t)
interference = 0.8 * np.sin(2.0 * np.pi * 180.0 * t)
gaussian_noise = rng.normal(0.0, 0.25, size=n_samples)
observed = clean_signal + interference + gaussian_noise

print("Frekuensi sampling (fs) :", fs, "Hz | Nyquist limit:", fs / 2.0, "Hz")
print("Jumlah sampel (N)       :", n_samples)
print("RMS sinyal bersih       :", round(float(np.sqrt(np.mean(clean_signal**2))), 4))
print("RMS sinyal teramati     :", round(float(np.sqrt(np.mean(observed**2))), 4))

