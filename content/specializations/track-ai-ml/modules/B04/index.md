# Modul B04: Model Evaluation, Cross-Validation & Hyperparameter Tuning

## 1. Mengapa Accuracy Saja Menipu pada Data Imbalanced?
Jika hanya 10% transaksi merupakan anomali (`fraud_flag=1`), model malas yang selalu menebak `0` tetap meraih akurasi 90%, padahal gagal 100% menangkap insiden! Karena itu gunakan metrik berbasis **Confusion Matrix**:
- **Precision (`TP / (TP + FP)`):** dari semua yang diprediksi anomali, berapa persen yang benar-benar anomali?
- **Recall (`TP / (TP + FN)`):** dari semua kejadian anomali nyata, berapa persen yang berhasil tertangkap?
- **F1-Score:** rata-rata harmonik antara Precision dan Recall.
- **ROC-AUC:** kemampuan model memberi skor probabilitas lebih tinggi ke kasus positif dibanding negatif di seluruh ambang keputusan.

---

## 2. Validasi Stabil dengan `StratifiedKFold`
Satu kali split berisiko menghasilkan nilai bagus atau jelek secara kebetulan pada dataset kecil. **`StratifiedKFold(n_splits=5)`** membagi data latih menjadi 5 lipatan seimbang proporsi kelasnya, lalu melatih dan memvalidasi 5 kali bergantian untuk mendapatkan nilai **mean ± std dev**.

---

## 3. GridSearchCV di Atas Pipeline Lengkap
Gunakan **`GridSearchCV`** di atas objek `Pipeline` agar `StandardScaler` dihitung ulang bersih di setiap lipatan CV (*zero leakage*):

```python
param_grid = {
    "rf__n_estimators": [30, 60],
    "rf__max_depth": [2, 4, None],
}
search = GridSearchCV(pipe, param_grid, cv=StratifiedKFold(4), scoring="roc_auc")
```

Holdout *test set* tetap tidak disentuh selama proses GridSearch sampai evaluasi akhir dijalankan pada `search.best_estimator_`.

---

## 4. Penyetelan Decision Threshold
Secara default `.predict()` memakai ambang probabilitas `0.50`. Dengan memanfaatkan `.predict_proba(X)[:, 1] >= threshold`, kita dapat menurunkan threshold (misal `0.30`) untuk menaikkan **Recall** saat risiko melewatkan insiden tinggi, atau menaikkannya saat biaya investigasi palsu mahal.

