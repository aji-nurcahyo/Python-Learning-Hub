# Tugas Praktik Chapter 16: Algorithm Performance Comparator

## Deskripsi Tugas
Dalam perancangan sistem backend dan pengolahan data telekomunikasi berskala besar, keputusan memilih algoritma tidak boleh hanya didasarkan pada perkiraan (*intuisi*), melainkan harus didukung oleh **analisis teoritis kompleksitas asimtotik (Big-O)** dan **pengujian empiris terukur (benchmarking)**.

Anda diminta merancang program laboratorium komparasi kinerja bernama `tugas_16.py` yang membandingkan efisiensi algoritma pencarian dan deteksi anomali pada berbagai skala ukuran dataset:
1. **Analisis Teoritis Big-O:** Fungsi kalkulasi estimasi operasi asimtotik untuk $O(1), O(\log n), O(n), O(n \log n), O(n^2)$.
2. **Empirical Benchmarker:** Mengukur waktu eksekusi presisi tinggi menggunakan `time.perf_counter()` dengan rata-rata repetisi berganda untuk meminimalkan deviasi beban sistem operasi.
3. **Penyelidikan Space-Time Tradeoff:** Membuktikan reduksi waktu eksekusi dari algoritma kuadratik $O(n^2)$ menjadi linier $O(n)$ dengan memanfaatkan memori hash set.
4. **Verifikasi Kebenaran Kasus Batas:** Menjamin bahwa algoritma yang cepat tetap menghasilkan keluaran yang 100% benar pada kondisi data kosong, nilai negatif, dan data duplikat.

---

## Petunjuk Pengerjaan

1. Buka berkas starter code `tugas_16.py`.
2. Lengkapi fungsi `estimasi_kompleksitas_teoritis(n)`.
3. Lengkapi fungsi `ukur_latensi_rata_rata(fungsi, *args, repetisi=5)`.
4. Lengkapi pengujian komparasi `komparasi_linear_vs_binary(skala_n, target)`.
5. Lengkapi pengujian komparasi `komparasi_duplikasi(data)`.
6. Pastikan laporan konsol menyajikan tabel perbandingan yang rapi, transparan, dan edukatif.

---

## Format Laporan Konsol Terminal

```text
======================================================================
         ALGORITHM PERFORMANCE COMPARATOR LAB (ENGINE 16)
======================================================================
1. Analisis Teoritis Pertumbuhan Asimtotik (Big-O):
   N = 10,000 Elemen:
   - O(1) konstan       : 1 operasi
   - O(log n) biner     : 14 operasi
   - O(n) linier        : 10,000 operasi
   - O(n log n) timsort : 132,877 operasi
   - O(n^2) kuadratik   : 100,000,000 operasi

2. Pengujian Empiris Pencarian (N = 50,000 Elemen, 5 Repetisi):
   - Linear Search O(n) : 0.8420 ms
   - Binary Search O(log n) : 0.0035 ms (Terurut)
   -> Binary Search 240.5x lebih cepat dibanding Linear Search!

3. Pengujian Empiris Space-Time Tradeoff (N = 2,000 Elemen):
   - Deteksi Duplikat Brute Force O(n^2) : 2.4510 ms (Ruang: O(1))
   - Deteksi Duplikat Hash Set O(n)     : 0.0520 ms (Ruang: O(n))
   -> Hash Set 47.1x lebih cepat dengan mengorbankan memori set!

4. Verifikasi Kasus Batas (Edge Cases):
   - Input List Kosong [] : PASS (Mengembalikan None aman)
   - Input Negatif & Nol  : PASS (Validasi tepat)
   Semua metrik empiris dan teoritis berhasil diverifikasi.
======================================================================
```

---

## Rubrik Penilaian (Total Bobot: 100 Poin)

| Kriteria Penilaian | Bobot | Deskripsi Capaian Kualitas |
|:---|:---:|:---|
| **1. Ketepatan Analisis Teoritis Big-O** | 25 Poin | Perhitungan formula $O(1), O(\log n), O(n), O(n \log n), O(n^2)$ akurat dan menghormati kasus batas numerik. |
| **2. Metodologi Benchmarking Empiris yang Adil** | 25 Poin | Menggunakan `time.perf_counter()`, memisahkan setup phase dari search phase, dan menerapkan multi-repetition averaging. |
| **3. Demonstrasi Space-Time Tradeoff** | 25 Poin | Mampu mengimplementasikan komparasi Brute Force $O(n^2)$ vs Hash Set $O(n)$ dengan hasil terukur. |
| **4. Uji Kebenaran Kasus Batas & Kerapian Kode** | 25 Poin | Menangani list kosong, angka negatif, data duplikat tanpa error, menyertakan type hints lengkap, dan format tabel rapi. |

