# Modul A01: Numerical Computing with NumPy

## 1. Mengapa Komputasi Numerik Membutuhkan `ndarray`?
Struktur `list` bawaan Python bersifat heterogen dan menyimpan pointer ke objek Python terpisah di memori. Akibatnya, operasi aritmetika pada jutaan angka melalui `for` loop menimbulkan overhead interpretasi tipe berulang kali.

NumPy menyediakan struktur data inti **`ndarray`** (*N-dimensional array*) yang menyimpan elemen bertipe seragam (`dtype` tunggal, misalnya `float64` atau `int32`) dalam blok memori kontigu, memungkinkan eksekusi instruksi level C dan optimasi vektorisasi perangkat keras.

### Perbedaan Utama `list` vs `ndarray`
- **Homogenitas Tipe:** Seluruh elemen `ndarray` wajib memiliki `dtype` yang konsisten.
- **Atribut Struktural:** Setiap array memiliki `.shape`, `.ndim`, `.size`, dan `.dtype`.
- **Slicing Sebagai View:** Irisan (*slice*) pada `ndarray` umumnya mengembalikan *view* ke buffer memori yang sama, bukan salinan baru, sehingga hemat RAM.

```python
import numpy as np

matriks = np.array([
    [28.4, 62.0, 18.2],
    [29.1, 60.5, 19.5],
    [36.5, 48.0, 45.2],
], dtype=np.float64)

print("Shape:", matriks.shape)  # (3, 3)
print("Dimensi:", matriks.ndim) # 2
```

---

## 2. Vectorization dan Aturan Broadcasting
**Vectorization** adalah teknik mengekspresikan operasi batch pada seluruh elemen array tanpa menuliskan loop Python eksplisit.

**Broadcasting** memungkinkan NumPy melakukan operasi aritmetika pada dua array dengan ukuran berbeda selama kedua bentuknya kompatibel menurut aturan:
1. Bandingkan dimensi dari kanan ke kiri (*trailing dimensions*).
2. Dua dimensi dianggap cocok jika keduanya sama panjang **atau** salah satunya bernilai `1`.
3. Jika salah satu array memiliki dimensi lebih sedikit, tambahkan dimensi ukuran `1` di sisi kiri (*leading dimensions*).

Sebagai contoh, menormalisasi matriks `(12, 4)` dengan vektor rata-rata per kolom `(4,)` akan memicu broadcasting `(4,) -> (1, 4) -> (12, 4)`.

---

## 3. Agregasi Berbasis `axis` dan Boolean Masking
Pada matriks 2D `(baris, kolom)`:
- `axis=0` melakukan agregasi ke bawah (menghasilkan statistik **per kolom**).
- `axis=1` melakukan agregasi ke kanan (menghasilkan statistik **per baris**).

**Boolean Masking** mempermudah penyaringan elemen bersyarat:

```python
latensi = matriks[:, 2]
anomali = matriks[latensi > 30.0]
```

Kombinasi `np.where(kondisi, nilai_benar, nilai_salah)` memungkinkan pelabelan atau substitusi nilai tervektorisasi dalam satu baris.

---

## 4. Ringkasan Praktik Baik
- Gunakan `np.genfromtxt(..., delimiter=",", skip_header=1)` untuk memuat dataset numerik CSV sederhana.
- Selalu periksa potensi pembagian nol (`np.where(std == 0, 1.0, std)`) saat menormalisasi fitur.
- Gunakan `.copy()` secara eksplisit jika Anda tidak ingin modifikasi *slice* memengaruhi array asli.

