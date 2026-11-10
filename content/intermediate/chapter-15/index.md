# Chapter 15 — Searching & Sorting Algorithms
> **Linear Search, Binary Search, Bubble Sort, Selection Sort, Insertion Sort & Timsort**  
> *Level 2 · Intermediate · Estimasi Belajar: 5 Jam Pembelajaran*

---

## 1. Pengantar Pencarian & Pengurutan Data

Dalam rekayasa komputasi, dua operasi yang paling sering dieksekusi oleh mesin adalah **mencari** (*searching*) informasi dan **mengurutkan** (*sorting*) data. Mulai dari perutean paket internet, pencarian rekaman basis data, hingga pemrosesan sinyal telekomunikasi, efisiensi algoritma menentukan apakah sebuah sistem dapat merespons dalam hitungan milidetik atau mengalami perlambatan (*bottleneck*).

Meskipun bahasa pemrograman modern seperti Python menyediakan fungsi bawaan berkinerja sangat tinggi (`in`, `sorted()`, `.sort()`), memahami algoritma klasik fundamental adalah prasyarat mutlak bagi perekayasa perangkat lunak untuk:
- Memahami bagaimana komputer mengorganisasi dan membandingkan data di tingkat mendasar.
- Menganalisis *trade-off* antara kompleksitas waktu komputasi (CPU) dan ruang memori (RAM).
- Memilih teknik yang tepat untuk kasus-kasus khusus (misal: data yang sudah hampir terurut).

---

## 2. Algoritma Pencarian Linier (*Linear Search*)

Pencarian linier adalah teknik pencarian paling alami dan intuitif: algoritma memeriksa setiap elemen di dalam koleksi data satu per satu secara berurutan, mulai dari indeks $0$ hingga elemen terakhir, sampai target ditemukan atau seluruh data habis diperiksa.

```python
def linear_search(data: list[object], target: object) -> int | None:
    """Mencari target secara sekuensial. Mengembalikan indeks atau None."""
    for indeks, elemen in enumerate(data):
        if elemen == target:
            return indeks
    return None
```

### Karakteristik & Analisis Kompleksitas
- **Kelebihan:** Bekerja pada sembarang data tanpa memerlukan prasyarat urutan data. Sangat sederhana dan tidak memerlukan memori tambahan ($O(1)$ *space*).
- **Kasus Terbaik (*Best Case*):** $O(1)$ — Ketika target berada tepat di elemen pertama.
- **Kasus Terburuk (*Worst Case*):** $O(n)$ — Ketika target berada di elemen terakhir atau tidak ada sama sekali. Rata-rata perbandingan yang dibutuhkan untuk $n$ elemen adalah $\frac{n}{2}$.

---

## 3. Algoritma Pencarian Biner (*Binary Search*)

Jika data telah terurut (*sorted*), kita dapat menerapkan paradigma **Divide and Conquer** melalui algoritma Pencarian Biner. Alih-alih memeriksa satu per satu, algoritma membandingkan target dengan nilai tengah (*midpoint*) array:
- Jika target sama dengan nilai tengah, pencarian selesai.
- Jika target lebih kecil dari nilai tengah, eliminasi separuh bagian kanan dan lanjutkan pencarian hanya pada paruh kiri.
- Jika target lebih besar dari nilai tengah, eliminasi separuh bagian kiri dan lanjutkan pada paruh kanan.

```python
def binary_search(data_terurut: list[int], target: int) -> tuple[int | None, int]:
    kiri = 0
    kanan = len(data_terurut) - 1
    langkah = 0

    while kiri <= kanan:
        langkah += 1
        tengah = (kiri + kanan) // 2
        if data_terurut[tengah] == target:
            return tengah, langkah
        elif data_terurut[tengah] < target:
            kiri = tengah + 1
        else:
            kanan = tengah - 1

    return None, langkah
```

### Prasyarat Mutlak & Efisiensi Eksponensial
> [!IMPORTANT]
> **Prasyarat Data Terurut:**  
> Binary search **hanya dapat bekerja jika data sudah terurut**. Menjalankan binary search pada list acak akan memotong separuh ruang pencarian secara keliru dan menghasilkan jawaban salah (*false negative*).

