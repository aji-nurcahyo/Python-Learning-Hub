# Chapter 13 — Advanced Functions
> **Parameter Dinamis (*args & **kwargs), Lambda, First-Class Citizens, Closures, dan Rekursi**  
> *Level 2 · Intermediate · Estimasi Belajar: 4–5 Jam Pembelajaran*

---

## 1. Pengantar Fungsi Tingkat Lanjut

Pada Level 1 (khususnya Chapter 10), Anda telah mempelajari dasar-dasar perancangan fungsi dengan deklarasi `def`, parameter formal, nilai balik `return`, serta aturan ruang lingkup variabel LEGB (*Local, Enclosing, Global, Built-in*). 

Dalam rekayasa perangkat lunak skala menengah hingga besar, fungsi dituntut untuk jauh lebih fleksibel:
- Menerima jumlah argumen yang dinamis tanpa mengubah tanda tangan fungsi (*function signature*).
- Menjamin stabilitas antarmuka melalui pembatasan posisi dan kata kunci (*positional-only* dan *keyword-only*).
- Mengisolasi *state* lokal menggunakan penutupan lingkup (*closures*) tanpa harus mendefinisikan kelas berorientasi objek secara penuh.
- Memperlakukan fungsi sebagai nilai yang dapat disimpan, dikirimkan sebagai parameter, dan dikembalikan oleh fungsi lain (*first-class citizens*).

Bab ini mengantarkan Anda menguasai paradigma fungsional dan sintaksis tingkat lanjut Python untuk membangun pustaka kode yang bersih, modular, dan teruji.

---

## 2. Parameter Posisi, Kata Kunci, Default, dan Pembatas Sintaksis

Python mengevaluasi pemanggilan fungsi melalui dua mekanisme pengiriman argumen:
1. **Positional Arguments:** Nilai dicocokkan berdasarkan urutan kemunculannya di tanda tangan fungsi.
2. **Keyword Arguments:** Nilai dicocokkan secara eksplisit menggunakan nama parameter: `nama_parameter=nilai`.

```python
def konfigurasi_perangkat(node_id: int, frekuensi_mhz: float = 2400.0, status: str = "AKTIF") -> str:
    return f"Node {node_id} @ {frekuensi_mhz} MHz [{status}]"

# Pemanggilan posisi, default, dan keyword
print(konfigurasi_perangkat(101))                                      # Default frekuensi & status
print(konfigurasi_perangkat(102, 5000.0))                             # Posisi override default
print(konfigurasi_perangkat(103, status="SIAGA", frekuensi_mhz=900.0)) # Keyword acak urutan
```

### Pembatas Sintaksis: Positional-Only (`/`) dan Keyword-Only (`*`)

Mulai Python 3.8 (PEP 570), Python memperkenalkan penanda garis miring (`/`) untuk menentukan parameter mana yang **hanya boleh** diisi secara posisi, dan tanda bintang (`*`) untuk parameter yang **wajib** diisi secara kata kunci (PEP 3102):

```python
def atur_antena(id_antena: int, /, gain_dbi: float, *, polarisasi: str = "VERTIKAL") -> str:
    """
    id_antena   : POSITIONAL-ONLY (wajib urutan, dilarang id_antena=1)
    gain_dbi    : BEBAS (bisa posisi atau kata kunci)
    polarisasi  : KEYWORD-ONLY (wajib polarisasi='HORISONTAL')
    """
    return f"Antena #{id_antena} (Gain: {gain_dbi} dBi, Polaritas: {polarisasi})"

# Pemanggilan valid:
print(atur_antena(1, 15.5, polarisasi="HORISONTAL"))
print(atur_antena(2, gain_dbi=18.0))

# Pemanggilan ILEGAL (akan memicu TypeError):
# atur_antena(id_antena=1, gain_dbi=15.5)  -> TypeError: positional-only argument passed as keyword
# atur_antena(1, 15.5, "HORISONTAL")       -> TypeError: takes 2 positional arguments but 3 were given
```

> [!NOTE]
> **Kapan Menggunakan `/` dan `*`?**  
> Gunakan `/` jika nama parameter tidak memiliki arti semantik bagi pengguna eksternal (misal: `abs(x)` atau `len(obj)`) sehingga pengembang bebas mengganti nama internal parameter tanpa merusak kode pemanggil. Gunakan `*` untuk parameter opsi/konfigurasi agar pengguna terbiasa menuliskan nama parameter secara eksplisit guna menghindari kesalahan argumen boolean atau numerik yang tertukar.

---

