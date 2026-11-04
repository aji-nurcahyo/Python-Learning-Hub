# Tugas Mandiri: Telecom Quality Metric Toolkit (Tested Package)
## Chapter 21 — Packages, Environments & Testing

### Deskripsi Tugas
Anda diminta untuk membangun sebuah paket pustaka Python terstandar bernama **`telecom_metrics`** yang modular, terdistribusi dengan berkas `pyproject.toml`, dan dilengkapi dengan suite pengujian otomatis menyeluruh (*test suite*).

Paket pustaka ini berfokus pada kalkulasi kualitas transmisi data jaringan telekomunikasi (Bit Error Rate, Signal-to-Noise Ratio, dan Throughput Shannon-Hartley).

---

### Kriteria Kebutuhan Teknis

1. **Struktur Direktori Proyek**:
   ```text
   telecom_project/
   ├── pyproject.toml
   ├── README.md
   ├── telecom_metrics/
   │   ├── __init__.py
   │   └── analyzer.py
   └── tests/
       ├── __init__.py
       └── test_analyzer.py
   ```

2. **Modul `analyzer.py`**:
   - `hitung_snr_db(signal_power_w: float, noise_power_w: float) -> float`:  
     Formula $\text{SNR (dB)} = 10 \cdot \log_{10}(P_{\text{signal}} / P_{\text{noise}})$.  
     Validasi: Lempar `ValueError` jika $P_{\text{noise}} \le 0$ atau $P_{\text{signal}} \le 0$.
   - `hitung_kapasitas_shannon(bandwidth_hz: float, snr_linier: float) -> float`:  
     Formula $C = B \cdot \log_2(1 + \text{SNR})$.  
     Validasi: Lempar `ValueError` jika $B \le 0$ atau $\text{SNR} < 0$.
   - `evaluasi_kelayakan_link(ber: float) -> str`:  
     Mengembalikan status `"LAYAK"` jika $\text{BER} \le 10^{-6}$, sebaliknya `"TIDAK LAYAK"`. Lempar `ValueError` jika $\text{BER} < 0$ atau $\text{BER} > 1.0$.

3. **Suite Pengujian Otomatis (`test_analyzer.py`)**:
   - Menerapkan **Fixture** (inisialisasi konfigurasi pengujian).
   - Menerapkan **Parameterized Testing** (menguji minimal 4 kasus kombinasi SNR).
   - Menerapkan **Exception Testing** (memverifikasi lemparan `ValueError` pada pembagian noise nol atau input negatif).

---

### Rubrik Penilaian (Total: 100 Poin)

| Kriteria Penilaian | Bobot | Deskripsi Indikator |
| :--- | :---: | :--- |
| **Arsitektur Package & __init__.py** | 25 Poin | Struktur paket memenuhi standar PEP 420/517, ekspor simbol terdefinisi via `__all__`, dan impor modul berjalan mulus. |
| **Fungsionalitas Matematis & Validasi** | 25 Poin | Fungsi SNR, kapasitas Shannon, dan evaluasi BER menghasilkan output matematis presisi dan memvalidasi input salah. |
| **Pola Automated Testing (Fixture & Param)** | 25 Poin | Test suite mengimplementasikan pola fixture untuk data uji dan tabel kasus uji parameterisasi. |
| **Exception Testing** | 15 Poin | Memverifikasi seluruh kondisi boundary dan input ilegal dengan assertion exception (`assertRaises` atau `pytest.raises`). |
| **Konfigurasi pyproject.toml & PEP 8** | 10 Poin | Berkas `pyproject.toml` terkonfigurasi standar PEP 621, penamaan modul bersih, dan type hint lengkap. |

