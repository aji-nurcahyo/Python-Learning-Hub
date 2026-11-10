# Tugas Terstruktur B04: Cross-Validation & Hyperparameter Tuning Engine

## Instruksi Implementasi (`tugas.py`)
1. `evaluate_with_cv(pipeline, X, y, n_splits=5) -> dict[str, float]`: gunakan `StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)` dan kembalikan `{"mean_roc_auc": ..., "std_roc_auc": ...}`.
2. `run_grid_search(X_train, y_train) -> GridSearchCV`: buat `Pipeline([("rf", RandomForestClassifier(random_state=42))])`, jalankan `GridSearchCV` dengan `scoring="roc_auc"` dan kembalikan objek `search` terlatih.
3. `threshold_tradeoff_table(y_true, y_prob, thresholds) -> pd.DataFrame`: susun tabel evaluasi kolom `threshold`, `precision`, `recall`, `f1` untuk setiap ambang batas.

## Rubrik Penilaian (Total 100 Poin)
- Stratified Cross-Validation & Bebas Leakage (30%)
- Implementasi GridSearchCV & Holdout Eval (30%)
- Threshold Tuning & Metrik Imbalanced (20%)
- Unit Testing & Kebersihan Kode (20%)