## 3. Parameter Arbitrer: `*args` dan `**kwargs`

Dalam banyak skenario praktis, jumlah data yang akan diproses oleh fungsi tidak dapat diprediksi saat fungsi didefinisikan. Python menyediakan dua operator kemas (*packing operators*):

### A. Variable-Length Positional Arguments (`*args`)
Operator bintang tunggal (`*`) mengemas semua kelebihan argumen posisi yang diberikan menjadi sebuah objek **tuple**:

```python
def hitung_rata_rata(*nilai: float) -> float:
    if not nilai:
        return 0.0
    return round(sum(nilai) / len(nilai), 2)

print(hitung_rata_rata(10.0, 20.0, 30.0))       # nilai = (10.0, 20.0, 30.0) -> Output: 20.0
print(hitung_rata_rata(85.5, 90.0, 95.0, 100.0)) # nilai = (85.5, 90.0, 95.0, 100.0)
```

### B. Arbitrary Keyword Arguments (`**kwargs`)
Operator bintang ganda (`**`) mengemas semua argumen kata kunci yang tidak tercantum dalam tanda tangan fungsi menjadi sebuah objek **dictionary**:

```python
def catat_log_server(level: str, pesan: str, **metadata: object) -> None:
    print(f"[{level.upper()}] {pesan}")
    for kunci, nilai in metadata.items():
        print(f"  > {kunci}: {nilai}")

catat_log_server("ERROR", "Koneksi gateway terputus", ip="10.0.0.1", port=8080, latency_ms=450.2)
```

### C. Pembongkaran Argumen (*Argument Unpacking*)
Kebalikan dari packing, kita dapat menggunakan `*` untuk membongkar elemen list/tuple ke dalam argumen posisi, dan `**` untuk membongkar pasangan dictionary ke argumen kata kunci:

```python
sampel = [14.0, 18.5, 22.0]
print(hitung_rata_rata(*sampel))  # Identik dengan hitung_rata_rata(14.0, 18.5, 22.0)

opsi = {"polarisasi": "CIRCULAR"}
print(atur_antena(3, 12.0, **opsi))
```

---

## 4. Jebakan Memori: Mutable Default Arguments

Salah satu kesalahan paling umum namun berbahaya dalam Python adalah menggunakan objek yang dapat diubah (*mutable object*, seperti `list` atau `dict`) sebagai nilai default parameter:

```python
# PERILAKU CACAT (MUTABLE DEFAULT):
def tambah_riwayat(item: str, daftar_riwayat: list[str] = []) -> list[str]:
    daftar_riwayat.append(item)
    return daftar_riwayat

print(tambah_riwayat("Log 1"))  # Output: ['Log 1']
print(tambah_riwayat("Log 2"))  # Output: ['Log 1', 'Log 2'] -> BUKAN ['Log 2']!
```

### Mengapa Hal Ini Terjadi?
Di dalam arsitektur CPython, ekspresi nilai default **hanya dievaluasi sekali** saat deklarasi fungsi dikompilasi ke dalam memori (*definition time*), bukan setiap kali fungsi dipanggil (*call time*). Akibatnya, setiap pemanggilan fungsi tanpa argumen eksplisit akan berbagi objek list yang persis sama di memori heap.

### Solusi Idiomatis: Sentinel `None`
Gunakan objek imutabel `None` sebagai penanda default, lalu buat instance list baru di dalam badan fungsi:

```python
def tambah_riwayat_benar(item: str, daftar_riwayat: list[str] | None = None) -> list[str]:
    if daftar_riwayat is None:
        daftar_riwayat = []  # List baru diisolasi untuk setiap panggilan mandiri
    daftar_riwayat.append(item)
    return daftar_riwayat

print(tambah_riwayat_benar("Log 1"))  # Output: ['Log 1']
print(tambah_riwayat_benar("Log 2"))  # Output: ['Log 2'] -> Bersih dan independen!
```

---

## 5. Fungsi Sebagai First-Class Citizen & Higher-Order Functions

Di dalam bahasa Python, fungsi adalah **warga kelas satu** (*first-class citizens*). Ini berarti fungsi memiliki status yang setara dengan tipe data skalar lainnya:
- Dapat disimpan ke dalam variabel.
- Dapat dimasukkan sebagai elemen di dalam koleksi data (*list, dict*).
- Dapat diteruskan sebagai argumen ke fungsi lain.
- Dapat dikembalikan sebagai nilai balik (*return value*) oleh fungsi lain.

Fungsi yang menerima fungsi lain sebagai parameter atau mengembalikan fungsi disebut **Higher-Order Function**.

