# Latihan Mandiri A02 — Data Manipulation with Pandas

## Latihan 1: Data Cleaning Transaksi
1. Baca berkas `datasets/retail_transactions_raw.csv` memakai `pd.read_csv`.
2. Hitung berapa nilai `NaN` yang muncul di setiap kolom dengan `.isna().sum()`.
3. Hapus baris duplikat berdasarkan kolom `order_id`.
4. Bersihkan spasi berlebih dan seragamkan huruf kapital kolom `city` dan `category`.

## Latihan 2: Agregasi & Enrichment
1. Isi `quantity` yang kosong dengan `1.0` dan `unit_price` kosong dengan median tiap kategori.
2. Hitung kolom baru `revenue = quantity * unit_price`.
3. Buat ringkasan total pesanan dan total omzet per kota serta tampilkan kota dengan omzet tertinggi.

