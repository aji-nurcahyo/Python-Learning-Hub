# Tugas Terstruktur A02: Pipeline Pembersihan & Agregasi Penjualan

## Deskripsi Masalah
Anda menerima file CSV transaksi harian dengan berbagai masalah kualitas data: kapitalisasi acak, spasi tersembunyi, baris ganda, serta nilai `quantity` dan `unit_price` yang hilang.

## Instruksi Implementasi (`tugas.py`)
1. `clean_transactions(df: pd.DataFrame) -> pd.DataFrame`:
   - Bekerjalah pada `.copy()` agar DataFrame asli tidak termutasi.
   - Rapikan string `city` dan `category` (`strip()` + `title()`).
   - Hapus duplikasi `order_id` (`keep="first"`).
   - Parsing `order_date` ke `datetime64`.
   - Isi missing `quantity` dengan `1.0` dan missing `unit_price` menggunakan median kategori terkait.
   - Tambahkan kolom `revenue = quantity * unit_price`.
2. `summarize_by_city(df_clean: pd.DataFrame) -> pd.DataFrame`:
   - Kelompokkan berdasarkan `city` (`as_index=False`) untuk menghasilkan `total_orders`, `total_qty`, dan `total_revenue`, diurutkan menurun berdasarkan `total_revenue`.

## Rubrik Penilaian (Total 100 Poin)
- Kebenaran Data Cleaning & Deduplikasi (30%)
- Strategi Imputasi Missing Values (25%)
- Agregasi GroupBy & Time-Series (25%)
- Unit Testing & Dokumentasi (20%)

