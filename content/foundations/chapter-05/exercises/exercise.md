# Latihan Terarah — Chapter 05: Conditional Statements

Kerjakan latihan-latihan berikut untuk memperkuat pemahaman logika percabangan, evaluasi multi-kondisi, dan pencegahan kesalahan logika umum.

---

### Latihan 1: Klasifikasi Suhu Ruang Server dengan Guard Clauses
**Tujuan:** Menggunakan pola *guard clauses* untuk mengevaluasi data batas.

1. Tulis fungsi `evaluasi_suhu_server(suhu_c: float) -> str`.
2. Terapkan aturan:
   - Jika $\text{suhu} < 10.0$ atau $\text{suhu} > 50.0$, kembalikan `"KONDISI KRITIS: Suhu Ekstrem"`.
   - Jika $35.0 \le \text{suhu} \le 50.0$, kembalikan `"PERINGATAN: Kipas Tambahan Aktif"`.
   - Jika kondisi lain, kembalikan `"NORMAL: Suhu Optimal (10 - 34.9 C)"`.
3. Uji fungsi dengan nilai: `5.0`, `24.5`, `38.0`, dan `55.0`.

---

### Latihan 2: Sistem Otentikasi Multi-Faktor (Logika Boolean Majemuk)
**Tujuan:** Menggabungkan operator relasional dan logika `and`, `or`, `not`.

1. Sebuah pintu shelter BTS dilindungi otentikasi dengan variabel:
   - `pin_valid` (boolean)
   - `kartu_terdaftar` (boolean)
   - `status_darurat` (boolean)
2. Akses pintu diberikan (`True`) jika:
   - Dalam kondisi `status_darurat == True` (akses darurat langsung dibuka), **ATAU**
   - Kedua syarat ini terpenuhi: `pin_valid == True` **DAN** `kartu_terdaftar == True`.
3. Cetak tabel status pengujian untuk seluruh kombinasi kemungkinan.

---

### Latihan 3: Penentu Jenis Segitiga (Batas Geometri Antena)
**Tujuan:** Menerapkan percabangan bersarang dan perbandingan kesetaraan nilai.

1. Diberikan tiga sisi menara rangka antena: $a$, $b$, dan $c$.
2. Pertama, validasi apakah ketiga sisi dapat membentuk segitiga:
   $$a + b > c \quad \text{dan} \quad a + c > b \quad \text{dan} \quad b + c > a$$
3. Jika valid, klasifikasikan:
   - "Segitiga Sama Sisi" jika ketiga sisinya sama panjang ($a == b == c$).
   - "Segitiga Sama Kaki" jika tepat dua sisinya sama panjang.
   - "Segitiga Sembarang" jika ketiga sisinya berbeda.
4. Jika tidak valid, cetak `"Bukan Segitiga Sah"`.
