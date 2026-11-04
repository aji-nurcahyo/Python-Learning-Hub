# Tugas Praktik Chapter 06: Sensor Data Monitoring Simulator

## Deskripsi Tugas
Dalam stasiun pemancar telekomunikasi (BTS), sistem pemantauan kondisi lingkungan (Environmental Monitoring System) terus-menerus membaca aliran data telemetri dari berbagai sensor (suhu ruang rak, tegangan suplai DC, kelembaban, dan daya pantul VSWR).

Anda diminta membuat program simulator pemrosesan aliran data sensor bernama `tugas_06.py` yang menggunakan struktur perulangan Python murni (tanpa modul eksternal).

---

## Petunjuk Pengerjaan

1. **Unduh Starter Code:** Buka berkas `tugas_06.py`.
2. **Koleksi Data Uji Deret Waktu:**
   Gunakan sampel deret telemetri suhu (Celsius):
   `[26.5, 28.0, 31.2, -999.0, 35.4, 38.0, 42.5, 85.0, 27.0]`
3. **Aturan Pemrosesan Iteratif:**
   - **Data Normal:** Cetak status pembacaan detik ke-$t$ dengan format rapi.
   - **Penyaringan Glitch (`continue`):** Nilai `-999.0` adalah kegagalan pembacaan sesaat sensor; lewati kalkulasi statistik.
   - **Penghitungan Ambang Peringatan:** Hitung berapa banyak sampel suhu normal yang melampaui ambang batas peringatan $\ge 35.0^\circ\text{C}$.
   - **Terminasi Darurat (`break`):** Jika suhu melonjak mencapai $\ge 80.0^\circ\text{C}$, cetak alarm bahaya shutdown dan hentikan pemantauan seketika.
4. **Ringkasan Statistik:**
   Setelah loop berhenti, tampilkan ringkasan metrik statistik (total sampel valid, nilai rata-rata, nilai terendah, nilai tertinggi, dan jumlah peringatan ambang batas).

---

## Format Laporan Output Terminal

```text
======================================================================
         SIMULATOR PEMANTAUAN TELEMETRI SENSOR BTS (ENGINE 06)
======================================================================
Detik 01: Suhu = 26.5 C | Status: NORMAL
Detik 02: Suhu = 28.0 C | Status: NORMAL
Detik 03: Suhu = 31.2 C | Status: NORMAL
Detik 04: [SENSOR NOISE] Nilai -999.0 C terdeteksi! Pembacaan dilewati.
Detik 05: Suhu = 35.4 C | Status: [PERINGATAN] Suhu Tinggi (>= 35 C)
Detik 06: Suhu = 38.0 C | Status: [PERINGATAN] Suhu Tinggi (>= 35 C)
Detik 07: Suhu = 42.5 C | Status: [PERINGATAN] Suhu Tinggi (>= 35 C)
Detik 08: [ALARM KRITIS] Suhu 85.0 C melampaui batas darurat (80 C)!
          Prosedur darurat aktif: Loop monitoring dihentikan segera.
----------------------------------------------------------------------
                   RINGKASAN STATISTIK TELEMETRI
----------------------------------------------------------------------
Total Siklus Waktu      : 8 Detik
Total Sampel Valid      : 6 Sampel
Jumlah Peringatan (>=35): 3 Kejadian
Suhu Minimum Terbaca    : 26.5 C
Suhu Maksimum Terbaca   : 42.5 C
Suhu Rata-Rata Valid    : 33.60 C
Status Akhir Operasi    : TERHENTI OLEH INTERUPSI ALARM KRITIS
======================================================================
```

---

## Rubrik Penilaian (Total Bobot: 100%)

| Kriteria Penilaian | Bobot | Deskripsi Capaian |
|:---|:---:|:---|
| **Implementasi Loop & Kontrol Alur** | 40% | Menggunakan `for` atau `while` secara tepat, menerapkan `continue` untuk glitch, dan `break` untuk kondisi darurat. |
| **Kalkulasi Akumulator & Statistik** | 30% | Menghitung total, rata-rata, min, max, dan counter ambang batas hanya dari data valid secara presisi. |
| **Penanganan Terminasi & Pelaporan** | 20% | Format laporan konsol rapi dengan f-strings dan menyajikan status terminasi yang benar. |
| **Kepatuhan Gaya PEP 8 & Pythonic** | 10% | Penamaan snake_case, modularitas fungsi, dan penyusunan blok `if __name__ == '__main__':`. |
