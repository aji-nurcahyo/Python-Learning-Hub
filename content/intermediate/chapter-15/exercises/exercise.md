# Latihan Terarah — Chapter 15: Searching & Sorting Algorithms

Perkuat pemahaman Anda mengenai algoritma pencarian (Linear vs Binary) dan algoritma pengurutan klasik (Bubble, Selection, Insertion) serta Timsort bawaan Python.

---

### Latihan 1: Deteksi Ambang Sinyal dengan Binary Search Modifikasi
**Tujuan:** Memodifikasi Binary Search untuk mencari elemen terkecil yang $\ge$ nilai ambang batas (*Lower Bound Search*).

1. Diberikan data frekuensi alokasi pita kanal (kHz) yang sudah terurut:
   ```python
   pita_frekuensi = [700, 850, 900, 1800, 2100, 2300, 2600, 3500]
   ```
2. Buat fungsi `cari_alokasi_terdekat(frekuensi_list: list[int], target: int) -> int | None`.
3. Jika nilai target tidak ada secara eksak, kembalikan frekuensi pertama yang berada di atas target.
4. Uji dengan target `1900 kHz` (harus mengembalikan `2100 kHz`).

---

### Latihan 2: Pengurutan Stabil Berdasarkan Kategori Prioritas
**Tujuan:** Memahami konsep stabilitas pengurutan (*Stable Sorting*) pada data multi-kunci.

1. Diberikan daftar tugas antrean transmisi:
   ```python
   antrean = [
       {"id": "T1", "level": "MEDIUM", "waktu": 10.2},
       {"id": "T2", "level": "HIGH",   "waktu": 5.4},
       {"id": "T3", "level": "LOW",    "waktu": 12.0},
       {"id": "T4", "level": "HIGH",   "waktu": 8.1},
       {"id": "T5", "level": "MEDIUM", "waktu": 3.0},
   ]
   ```
2. Definisikan bobot prioritas: `{"HIGH": 1, "MEDIUM": 2, "LOW": 3}`.
3. Urutkan tugas berdasarkan level prioritas tanpa merusak urutan relatif tugas pada level yang sama (*stable sort*).
4. Bandingkan hasilnya menggunakan `sorted()` Python murni.

---

### Latihan 3: Perhitungan Jumlah Swap pada Bubble Sort
**Tujuan:** Menganalisis operasi dasar dan efisiensi algoritma pengurutan.

1. Modifikasi algoritma Bubble Sort agar mencatat dan mengembalikan total pertukaran elemen (*swap count*):
   `bubble_sort_dengan_swap(data) -> tuple[list, int]`.
2. Uji dengan tiga jenis data:
   - Data sudah terurut: `[1, 2, 3, 4, 5]` (swap = 0).
   - Data terbalik: `[5, 4, 3, 2, 1]` (swap = 10).
   - Data acak: `[4, 2, 5, 1, 3]`.

---

### Latihan 4: Insertion Sort pada Aliran Data Masuk (Streaming Insertion)
**Tujuan:** Memanfaatkan keunggulan Insertion Sort pada penambahan data baru ke koleksi terurut.

1. Buat fungsi `sisipkan_ke_terurut(data_terurut: list[float], elemen_baru: float) -> list[float]`.
2. Sisipkan `elemen_baru` ke posisi indeks yang tepat sehingga daftar tetap terurut dengan kompleksitas $O(n)$ tanpa perlu melakukan sort ulang penuh.

