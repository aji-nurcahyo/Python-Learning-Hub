# Chapter 06 — Loops & Iteration
> **Pengulangan for, while, range, break, continue & else**  
> *Level 1 · Foundations · Beginner · Estimasi Belajar: 4 Jam*

---

## 1. Pengantar Iterasi & Pengulangan

Salah satu kekuatan utama komputer dibandingkan manusia adalah kemampuannya mengeksekusi tugas kalkulasi yang sama secara berulang-ulang dengan kecepatan tinggi dan tanpa kelelahan. Proses pengulangan blok instruksi ini disebut **iterasi** (*iteration*) atau **loop**.

Di dalam Python, terdapat dua paradigma pengulangan utama:
1. **Definite Iteration (`for` loop):** Jumlah perulangan telah diketahui sebelumnya atau terikat pada panjang suatu koleksi data (*sequence/iterable*).
2. **Indefinite Iteration (`while` loop):** Jumlah perulangan tidak diketahui di awal dan bergantung pada kebenaran suatu kondisi dinamis yang dievaluasi saat runtime.

---

## 2. Pengulangan Terhitung dengan `for` dan `range()`

Fungsi bawaan `range(start, stop[, step])` menghasilkan deret bilangan aritmatika yang sangat efisien dalam memori:
- `start`: Nilai awal inklusif (default adalah `0`).
- `stop`: Batas akhir **eksklusif** (loop berhenti sebelum menyentuh nilai ini).
- `step`: Besar kenaikan atau penurunan antar nilai (default adalah `1`).

```python
# Iterasi 5 kali: 0, 1, 2, 3, 4
for i in range(5):
    print(f"Iterasi ke-{i}")

# Iterasi dengan kelipatan 5: 10, 15, 20, 25, 30
for f in range(10, 31, 5):
    print(f"Kanal Frekuensi: {f} MHz")
```

---

## 3. Pengulangan Kondisional dengan `while` Loop

Struktur `while` mengeksekusi blok kode selama kondisi pengujian bernilai `True`:

```python
daya = 10.0
while daya < 40.0:
    print(f"Meningkatkan daya pancar: {daya:.1f} W")
    daya += 10.0  # Pembaruan variabel loop (mencegah infinite loop)
```

> [!WARNING]
> **Pencegahan Perulangan Tak Hingga (*Infinite Loop*):**  
> Pastikan variabel kondisi selalu diperbarui di dalam badan loop `while`. Jika kondisi tidak pernah berubah menjadi `False`, program akan terkunci dalam perulangan abadi yang menghabiskan CPU.

---

## 4. Pola Algoritma Dasar: Akumulator & Pencacah (*Counter*)

Dalam rekayasa pengolahan data, dua pola loop paling sering diterapkan:

### A. Pola Pencacah (*Counter Pattern*)
Digunakan untuk menghitung berapa kali suatu peristiwa terjadi:
```python
cacah_sinyal_lemah = 0
for sinyal in daftar_rsrp:
    if sinyal < -90.0:
        cacah_sinyal_lemah += 1
```

### B. Pola Akumulator (*Accumulator Pattern*)
Digunakan untuk menjumlahkan nilai secara bertahap:
```python
total_daya = 0.0
for p in daftar_daya:
    total_daya += p
rata_rata = total_daya / len(daftar_daya) if daftar_daya else 0.0
```

---

## 5. Kontrol Alur Iterasi: `break`, `continue`, dan Klausa `else`

Python menyediakan kata kunci kendali untuk memodifikasi siklus perulangan:

- **`break`:** Menghentikan loop seketika dan langsung keluar dari blok perulangan. Sangat penting untuk memutus loop saat terdeteksi alarm darurat atau saat elemen target telah ditemukan.
- **`continue`:** Mengabaikan sisa instruksi pada iterasi saat ini dan langsung melompat ke iterasi berikutnya. Sangat berguna untuk menyaring data rusak (*glitch/noise*).
- **Klausa `else` pada Loop:** Fitur khas Python di mana blok `else:` akan dieksekusi **hanya jika** loop selesai secara normal (tidak dihentikan secara paksa oleh `break`).

