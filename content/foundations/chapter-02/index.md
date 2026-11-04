# Chapter 02 — Variables & Data Types
> **Variabel Dinamis, Tipe Data Skalar & Konversi Tipe**  
> *Level 1 · Foundations · Beginner · Estimasi Belajar: 3 Jam*

---

## 1. Konsep Variabel & Alokasi Memori

Dalam pemrograman komputer, sebuah program harus dapat menyimpan, melacak, dan memanipulasi informasi dalam memori sementara (*RAM*). Di dalam bahasa Python, **variabel** bukanlah wadah (*box*) fisik tempat data diletakkan, melainkan **label atau penunjuk referensi (*reference tag*)** yang ditempelkan ke suatu objek di memori.

```text
[Label Variabel] ──── Referensi ────► [Objek Nilai di Heap Memory]
 frekuensi_mhz                          1800.0 (float, id: 0x10a2b8)
```

Ketika Anda mengeksekusi pernyataan penugasan:
```python
frekuensi_mhz = 1800.0
```
CPython akan:
1. Mengalokasikan objek bilangan desimal `1800.0` di memori komputer (*Heap Memory*).
2. Memberikan pengenal memori unik untuk objek tersebut (dapat diperiksa menggunakan fungsi `id()`).
3. Mengaitkan nama variabel `frekuensi_mhz` sebagai label penunjuk objek tersebut.

### Konvensi Penamaan Variabel (PEP 8)
- Gunakan huruf kecil dipisahkan garis bawah (*snake_case*), contoh: `daya_pemancar`, `kecepatan_cahaya`.
- Nama variabel tidak boleh diawali angka dan tidak boleh menggunakan kata kunci bawaan (*reserved keywords*) seperti `if`, `for`, `class`, atau `def`.
- Pilih nama yang memiliki arti (*meaningful*), hindari nama satu huruf seperti `x` atau `y` kecuali untuk indeks perulangan atau variabel koordinat matematis.

---

## 2. Tipe Data Skalar Primitif

Python menyediakan empat tipe data skalar fundamental:

| Tipe Data | Representasi Python | Contoh Nilai | Keterangan |
|:---|:---:|:---|:---|
| **Integer** | `int` | `1024`, `-40`, `0` | Bilangan bulat dengan presisi arbitrer (tidak ada batasan ukuran selama memori tersedia). |
| **Floating-Point** | `float` | `2.45`, `-88.5`, `3e8` | Bilangan riil berbasis standar IEEE 754 presisi ganda (*double precision*). |
| **String** | `str` | `"BTS-01"`, `'LTE'` | Koleksi karakter teks yang diapit tanda petik tunggal `'` atau ganda `"`. |
| **Boolean** | `bool` | `True`, `False` | Nilai logika kebenaran; merupakan subkelas dari tipe `int` (True bernilai 1, False bernilai 0). |

Untuk memeriksa tipe objek saat program berjalan, gunakan fungsi `type()`:
```python
kapasitas = 64
print(type(kapasitas))  # <class 'int'>
```

---

## 3. Pengetikan Dinamis (*Dynamic Typing*)

Python adalah bahasa dengan pengetikan dinamis (*dynamically typed language*). Artinya, Anda tidak perlu mendeklarasikan tipe data secara eksplisit saat membuat variabel, dan sebuah variabel dapat dialihkan menunjuk ke tipe objek yang berbeda selama siklus program berlangsung:

```python
sinyal = "Normal"  # Menunjuk objek string (str)
sinyal = -85       # Re-assigned menunjuk objek integer (int)
sinyal = -85.75    # Re-assigned menunjuk objek float
```

Meskipun fleksibel, pengetikan dinamis menuntut kehati-hatian pengembang agar tidak memicu kesalahan runtime seperti `TypeError`. Untuk memvalidasi tipe data yang aman dalam logika rekayasa, gunakan fungsi `isinstance(obj, tipe)`:

```python
if isinstance(sinyal, (int, float)):
    print("Nilai sinyal valid untuk perhitungan numerik.")
```

---

## 4. Konversi Tipe Data Eksplisit (*Type Casting*)

Seringkali data yang diterima dari masukan pengguna atau transmisi jaringan berbentuk teks (`str`), meskipun nilai sebenarnya adalah angka numerik. Python menyediakan fungsi konversi tipe eksplisit:

1. `int(x)`: Mengonversi nilai ke integer bulat. Jika mengonversi float, bagian desimal dipotong (*truncated*).
2. `float(x)`: Mengonversi teks atau integer menjadi desimal floating-point.
3. `str(x)`: Mengonversi representasi objek apa pun menjadi teks string.
4. `bool(x)`: Mengevaluasi nilai kebenaran (*Truthy* atau *Falsy*).

### Konsep Truthy dan Falsy
Di Python, nilai-nilai berikut dievaluasi sebagai `False` (*Falsy*):
- Angka nol numerik: `0`, `0.0`
- Koleksi atau teks kosong: `""`, `[]`, `()`, `{}`, `set()`
- Nilai ketiadaan: `None`
- Nilai boolean: `False`

Seluruh nilai lainnya dievaluasi sebagai `True` (*Truthy*).

---

## 5. Studi Kasus Rekayasa: Parameter Transceiver BTS

Dalam pengelolaan stasiun pemancar seluler (Base Transceiver Station), setiap perangkat transceiver didefinisikan oleh beberapa parameter operasional inti dengan berbagai tipe data:

```python
# Parameter transceiver BTS
node_id: str = "BTS-BandarLampung-04"
frekuensi_mhz: float = 1800.0
daya_tx_watt: int = 40
operasional: bool = True

# Pemeriksaan parameter sebelum transmisi
print(f"Stasiun {node_id}: Frekuensi {frekuensi_mhz} MHz, Daya {daya_tx_watt} W. Status: {operasional}")
```

Dengan memahami tipe data skalar secara kokoh, insinyur perangkat lunak dapat mencegah galat fatal seperti mencoba menjumlahkan string dengan angka tanpa konversi tipe terlebih dahulu.

---

## 6. Ringkasan Bab

- Variabel di Python bekerja sebagai label referensi memori (*reference pointers*) ke objek nilai di memori Heap.
- Empat tipe data skalar dasar adalah `int`, `float`, `str`, dan `bool`.
- Tipe data ditentukan secara dinamis saat runtime (*dynamic typing*).
- Fungsi `type()` digunakan untuk menginspeksi tipe data, sedangkan `isinstance()` digunakan untuk validasi tipe yang aman dan fleksibel.
- Fungsi casting `int()`, `float()`, `str()`, dan `bool()` memungkinkan konversi tipe data yang aman dan terprediksi.

---

## 7. Referensi & Sumber Belajar Terbuka

1. **Python Software Foundation**, *Using Python as a Calculator (Numbers & Strings)*, [https://docs.python.org/3/tutorial/introduction.html](https://docs.python.org/3/tutorial/introduction.html) (PSF License 2.0).
2. **Allen B. Downey**, *Think Python (3rd Edition)*, Chapter 2: Variables, Expressions and Statements, [https://allendowney.github.io/ThinkPython/](https://allendowney.github.io/ThinkPython/) (CC BY-NC 4.0).
3. **Asabeneh S. Yetayeh**, *30 Days Of Python*, Day 02: Variables, Builtin Functions, [https://github.com/Asabeneh/30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) (MIT License).
4. **David J. Malan**, *CS50’s Introduction to Programming with Python*, Week 0: Functions, Variables, [https://cs50.harvard.edu/python/](https://cs50.harvard.edu/python/) (CC BY-NC-SA 4.0).
