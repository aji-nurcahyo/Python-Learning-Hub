# Modul B01: ML Foundations & Scikit-Learn Pipelines

## 1. Paradigma Pemodelan Prediktif yang Disiplin
Dalam Machine Learning (*supervised learning*), tujuan utama kita bukanlah menghafal data pelatihan, melainkan menghasilkan **generalisasi akurat pada data baru** yang belum pernah dilihat model saat pelatihan.

Dua aturan emas sebelum menyentuh algoritma apa pun:
1. Pisahkan data pelatihan dan data pengujian **sejak paling awal**.
2. Seluruh langkah pra-pemrosesan (*imputation*, *scaling*, *encoding*) wajib dikemas di dalam `Pipeline`.

---

## 2. Stratified `train_test_split` & Reprodusibilitas
Ketika label target tidak seimbang (*imbalanced*), pemotongan acak biasa bisa membuat proporsi kelas target timpang antara train dan test set. Parameter `stratify=y` mempertahankan distribusi kelas secara seimbang, sedangkan `random_state=42` menjamin hasil pemotongan identik setiap kali eksperimen dijalankan ulang.

---

## 3. ColumnTransformer untuk Fitur Campuran
Dataset dunia nyata mencampur angka kontinu (misal `tenure_months`, `monthly_spend_k`) dan kategori teks (`contract_type`, `region`). `ColumnTransformer` memungkinkan kita mengarahkan tiap kelompok kolom ke sub-pipeline berbeda tanpa kebocoran data:
- **Numerik:** `SimpleImputer(strategy="median")` diikuti `StandardScaler()`.
- **Kategorikal:** `SimpleImputer(strategy="most_frequent")` diikuti `OneHotEncoder(handle_unknown="ignore")`.

---

## 4. Bahaya Data Leakage & Pentingnya Baseline
**Data Leakage** terjadi saat statistik dari data uji (seperti rata-rata global untuk scaling atau median imputasi) bocor masuk selama proses training. Akibatnya metrik pengujian tampak tinggi palsu, tetapi gagal saat deployment.

Selain itu, selalu jalankan **`DummyClassifier`** (memprediksi kelas mayoritas) terlebih dahulu sebagai tolok ukur bawah (*baseline*): jika model kompleks Anda tidak jauh melampaui akurasi tebak mayoritas, fitur atau data Anda masih perlu dibenahi.

