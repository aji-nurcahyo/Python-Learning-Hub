# Panduan Standar Bahasa Teknis (Technical Language Style Guide)
## Python Learning Hub — Official Technical Writing & Terminology Standard

> **Versi Panduan:** 1.0.0  
> **Tanggal Efektif:** 4 November 2026  
> **Target Audiens:** Penulis modul, kurikulum developer, instruktur, dan kontributor konten  
> **Prinsip Utama:** Bahasa pengantar resmi adalah **Bahasa Indonesia** yang natural, lugas, dan baku, dengan mempertahankan **terminologi teknis Python standar dalam Bahasa Inggris** untuk mencegah kerancuan makna atau terjemahan harfiah (*literal translation*) yang canggung.

---

## 1. Kebijakan Bahasa Resmi (*Language Policy*)

1. **Bahasa Pengantar:** Seluruh narasi penjelasan konsep, pengantar bab, petunjuk instruksi latihan, deskripsi tugas, dan rubrik penilaian ditulis dalam **Bahasa Indonesia formal dan komunikatif**.
2. **Terminologi Pemrograman:** Istilah teknis inti pemrograman Python **tetap ditulis dalam Bahasa Inggris** (diformat sebagai `code span` atau teks miring/tegak sesuai konteks), terutama istilah yang telah menjadi konvensi global dunia rekayasa perangkat lunak.
3. **Larangan Terjemahan Harfiah (*No Literal Translations*):** Dilarang keras menerjemahkan secara kaku kata-kata teknis yang jika diterjemahkan justru menimbulkan kebingungan konseptual bagi mahasiswa dan developer (misalnya: tidak menerjemahkan `dictionary` menjadi "kamus", `slicing` menjadi "irisan", `list` menjadi "daftar", atau `exception` menjadi "pengecualian").

---

## 2. Tabel Istilah Teknis yang Wajib Dipertahankan dalam Bahasa Inggris

Terminologi berikut **tidak boleh diterjemahkan secara harfiah** dalam materi pembelajaran Python Learning Hub:

| Terminologi Asli (Wajib Dipakai) | Terjemahan Harfiah yang DILARANG | Contoh Penerapan yang BENAR |
| :--- | :--- | :--- |
| **`list`** | daftar | `list` digunakan untuk menyimpan sekumpulan elemen terurut yang mutable. |
| **`tuple`** | tupel / daftar tetap | `tuple` bersifat immutable dan aman untuk integritas data koordinat. |
| **`dictionary`** / **`dict`** | kamus | `dictionary` menyimpan data dalam bentuk pasangan `key-value`. |
| **`set`** | himpunan (dalam konteks tipe) | Gunakan `set` untuk operasi keanggotaan dan deduplikasi data. |
| **`string`** / **`str`** | untai / tali | Manipulasi teks dilakukan dengan metode bawaan pada objek `string`. |
| **`function`** | fungsi (tetap boleh "fungsi") | Mendefinisikan `function` modular dengan kata kunci `def`. |
| **`method`** | metode | `method` adalah fungsi yang terikat pada suatu objek atau class. |
| **`class`** | kelas | `class` bertindak sebagai blueprint untuk menginisialisasi objek. |
| **`object`** | objek | Setiap nilai di Python direpresentasikan sebagai sebuah `object`. |
| **`attribute`** | atribut | Mengakses `attribute` objek menggunakan notasi titik (`obj.attr`). |
| **`module`** | modul | Mengimpor `module` bawaan `math` dan `sys`. |
| **`package`** | paket | Mengorganisasi kode ke dalam `package` berstruktur hierarkis. |
| **`exception`** | pengecualian | Menangkap `exception` saat runtime menggunakan blok `try-except`. |
| **`error handling`** | penanganan kesalahan | Menerapkan `error handling` defensif untuk menjaga keandalan sistem. |
| **`debugging`** | penelusuran galat | Melakukan `debugging` sistematis dengan breakpoint dan `pdb`. |
| **`loop`** | gelung | Menghentikan `loop` lebih awal dengan statement `break`. |
| **`comprehension`** | pemahaman | Menulis `list comprehension` ringkas untuk transformasi data. |
| **`slicing`** | irisan / pengirisan | Gunakan `slicing` `data[start:stop:step]` untuk mengambil sub-array. |
| **`indexing`** | pengindeksan | Mengakses elemen melalui `indexing` berbasis nol (*zero-based indexing*). |
| **`iterator`** | pengulang / penelusur | Objek `iterator` mengimplementasikan metode `__iter__()` dan `__next__()`. |
| **`iterable`** | dapat diulang | List dan tuple merupakan struktur data yang bersifat `iterable`. |
| **`generator`** | pembangkit | `generator` mengevaluasi elemen secara lazy (*on-demand*) dengan `yield`. |
| **`decorator`** | penghias | Menerapkan `decorator` `@property` untuk enkapsulasi getter. |
| **`inheritance`** | pewarisan | Menurunkan atribut dan method superclass melalui `inheritance`. |
| **`polymorphism`** | polimorfisme | Memanfaatkan `polymorphism` antarmuka melalui method overriding. |
| **`encapsulation`** | pengkapsulan | Menyembunyikan state internal objek melalui prinsip `encapsulation`. |
| **`constructor`** | pembangun | Method `__init__()` bertindak sebagai `constructor` inisialisasi instance. |
| **`scope`** | cakupan | Variabel lokal dibatasi oleh `scope` fungsi tempat ia dideklarasikan. |
| **`return value`** | nilai balik | Fungsi menghasilkan `return value` yang dikembalikan ke pemanggil. |
| **`parameter`** | parameter | `parameter` didefinisikan pada deklarasi tanda tangan fungsi. |
| **`argument`** | argumen | Nilai aktual yang dikirim saat pemanggilan fungsi adalah `argument`. |
| **`key-value pair`** | pasangan kunci-nilai | Mengiterasi `key-value pair` menggunakan `dict.items()`. |
| **`sorting`** | pengurutan (konteks algoritma) | Melakukan `sorting` data dengan algoritma Timsort bawaan. |
| **`searching`** | pencarian (konteks algoritma) | Melakukan `searching` linear $O(n)$ atau binary search $O(\log n)$. |
| **`runtime`** | waktu jalan / waktu eksekusi | Terjadi runtime exception `ZeroDivisionError` saat pembagian nol. |
| **`unit test`** | uji unit | Memverifikasi ketepatan logika modul dengan `unit test` otomatis. |
| **`type hint`** | petunjuk tipe | Menambahkan `type hint` eksplisit untuk dokumentasi dan static analysis. |
| **`virtual environment`**| lingkungan virtual | Mengisolasi dependensi proyek dalam `virtual environment` (`.venv`). |
| **`file handling`** | penanganan berkas | Mengelola pembacaan dan penulisan berkas melalui `file handling`. |
| **`serialization`** | serialisasi | Proses `serialization` data objek Python menjadi string JSON. |
| **`deserialization`** | deserialisasi | Proses `deserialization` payload JSON mentah menjadi dictionary. |

---

## 3. Istilah Bahasa Indonesia yang Dianjurkan

Kosakata Bahasa Indonesia berikut telah mapan dalam terminologi akademik dan industri komputasi serta sangat dianjurkan untuk digunakan dalam kalimat narasi:

- **variabel** (bukan *peubah*)
- **algoritma** (bukan *tatacara*)
- **percabangan** / **kondisional** (alur seleksi logika `if-elif-else`)
- **perulangan** / **iterasi** (eksekusi berulang `for` dan `while`)
- **operator** (simbol komputasi seperti `+`, `-`, `==`, `and`)
- **ekspresi** (kombinasi nilai dan operator yang menghasilkan nilai)
- **masukan** (data masukan dari pengguna / argumen fungsi)
- **keluaran** (hasil cetak / keluaran program di terminal)
- **pengujian** (proses validasi kebenaran fungsional program)
- **struktur data** (organisasi penyimpanan koleksi data)
- **konkurensi** (penanganan multi-tugas secara bersamaan)
- **rekursi** (fungsi yang memanggil dirinya sendiri)

---

## 4. Konvensi Penulisan & Tipografi

