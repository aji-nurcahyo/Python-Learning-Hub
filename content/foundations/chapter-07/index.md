# Chapter 07 — Strings & Text Processing
> **Indexing, Slicing, Immutability & Metode String**  
> *Level 1 · Foundations · Beginner · Estimasi Belajar: 3–4 Jam*

---

## 1. Karakteristik Fundamental String di Python

Dalam pemrograman komputer, teks direpresentasikan sebagai **string** (`str`), yaitu untaian karakter terurut (*ordered sequence of characters*). Di Python 3, string secara baku menggunakan pengodean **Unicode (UTF-8)**, sehingga mampu menampung karakter dari berbagai aksara dunia dan simbol teknis.

Dua sifat inti string di Python:
1. **Sequence Terurut (*Ordered Sequence*):** Setiap karakter memiliki posisi indeks numerik tetap yang dimulai dari nol (`0`).
2. **Bersifat Kekal (*Immutable*):** Setelah sebuah objek string dibuat di memori, isi karakter di dalamnya **tidak dapat diubah, ditambah, atau dihapus secara langsung**. Setiap operasi pemanipulasian string akan menghasilkan **objek string baru** di memori.

```python
teks = "Python"
# teks[0] = "J"  # TypeError: 'str' object does not support item assignment
teks_baru = "J" + teks[1:]  # Cara yang benar: membuat objek string baru 'Jython'
```

---

## 2. Pengindeksan Karakter (*Indexing & Negative Indexing*)

Python mendukung pengindeksan positif dari kiri (mulai dari `0`) dan pengindeksan negatif dari kanan (mulai dari `-1`):

```text
Karakter:   P    y    t    h    o    n
Indeks +:   0    1    2    3    4    5
Indeks -:  -6   -5   -4   -3   -2   -1
```

```python
kode = "BTS-01"
print(kode[0])   # 'B' (karakter pertama)
print(kode[-1])  # '1' (karakter terakhir)
print(kode[-2])  # '0' (karakter kedua dari belakang)
```

---

## 3. Pemotongan Substring (*Slicing Notation*)

Slicing memungkinkan Anda mengekstrak potongan substring menggunakan sintaks:
$$\mathbf{string}[\mathbf{start} : \mathbf{stop} : \mathbf{step}]$$

- `start`: Indeks awal pemotongan (inklusif). Jika dikosongkan, default adalah `0`.
- `stop`: Indeks akhir pemotongan (**eksklusif**). Jika dikosongkan, default adalah akhir string.
- `step`: Langkah inkremen/arah pergerakan (default adalah `1`).

```python
payload = "HEADER_DATA_CRC"

print(payload[0:6])   # 'HEADER' (indeks 0 sampai 5)
print(payload[7:11])  # 'DATA'
print(payload[12:])   # 'CRC' (dari indeks 12 hingga selesai)
print(payload[:6])    # 'HEADER' (dari awal hingga indeks 5)
print(payload[::2])   # 'HAE_AACC' (setiap langkah 2 karakter)
print(payload[::-1])  # 'CRC_ATAD_REDAEH' (pembalikan string utuh!)
```

---

## 4. Metode String Bawaan Penting (*Essential String Methods*)

Python menyediakan pustaka metode manipulasi teks yang sangat kaya:

| Metode | Fungsi / Deskripsi | Contoh | Hasil |
|:---|:---|:---|:---|
| `.strip()` | Menghapus spasi atau karakter whitespace di awal & akhir | `"  LTE  ".strip()` | `"LTE"` |
| `.lower()` | Mengonversi seluruh huruf menjadi huruf kecil | `"Wi-Fi".lower()` | `"wi-fi"` |
| `.upper()` | Mengonversi seluruh huruf menjadi huruf kapital | `"node".upper()` | `"NODE"` |
| `.title()` | Mengubah huruf pertama setiap kata menjadi kapital | `"aji pamungkas".title()` | `"Aji Pamungkas"` |
| `.split(sep)` | Memecah string menjadi list potongan berdasarkan pemisah | `"A;B;C".split(";")` | `['A', 'B', 'C']` |
| `.join(list)` | Menggabungkan elemen iterable dengan string perekat | `"-".join(['BTS', '01'])` | `"BTS-01"` |
| `.replace(a, b)` | Menggantikan kemunculan substring `a` dengan `b` | `"v1.0".replace("1", "2")` | `"v2.0"` |
| `.find(sub)` | Mengembalikan indeks pertama substring (atau `-1` jika nihil) | `"Koneksi".find("neks")` | `2` |
| `.count(sub)` | Menghitung frekuensi kemunculan substring | `"BANANA".count("A")` | `3` |
| `.startswith(x)`| Memeriksa apakah string diawali prefiks tertentu | `"NODE-1".startswith("NODE")`| `True` |
| `.endswith(x)` | Memeriksa apakah string diakhiri sufiks tertentu | `"data.csv".endswith(".csv")`| `True` |

