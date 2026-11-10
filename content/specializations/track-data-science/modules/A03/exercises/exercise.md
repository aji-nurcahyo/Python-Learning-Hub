# Latihan Mandiri A03 — Exploratory Data Analysis

## Latihan 1: Audit Distribusi QoS
1. Muat `datasets/telecom_qos_kpi.csv`.
2. Hitung `mean`, `median`, `Q1`, `Q3`, `IQR`, dan `skew()` untuk kolom `latency_ms` dan `packet_loss_pct`.
3. Jelaskan mengapa kedua metrik tersebut menunjukkan skew positif.

## Latihan 2: Korelasi & Segmentasi
1. Hitung korelasi Pearson dan Spearman antara `latency_ms` dan `packet_loss_pct`.
2. Buat `pd.crosstab(df["technology"], df["sla_status"])`.
3. Identifikasi apakah status `DEGRADED`/`CRITICAL` seluruhnya terjadi pada teknologi 4G.

