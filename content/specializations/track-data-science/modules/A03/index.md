# Modul A03: Exploratory Data Analysis (EDA)

## 1. Tujuan Utama EDA Sebelum Pemodelan
**Exploratory Data Analysis (EDA)** adalah fase investigasi sistematis untuk memahami struktur, kecenderungan sentral, penyebaran, anomali, serta hubungan antar variabel sebelum kita membangun visualisasi presentasi maupun model prediktif.

Kesalahan fatal analisis data adalah langsung memakai rata-rata global (`mean`) tanpa mengecek bentuk distribusi atau keberadaan *outlier*.

---

## 2. Distribusi: Mean vs Median, IQR, dan Skewness
- **Mean:** sensitif terhadap nilai ekstrem karena menjumlahkan seluruh besaran angka.
- **Median (Q2 / Persentil ke-50):** nilai tengah setelah data diurutkan; tahan terhadap outlier (*robust*).
- **Interquartile Range (`IQR = Q3 - Q1`):** rentang 50% data di tengah distribusi.
- **Skewness:** ukuran ketidaksimetrisan distribusi. Jika `mean > median` dan `skew > 0`, data menceng ke kanan (*right-skewed*), umum terjadi pada latensi jaringan atau waktu respons web.

---

## 3. Deteksi Outlier secara Kuantitatif
Dua teknik baku dalam EDA Python:
1. **Metode Pagar Tukey (IQR Rule):**
   - Batas bawah: `Q1 - 1.5 * IQR`
   - Batas atas: `Q3 + 1.5 * IQR`
   Tidak mengasumsikan distribusi Normal.
2. **Metode Z-Score:**
   - Mengukur jarak relatif tiap observasi dalam satuan standar deviasi: `z = (x - mean) / std`.
   - Umumnya nilai `|z| > 2.5` atau `3.0` ditandai kandidat anomali pada distribusi simetris.

```python
q1 = s.quantile(0.25)
q3 = s.quantile(0.75)
iqr = q3 - q1
outliers = s[(s < q1 - 1.5 * iqr) | (s > q3 + 1.5 * iqr)]
```

---

## 4. Korelasi Linear vs Monotonik & Segmentasi
- **Korelasi Pearson (`method="pearson"`):** mengukur kekuatan hubungan **linear** antar dua variabel numerik. Rentan terdistorsi outlier.
- **Korelasi Spearman (`method="spearman"`):** mengukur hubungan **monotonik berbasis peringkat (rank)**; tetap stabil meski data melengkung non-linear atau mengandung nilai ekstrem.
- **`pd.crosstab`:** memeriksa hubungan frekuensi antar dua kolom kategorikal (misal `region` vs `sla_status`).