```python
from typing import Callable

def kuadratkan(x: float) -> float:
    return x ** 2

def kalikan_sepuluh(x: float) -> float:
    return x * 10.0

def transformasikan_data(data: list[float], operasi: Callable[[float], float]) -> list[float]:
    """Higher-Order Function yang mengeksekusi operasi kustom pada setiap elemen data."""
    return [operasi(elemen) for elemen in data]

angka = [1.0, 2.0, 3.0, 4.0]
print("Kuadrat :", transformasikan_data(angka, kuadratkan))
print("Kali 10 :", transformasikan_data(angka, kalikan_sepuluh))
```

---

## 6. Ekspresi Lambda: Fungsi Anonim Satu Baris

Ekspresi `lambda` memungkinkan pembuatan fungsi anonim (*tanpa nama*) yang ringkas untuk digunakan secara instan. Sintaks dasar lambda adalah:
$$\text{lambda}\ \text{parameter}_1, \text{parameter}_2, \dots : \text{ekspresi}$$

```python
# Lambda konversi Celsius ke Fahrenheit
c_to_f = lambda c: (c * 9/5) + 32
print(f"100 C = {c_to_f(100)} F")
```

### Penerapan Utama Lambda: Custom Key pada Sorting
Ekspresi lambda paling sering digunakan sebagai argumen `key` pada fungsi `sorted()` atau metode `.sort()` ketika mengurutkan data majemuk (*list of dictionaries* atau tuples):

```python
server_nodes = [
    {"nama": "Node-Alpha", "beban_persen": 82.5, "koneksi": 150},
    {"nama": "Node-Beta",  "beban_persen": 45.0, "koneksi": 40},
    {"nama": "Node-Gamma", "beban_persen": 82.5, "koneksi": 90},
]

# Urutkan berdasarkan beban tertinggi (descending), jika sama urutkan koneksi terbanyak
terurut = sorted(server_nodes, key=lambda s: (s["beban_persen"], s["koneksi"]), reverse=True)
for s in terurut:
    print(f"  {s['nama']:<12} | Beban: {s['beban_persen']}% | Koneksi: {s['koneksi']}")
```

---

## 7. Closures, Lexical Scope, dan Kata Kunci `nonlocal`

Sebuah **Closure** terjadi ketika sebuah fungsi bersarang (*inner function*) mengikat dan mengingat variabel-variabel di lingkungan luarnya (*enclosing scope*), bahkan setelah fungsi terluar (*outer function*) telah selesai dieksekusi dan keluar dari call stack.

```python
from typing import Callable

def buat_pemberi_diskon(persen_diskon: float) -> Callable[[float], float]:
    """Pabrik fungsi closure yang mengunci variabel persen_diskon."""
    def hitung_harga_akhir(harga_awal: float) -> float:
        potongan = harga_awal * (persen_diskon / 100.0)
        return round(harga_awal - potongan, 2)
    
    return hitung_harga_akhir

diskon_member = buat_pemberi_diskon(15.0)  # Menghasilkan closure dengan diskon 15%
diskon_promo  = buat_pemberi_diskon(30.0)  # Menghasilkan closure dengan diskon 30%

print("Harga Rp100.000 (Member): Rp", diskon_member(100000.0)) # Rp 85000.0
print("Harga Rp100.000 (Promo) : Rp", diskon_promo(100000.0))  # Rp 70000.0
```

### Kata Kunci `nonlocal`
Jika fungsi di dalam closure perlu **memodifikasi** nilai variabel di enclosing scope (bukan hanya membacanya), gunakan pernyataan `nonlocal`:

```python
def buat_akumulator_saldo(saldo_awal: float = 0.0) -> Callable[[float], float]:
    saldo = saldo_awal

    def transaksi(nominal: float) -> float:
        nonlocal saldo  # Mengizinkan mutasi variabel saldo di enclosing scope
        saldo += nominal
        return saldo

    return transaksi

tabungan = buat_akumulator_saldo(1000.0)
print(tabungan(250.0))   # Saldo menjadi 1250.0
print(tabungan(-100.0))  # Saldo menjadi 1150.0
```

---

## 8. Rekursi: Base Case dan Recursive Step

**Rekursi** adalah teknik pemrograman di mana sebuah fungsi memanggil dirinya sendiri secara berulang untuk menyelesaikan sub-masalah yang berukuran lebih kecil, hingga mencapai kondisi batas akhir yang disebut **Base Case**.

