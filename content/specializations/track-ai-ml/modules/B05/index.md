# Modul B05 (Capstone): Predictive Analytics Application

## 1. Siklus Lengkap Sistem ML Siap Produksi
Pada modul capstone Track B ini, seluruh fondasi `B01`–`B04` dirakit menjadi aplikasi prediktif terpadu:
1. **Feature Engineering Konsisten:** transformasi domain seperti `load_per_mhz` dan `loss_latency_index` dibungkus dalam helper murni (atau `FunctionTransformer`) sehingga dijalankan identik saat pelatihan dan inferensi.
2. **Pemilihan Model Berbasis CV & Baseline:** kandidat (`DummyClassifier`, `LogisticRegression`, `RandomForestClassifier`) dinilai via `StratifiedKFold` ROC-AUC di `X_train`, lalu model terbaik diuji final pada holdout `X_test`.
3. **Model Persistence dengan `joblib`:** menyimpan seluruh `Pipeline` (imputer, scaler, dan classifier sekaligus) ke file `.joblib` beserta `model_metadata.json` berisi daftar fitur, versi, dan skor holdout.
4. **Batch Inference Engine:** memuat model tersimpan, menghitung `failure_probability`, dan menerbitkan daftar prioritas pemeliharaan preventif.

---

## 2. Mengapa Training-Serving Parity Krusial?
Banyak kegagalan ML nyata terjadi bukan karena algoritma kurang canggih, melainkan **training-serving skew**: urutan kolom berubah, rumus fitur sedikit berbeda, atau parameter scaler terlewat saat model dideploy. Membungkus seluruh langkah transformasi ke dalam satu `Pipeline` plus validasi unit test *roundtrip* via `joblib` menutup celah tersebut sepenuhnya.

