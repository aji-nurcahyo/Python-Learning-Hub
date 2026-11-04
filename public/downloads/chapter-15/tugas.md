# Tugas Praktik Chapter 15: Network Metric Search & Ranking Engine

## Deskripsi Tugas
Dalam pusat kendali operasi jaringan telekomunikasi (*Network Operation Center* / NOC), data kinerja ratusan stasiun pemancar (BTS) dan rute transmisi dicatat secara berkala. Sistem membutuhkan algoritma pencarian cepat untuk melacak node tertentu serta mekanisme pemeringkatan (*ranking*) multi-kriteria untuk mengidentifikasi perangkat yang mengalami degradasi performa.

Anda diminta melengkapi pustaka algoritma mandiri pada berkas `tugas_15.py`:
1. **Algoritma Pencarian:** Mengimplementasikan Linear Search untuk pencarian nama/ID umum, dan Binary Search teroptimasi untuk pencarian alamat IP atau kanal frekuensi terurut.
2. **Algoritma Pengurutan Manual:** Mengimplementasikan Bubble Sort, Selection Sort, dan Insertion Sort murni secara mandiri tanpa menggunakan fungsi bawaan `sorted()`.
3. **Pemeringkatan Lanjut (Timsort):** Menerapkan fungsi bawaan Python `sorted()` dengan *custom lambda key* multi-kriteria untuk menghasilkan pemeringkatan perangkat yang stabil (*stable ranking*).

---

## Petunjuk Pengerjaan

1. Buka berkas starter code `tugas_15.py`.
2. Lengkapi fungsi `cari_linier_node(daftar_node, target_id)`.
3. Lengkapi fungsi `cari_biner_frekuensi(daftar_frekuensi, target_khz)`.
4. Lengkapi fungsi pengurutan manual `urut_bubble(data)`, `urut_selection(data)`, dan `urut_insertion(data)`.
5. Lengkapi fungsi pemeringkatan `peringkatkan_performa_bts(daftar_bts)` berdasarkan kriteria:
   - Terurut 1: Latensi terendah (ascending).
   - Terurut 2: Daya terima (RSRP) terkuat (descending).
6. Uji kebenaran program pada kasus uji ekstrem: list kosong, satu elemen, duplikat, dan nilai negatif.

---

## Format Laporan Konsol Terminal

```text
======================================================================
         NETWORK METRIC SEARCH & RANKING ENGINE (ENGINE 15)
======================================================================
1. Pengujian Algoritma Pencarian:
   - Linear Search ID 'BTS-04' : Ditemukan pada indeks ke-3
   - Binary Search Frekuensi 2100 kHz : Ditemukan (4 perbandingan)
   - Binary Search Frekuensi 9999 kHz : Tidak Ditemukan (Hasil: None)

2. Pengujian Algoritma Pengurutan Klasik (Sampel Daya dBm):
   Data Awal      : [-85.0, -110.0, -72.5, -95.0, -60.0]
   Bubble Sort    : [-110.0, -95.0, -85.0, -72.5, -60.0]
   Selection Sort : [-110.0, -95.0, -85.0, -72.5, -60.0]
   Insertion Sort : [-110.0, -95.0, -85.0, -72.5, -60.0]

3. Pemeringkatan Performa Multi-Kriteria (Timsort Stabil):
   Rank 1: BTS-Utara   | Latensi:  4.2 ms | RSRP: -65.0 dBm
   Rank 2: BTS-Pusat   | Latensi:  8.5 ms | RSRP: -72.0 dBm
   Rank 3: BTS-Selatan | Latensi: 14.0 ms | RSRP: -88.0 dBm
   Semua algoritma pencarian dan pengurutan diverifikasi valid.
======================================================================
```

---

## Rubrik Penilaian (Total Bobot: 100 Poin)

| Kriteria Penilaian | Bobot | Deskripsi Capaian Kualitas |
|:---|:---:|:---|
| **1. Kebenaran Linear & Binary Search** | 25 Poin | Menerapkan algoritma pencarian secara presisi, menghormati prasyarat list terurut pada binary search, dan menangani target nihil. |
| **2. Implementasi Bubble & Selection Sort** | 25 Poin | Algoritma manual Bubble Sort (dengan deteksi early stop) dan Selection Sort berjalan tanpa bantuan fungsi bawaan. |
| **3. Implementasi Insertion Sort & Stabilitas** | 25 Poin | Algoritma Insertion Sort menggeser prefix dengan tepat dan memahami konsep pengurutan stabil. |
| **4. Pemeringkatan Multi-Kriteria Timsort & Edge Cases** | 25 Poin | Menerapkan custom lambda key multi-atribut, menangani kasus batas (kosong, 1 elemen, duplikat, negatif), dan format PEP 8 rapi. |