### Struktur Fungsi Rekursif:
1. **Base Case:** Kondisi penghentian mutlak tanpa melakukan panggilan rekursif lanjutan.
2. **Recursive Step:** Pemanggilan fungsi diri sendiri dengan argumen yang dimodifikasi menuju base case.

```python
def hitung_pangkat(basis: float, eksponen: int) -> float:
    """Menghitung basis^eksponen secara rekursif."""
    if eksponen == 0:
        return 1.0  # Base Case: x^0 = 1
    if eksponen < 0:
        return 1.0 / hitung_pangkat(basis, -eksponen)
    return basis * hitung_pangkat(basis, eksponen - 1)  # Recursive Step

print(f"2^8 = {hitung_pangkat(2.0, 8)}")  # Output: 256.0
```

> [!WARNING]
> **Pencegahan `RecursionError`:**  
> Jika base case tidak pernah tercapai atau pemanggilan terlalu dalam, Python akan melemparkan `RecursionError: maximum recursion depth exceeded`. Batas kedalaman stack default CPython adalah 1000 frame (dapat diperiksa melalui `sys.getrecursionlimit()`).

---

## 9. Anotasi Fungsi (*Type Hints*) & Pustaka `typing`

Mulai Python 3.5+, sintaksis anotasi tipe (*type hints*) distandarisasi untuk meningkatkan kualitas kode (*code quality*), dokumentasi mandiri, dan dukungan tooling static analysis:

```python
from typing import Any, Callable, Union

def validasi_dan_transformasi(
    nilai_masukan: Union[int, float, str],
    aturan_validasi: Callable[[float], bool],
    penangan_galat: Callable[[str], None] | None = None
) -> float | None:
    try:
        angka = float(nilai_masukan)
    except ValueError:
        if penangan_galat:
            penangan_galat(f"Gagal konversi numerik: {nilai_masukan}")
        return None

    return angka if aturan_validasi(angka) else None
```

Anotasi tidak membebani performa runtime eksekusi karena diabaikan saat eksekusi CPython biasa, namun metadata anotasi disimpan dan dapat diinspeksi secara dinamis melalui atribut fungsi `func.__annotations__`.

---

## 10. Mini Proyek: Flexible Data Processor

Pada modul ini, Anda merancang sistem pemroses dataset numerik bernama **Flexible Data Processor** yang mengintegrasikan seluruh materi:
- `make_scaler`: Closure yang menghasilkan fungsi penskalaan $f(x) = x \times \text{factor} + \text{offset}$.
- `make_threshold_filter`: Closure yang menghasilkan fungsi predikat penyaring nilai.
- `apply_pipeline`: Higher-order function yang menerapkan rantai fungsi transformasi (`*transforms`) dan filter predikat opsional.
- `summarize_dataset`: Agregator dinamis yang menerima metrik bawaan (`*metrics`) dan metrik kustom tak terbatas (`**custom_aggregators`).

```bash
# Jalankan demonstrasi deterministik
python content/intermediate/chapter-13/code/contoh.py

# Jalankan pengujian unit otomatis
python -m unittest content/intermediate/chapter-13/tests/test_advanced_functions.py
```

---

## 11. Rangkuman & Referensi Pustaka

### Intisari Pembelajaran:
- Gunakan pembatas `/` untuk argumen yang murni berbasis posisi dan `*` untuk parameter yang wajib dinyatakan secara eksplisit dengan namanya.
- Manfaatkan `*args` untuk parameter posisi fleksibel dan `**kwargs` untuk opsi konfigurasi atau kamus dinamis.
- Hindari *mutable default argument* (`data=[]`), selalu gunakan idiom sentinel `data=None`.
- Fungsi adalah objek *first-class* yang dapat digabungkan ke dalam pola *higher-order pipeline*.
- *Closures* membungkus variabel lingkungan lokal untuk menghasilkan fungsi berstatus tanpa overhead kelas OOP.
- Rancang fungsi rekursif dengan memastikan *base case* selalu dapat dicapai.

### Referensi Pustaka:
1. Python Software Foundation. *The Python Tutorial: More on Defining Functions (Section 4.8)*. https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions
2. Python Enhancement Proposals (PEP 570). *Python Positional-Only Parameters*. https://peps.python.org/pep-0570/
3. Python Enhancement Proposals (PEP 3102). *Keyword-Only Arguments*. https://peps.python.org/pep-3102/
4. Allen B. Downey. *Think Python 2e: Functions and Interfaces*. Green Tea Press.
5. Asabeneh Yetayeh. *30 Days of Python: Day 14 - Higher Order Functions*. https://github.com/Asabeneh/30-Days-Of-Python
