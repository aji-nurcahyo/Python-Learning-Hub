# Chapter 03 — Operators & Expressions
> **Aritmatika, Perbandingan, Logika & Presedensi Operator**  
> *Level 1 · Foundations · Beginner · Estimasi Belajar: 3 Jam*

---

## 1. Pengantar Operator & Ekspresi

Dalam pemrograman komputer, **operator** adalah simbol khusus yang menginstruksikan interpreter untuk melakukan operasi matematika, relasional, atau logika tertentu pada satu atau lebih nilai data. Nilai yang dioperasikan disebut **operan** (*operand*). Kombinasi antara operator, variabel, literal, dan pemanggilan fungsi yang menghasilkan suatu nilai keluaran disebut sebagai **ekspresi** (*expression*).

---

## 2. Operator Aritmatika Python

Python menyediakan sekumpulan operator aritmatika yang lengkap dan intuitif:

| Operator | Operasi | Contoh | Hasil | Keterangan |
|:---:|:---|:---:|:---:|:---|
| `+` | Penjumlahan | `15 + 4` | `19` | Menjumlahkan dua nilai numerik |
| `-` | Pengurangan | `15 - 4` | `11` | Mengurangkan operan kanan dari kiri |
| `*` | Perkalian | `15 * 4` | `60` | Mengalikan dua operan |
| `/` | Pembagian Riil | `15 / 4` | `3.75` | Selalu menghasilkan tipe `float` |
| `//` | Pembagian Bulat (*Floor Division*) | `15 // 4` | `3` | Membulatkan ke bawah menuju bilangan bulat terdekat |
| `%` | Modulo (*Sisa Bagi*) | `15 % 4` | `3` | Mengembalikan sisa hasil bagi bulat |
| `**` | Eksponensial (*Pangkat*) | `2 ** 4` | `16` | Operan kiri dipangkatkan operan kanan |

> [!NOTE]
> Perhatikan bahwa operator pembagian tunggal `/` di Python 3 **selalu** menghasilkan tipe data `float`, meskipun kedua operannya adalah bilangan bulat genap (misalnya `8 / 2` menghasilkan `4.0`, bukan `4`).

---

## 3. Operator Perbandingan (Relasional)

Operator perbandingan digunakan untuk membandingkan dua nilai dan selalu menghasilkan nilai logika bertipe `bool` (`True` atau `False`):

- `==` : Sama dengan (*Equal to*)
- `!=` : Tidak sama dengan (*Not equal to*)
- `>`  : Lebih besar dari (*Greater than*)
- `<`  : Lebih kecil dari (*Less than*)
- `>=` : Lebih besar atau sama dengan
- `<=` : Lebih kecil atau sama dengan

Dalam bidang rekayasa sinyal nirkabel, operator pembanding sering dipakai untuk memeriksa apakah kekuatan sinyal terukur (RSRP) berada di atas nilai ambang batas (*threshold*):
```python
rsrp_terukur = -85
ambang_sinyal_bagus = -90

sinyal_memenuhi_syarat = rsrp_terukur >= ambang_sinyal_bagus  # True (-85 lebih besar dari -90)
```

---

## 4. Operator Logika & Evaluasi Short-Circuit

Python menyediakan tiga operator logika boolean: `and`, `or`, dan `not`.

1. **`and` (Konjungsi):** Menghasilkan `True` hanya jika kedua operan bernilai `True`.
2. **`or` (Disjungsi):** Menghasilkan `True` jika salah satu atau kedua operan bernilai `True`.
3. **`not` (Negasi/Inversi):** Membalik nilai kebenaran (`not True` menjadi `False`, `not False` menjadi `True`).

### Evaluasi Pemotongan Pendek (*Short-Circuit Evaluation*)
Interpreter Python mengevaluasi ekspresi logika dari kiri ke kanan secara efisien:
- Pada ekspresi `A and B`: Jika operan $A$ bernilai `False`, Python **tidak akan mengevaluasi** operan $B$ karena hasil akhirnya sudah pasti `False`.
- Pada ekspresi `A or B`: Jika operan $A$ bernilai `True`, Python **tidak akan mengevaluasi** operan $B$ karena hasil akhirnya sudah pasti `True`.

Sifat ini sangat bermanfaat untuk mencegah error pembagian dengan nol atau mengakses properti objek yang tidak ada (*null-safety*):
```python
pembagi = 0
# Aman dieksekusi tanpa ZeroDivisionError karena pembagi != 0 menghasilkan False seketika
aman = (pembagi != 0) and (100 / pembagi > 5)
```

