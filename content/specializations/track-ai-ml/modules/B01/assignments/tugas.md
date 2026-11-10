# Tugas Terstruktur B01: Builder Pipeline Churn Prediction

## Instruksi Implementasi (`tugas.py`)
1. `split_features_target(df, target_col, test_size=0.25, random_state=42)`: pisahkan kolom `customer_id` dan target, lalu kembalikan `X_train, X_test, y_train, y_test` berstratifikasi.
2. `build_preprocessing_pipeline(numeric_cols, categorical_cols) -> ColumnTransformer`: gabungkan `SimpleImputer(strategy="median")` + `StandardScaler()` untuk fitur numerik serta `SimpleImputer(strategy="most_frequent")` + `OneHotEncoder(handle_unknown="ignore")` untuk kategori.
3. `train_and_compare_baseline(...) -> dict[str, float]`: latih `DummyClassifier` dan `Pipeline([("prep", ...), ("clf", LogisticRegression())])` lalu kembalikan akurasi masing-masing pada test set.

## Rubrik Penilaian (100 Poin)
- Stratified Split & Reprodusibilitas Seed (25%)
- Arsitektur ColumnTransformer & Pipeline (35%)
- Perbandingan Baseline yang Jujur (20%)
- Unit Testing & Dokumentasi (20%)

