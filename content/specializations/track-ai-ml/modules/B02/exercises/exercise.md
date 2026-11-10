# Latihan Mandiri B02 — Regression & Classification

## Latihan 1: Regresi Throughput Menara
1. Muat `datasets/network_capacity_metrics.csv`.
2. Prediksi kolom `throughput_mbps` memakai `Pipeline([StandardScaler(), Ridge(alpha=1.0)])`.
3. Hitung nilai `MAE`, `RMSE`, dan `R2` di atas test set (`test_size=0.25`, `random_state=42`).

## Latihan 2: Klasifikasi Risiko Kongesti
1. Prediksi `congestion_risk` dengan `LogisticRegression` serta `RandomForestClassifier`.
2. Cetak `.predict_proba(X_test)[:, 1]` dan bandingkan fitur terpenting berdasarkan `.feature_importances_`.

