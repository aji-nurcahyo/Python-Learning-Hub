# Chapter 05 — Conditional Statements
> **Pengambilan Keputusan: if, elif, else & Guard Clauses**  
> *Level 1 · Foundations · Beginner · Estimasi Belajar: 3–4 Jam*

---

## 1. Pengantar Logika Percabangan

Dalam pemrograman komputer, alur program normal berjalan secara sekuensial (baris demi baris dari atas ke bawah). Namun, program yang cerdas dan realistis harus mampu **mengambil keputusan** (*decision making*) secara adaptif berdasarkan kondisi atau data masukan yang diterimanya.

Mekanisme pengambilan keputusan ini dikendalikan oleh **pernyataan kondisional** (*conditional statements*), di mana blok kode tertentu hanya akan dieksekusi jika suatu ekspresi boolean menghasilkan nilai kebenaran `True`.

```text
               [Ekspresi Boolean]
                     │
            True ────┴──── False
             │               │
             ▼               ▼
     [Blok if/elif]     [Blok else / Lewati]
```

---

## 2. Struktur Dasar: `if`, `if-else`, dan `if-elif-else`

Python menyediakan tiga tingkatan struktur logika kondisional:

### A. Pernyataan `if` Tunggal
Digunakan jika suatu tindakan hanya dilakukan ketika syarat terpenuhi:
```python
daya_mw = 120.0
if daya_mw > 100.0:
    print("Peringatan: Daya transmisi melebihi batas standar operasi!")
```

### B. Pernyataan `if-else` (Dua Cabang Pilihan)
Digunakan ketika terdapat alternatif tindakan saat kondisi bernilai `False`:
```python
koneksi_aktif = True
if koneksi_aktif:
    print("Node terhubung ke jaringan core.")
else:
    print("Node terputus! Memulai prosedur rekoneksi otomatis...")
```

### C. Pernyataan `if-elif-else` (Banyak Cabang Pilihan)
Klausa `elif` (singkatan dari *else if*) memungkinkan pengujian kondisi beruntun hingga ditemukan kondisi pertama yang bernilai `True`:
```python
nilai = 85.0
if nilai >= 80.0:
    grade = "A"
elif nilai >= 70.0:
    grade = "B"
elif nilai >= 60.0:
    grade = "C"
elif nilai >= 50.0:
    grade = "D"
else:
    grade = "E"
```

> [!IMPORTANT]
> Urutan penulisan cabang `elif` sangat menentukan kebenaran program! CPython mengevaluasi cabang dari atas ke bawah dan langsung melompat keluar dari seluruh blok kondisional setelah cabang pertama yang bernilai `True` selesai dieksekusi.

---

## 3. Menggabungkan Kondisi dengan Operator Logika

Seringkali keputusan bergantung pada lebih dari satu parameter. Gunakan operator logika `and`, `or`, dan `not`:

```python
tegangan = 48.5  # Volt
suhu = 35.0      # Celsius
siap_transmisi = (44.0 <= tegangan <= 56.0) and (suhu <= 50.0)

if siap_transmisi:
    print("Parameter daya dan termal stasiun pemancar dalam kondisi optimal.")
```

---

## 4. Percabangan Bersarang (*Nested Conditions*) vs Guard Clauses

Ketika percabangan diletakkan di dalam percabangan lain, struktur tersebut dinamakan **percabangan bersarang** (*nested conditional*):

```python
if terdaftar:
    if verifikasi_dua_faktor:
        print("Akses ke panel BTS diberikan.")
    else:
        print("Menunggu token 2FA.")
else:
    print("ID pengguna tidak dikenal.")
```

### Praktik Terbaik Rekayasa: Menerapkan Guard Clauses
Percabangan bersarang yang terlalu dalam (*deeply nested code*) menyulitkan pembacaan kode dan rentan menimbulkan *bug*. Standar rekayasa perangkat lunak modern menganjurkan teknik **Guard Clauses** (pemeriksaan batas awal dengan keluar/kembali lebih dini):

```python
def periksa_akses(terdaftar: bool, dua_faktor: bool) -> str:
    # Guard clause 1: Tolak segera jika tidak terdaftar
    if not terdaftar:
        return "ID pengguna tidak dikenal."
    # Guard clause 2: Tolak jika belum verifikasi 2FA
    if not dua_faktor:
        return "Menunggu token 2FA."
    # Jalur utama (happy path) berada di level indentasi terluar
    return "Akses ke panel BTS diberikan."
```

---

## 5. Ekspresi Kondisional Ternary (Ternary Operator)

