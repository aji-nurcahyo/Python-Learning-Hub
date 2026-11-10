# Tugas Terstruktur B02: Benchmark Supervised Learning

## Instruksi Implementasi (`tugas.py`)
1. `evaluate_regressors(df: pd.DataFrame) -> pd.DataFrame`: bandingkan `DummyRegressor`, `LinearRegression`, dan `Ridge(alpha=1.0)` dengan metrik `mae`, `rmse`, `r2` pada test set terpisah.
2. `evaluate_classifiers(df: pd.DataFrame) -> pd.DataFrame`: bandingkan `DummyClassifier`, `LogisticRegression`, dan `RandomForestClassifier` dengan `accuracy` serta `f1_score`.
3. `top_feature_importances(df: pd.DataFrame) -> list[tuple[str, float]]`: latih `RandomForestClassifier(n_estimators=60, random_state=42)` pada data latih lalu urutkan skor pentingnya fitur secara menurun.

## Rubrik Penilaian (Total 100 Poin)
- Implementasi Pipeline Regresi & Metrik (30%)
- Implementasi Klasifikasi & Probabilitas (25%)
- Komparasi Baseline & Interpretasi Fitur (25%)
- Unit Testing & Kebersihan Kode (20%)