Setiap perbandingan memotong ruang pencarian menjadi setengahnya ($N \to \frac{N}{2} \to \frac{N}{4} \to \dots \to 1$). Kompleksitas waktu binary search adalah **$O(\log n)$**.

| Ukuran Dataset ($N$) | Linear Search (Kasus Terburuk) | Binary Search (Kasus Terburuk) |
|:---:|:---:|:---:|
| $10$ | 10 perbandingan | 4 perbandingan |
| $1.000$ | 1.000 perbandingan | 10 perbandingan |
| $1.000.000$ | 1.000.000 perbandingan | 20 perbandingan |
| $1.000.000.000$ | 1.000.000.000 perbandingan | 30 perbandingan |

---

## 4. Algoritma Pengurutan Gelembung (*Bubble Sort*)

Bubble Sort bekerja dengan membandingkan pasangan elemen bertetangga dan menukarnya jika urutannya salah. Melalui proses ini, nilai-nilai terbesar akan "mengapung" ke posisi akhir seperti gelembung udara di dalam air.

```python
def bubble_sort(data: list[float]) -> list[float]:
    arr = list(data)
    n = len(arr)
    for i in range(n):
        ada_pertukaran = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Pertukaran (swap)
                ada_pertukaran = True
        # Optimasi Early Exit: Jika tidak ada pertukaran, data sudah terurut!
        if not ada_pertukaran:
            break
    return arr
```

- **Kompleksitas Waktu:** $O(n^2)$ pada kasus rata-rata dan terburuk; $O(n)$ pada kasus terbaik (data sudah terurut dengan optimasi flag).
- **Ruang Memori:** $O(1)$ (*In-Place*).

---

## 5. Algoritma Pengurutan Seleksi (*Selection Sort*)

Selection Sort membagi list menjadi dua bagian: bagian kiri yang sudah terurut dan bagian kanan yang belum terurut. Pada setiap iterasi, algoritma memindai seluruh bagian kanan untuk mencari nilai terkecil, lalu menukarnya ke posisi awal bagian yang belum terurut.

```python
def selection_sort(data: list[float]) -> list[float]:
    arr = list(data)
    n = len(arr)
    for i in range(n):
        indeks_min = i
        for j in range(i + 1, n):
            if arr[j] < arr[indeks_min]:
                indeks_min = j
        if indeks_min != i:
            arr[i], arr[indeks_min] = arr[indeks_min], arr[i]
    return arr
```

- **Karakteristik Khas:** Selection Sort melakukan perbandingan sebanyak $\frac{n(n-1)}{2}$ kali pada semua kasus ($O(n^2)$), tetapi menjamin **maksimal $n$ kali pertukaran fisik** (*swap*), berguna jika biaya penulisan memori sangat mahal.

---

## 6. Algoritma Pengurutan Sisip (*Insertion Sort*)

Insertion Sort bekerja layaknya seseorang yang menyusun kartu remi di tangannya. Elemen diambil satu per satu dari bagian yang belum terurut, lalu disisipkan ke posisi yang tepat pada bagian prefix yang sudah terurut dengan cara menggeser elemen yang lebih besar ke kanan.

```python
def insertion_sort(data: list[float]) -> list[float]:
    arr = list(data)
    for i in range(1, len(arr)):
        kunci = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > kunci:
            arr[j + 1] = arr[j]  # Pergeseran ke kanan
            j -= 1
        arr[j + 1] = kunci      # Penyisipan kunci
    return arr
```

### Keunggulan Adaptif pada *Nearly Sorted Data*
Insertion Sort sangat cepat pada kumpulan data yang sudah hampir terurut (*nearly sorted*), di mana kondisi `while` jarang terpenuhi sehingga kompleksitasnya mendekati **$O(n)$ linier**. Karakteristik inilah yang menjadikannya komponen inti dari algoritma Timsort modern.

---

## 7. Pengurutan Bawaan Python: `sorted()` vs `.sort()` dan Timsort

Python menyediakan dua mekanisme pengurutan bawaan:
1. **Fungsi Global `sorted(iterable, key=None, reverse=False)`:** Mengembalikan list baru yang terurut tanpa memodifikasi iterable asli (*non-destructive*).
2. **Metode List `list.sort(key=None, reverse=False)`:** Mengurutkan list secara langsung di tempat (*in-place mutation*) dan mengembalikan `None`.