```python
for suhu in sensor_stream:
    if suhu == -999.0:  # Data sensor error
        continue        # Lewati data rusak
    if suhu > 85.0:     # Suhu bahaya kebakaran
        print("BAHAYA: Mesin dimatikan!")
        break
else:
    print("Seluruh pemantauan selesai tanpa insiden kritis.")
```

---

## 6. Perulangan Bersarang (*Nested Loops*)

Loop yang diletakkan di dalam loop lain disebut *nested loop*. Setiap satu kali perulangan pada loop luar (*outer loop*), loop dalam (*inner loop*) akan dieksekusi secara lengkap:

```python
# Pembangkitan koordinat kisi antena MIMO 4x4
for baris in range(1, 5):
    for kolom in range(1, 5):
        print(f"[Antena {baris},{kolom}]", end=" ")
    print()  # Ganti baris setelah kolom selesai
```

---

## 7. Studi Kasus Rekayasa: Pencarian Nilai Ekstrem (Min/Max Manual)

Meskipun Python memiliki fungsi bawaan `min()` dan `max()`, memahami algoritma pencarian nilai minimum dan maksimum manual sangat fundamental:

```python
data_sinyal = [-88.0, -95.5, -74.0, -102.0, -81.5]

nilai_terkecil = data_sinyal[0]
nilai_terbesar = data_sinyal[0]

for s in data_sinyal[1:]:
    if s < nilai_terkecil:
        nilai_terkecil = s
    if s > nilai_terbesar:
        nilai_terbesar = s

print(f"Sinyal Terlemah : {nilai_terkecil} dBm")
print(f"Sinyal Terkuat  : {nilai_terbesar} dBm")
```

---

## 8. Kesalahan Umum pada Perulangan (*Common Pitfalls*)

1. **Kesalahan Batas (*Off-by-One Error*):** Mengingat `range(1, 10)` hanya berjalan dari 1 sampai 9. Jika ingin angka 10 ikut diproses, gunakan `range(1, 11)`.
2. **Infinite Loop pada `while`:** Lupa memperbarui variabel pencacah di dalam blok loop.
3. **Memodifikasi Koleksi Saat Sedang Diiterasi:** Menghapus elemen dari list saat melakukan loop `for item in list:` dapat menyebabkan elemen terlewati karena indeks bergeser.
4. **Variabel Akumulator Tidak Diinisialisasi di Luar Loop:** Menginisialisasi `total = 0` di dalam badan loop menyebabkan nilainya terus ter-reset pada setiap putaran.

---

## 9. Ringkasan Bab

- `for` digunakan untuk iterasi yang batasnya terdefinisi; `while` digunakan untuk iterasi kondisional.
- Fungsi `range(start, stop, step)` menghasilkan rentang bilangan aritmatika tanpa menduplikasi alokasi memori.
- `break` memutus perulangan seketika; `continue` melompati sisa baris pada putaran aktif.
- Pola akumulator dan counter adalah landasan komputasi statistik data streaming.
- Klausa `else` pada loop dieksekusi hanya jika perulangan tuntas tanpa interupsi `break`.

---

## 10. Referensi & Sumber Belajar Terbuka

1. **Python Software Foundation**, *More Control Flow Tools: for Statements and range()*, [https://docs.python.org/3/tutorial/controlflow.html#for-statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements) (PSF License 2.0).
2. **Allen B. Downey**, *Think Python (3rd Edition)*, Chapter 6: Iteration, [https://allendowney.github.io/ThinkPython/](https://allendowney.github.io/ThinkPython/) (CC BY-NC 4.0).
3. **Software Carpentry**, *Programming with Python: Repeating Actions with Loops*, [https://swcarpentry.github.io/python-novice-inflammation/02-loop/](https://swcarpentry.github.io/python-novice-inflammation/02-loop/) (CC BY 4.0).
4. **David J. Malan**, *CS50’s Introduction to Programming with Python*, Week 2: Loops, [https://cs50.harvard.edu/python/](https://cs50.harvard.edu/python/) (CC BY-NC-SA 4.0).
