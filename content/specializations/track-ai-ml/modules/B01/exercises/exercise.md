# Latihan Mandiri B01 — Scikit-Learn Pipelines

## Latihan 1: Stratified Split & ColumnTransformer
1. Muat `datasets/customer_churn_features.csv`.
2. Bagi dataset memakai `train_test_split(..., test_size=0.25, stratify=y, random_state=42)`.
3. Bangun `ColumnTransformer` dengan sub-pipeline `SimpleImputer` + `StandardScaler` untuk fitur numerik dan `OneHotEncoder(handle_unknown="ignore")` untuk kategori.
4. Uji perbandingan akurasi `DummyClassifier` melawan `LogisticRegression`.

