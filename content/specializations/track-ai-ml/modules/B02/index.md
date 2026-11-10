# Modul B02: Supervised Learning — Regression & Classification

## 1. Regresi: Linear Regression vs Ridge Regularization
Ketika target bernilai numerik kontinu (misal `throughput_mbps`), algoritma **Linear Regression** mencari kombinasi bobot linear yang meminimalkan *Mean Squared Error (MSE)*.

Namun ketika fitur saling berkorelasi (*multicollinearity*), bobot koefisien linear bisa meledak ekstrem. **Ridge Regression** menambahkan penalti L2 (`alpha * sum(w^2)`) untuk menstabilkan koefisien dan mengurangi risiko *overfitting*.

### Metrik Evaluasi Regresi Wajib
- **MAE (Mean Absolute Error):** rata-rata galat absolut dalam satuan target asli (mudah dipahami bisnis).
- **RMSE (Root Mean Squared Error):** menghukum prediksi yang meleset besar karena dikuadratkan terlebih dahulu.
- **$R^2$ Score:** proporsi varians target yang berhasil dijelaskan oleh model (mendekati `1.0` makin baik, `0.0` setara tebak rata-rata).

---

## 2. Klasifikasi: Logistic Regression
Meskipun bernama "Regression", **Logistic Regression** memodelkan probabilitas keanggotaan kelas biner ($0 \dots 1$) melalui fungsi sigmoid.
- `.predict(X)`: menghasilkan label kelas biner (`0` atau `1`) dengan ambang default `0.5`.
- `.predict_proba(X)[:, 1]`: mengembalikan probabilitas kontinu risiko kongesti — sangat berguna untuk pemeringkatan prioritas eskalasi.

---

## 3. Model Berbasis Pohon: Decision Tree & Random Forest
- **Decision Tree:** membagi ruang fitur secara rekursif lewat aturan *if-else* yang paling memurnikan target (Gini / Entropy). Mudah divisualisasikan, namun satu pohon terlalu dalam rentan *overfitting* terhadap noise data latih.
- **Random Forest:** melatih puluhan hingga ratusan *Decision Tree* di atas *bootstrap sample* acak dan memilih kandidat fitur acak di setiap pemisahan simpul (*split*). Hasil akhirnya berupa voting mayoritas yang stabil sekaligus menyediakan skor `.feature_importances_`.

