# Modul E03: Digital Signal Processing with SciPy & FFT

## 1. Teorema Sampling Nyquist & Aliasing
Ketika sinyal analog dicuplik oleh ADC (*Analog-to-Digital Converter*) pada laju $f_s$ (Hz), komponen frekuensi tertinggi yang dapat direpresentasikan tanpa distorsi (**batas Nyquist**) adalah $f_s / 2$. Jika sinyal asli memiliki komponen lebih tinggi dari $f_s / 2$, komponen tersebut akan terlipat menjadi frekuensi palsu (*aliasing*).

---

## 2. Analisis Spektrum dengan `scipy.fft.rfft`
Untuk sinyal bernilai riil (*real-valued telemetry*), gunakan **`scipy.fft.rfft(signal)`** dan **`rfftfreq(N, d=1/fs)`** karena lebih cepat dan hanya menghitung spektrum frekuensi positif tanpa cerminan negatif:

```python
from scipy.fft import rfft, rfftfreq
import numpy as np

freqs = rfftfreq(len(sig), d=1.0 / fs)
mag = (2.0 / len(sig)) * np.abs(rfft(sig))
```

---

## 3. Desain Filter Butterworth Modern (`output="sos"` & `sosfiltfilt`)
Untuk memisahkan sinyal utama (misal $40\text{ Hz}$) dari gangguan frekuensi tinggi ($180\text{ Hz}$):
1. Rancang filter dengan **`scipy.signal.butter(N=4, Wn=cutoff_hz, btype="low", fs=fs, output="sos")`** (`output="sos"` menjamin stabilitas numerik untuk orde berapa pun).
2. Jalankan **`sosfiltfilt(sos, signal)`** — penyaringan dua arah (maju lalu mundur) yang meniadakan pergeseran waktu (*zero-phase distortion*) sekaligus menggandakan ketajaman redaman.

---

## 4. Evaluasi Kinerja Penyaringan dengan SNR (dB)
Kualitas pembersihan sinyal dibandingkan referensi bersih $x_{\text{clean}}$ diukur melalui **Signal-to-Noise Ratio (SNR)** dalam desibel:
$$\text{SNR}_{\text{dB}} = 10 \log_{10} \left( \frac{\sum x_{\text{clean}}^2}{\sum (x_{\text{obs}} - x_{\text{clean}})^2} \right)$$
Peningkatan SNR positif membuktikan filter efektif membuang interferensi tanpa merusak sinyal utama.

