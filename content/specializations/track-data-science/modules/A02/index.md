# Modul A02: Data Manipulation with Pandas

## 1. Struktur Data Tabular: `Series` dan `DataFrame`
Jika NumPy unggul pada matriks numerik seragam, analisis bisnis dan teknik sering berhadapan dengan tabel berisi campuran teks, tanggal, kategori, dan angka berlabel kolom. Pandas menyediakan dua struktur data utama:
- **`Series`**: array 1D berindeks beserta metadata nama dan `dtype`.
- **`DataFrame`**: tabel 2D berlabel baris (`index`) dan kolom (`columns`), di mana setiap kolom merupakan sebuah `Series`.

### Aturan Pemilihan Data: `.loc` vs `.iloc`
- `.loc[row_labels, col_labels]`: seleksi berbasis **nama label** (inklusif di kedua ujung slice).
- `.iloc[row_pos, col_pos]`: seleksi berbasis **posisi integer nol-indeks** (eksklusif di batas akhir).

```python
subset = df.loc[df["city"] == "Jakarta", ["order_id", "category", "unit_price"]]
```

---

## 2. Siklus Data Cleaning di Dunia Nyata
Data mentah hampir selalu memiliki empat gangguan klasik:
1. **Spasi & Kapitalisasi Tidak Seragam:** `" electronics "` vs `"ELECTRONICS"`. Gunakan `.str.strip().str.title()`.
2. **Duplikasi Baris:** Rekaman ganda dengan ID transaksi sama. Bersihkan via `drop_duplicates(subset=["order_id"], keep="first")`.
3. **Missing Values (`NaN`):** Periksa dengan `df.isna().sum()`. Pilih imputasi berbasis kelompok (`groupby().transform("median")`) agar tidak mencampur distribusi kategori berbeda.
4. **Tipe Tanggal Mentah:** Konversi string menjadi objek waktu via `pd.to_datetime(..., errors="coerce")`.

---

## 3. Strategi Split-Apply-Combine (`groupby` & `pivot_table`)
`groupby()` memecah tabel menjadi grup logis, menerapkan fungsi agregasi secara independen, lalu menggabungkan hasilnya ke bentuk tabel ringkas:

```python
ringkasan = (
    df.groupby(["city", "category"], as_index=False)
    .agg(total_qty=("quantity", "sum"), avg_price=("unit_price", "mean"))
)
```

Named aggregation (`kolom_hasil=("kolom_asal", "fungsi")`) membuat hasil langsung rapi dengan header satu tingkat (*single-level columns*).

---

## 4. Menggabungkan Tabel (`pd.merge`)
Ketika informasi transaksi terpisah dari tabel master wilayah atau tarif pajak, gunakan `pd.merge(left, right, on="kunci", how="left")`:
- `inner`: hanya kunci yang muncul di kedua tabel.
- `left`: mempertahankan seluruh baris transaksi meskipun referensi master belum terdaftar (memudahkan audit kunci yatim / *orphan keys*).