Untuk penugasan variabel satu baris sederhana berdasarkan kondisi, Python menyediakan operator ternary dengan sintaks:
$$\text{nilai\_jika\_true}\ \mathbf{if}\ \text{kondisi}\ \mathbf{else}\ \text{nilai\_jika\_false}$$

```python
rsrp = -78.0
status = "Optimal" if rsrp >= -85.0 else "Perlu Evaluasi"
```

---

## 6. Studi Kasus Rekayasa: Klasifikasi Kualitas Sinyal RSRP

Dalam sistem seluler LTE/5G, parameter **RSRP** (*Reference Signal Received Power*) mencerminkan kuat sinyal pembawa yang diterima perangkat pengguna dari stasiun pemancar.

> [!NOTE]
> **Catatan Pedagogis Standar Pembelajaran:**  
> Ambang batas nilai RSRP pada contoh ini adalah **asumsi instruksional** untuk melatih logika percabangan berjenjang, bukan standar mutlak universal dari 3GPP maupun vendor spesifik.

Kriteria klasifikasi pembelajaran:
- $\text{RSRP} \ge -80.0\text{ dBm} \implies$ **Sangat Baik (Excellent)**
- $-90.0\text{ dBm} \le \text{RSRP} < -80.0\text{ dBm} \implies$ **Baik (Good)**
- $-100.0\text{ dBm} \le \text{RSRP} < -90.0\text{ dBm} \implies$ **Cukup (Fair)**
- $\text{RSRP} < -100.0\text{ dBm} \implies$ **Buruk (Poor)**

```python
def evaluasi_sinyal(rsrp_dbm: float) -> str:
    if rsrp_dbm >= -80.0:
        return "Sangat Baik (Excellent)"
    elif rsrp_dbm >= -90.0:
        return "Baik (Good)"
    elif rsrp_dbm >= -100.0:
        return "Cukup (Fair)"
    else:
        return "Buruk (Poor)"
```

---

## 7. Kesalahan Logika Umum Pemula (*Common Pitfalls*)

1. **Tertukar antara `=` dan `==`:** Tanda tunggal `=` adalah penugasan (*assignment*), sedangkan tanda ganda `==` adalah pembanding kesetaraan.
2. **Kondisi Tak Terjangkau (*Dead/Unreachable Code*):** Menuliskan rentang yang lebih luas sebelum rentang yang lebih sempit:
   ```python
   # SALAH: elif skor >= 60 tidak akan pernah terjangkau jika >= 50 ditaruh di atasnya
   if skor >= 50:
       print("Lulus")
   elif skor >= 85: # KODE MATI (Tidak pernah dieksekusi)
       print("Cumlaude")
   ```
3. **Pengabaian Nilai Batas (*Off-by-One / Boundary Errors*):** Menggunakan `>` padahal spesifikasi meminta `>=` (lebih besar atau sama dengan).
4. **Percampuran Evaluasi Boolean dan String:** Menulis `if status == "Aktif" or "Siaga":` padahal maksudnya adalah `if status == "Aktif" or status == "Siaga":` (karena `"Siaga"` sebagai string non-kosong selalu bernilai `True`).

---

## 8. Ringkasan Bab

- Logika percabangan memungkinkan program menentukan jalur eksekusi alternatif berdasarkan nilai boolean.
- Klausa `if`, `elif`, dan `else` dievaluasi dari atas ke bawah; evaluasi berhenti pada kondisi pertama yang benar.
- Operator logika `and`, `or`, dan `not` menggabungkan beberapa kriteria keputusan.
- Teknik *Guard Clauses* meningkatkan keterbacaan kode dibandingkan *nested if* yang bertingkat dalam.
- Operator ternary memungkinkan penugasan bersyarat satu baris yang bersih.

---

## 9. Referensi & Sumber Belajar Terbuka

1. **Python Software Foundation**, *More Control Flow Tools: if Statements*, [https://docs.python.org/3/tutorial/controlflow.html#if-statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements) (PSF License 2.0).
2. **Allen B. Downey**, *Think Python (3rd Edition)*, Chapter 5: Conditionals and Recursion, [https://allendowney.github.io/ThinkPython/](https://allendowney.github.io/ThinkPython/) (CC BY-NC 4.0).
3. **David J. Malan**, *CS50’s Introduction to Programming with Python*, Week 1: Conditionals, [https://cs50.harvard.edu/python/](https://cs50.harvard.edu/python/) (CC BY-NC-SA 4.0).
4. **Asabeneh S. Yetayeh**, *30 Days Of Python*, Day 09: Conditionals, [https://github.com/Asabeneh/30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) (MIT License).