### Mengapa Timsort Sangat Tangguh?
Algoritma pengurutan internal Python dirancang oleh Tim Peters pada tahun 2002 dengan nama **Timsort**. Timsort adalah algoritma adaptif hibrida yang menggabungkan efisiensi **Merge Sort** ($O(n \log n)$ pada kasus terburuk) dengan kecepatan **Insertion Sort** pada sub-deret data kecil (*runs*).

> [!NOTE]
> **Pesan Rekayasa Perangkat Lunak:**  
> Untuk aplikasi perangkat lunak produksi nyata, **selalu gunakan `sorted()` atau `.sort()` bawaan Python**. Implementasi C murni Timsort di CPython telah dioptimasi selama lebih dari dua dekade dan jauh lebih cepat, hemat energi, serta aman daripada algoritma sorting buatan tangan.

---

## 8. Pemeringkatan Multi-Kriteria & Konsep Pengurutan Stabil (*Stable Sort*)

Sebuah algoritma pengurutan dikatakan **stabil** (*stable*) jika mempertahankan urutan relatif asli dari elemen-elemen yang memiliki nilai pembanding yang sama. Baik `sorted()` maupun `.sort()` dijamin stabil.

Untuk melakukan pemeringkatan dengan banyak kriteria, gunakan argumen `key` dengan ekspresi `lambda` yang mengembalikan sebuah **tuple**:

```python
stasiun_jaringan = [
    {"nama": "BTS-Alpha", "latensi_ms": 10.0, "daya_mw": 80.0},
    {"nama": "BTS-Beta",  "latensi_ms": 5.0,  "daya_mw": 60.0},
    {"nama": "BTS-Gamma", "latensi_ms": 5.0,  "daya_mw": 120.0},
]

# Kriteria 1: Latensi terendah (Ascending)
# Kriteria 2: Daya tertinggi (Descending -> gunakan tanda minus -daya_mw)
ranking = sorted(stasiun_jaringan, key=lambda b: (b["latensi_ms"], -b["daya_mw"]))
for r, b in enumerate(ranking, start=1):
    print(f"#{r}: {b['nama']} (Latensi: {b['latensi_ms']} ms, Daya: {b['daya_mw']} mW)")
```

---

## 9. Mini Proyek: Data Search & Ranking System

Modul `search_sort.py` mengintegrasikan implementasi murni algoritma pencarian dan pengurutan yang telah diuji secara komprehensif pada kondisi batas:
- `linear_search`: Pencarian linier $O(n)$ pada data umum.
- `binary_search`: Pencarian biner $O(\log n)$ dengan pelacakan langkah perbandingan.
- `bubble_sort`, `selection_sort`, `insertion_sort`: Tiga pengurutan klasik manual.
- `rank_records`: Pemeringkatan stabil berbasis Timsort.

```bash
# Jalankan demonstrasi deterministik
python content/intermediate/chapter-15/code/contoh.py

# Jalankan Unit Testing otomatis
python -m unittest content/intermediate/chapter-15/tests/test_search_sort.py
```

---

## 10. Rangkuman & Referensi Pustaka

### Intisari Pembelajaran:
- Linear search fleksibel pada data acak tetapi berskala $O(n)$.
- Binary search membagi ruang pencarian menjadi setengahnya ($O(\log n)$), namun wajib mensyaratkan data terurut.
- Bubble Sort, Selection Sort, dan Insertion Sort memiliki kompleksitas rata-rata $O(n^2)$.
- Insertion Sort unggul pada data yang hampir terurut dan menjadi pondasi Timsort.
- Timsort adalah algoritma hibrida stabil berkinerja $O(n \log n)$ yang menjadi standar industri.

### Referensi Terbuka:
1. Python Software Foundation. *Sorting HOWTO*. https://docs.python.org/3/howto/sorting.html
2. Allen B. Downey. *Think Python 2e: Case Study: Word Play (Searching)*. Green Tea Press.
3. Tim Peters. *Timsort Description in CPython source tree*. `Objects/listsort.txt`.
4. Oleksii Trekhleb. *learn-python: Search & Sorting Algorithms*. https://github.com/trekhleb/learn-python
