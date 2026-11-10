# Modul A04: Data Visualization with Matplotlib & Seaborn

## 1. Memahami Object-Oriented API Matplotlib
Matplotlib memiliki dua antarmuka utama: gaya global (`pyplot` / `plt.plot`) dan **Object-Oriented API** (`fig, ax = plt.subplots()`). Untuk laporan analitik terstruktur dan multi-panel dashboard, selalu gunakan Object-Oriented API karena:
- **`Figure` (`fig`):** kanvas utama yang menampung satu atau banyak panel grafik serta mengatur ukuran (`figsize`) dan ekspor (`savefig`).
- **`Axes` (`ax`):** area plot individual yang mengatur sumbu, skala, ticks, legenda, dan garis batas data.

```python
fig, ax = plt.subplots(figsize=(8, 4.5), dpi=150)
ax.bar(x, y, color="#2563eb")
ax.set_title("Rata-rata Latensi per Wilayah")
ax.set_ylabel("Latensi (ms)")
fig.savefig("out.png", bbox_inches="tight")
plt.close(fig)
```

---

## 2. Memilih Visualisasi Statistik di Seaborn
Seaborn bekerja mulus di atas `DataFrame` Pandas dan mewarisi kendali `ax=` dari Matplotlib:
- **Distribusi 1 Variabel:** `sns.histplot(data=df, x="latency_ms", kde=True, ax=ax)` menampilkan histogram plus kurva kepadatan.
- **Perbandingan Antar Kategori:** `sns.boxplot(...)` menunjukkan Q1, median, Q3, dan titik outlier secara padat tanpa menyembunyikan sebaran.
- **Hubungan 2 Numerik + Segmen:** `sns.scatterplot(..., x="traffic_gbps", y="latency_ms", hue="technology")`.
- **Matriks Korelasi:** `sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0)`.

---

## 3. Prinsip Desain Grafik Bebas Chartjunk
- Berikan judul berorientasi wawasan, **bukan sekadar nama variabel**.
- Sertakan **satuan ukur** pada setiap label sumbu (misal `Latensi (ms)`, `Trafik (Gbps)`).
- Kurangi garis tepi berlebih dengan `ax.spines["top"].set_visible(False)` dan `ax.spines["right"].set_visible(False)`.
- Gunakan palet ramah buta warna (`"colorblind"`, `viridis`, atau palet divergen terpusat di 0 untuk korelasi).
- Selalu panggil `plt.close(fig)` sesudah menyimpan berkas agar RAM tidak bocor saat memproduksi banyak laporan otomatis.

