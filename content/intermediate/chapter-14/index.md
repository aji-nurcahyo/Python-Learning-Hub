# Chapter 14 — Comprehensions & Iterators
> **List, Dict, Set Comprehensions, Generator Expressions & Protokol Iterator**  
> *Level 2 · Intermediate · Estimasi Belajar: 4–5 Jam Pembelajaran*

---

## 1. Pengantar Transformasi Data Ekspresif

Dalam pemrograman prosedural tradisional, memproses sebuah koleksi data umumnya memerlukan pembuatan list penampung kosong, iterasi loop `for` eksplisit, evaluasi percabangan `if`, dan pemanggilan metode `.append()` secara berulang:

```python
# Pendekatan Tradisional (Imperatif)
sinyal_mentah = [12.0, -5.0, 18.5, 0.0, 25.0]
sinyal_positif = []
for s in sinyal_mentah:
    if s > 0.0:
        sinyal_positif.append(s * 2)
```

Meskipun valid, pola ini bertele-tele dan menyamarkan maksud utama kode: **memfilter data positif dan mengalikannya dengan dua**. 

Bahasa Python menyediakan fitur sintaksis yang sangat ekspresif bernama **Comprehensions** dan **Generator Expressions**. Fitur ini memadukan pembuatan koleksi, perulangan, dan pemfilteran dalam satu ekspresi deklaratif yang ringkas, mudah dibaca, dan dieksekusi lebih cepat pada tingkat *bytecode* CPython.

---

## 2. List Comprehensions: Transformasi & Pemfilteran Kondisional

Sintaks dasar list comprehension adalah:
$$[\text{ekspresi}\ \textbf{for}\ \text{item}\ \textbf{in}\ \text{iterable}\ (\textbf{if}\ \text{kondisi})]$$

```python
# Pendekatan Pythonic (List Comprehension)
sinyal_mentah = [12.0, -5.0, 18.5, 0.0, 25.0]
sinyal_positif = [s * 2 for s in sinyal_mentah if s > 0.0]
print(sinyal_positif)  # Output: [24.0, 37.0, 50.0]
```

### Pemfilteran (`if`) vs Percabangan Nilai (`if-else` Ternary)
Perhatikan perbedaan posisi kata kunci `if` berikut:
1. **Klausa Filter (`if` di akhir):** Menentukan apakah elemen dimasukkan ke dalam hasil atau diabaikan.
2. **Klausa Ternary (`if-else` di awal):** Menentukan nilai transformasi apa yang dihasilkan untuk setiap elemen yang diiterasi.

```python
pengukuran_dbm = [-110.0, -85.0, -65.0, -95.0]

# 1. Filter: Hanya ambil sinyal kuat (>= -90 dBm)
sinyal_kuat = [p for p in pengukuran_dbm if p >= -90.0]
# Hasil: [-85.0, -65.0]

# 2. Ternary: Beri label status untuk SEMUA elemen
kategori = ["LAYAK" if p >= -90.0 else "DROP" for p in pengukuran_dbm]
# Hasil: ['DROP', 'LAYAK', 'LAYAK', 'DROP']
```

---

## 3. Nested Comprehensions: Matriks 2D & Grid Spasial

List comprehension dapat disusun secara bersarang (*nested*) untuk menangani struktur data berdimensi banyak:

### A. Pembangkitan Grid 2D (Matriks)
```python
# Membuat matriks 3x3 berisi koordinat node
grid = [[f"({r},{c})" for c in range(3)] for r in range(3)]
# Hasil:
# [['(0,0)', '(0,1)', '(0,2)'],
#  ['(1,0)', '(1,1)', '(1,2)'],
#  ['(2,0)', '(2,1)', '(2,2)']]
```