---

## 5. Validasi Tipe Karakter (*Character Type Checking*)

Untuk membersihkan dan memvalidasi data pengenal perangkat atau masukan formulir:
- `.isalnum()`: `True` jika seluruh karakter adalah huruf atau angka (tanpa spasi/simbol).
- `.isalpha()`: `True` jika seluruh karakter hanya huruf alfabet.
- `.isdigit()`: `True` jika seluruh karakter hanya digit angka bulat (`0-9`).
- `.isspace()`: `True` jika seluruh karakter hanya whitespace (spasi, tab, newline).

---

## 6. Parsing Pesan Sensor Terstruktur

Dalam telemetri jaringan IoT dan BTS, pesan sensor sering kali dikirim dalam format terstruktur sederhana dengan pemisah (*delimiter*):

```python
payload_mentah = "ID=NODE-04;FREQ=1800.5;PWR=40.0;STAT=ACTIVE"

# 1. Pecah payload menjadi pasangan-pasangan kunci=nilai
pasangan_token = payload_mentah.split(";")

data = {}
for token in pasangan_token:
    kunci, nilai = token.split("=")
    data[kunci] = nilai

print(f"Perangkat: {data['ID']} beroperasi pada {data['FREQ']} MHz dengan daya {data['PWR']} W.")
```

---

## 7. Kesalahan Umum Pengolahan String (*Common Pitfalls*)

1. **Percobaan Mutasi Karakter (*Item Assignment Error*):** Mencoba mengubah karakter secara langsung: `teks[0] = 'X'`. Solusi: buat string baru dengan penggabungan atau *slicing*.
2. **Indeks Di Luar Jangkauan (*IndexError: string index out of range*):** Mengakses indeks $\ge \text{len}(s)$. Selalu periksa panjang string dengan `len(s)` atau gunakan slicing `s[0:10]` yang aman dari *IndexError*.
3. **Lupa Bahwa Metode String Mengembalikan String Baru:** Menulis `teks.strip()` tanpa menampungnya kembali ke variabel: `teks = teks.strip()`.
4. **Kesalahan Pemisah `.split()`:** Jika pemisah tidak ditemukan, `.split()` akan mengembalikan list berisi 1 elemen (string utuh asli), bukan galat.

---

## 8. Ringkasan Bab

- String adalah sequence immutable dari karakter Unicode.
- Pengindeksan zero-based mendukung indeks positif (kiri) dan negatif (kanan).
- Slicing `[start:stop:step]` mengekstrak bagian teks dengan aman tanpa memodifikasi string asli.
- Metode bawaan seperti `.strip()`, `.split()`, `.join()`, `.replace()`, dan `.find()` adalah alat vital dalam pembersihan dan parsing teks.
- Validasi pengenal perangkat dan penguraian protokol IoT dapat diimplementasikan dengan kombinasi slicing dan split.

---

## 9. Referensi & Sumber Belajar Terbuka

1. **Python Software Foundation**, *An Informal Introduction to Python: Text*, [https://docs.python.org/3/tutorial/introduction.html#text](https://docs.python.org/3/tutorial/introduction.html#text) (PSF License 2.0).
2. **Python Software Foundation**, *Standard Library: String Methods*, [https://docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods) (PSF License 2.0).
3. **Allen B. Downey**, *Think Python (3rd Edition)*, Chapter 7: Strings, [https://allendowney.github.io/ThinkPython/](https://allendowney.github.io/ThinkPython/) (CC BY-NC 4.0).
4. **Asabeneh S. Yetayeh**, *30 Days Of Python*, Day 04: Strings, [https://github.com/Asabeneh/30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) (MIT License).
