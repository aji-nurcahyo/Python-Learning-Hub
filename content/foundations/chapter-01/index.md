# Chapter 01 — Introduction to Python
> **Filosofi, Ekosistem & Eksekusi Program Pertama**  
> *Level 1 · Foundations · Beginner · Estimasi Belajar: 2–3 Jam*

---

## 1. Pengantar Pemrograman & Bahasa Python

Dalam dunia rekayasa komputasi dan teknologi informasi modern, bahasa pemrograman merupakan jembatan utama antara logika pemikiran manusia dan eksekusi instruksi pada mesin komputasi. **Python** adalah bahasa pemrograman tingkat tinggi (*high-level*), berorientasi objek (*object-oriented*), dan bersifat serbaguna (*general-purpose*) yang diciptakan oleh **Guido van Rossum** dan dirilis pertama kali pada tahun 1991.

### Mengapa Python?
Python dirancang dengan penekanan kuat pada **keterbacaan kode** (*code readability*). Filosofi desainnya menyatakan bahwa "kode lebih sering dibaca daripada ditulis". Karakteristik utama Python meliputi:
1. **Sintaks Bersih dan Ekspresif:** Menggunakan indentasi visual alami alih-alih kurung kurawal `{}` atau kata kunci pembuka/penutup seperti `begin ... end`.
2. **Multi-paradigma:** Mendukung pemrograman prosedural, fungsional, dan berorientasi objek secara fleksibel.
3. **Ekosistem Standard Library yang Lengkap ("Batteries Included"):** Dilengkapi pustaka bawaan untuk pengolahan teks, matematika numerik, komunikasi jaringan, manajemen sistem berkas, hingga kriptografi.
4. **Relevansi Luas:** Menjadi standar de-facto dalam *Data Science*, *Machine Learning*, otomasi infrastruktur jaringan telekomunikasi (*Network Automation*), dan pengembangan *Cloud & Backend*.

---

## 2. Cara Kerja Interpreter CPython

Secara umum, bahasa pemrograman dibagi menjadi bahasa terkompilasi (*compiled*) dan bahasa terinterpretasi (*interpreted*). Python menggunakan model hibrida melalui implementasi baku resminya, yaitu **CPython**:

```text
[Kode Sumber (.py)] 
       │
       ▼ (Kompilasi Otomatis)
[Python Bytecode (.pyc dalam __pycache__)]
       │
       ▼ (Interpretasi Virtual Machine)
[Python Virtual Machine (PVM) -> CPU Execution]
```

1. **Tahap Kompilasi Bytecode:** Saat sebuah berkas `.py` dijalankan, interpreter CPython terlebih dahulu mengompilasinya menjadi representasi perantara tingkat rendah yang disebut **Bytecode** (`.pyc`).
2. **Tahap Eksekusi Mesin Virtual (PVM):** PVM membaca rangkaian instruksi bytecode dan menerjemahkannya ke dalam bahasa mesin instruksi CPU fisik komputer.
3. **Sifat Interaktif (REPL):** Python menyediakan lingkungan *Read-Eval-Print Loop* di mana setiap baris ekspresi dapat langsung dievaluasi seketika tanpa harus menyusun alur kompilasi penuh.

---

## 3. Menulis dan Menjalankan Skrip Pertama

Program paling mendasar dalam pemrograman adalah menampilkan pesan teks ke layar konsol terminal menggunakan fungsi bawaan `print()`.

```python
# Program Pertama di Python Learning Hub
print("Selamat datang di Python Learning Hub!")
print("Belajar Pemrograman Python untuk Rekayasa Telekomunikasi.")
```

### Aturan Dasar Penulisan Kode Python
- **Komentar (*Comments*):** Karakter tanda pagar `#` digunakan untuk menulis komentar satu baris. Interpreter akan mengabaikan seluruh teks setelah tanda `#` hingga akhir baris tersebut.
- **Docstring:** Teks yang diapit oleh tripel kutip `""" ... """` atau `''' ... '''` digunakan untuk mendokumentasikan modul atau fungsi sesuai pedoman standar **PEP 257**.
- **Kepekaan Huruf (*Case Sensitivity*):** Variabel `sinyal`, `Sinyal`, dan `SINYAL` adalah tiga entitas yang sepenuhnya berbeda di dalam memori.
- **Indentasi 4 Spasi (*Indentation Rule*):** Berdasarkan panduan gaya **PEP 8**, Python menggunakan 4 spasi untuk mendefinisikan blok kendali atau hierarki eksekusi logika. Hindari mencampur karakter spasi dan tab.

---

## 4. Studi Kasus Komputasi: Propagasi Gelombang Radio

Dalam bidang rekayasa telekomunikasi, kita sering menghitung waktu tempuh perambatan gelombang radio (*propagation delay*) dari pemancar (Base Transceiver Station / BTS) ke perangkat penerima (User Equipment / UE).

Rumus fisika dasar perambatan gelombang:
$$t = \frac{d}{v}$$

Di mana:
- $t$ adalah waktu tempuh perambatan gelombang (sekon).
- $d$ adalah jarak spasial antara pemancar dan penerima (meter).
- $v$ adalah kecepatan rambat gelombang elektromagnetik ($3 \times 10^8\text{ m/s}$).

Jika jarak $d = 1500\text{ meter}$, maka waktu rambat dapat dihitung secara instan melalui skrip Python sederhana:

```python
jarak_meter = 1500.0
kecepatan_cahaya = 3e8

waktu_propagasi_detik = jarak_meter / kecepatan_cahaya
waktu_propagasi_mikrodetik = waktu_propagasi_detik * 1e6

print("Waktu Tempuh Propagasi:", waktu_propagasi_mikrodetik, "mikrodetik")
```

---

## 5. Ringkasan Bab

- Python adalah bahasa pemrograman interpretatif tingkat tinggi dengan fokus utama pada kejelasan sintaks dan produktivitas pengembang.
- CPython menerjemahkan kode sumber menjadi bytecode sebelum dieksekusi oleh Python Virtual Machine (PVM).
- Komentar satu baris diawali `#` dan tidak diproses oleh mesin.
- Python bersifat *case-sensitive* dan mewajibkan indentasi yang konsisten (standar 4 spasi PEP 8).
- Eksekusi skrip dimulai dari baris paling atas menuju baris terbawah secara sekuensial.

---

## 6. Referensi & Sumber Belajar Terbuka

1. **Python Software Foundation**, *The Python Tutorial: Whetting Your Appetite & Using the Python Interpreter*, [https://docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/) (PSF License 2.0).
2. **Allen B. Downey**, *Think Python: How to Think Like a Computer Scientist (3rd Edition)*, Chapter 1: The Way of the Program, [https://allendowney.github.io/ThinkPython/](https://allendowney.github.io/ThinkPython/) (CC BY-NC 4.0).
3. **Asabeneh S. Yetayeh**, *30 Days Of Python*, Day 01: Introduction, [https://github.com/Asabeneh/30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) (MIT License).
4. **David J. Malan**, *CS50’s Introduction to Programming with Python*, Week 0: Functions, Variables, [https://cs50.harvard.edu/python/](https://cs50.harvard.edu/python/) (CC BY-NC-SA 4.0).