### B. Perataan Matriks (*Matrix Flattening*)
Untuk mengubah matriks 2D menjadi list 1D datar, tuliskan urutan loop persis seperti penulisan loop bersarang tradisional:
```python
matriks = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Ekuivalen dengan:
# for baris in matriks:
#     for angka in baris:
#         hasil.append(angka)
flat = [angka for baris in matriks for angka in baris]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

> [!TIP]
> **Aturan Keterbacaan (*Readability Rule*):**  
> Hindari membuat nested comprehension dengan lebih dari dua tingkat perulangan. Jika logika Anda membutuhkan tiga tingkat loop atau filter yang rumit, tulislah for loop biasa dengan indentasi jelas demi kemudahan pemeliharaan kode tim.

---

## 4. Dictionary Comprehensions

Sintaks dictionary comprehension menggunakan kurung kurawal `{}` dengan pasangan kunci-nilai yang dipisahkan tanda titik dua (`kunci: nilai`):

```python
daftar_node = [
    {"ip": "10.0.0.1", "nama": "Gateway-Utama", "status": "UP"},
    {"ip": "10.0.0.2", "nama": "Switch-Lt1",     "status": "UP"},
    {"ip": "10.0.0.3", "nama": "AP-Taman",        "status": "DOWN"},
]

# 1. Peta Indeks Asosiatif: IP -> Nama Node (Pencarian O(1))
peta_ip = {node["ip"]: node["nama"] for node in daftar_node}
# {'10.0.0.1': 'Gateway-Utama', '10.0.0.2': 'Switch-Lt1', '10.0.0.3': 'AP-Taman'}

# 2. Pemfilteran Kamus: Hanya node yang aktif
node_aktif = {node["ip"]: node["nama"] for node in daftar_node if node["status"] == "UP"}

# 3. Inversi Kamus (Membalik Relasi)
kode_protokol = {80: "HTTP", 443: "HTTPS", 22: "SSH"}
nama_protokol = {nama: port for port, nama in kode_protokol.items()}
```

---

## 5. Set Comprehensions

Set comprehension menghasilkan himpunan (*set*) matematika di mana seluruh elemen otomatis diurutkan secara unik tanpa duplikasi:

```python
log_ip_mentah = [
    "192.168.1.1", "  192.168.1.5  ", "192.168.1.1",
    "10.0.0.1", "192.168.1.5", "10.0.0.1 "
]

# Normalisasi teks dan deduplikasi instan
ip_unik = {ip.strip() for ip in log_ip_mentah}
print(ip_unik)  # {'192.168.1.1', '192.168.1.5', '10.0.0.1'}
```

---

## 6. Protokol Iterator: `iter()` dan `next()`

Semua perulangan `for` dalam Python bekerja di atas **Protokol Iterator** (*Iterator Protocol*):
1. **Iterable:** Objek yang mengimplementasikan metode `__iter__()` dan menghasilkan iterator saat dipanggil `iter(obj)`.
2. **Iterator:** Objek aliran yang memiliki status posisi internal dan mengimplementasikan metode `__next__()` untuk mengambil elemen berikutnya.

```python
perangkat = ["Router", "Switch", "Antena"]
it = iter(perangkat)

print(next(it))  # 'Router'
print(next(it))  # 'Switch'
print(next(it))  # 'Antena'
# print(next(it)) -> Melemparkan eksepsi StopIteration!

# Pengambilan aman menggunakan sentinel default:
print(next(it, "HABIS"))  # 'HABIS' (tidak melempar error)
```

Perulangan `for x in perangkat:` pada dasarnya mengeksekusi mekanisme `iter()` dan `next()` ini secara otomatis di balik layar dan menangkap sinyal `StopIteration` secara diam-diam.

---

## 7. Perkakas Bawaan: `enumerate()` dan `zip()`

Python menyediakan fungsi bawaan untuk memperkaya siklus iterasi:

### A. `enumerate(iterable, start=0)`
Menghasilkan pasangan indeks terhitung dan elemen koleksi:
```python
stasiun = ["BTS-A", "BTS-B", "BTS-C"]
for nomor, nama in enumerate(stasiun, start=1):
    print(f"Node #{nomor}: {nama}")
```

### B. `zip(*iterables)`
Menggabungkan beberapa koleksi secara paralel seperti gerigi ritsleting (*zipper*):
```python
node_ids = ["N1", "N2", "N3"]
daya_mw = [45.0, 78.5, 90.0]
frekuensi = [900, 1800, 2100]