### A. Format Kode Inline (`code span`)
Gunakan backtick (`` `...` ``) untuk:
- Nama tipe data bawaan (`int`, `float`, `str`, `bool`, `list`, `dict`, `set`, `tuple`).
- Sintaksis dan kata kunci Python (`def`, `return`, `with`, `try`, `except`, `raise`, `class`, `import`).
- Nama variabel, fungsi, method, class, dan argumen (`hitung_snr()`, `node_id`, `data_processor`).
- Nama file, path direktori, dan ekstensi berkas (`config.json`, `data.csv`, `main.py`, `pathlib.Path`).

### B. Format Teks Penjelasan
- **Huruf Tebal (**teks**)**: Digunakan untuk menekankan konsep kunci atau istilah penting saat pertama kali diperkenalkan.
- **Huruf Miring (*teks*)**: Digunakan untuk istilah serapan asing dalam frasa non-kode, misalnya *lazy evaluation*, *eager loading*, *space-time tradeoff*, *early-stop*.
- **KaTeX / LaTeX Math**: Digunakan untuk formula matematis atau notasi asimtotik komputasi ($O(1)$, $O(\log n)$, $O(n)$, $O(n \log n)$, $O(n^2)$).

---

## 5. Kaidah Penulisan Komentar Kode Python

Komentar di dalam berkas Python (`# komentar`) dan docstring (`"""docstring"""`) harus mematuhi kaidah:
1. **Bahasa Indonesia Baku & Jelas:** Komentar baris bertujuan memandu pembelajar memahami alur algoritma.
2. **Singkat dan Kontekstual:** Menjelaskan *alasan* (why) dan bukan sekadar mengulang kode (what).
3. **Identifier Tetap Bahasa Indonesia / Standar Teknis:**
   ```python
   # BENAR:
   # 1. Menyiapkan dataset pencarian berukuran 10.000 elemen
   dataset = list(range(10_000))
   target = 9_999

   # 2. Uji lookup menggunakan set O(1)
   himpunan_data = set(dataset)
   ditemukan = target in himpunan_data
   ```

---

## 6. Contoh Perbandingan Frasa (*Before & After*)

| Kalimat Canggung / Terjemahan Kaku | Kalimat Standar yang Disempurnakan |
| :--- | :--- |
| *Kamus Python digunakan untuk menyimpan pasangan kunci dan nilai.* | *`dictionary` digunakan untuk menyimpan data dalam bentuk pasangan `key-value`.* |
| *Gunakan irisan untuk memotong daftar menjadi potongan lebih kecil.* | *Gunakan `slicing` untuk mengambil subset elemen dari `list`.* |
| *Pengecualian dilemparkan saat indeks daftar melampaui batas.* | *Runtime exception `IndexError` dipicu saat indeks `list` berada di luar rentang valid.* |
| *Pembangkit melakukan evaluasi malas dengan menghasilkan nilai demi nilai.* | *`generator` menerapkan evaluasi lazy (*on-demand*) menggunakan kata kunci `yield`.* |
| *Penghias fungsi membungkus fungsi lain dengan logika tambahan.* | *`decorator` menerima sebuah fungsi dan mengembalikan fungsi baru dengan fungsionalitas tambahan.* |
| *Petunjuk tipe diperiksa oleh pemeriksa tipe statis.* | *`type hint` divalidasi oleh static type checker seperti mypy.* |
| *Penanganan berkas menggunakan manajer konteks memastikan berkas ditutup.* | *`file handling` menggunakan context manager `with` menjamin berkas ditutup secara otomatis.* |

---

## 7. Panduan Khusus Slide Presentasi (Reveal.js)

1. **Judul Slide:** Ringkas, langsung ke inti konsep, tanpa singkatan non-standar.
2. **Kepadatan Teks:** Maksimal 3–5 butir poin per slide. Jangan menyalin paragraf panjang modul ke dalam slide.
3. **Pemisahan Kode:** Jika kode contoh lebih dari 12–15 baris, bagi menjadi 2 slide berturutan (misal: "Implementasi Bagian 1" dan "Implementasi Bagian 2").
4. **Identitas Resmi:** Seluruh slide wajib menyertakan identitas platform resmi:
   - Platform: **Python Learning Hub**
   - Tagline: **Learn Python, One Chapter at a Time**
   - Author: **Aji Pamungkas Tri Nurcahyo**
   - Institusi: **Institut Teknologi Sumatera**
   - Bebas dari istilah legacy (*pertemuan*, *pengkom*, *alpro*, *prodi*, *fakultas*).
