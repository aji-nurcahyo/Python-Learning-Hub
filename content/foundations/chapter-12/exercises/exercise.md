# Latihan Mandiri & Tantangan Ekstensi — Chapter 12: Foundations Capstone Project

Gunakan latihan berikut untuk memperdalam dan memperluas arsitektur aplikasi **Student Data Management System** Anda dengan fitur-fitur analitik dan transformasi data tingkat lanjut.

---

### Tantangan 1: Pengurutan Ranking Mahasiswa (Sorting Algorithm)
**Tujuan:** Mengimplementasikan pengurutan data terstruktur menggunakan fungsi bawaan `sorted()` dengan argumen kustom `key` dan opsi urutan terbalik (*descending*).

1. Buat fungsi `sort_students(students: list[dict], by: str = "grade", descending: bool = True) -> list[dict]`.
2. Fungsi harus mendukung pengurutan berdasarkan:
   - `"grade"`: Mengurutkan dari nilai tertinggi ke terendah (ranking prestasi kelas).
   - `"name"`: Mengurutkan secara alfabetis berdasarkan nama lengkap ($A \to Z$ atau $Z \to A$).
   - `"nim"`: Mengurutkan berdasarkan urutan nomor registrasi mahasiswa.
3. Pastikan fungsi mengembalikan salinan *list* baru (*immutable list operation*) tanpa mengubah urutan asli pada basis data utama.

---

### Tantangan 2: Pemfilteran Berdasarkan Ambang Batas Kelulusan (Filter Predicate)
**Tujuan:** Menerapkan teknik pemfilteran koleksi data menggunakan list comprehension atau fungsi `filter()`.

1. Buat fungsi `filter_passing_students(students: list[dict], passing_threshold: float = 70.0) -> tuple[list[dict], list[dict]]`.
2. Pisahkan data mahasiswa menjadi dua kelompok:
   - Mahasiswa Lulus: Nilai $\ge \text{passing\_threshold}$.
   - Mahasiswa Remedial / Tidak Lulus: Nilai $< \text{passing\_threshold}$.
3. Tampilkan persentase kelulusan kelas dalam format persentase dua desimal (misalnya: `Tingkat Kelulusan: 75.00%`).

---

### Tantangan 3: Distribusi Frekuensi Predikat Nilai (Frequency Distribution)
**Tujuan:** Menggunakan struktur data kamus (*dictionary counter*) untuk menghitung sebaran data kategori nilai.

1. Buat fungsi `calculate_grade_distribution(students: list[dict]) -> dict[str, int]`.
2. Konversi setiap nilai mahasiswa ke predikat huruf ($A, B, C, D, E$) berdasarkan skala standar:
   - $A: \text{Nilai} \ge 80.0$
   - $B: 70.0 \le \text{Nilai} < 80.0$
   - $C: 60.0 \le \text{Nilai} < 70.0$
   - $D: 50.0 \le \text{Nilai} < 60.0$
   - $E: \text{Nilai} < 50.0$
3. Cetak visualisasi diagram batang teks (*ASCII bar chart*) sederhana di konsol:
   ```text
   A (Nilai >= 80) : [==========] 2 mahasiswa (50.0%)
   B (70 <= Nilai < 80): [=====] 1 mahasiswa (25.0%)
   C (60 <= Nilai < 70): [=====] 1 mahasiswa (25.0%)
   D (50 <= Nilai < 60): [] 0 mahasiswa (0.0%)
   E (Nilai < 50)  : [] 0 mahasiswa (0.0%)
   ```