for nid, pwr, freq in zip(node_ids, daya_mw, frekuensi):
    print(f"{nid} -> {pwr} mW @ {freq} MHz")
```

---

## 8. Generator Expressions: Evaluasi Lazy & Efisiensi Memori

Ketika memproses kumpulan data berukuran masif (misalnya jutaan baris log atau telemetri sensor waktu nyata), list comprehension dapat menghabiskan seluruh memori RAM karena seluruh elemen dialokasikan seketika (*eager evaluation*).

**Generator Expression** memecahkan masalah ini dengan menerapkan evaluasi tunda (*lazy evaluation*). Nilai hanya dihitung satu per satu saat diminta oleh konsumen data. Sintaksnya identik dengan list comprehension, tetapi menggunakan tanda kurung biasa `()`:

```python
import sys

# List Comprehension: Eager (Memori Besar)
list_kuadrat = [x ** 2 for x in range(1_000_000)]
memori_list = sys.getsizeof(list_kuadrat)  # ~8.4 MegaByte

# Generator Expression: Lazy (Memori Konstan)
gen_kuadrat = (x ** 2 for x in range(1_000_000))
memori_gen = sys.getsizeof(gen_kuadrat)    # ~104 Byte!

print(f"Ukuran RAM List      : {memori_list:,} byte")
print(f"Ukuran RAM Generator : {memori_gen:,} byte")
print(f"Rasio Penghematan    : {memori_list / memori_gen:.0f}x lebih hemat!")
```

Generator expression dapat langsung dialirkan ke fungsi agregator seperti `sum()`, `max()`, `min()`, atau loop `for` tanpa tanda kurung dobel:
```python
total_daya = sum(float(r["daya"]) for r in dataset_besar if r["daya"] > 0)
```

---

## 9. Mini Proyek: Dataset Transformation Toolkit

Pada modul ini, Anda membangun pustaka pengolah data bernama **Dataset Transformation Toolkit** (`transform_toolkit.py`):
- `filter_and_transform`: List comprehension dengan kondisi ambang batas dan penskalaan gain.
- `build_index_map`: Dict comprehension untuk lookup cepat $O(1)$ berdasarkan atribut primer.
- `extract_unique_categories`: Set comprehension untuk isolasi kategori unik ternormalisasi.
- `flatten_matrix`: Nested comprehension untuk meratakan topologi matriks 2D menjadi 1D.
- `stream_transformed_data`: Generator expression untuk streaming data hemat memori.

```bash
# Jalankan demonstrasi deterministik
python content/intermediate/chapter-14/code/contoh.py

# Jalankan pengujian unit otomatis
python -m unittest content/intermediate/chapter-14/tests/test_comprehensions.py
```

---

## 10. Rangkuman & Referensi Pustaka

### Intisari Pembelajaran:
- List comprehension menggantikan pola perulangan akumulator menjadi ekspresi deklaratif satu baris yang elegan.
- Bedakan klausa `if` di akhir (sebagai filter elemen) dengan operator ternary `if-else` di awal (sebagai pemilih nilai).
- Gunakan dict comprehension untuk membuat tabel lookup berindeks hash dan set comprehension untuk deduplikasi.
- Pahami protokol iterator (`iter()` dan `next()`) yang menjadi motor penggerak perulangan di Python.
- Gunakan generator expression `(expr for x in data)` saat memproses volume data masif untuk mencegah kehabisan memori RAM.

### Referensi Terbuka:
1. Python Software Foundation. *The Python Tutorial: List Comprehensions (Section 5.1.3)*. https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
2. Python Enhancement Proposals (PEP 289). *Generator Expressions*. https://peps.python.org/pep-0289/
3. Allen B. Downey. *Think Python 2e: Lists and Dictionaries*. Green Tea Press.
4. Asabeneh Yetayeh. *30 Days of Python: Day 13 - List Comprehension*. https://github.com/Asabeneh/30-Days-Of-Python
