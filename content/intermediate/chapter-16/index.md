# Chapter 16: Algorithm Analysis & Problem Solving

Selamat datang di **Chapter 16: Algorithm Analysis & Problem Solving**. Modul ini menjembatani kemampuan teknis menulis kode Python dengan pemikiran analitis rekayasa perangkat lunak: bagaimana mengevaluasi efisiensi komputasi, mengukur konsumsi sumber daya waktu dan memori, serta merancang solusi algoritmik yang terukur (*scalable*) dan tangguh.

---

## 1. Pendahuluan: Mengapa Analisis Algoritma Diperlukan?

Dalam rekayasa komputasi, sebuah solusi yang menghasilkan jawaban benar belumlah tentu dapat digunakan dalam sistem nyata. Pertimbangkan skenario berikut: Anda memiliki dua fungsi pencarian data sinyal telekomunikasi. Fungsi pertama menyelesaikan tugas dalam 0.001 detik pada 100 data, namun membutuhkan 100 detik pada 1.000.000 data. Fungsi kedua membutuhkan 0.005 detik pada 100 data, namun hanya memerlukan 0.02 detik pada 1.000.000 data.

Jika kita hanya menguji pada dataset kecil (100 elemen), fungsi pertama tampak lebih unggul. Namun pada skala produksi, fungsi pertama mengalami kegagalan performa (*performance bottleneck*).

Analisis algoritma memberikan kerangka kerja teoretis dan matematis independen dari spesifikasi perangkat keras (CPU, RAM, OS) untuk memprediksi perilaku konsumsi sumber daya seiring bertambahnya ukuran masukan ($n$).

---

## 2. Model Komputasi RAM dan Definisi Ukuran Masukan

Untuk menganalisis efisiensi secara objektif, ilmu komputer menggunakan model komputasi teoritis bernama **Random Access Machine (RAM)**:
1. Setiap operasi aritmatika dasar (`+`, `-`, `*`, `/`, `%`), perbandingan (`==`, `<`, `>`), dan penugasan variabel membutuhkan satu satuan waktu konstan ($O(1)$).
2. Setiap pengaksesan elemen list berdasarkan indeks (`arr[i]`) atau pencarian kunci kamus (`dict[key]`) memakan waktu konstan.
3. Total waktu eksekusi diproksikan dari akumulasi total operasi primitif yang dieksekusi terhadap ukuran masukan $n$.

Ukuran masukan ($n$) bergantung pada domain permasalahan:
- Untuk operasi list/tuple/string: $n$ adalah panjang data (`len(collection)`).
- Untuk operasi matriks atau grid: masukan berukuran $n \times m$.
- Untuk representasi angka biner: $n$ adalah jumlah bit representasi bilangan.

---

## 3. Notasi Asimtotik (Big-O Notation)

Notasi **Big-O** menggambarkan batas atas (*upper bound*) dari laju pertumbuhan fungsi kebutuhan komputasi terhadap ukuran masukan $n$ saat $n$ mendekati tak hingga. Secara matematis:
$$f(n) \in O(g(n)) \iff \exists c > 0, n_0 \ge 0 \quad \text{s.t.} \quad |f(n)| \le c \cdot g(n) \quad \forall n \ge n_0$$

### Hierarki Kompleksitas Waktu Standar

| Notasi Big-O | Nama Kompleksitas | Laju Pertumbuhan Relatif | Contoh Kasus Nyata |
| :--- | :--- | :--- | :--- |
| **$O(1)$** | Konstan (*Constant*) | Tidak berubah saat $n$ bertambah | Akses indeks list `arr[0]`, lookup dict `cache[key]`, `pop()` ujung list |
| **$O(\log n)$** | Logaritmik (*Logarithmic*) | Bertambah sangat lambat; membagi ruang pencarian separuh | Binary search pada list terurut, pencarian pada balanced BST |
| **$O(n)$** | Linear (*Linear*) | Proporsional langsung terhadap $n$ | Linear search, iterasi seluruh list tunggal, `sum(arr)`, `min(arr)` |
| **$O(n \log n)$** | Linearitmik (*Linearithmic*) | Standar optimal algoritma perbandingan sort | Merge sort, Timsort (`sorted()` dan `list.sort()`) |
| **$O(n^2)$** | Kuadratik (*Quadratic*) | Tumbuh proporsional terhadap kuadrat masukan | Nested loop ganda, Bubble sort, Selection sort, Insertion sort |
| **$O(2^n)$** | Eksponensial (*Exponential*) | Menggandakan waktu setiap penambahan 1 masukan | Rekursi Fibonacci naif, brute-force subset generation |
| **$O(n!)$** | Faktorial (*Factorial*) | Tidak praktis untuk $n > 12$ | Permutasi brute-force Traveling Salesperson Problem (TSP) |

### Aturan Simplifikasi Big-O
1. **Abaikan Konstanta Multiplikatif**: $O(3n^2 + 50n) \implies O(n^2)$.
2. **Ambil Suku Dominan Tertinggi**: $O(n^3 + 1000n^2 + 50000) \implies O(n^3)$.
3. **Penjumlahan Loop Berurutan**: Jika loop A memakan $O(n)$ dan loop B memakan $O(m)$, totalnya adalah $O(n + m)$.
4. **Perkalian Loop Bersarang**: Jika loop terluar berjalan $n$ kali dan loop terdalam berjalan $m$ kali, totalnya adalah $O(n \times m)$.

---

## 4. Kompleksitas Ruang (Space Complexity)

Selain waktu eksekusi, sebuah algoritma mengonsumsi memori kerja komputer. Kompleksitas ruang mengukur alokasi memori tambahan (*auxiliary space*) yang dibutuhkan selain masukan data awal.

