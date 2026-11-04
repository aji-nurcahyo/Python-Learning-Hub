# Latihan Terarah — Chapter 06: Loops & Iteration

Kerjakan latihan berikut untuk menguji pemahaman Anda mengenai for loop, while loop, kendali break dan continue, serta algoritma akumulator.

---

### Latihan 1: Retransmisi Paket dengan Batas Percobaan (while Loop & break)
**Tujuan:** Menggunakan while loop dengan batas pencacah maksimal (*retry limit*).

1. Sebuah node pemancar mencoba mengirim paket data dengan batas maksimal 5 kali percobaan.
2. Diberikan deret respon transmisi: `["TIMEOUT", "TIMEOUT", "ACK_OK", "TIMEOUT"]`.
3. Gunakan loop `while` untuk mensimulasikan percobaan pengiriman.
4. Jika menerima `"ACK_OK"`, cetak `"Paket berhasil terkirim pada percobaan ke-X!"` dan hentikan loop dengan `break`.
5. Jika telah mencapai 5 kali percobaan dan belum berhasil, cetak `"Gagal mengirim paket: Batas percobaan terlampaui"`.

---

### Latihan 2: Penyaring Derau Sinyal (for Loop & continue)
**Tujuan:** Mengabaikan data anomali menggunakan `continue`.

1. Diberikan data pengukuran daya sinyal dalam miliwatt:
   ```python
   data_sinyal = [12.0, -5.0, 15.5, 0.0, 22.0, -1.0, 18.0]
   ```
2. Nilai $\le 0.0$ merupakan data rusak (*noise/invalid*).
3. Gunakan `for` loop dan `continue` untuk mengabaikan nilai $\le 0.0$.
4. Hitung total dan rata-rata daya dari seluruh data yang valid saja.

---

### Latihan 3: Matriks Pola Penguatan Antena (Nested Loop)
**Tujuan:** Menghasilkan tabel koordinat atau pola bertingkat menggunakan loop bersarang.

1. Buat skrip yang mencetak pola segitiga daya bertingkat (tinggi 5 baris):
   ```text
   *
   **
   ***
   ****
   *****
   ```
2. Gunakan dua tingkat perulangan `for` (bukan perkalian string `* n`).
3. Modifikasi agar menampilkan nomor level pada setiap barisnya.

