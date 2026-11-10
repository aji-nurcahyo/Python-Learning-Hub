# Tugas Capstone Track B: Predictive Maintenance & Inference System

## Instruksi Implementasi (`tugas.py`)
1. `add_domain_features(df: pd.DataFrame) -> pd.DataFrame`: tambahkan `load_per_mhz` dan `loss_latency_index` pada `.copy()`.
2. `train_and_select_model(train_df: pd.DataFrame) -> tuple[object, dict, pd.DataFrame]`: bandingkan `DummyClassifier`, `LogisticRegression`, dan `RandomForestClassifier` via `StratifiedKFold` ROC-AUC di `X_train`, lalu evaluasi model terbaik pada holdout `X_test`.
3. `save_model_bundle(model, metrics: dict, out_dir: Path) -> Path`: simpan `maintenance_pipeline.joblib` dan `model_metadata.json`.
4. `score_new_batch(bundle_dir: Path, batch_csv: Path) -> list[dict]`: muat model dari `bundle_dir`, hitung fitur domain batch baru, dan kembalikan daftar prediksi terurut risiko tertinggi.

## Rubrik Penilaian (Total 100 Poin)
- Rekayasa Fitur Domain & Konsistensi Pipeline (25%)
- Seleksi Model & Evaluasi Holdout Anti-Leakage (30%)
- Serialisasi Joblib & Batch Inference Engine (25%)
- Kualitas Arsitektur & Cakupan Pytest (20%)