### Contoh Perbandingan Kompleksitas Ruang:
- **Ruang Konstan $O(1)$**: Melakukan swapping in-place pada list masukan menggunakan dua variabel penunjuk (`left`, `right`). Tidak ada alokasi struktur data baru.
- **Ruang Linear $O(n)$**: Membuat list salinan baru berukuran $n$, misalnya `result = [x * 2 for x in data]`, atau pemanggilan tumpukan rekursi (*call stack*) sedalam $n$ frame.
- **Ruang Kuadratik $O(n^2)$**: Membuat tabel lookup matriks 2D berukuran $n \times n$.

> [!TIP]
> **Space-Time Tradeoff**: Dalam optimasi nyata, kita sering mengorbankan memori untuk menghemat waktu komputasi. Contoh paling umum adalah tabel *memoization* atau *hash map lookup*: alih-alih menghitung ulang fungsi $O(n)$, kita menyimpan hasil sebelumnya dalam kamus ($O(n)$ memori) untuk mendapatkan akses waktu $O(1)$.

---

## 5. Analisis Kasus: Best-Case, Average-Case, dan Worst-Case

Kinerja sebuah algoritma dapat bervariasi secara dramatis tergantung susunan spesifik data masukan:
- **Best-Case ($\Omega$ - Omega)**: Skenario paling ideal. Contoh: linear search langsung menemukan target pada indeks pertama ($O(1)$).
- **Average-Case ($\Theta$ - Theta)**: Skenario rata-rata dengan distribusi masukan acak seragam.
- **Worst-Case ($O$ - Big-O)**: Skenario terburuk yang memberikan jaminan batas atas kinerja. Rekayasa perangkat lunak sistem kritis umumnya bertumpu pada jaminan batas terburuk (*worst-case guarantee*).

---

## 6. Pengukuran Empiris dengan `time.perf_counter()`

Meskipun analisis Big-O memberikan prediksi teoretis, implementasi praktis menuntut validasi empiris di dunia nyata. Python menyediakan fungsi berpresisi tinggi `time.perf_counter()` dalam pustaka standar:

```python
import time

def ukur_durasi(func, *args, **kwargs) -> tuple[float, any]:
    """Mengukur waktu eksekusi presisi tinggi dari fungsi callable."""
    mulai = time.perf_counter()
    hasil = func(*args, **kwargs)
    selesai = time.perf_counter()
    durasi_detik = selesai - mulai
    return durasi_detik, hasil
```

### Prosedur Benchmarking yang Akurat:
1. **Lakukan Warm-up**: Eksekusi fungsi satu kali sebelum pengukuran agar interpreter melakukan translasi bytecode dan pengisian cache.
2. **Ulangi Multi-Runs**: Lakukan pengukuran beberapa kali (misal 5 atau 10 iterasi) lalu hitung nilai minimum atau rata-rata untuk meminimalkan gangguan *context switching* sistem operasi.
3. **Gunakan Ukuran Masukan Bergradasi**: Uji dengan ukuran $n = 100, 1000, 10000, 100000$ untuk memetakan kurva pertumbuhan waktu terhadap teori.

---

## 7. Pola Pemecahan Masalah Algoritmik

Ketika dihadapkan pada persoalan komputasi yang rumit, terapkan metodologi terstruktur:

1. **Dekomposisi Permasalahan**: Pecah masalah besar menjadi sub-masalah kecil yang mandiri (*divide and conquer*).
2. **Karakterisasi Masukan dan Keluaran**: Definisikan tipe data, rentang nilai, batas ekstrem ($n=0$, $n=1$, angka negatif, duplikasi data), dan invariansi logika.
3. **Mulai dari Brute Force**: Tulis algoritma naif yang terbukti benar terlebih dahulu sebagai tolok ukur kebenaran (*ground truth*).
4. **Identifikasi Bottleneck**: Temukan loop bersarang yang tidak perlu, perhitungan berulang yang dapat di-*cache*, atau operasi pencarian linear yang dapat diganti dengan tabel hash.
5. **Verifikasi Edge Cases**: Uji apakah algoritma menangani list kosong, list berukuran satu elemen, nilai ekstrim, atau urutan data terbalik tanpa menimbulkan error `IndexError` atau `RecursionError`.

---

## 8. Proyek Terapan: Algorithm Performance Comparator

Sebagai aplikasi praktis, modul ini menyediakan modul `AlgorithmPerformanceComparator` dalam paket `content/intermediate/chapter-16/code/benchmarker.py`. Modul ini memungkinkan kita:
- Menjalankan pengujian multi-algoritma pada berbagai skala ukuran masukan secara otomatis.
- Mengumpulkan data runtime empiris dan mengonversinya ke dalam representasi tabel performa.
- Memverifikasi secara langsung perbedaan drastis antara algoritma $O(n)$ dan $O(n^2)$.

```python
from benchmarker import AlgorithmPerformanceComparator

comparator = AlgorithmPerformanceComparator(iterations=5)
comparator.register("linear_search", lambda arr: 999999 in arr)
comparator.register("set_lookup", lambda s: 999999 in s)

results = comparator.benchmark_sizes([1000, 5000, 10000])
comparator.display_report(results)
```

---

## 9. Referensi Pembelajaran

1. **Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C.** (2022). *Introduction to Algorithms* (4th ed.). MIT Press.
2. **Python Software Foundation.** *TimeComplexity Wiki*. https://wiki.python.org/moin/TimeComplexity
3. **Downey, A.** (2015). *Think Python: How to Think Like a Computer Scientist*. Green Tea Press.
4. **Trekhleb, O.** *Learn Python - Algorithms & Complexity*. GitHub Repository.