---

## 5. Presedensi Operator & Compound Assignment

Ketika sebuah ekspresi memiliki banyak operator, Python menerapkan aturan hierarki prioritas pengerjaan (*Order of Precedence*):

1. **Tanda Kurung `()`:** Memiliki prioritas tertinggi.
2. **Eksponensial `**`:** Dikerjakan berikutnya (asosiatif kanan-ke-kiri).
3. **Perkalian, Pembagian, Modulo `*`, `/`, `//`, `%`:** Dikerjakan sebelum penjumlahan.
4. **Penjumlahan dan Pengurangan `+`, `-`:** Dikerjakan dari kiri ke kanan.
5. **Operator Perbandingan `==`, `!=`, `<`, `>`, `<=`, `>=`**
6. **Operator Logika `not`, `and`, `or`** (berurutan: `not` dulu, lalu `and`, lalu `or`).

### Operator Penugasan Gabungan (*Compound Assignment*)
Untuk mempersingkat pembaruan nilai variabel, Python menyediakan operator gabungan seperti:
- `x += 5` setara dengan `x = x + 5`
- `x -= 2` setara dengan `x = x - 2`
- `x *= 3` setara dengan `x = x * 3`
- `x //= 2` setara dengan `x = x // 2`

---

## 6. Studi Kasus Rekayasa: Panjang Gelombang & Konversi Daya dBm

Dalam sistem komunikasi radio, panjang gelombang elektromagnetik ($\lambda$) berbanding terbalik dengan frekuensi pembawa ($f$):
$$\lambda = \frac{c}{f}$$

Di mana $c = 3 \times 10^8\text{ m/s}$. Pada frekuensi $f = 1.8\text{ GHz}$ ($1.8 \times 10^9\text{ Hz}$):
$$\lambda = \frac{3 \times 10^8}{1.8 \times 10^9} = 0.1667\text{ meter} \approx 16.67\text{ cm}$$

Selain itu, daya pemancar radio sering dinyatakan dalam desibel-miliwatt ($\text{dBm}$) untuk menyederhanakan perhitungan rugi-rugi lintasan:
$$P_{\text{dBm}} = 10 \cdot \log_{10}(P_{\text{mW}})$$

Pada daya 40 Watt ($40\,000\text{ mW}$):
$$P_{\text{dBm}} = 10 \cdot \log_{10}(40000) = 10 \cdot 4.602 = 46.02\text{ dBm}$$

```python
import math

c = 3e8
f_hz = 1.8e9
panjang_gelombang = c / f_hz

daya_mw = 40000
daya_dbm = 10 * math.log10(daya_mw)

print(f"Panjang Gelombang: {panjang_gelombang * 100:.2f} cm")
print(f"Level Daya: {daya_dbm:.2f} dBm")
```

---

## 7. Ringkasan Bab

- Operator adalah simbol instruksi komputasi yang memanipulasi satu atau lebih operan.
- Pembagian `/` di Python selalu menghasilkan float; pembagian bulat `//` menghasilkan integer yang dibulatkan ke bawah; operator `%` mengembalikan sisa pembagian.
- Operator perbandingan menghasilkan nilai boolean `True` atau `False`.
- Operator logika `and` dan `or` bekerja menggunakan prinsip *short-circuit evaluation*.
- Gunakan tanda kurung `()` secara eksplisit untuk menjamin urutan evaluasi ekspresi matematika yang kompleks.

---

## 8. Referensi & Sumber Belajar Terbuka

1. **Python Software Foundation**, *An Informal Introduction to Python: Numbers*, [https://docs.python.org/3/tutorial/introduction.html#numbers](https://docs.python.org/3/tutorial/introduction.html#numbers) (PSF License 2.0).
2. **Allen B. Downey**, *Think Python (3rd Edition)*, Chapter 2.4: Expressions and Statements, [https://allendowney.github.io/ThinkPython/](https://allendowney.github.io/ThinkPython/) (CC BY-NC 4.0).
3. **Asabeneh S. Yetayeh**, *30 Days Of Python*, Day 03: Operators, [https://github.com/Asabeneh/30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) (MIT License).
4. **Oleksii Trekhleb**, *Learn Python: Operators*, [https://github.com/trekhleb/learn-python](https://github.com/trekhleb/learn-python) (MIT License).
