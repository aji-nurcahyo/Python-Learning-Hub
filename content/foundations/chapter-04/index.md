# Chapter 04 — Input & Output
> **Interaksi Pengguna & Pemformatan Teks Modern**  
> *Level 1 · Foundations · Beginner · Estimasi Belajar: 2–3 Jam*

---

## 1. Konsep Alur Input/Output Standar (I/O)

Sebagian besar program komputer bekerja berdasarkan model mendasar:
$$\text{Input (Masukan)} \longrightarrow \text{Process (Pemrosesan Logika)} \longrightarrow \text{Output (Keluaran)}$$

Dalam sistem operasi berbasis Unix dan Windows, program berinteraksi dengan dunia luar melalui aliran (*streams*) standar:
- **Standard Input (`stdin`):** Aliran masukan, biasanya berasal dari ketikan keyboard pengguna di konsol.
- **Standard Output (`stdout`):** Aliran keluaran utama, ditampilkan di layar terminal.
- **Standard Error (`stderr`):** Aliran khusus untuk menampilkan pesan galat atau peringatan sistem.

---

## 2. Mengontrol Keluaran dengan `print()`

Fungsi `print()` adalah fungsi bawaan yang paling sering digunakan untuk mengirim data ke `stdout`. Secara default:
1. Setiap argumen dipisahkan dengan spasi (`' '`).
2. Di akhir keluaran selalu ditambahkan karakter baris baru (*newline* `'\n'`).

Anda dapat mengontrol perilaku ini menggunakan dua kata kunci parameter khusus:
- **`sep` (*Separator*):** Menentukan karakter pemisah antar argumen.
- **`end` (*Ending*):** Menentukan karakter penutup setelah semua argumen dicetak.

```python
# Menggunakan pemisah khusus
print("192", "168", "1", "1", sep=".")  # 192.168.1.1

# Menghindari baris baru dengan end="..."
print("Menghubungkan ke server", end="...")
print(" [BERHASIL]")
```

---

## 3. Menerima Masukan Pengguna dengan `input()`

Fungsi `input([prompt])` menjeda eksekusi program dan menunggu pengguna mengetik teks di konsol terminal hingga menekan tombol `Enter`.

> [!IMPORTANT]
> Nilai kembalian fungsi `input()` **selalu bertipe string (`str`)**, bahkan jika pengguna hanya mengetikkan angka (misalnya `"1800"`).

Oleh karena itu, jika data masukan akan digunakan dalam perhitungan matematis, Anda wajib melakukan *type casting* eksplisit:
```python
# Contoh interaktif (saat dijalankan di terminal)
teks_frekuensi = input("Masukkan frekuensi kerja (MHz): ")
frekuensi_mhz = float(teks_frekuensi)  # Konversi ke float untuk perhitungan
```

---

## 4. Interpolasi String Modern dengan f-Strings (PEP 498)

Diperkenalkan sejak Python 3.6, **Formatted String Literals** (dikenal sebagai **f-strings**) adalah cara tercepat, paling bersih, dan paling mudah dibaca untuk menyisipkan ekspresi ke dalam string.

Ciri khas f-string adalah awalan huruf `f` atau `F` sebelum tanda kutip pembuka, dan penempatan variabel atau ekspresi di dalam kurung kurawal `{}`:

```python
nama_node = "BTS-Sukarame-01"
daya = 43.5

# Variabel disisipkan langsung
print(f"Stasiun {nama_node} beroperasi pada daya {daya} dBm.")

# Ekspresi matematika langsung di dalam kurung kurawal
print(f"Daya ganda: {daya * 2} dBm")
print(f"Status uppercase: {nama_node.upper()}")
```

---

## 5. Penentu Format (*Format Specifiers*)

Di dalam f-string, Anda dapat menambahkan tanda titik dua `:` diikuti kode penentu format (*specifier*) untuk mengontrol tampilan visual data:

| Format Specifier | Makna / Kegunaan | Contoh Ekspresi | Hasil Keluaran |
|:---|:---|:---:|:---:|
| `:.2f` | Angka desimal dibulatkan 2 angka di belakang koma | `f"{3.14159:.2f}"` | `3.14` |
| `:.3e` | Notasi ilmiah eksponensial (scientific) | `f"{300000000:.2e}"` | `3.00e+08` |
| `:.1%` | Format persentase dengan 1 desimal | `f"{0.9875:.1%}"` | `98.8%` |
| `:04d` | Bilangan bulat dengan *zero-padding* hingga 4 digit | `f"{7:04d}"` | `0007` |
| `:,` | Pemisah ribuan menggunakan tanda koma | `f"{1500000:,}"` | `1,500,000` |

---

## 6. Desain Antarmuka Teks: Perataan Kolom Tabel (*Alignment*)

Untuk menampilkan data laporan telemetri yang rapi di konsol terminal, Python menyediakan operator perataan teks:
- `<` : Rata kiri (*Left-aligned*)
- `>` : Rata kanan (*Right-aligned*)
- `^` : Rata tengah (*Center-aligned*)

```python
print("=" * 45)
print(f"{'KODE BTS':<12} | {'FREKUENSI':^14} | {'STATUS':>12}")
print("=" * 45)
print(f"{'BTS-01':<12} | {900.0:^10.1f} MHz | {'ONLINE':>12}")
print(f"{'BTS-02':<12} | {1800.5:^10.1f} MHz | {'ONLINE':>12}")
print("=" * 45)
```

Hasil keluaran di terminal:
```text
=============================================
KODE BTS     |   FREKUENSI    |       STATUS
=============================================
BTS-01       |   900.0    MHz |       ONLINE
BTS-02       |   1800.5   MHz |       ONLINE
=============================================
```

---

## 7. Ringkasan Bab

- Aliran standar I/O mencakup `stdin` (masukan), `stdout` (keluaran), dan `stderr` (galat).
- `print()` mendukung argumen `sep` (pemisah antar data) dan `end` (karakter akhiran baris).
- `input()` selalu mengembalikan string; lakukan `int()` atau `float()` jika memerlukan nilai numerik.
- Formatted string literals (f-strings) adalah standar baku interpolasi string modern di Python.
- Format specifiers (`:.2f`, `:,`, `:04d`) dan perataan teks (`<`, `>`, `^`) memungkinkan pembuatan laporan data tabel yang profesional.

---

## 8. Referensi & Sumber Belajar Terbuka

1. **Python Software Foundation**, *Fancier Output Formatting (f-strings & str.format)*, [https://docs.python.org/3/tutorial/inputoutput.html](https://docs.python.org/3/tutorial/inputoutput.html) (PSF License 2.0).
2. **David J. Malan**, *CS50’s Introduction to Programming with Python*, Week 0: Functions, Variables, [https://cs50.harvard.edu/python/](https://cs50.harvard.edu/python/) (CC BY-NC-SA 4.0).
3. **Allen B. Downey**, *Think Python (3rd Edition)*, Chapter 7.3: Formatted String Literals, [https://allendowney.github.io/ThinkPython/](https://allendowney.github.io/ThinkPython/) (CC BY-NC 4.0).
4. **Asabeneh S. Yetayeh**, *30 Days Of Python*, Day 04: Strings & Formatting, [https://github.com/Asabeneh/30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) (MIT License).
