# Latihan Terarah — Chapter 16: Algorithm Analysis & Problem Solving

Uji kemampuan analitis Anda dalam menghitung kompleksitas Big-O, merancang benchmark empiris yang adil, serta menganalisis pertukaran ruang dan waktu (*Space-Time Tradeoffs*).

---

### Latihan 1: Analisis Notasi Asimtotik Kode Sumber (Big-O Calculation)
**Tujuan:** Menentukan kompleksitas waktu secara analitis dari potongan kode.

Tentukan notasi Big-O untuk ketiga fungsi berikut dan jelaskan alasannya:

```python
# Kasus A:
def fungsi_a(data: list[int]) -> int:
    return data[0] if data else 0

# Kasus B:
def fungsi_b(data: list[int]) -> int:
    total = 0
    for x in data:
        total += x
    return total

# Kasus C:
def fungsi_c(n: int) -> list[tuple[int, int]]:
    pasangan = []
    for i in range(n):
        for j in range(i, n):
            pasangan.append((i, j))
    return pasangan
```

---

### Latihan 2: Pengujian Empiris Fairness Benchmarking
**Tujuan:** Merancang lingkungan pengukuran kinerja yang adil (*fair comparison*).

1. Mengapa membandingkan waktu Linear Search vs Binary Search pada list yang baru saja dibuat tidak adil jika waktu pembuatan list dan pengurutan awal dihitung ke dalam waktu Binary Search?
2. Buat skrip menggunakan `time.perf_counter()` yang memisahkan **tahap persiapan data** (*setup phase*) dari **tahap pencarian berulang** ($10.000$ kali pencarian).
3. Buktikan pada jumlah pencarian berulang ke berapa Binary Search mulai mengungguli Linear Search meskipun ditambah biaya pengurutan di awal.

---

### Latihan 3: Space-Time Tradeoff: Peringkas Frekuensi Karakter
**Tujuan:** Mengorbankan ruang memori untuk mereduksi waktu eksekusi dari $O(n^2)$ menjadi $O(n)$.

1. Diberikan string teks telemetri panjang: `"AABBCDEFFAA...10000_karakter"`.
2. Pendekatan 1 (Tanpa memori tambahan): Untuk setiap karakter, hitung kemunculannya menggunakan metode `.count()` ($O(n^2)$).
3. Pendekatan 2 (Dengan kamus frekuensi): Gunakan satu kamus dictionary untuk mencatat frekuensi dalam satu kali iterasi ($O(n)$ waktu, $O(k)$ ruang).
4. Bandingkan waktu eksekusi kedua pendekatan menggunakan `time.perf_counter()`.

---

### Latihan 4: Deteksi Pasangan Dua Angka Penjumlahan (Two Sum Problem)
**Tujuan:** Menerapkan dekomposisi masalah dan struktur data hash untuk memecahkan problem klasik $O(n)$.

1. Diberikan list bilangan bulat `angka = [2, 7, 11, 15]` dan nilai target `jumlah = 9`.
2. Rancang fungsi `temukan_pasangan_two_sum(angka: list[int], target: int) -> tuple[int, int] | None`.
3. Gunakan kamus penampung komplemen `{target - x: idx}` untuk menemukan indeks pasangan dalam satu lintasan $O(n)$ tanpa nested loop $O(n^2)$.
