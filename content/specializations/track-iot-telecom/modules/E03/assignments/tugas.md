# Tugas Terstruktur E03: Spectral Analyzer & Digital Denoising Engine

## Instruksi Implementasi (`tugas.py`)
1. `extract_dominant_frequencies(signal: np.ndarray, fs: float, top_k: int = 2) -> list[tuple[float, float]]`: hitung magnitudo spektrum via `rfft` & `rfftfreq` lalu kembalikan `(freq_hz, amplitude)` terbesar.
2. `apply_butter_lowpass(signal: np.ndarray, fs: float, cutoff_hz: float, order: int = 4) -> np.ndarray`: periksa `cutoff_hz < fs / 2.0`, rancang filter `output="sos"`, lalu saring memakai `sosfiltfilt`.
3. `compute_snr_db(clean_ref: np.ndarray, observed: np.ndarray) -> float`: hitung SNR dalam satuan desibel.
4. Uji peningkatan SNR dan penekanan frekuensi interferensi lewat `pytest`.

## Rubrik Penilaian (Total 100 Poin)
- Ketepatan Analisis Spektrum FFT (30%)
- Desain Filter Butterworth Zero-Phase (30%)
- Perhitungan Metrik SNR & Chart Export (20%)
- Unit Testing DSP Deterministik (Pytest) (20%)

