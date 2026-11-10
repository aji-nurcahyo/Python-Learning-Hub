# Latihan Mandiri B04 — Model Evaluation & Hyperparameter Tuning

## Latihan 1: Metrik Imbalanced & Cross-Validation
1. Muat `datasets/fraud_alert_sample.csv` lalu bagi menjadi train/test set berstratifikasi (`test_size=0.25`).
2. Jalankan `StratifiedKFold(n_splits=5)` pada data latih untuk menghitung rata-rata serta std dev `roc_auc` dan `f1`.
3. Jelaskan mengapa akurasi mentah kurang mencerminkan kualitas deteksi kasus positif minoritas.

## Latihan 2: GridSearchCV & Threshold Tuning
1. Bungkus `RandomForestClassifier(random_state=42)` dalam `Pipeline` dan lakukan pencarian `GridSearchCV` pada `n_estimators` dan `max_depth`.
2. Evaluasi model terbaik di holdout test set untuk nilai threshold `0.25`, `0.50`, dan `0.75`.

