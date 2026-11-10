# Latihan Mandiri E03 — Digital Signal Processing (SciPy & FFT)

## Latihan 1: Analisis Spektrum & Filtering
1. Bangkitkan sinyal uji pada `fs=800` Hz memakai `np.linspace(0, 1.0, 800, endpoint=False)`.
2. Hitung puncak frekuensi dominan menggunakan `scipy.fft.rfft` dan `rfftfreq`.
3. Terapkan `scipy.signal.butter(..., output="sos")` + `sosfiltfilt` dengan frekuensi potong `85 Hz`.
4. Bandingkan nilai SNR (dB) sebelum vs sesudah penyaringan dan jalankan `pytest code/test_e03_dsp.py`.

