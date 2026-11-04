# Tugas Praktik Chapter 05: Student Grade and Signal Quality Classifier

## Deskripsi Tugas
Dalam perancangan perangkat lunak analitik, pengembang dituntut mampu membangun modul pengambil keputusan (*decision engine*) yang tangguh. Modul ini harus mampu memvalidasi masukan mentah, menangani kondisi batas (*boundary values*), mengklasifikasikan data ke dalam kategori yang tepat, serta memberikan penjelasan logis diagnostik.

Anda diminta membuat program Python terstruktur bernama `tugas_05.py` yang memiliki dua mesin klasifikasi:
1. **Engine 1 — Klasifikasi Nilai Akademik Mahasiswa:**
   - Masukan: Skor numerik $0.0 \le \text{skor} \le 100.0$.
   - Kategori: A ($\ge 80$), B ($70 \le \text{skor} < 80$), C ($60 \le \text{skor} < 70$), D ($50 \le \text{skor} < 60$), E ($< 50$).
   - Validasi: Tolak nilai di luar rentang $0 - 100$ atau format non-numerik.
2. **Engine 2 — Klasifikasi Kualitas Sinyal RSRP (Telekomunikasi):**
   - Masukan: Kuat sinyal RSRP (dBm) dalam rentang operasional valid $-140.0 \le \text{RSRP} \le -40.0\text{ dBm}$.
   - Kategori (Asumsi Pedagogis):
     - Sangat Baik: $\text{RSRP} \ge -80.0\text{ dBm}$ (throughput maksimal, latensi rendah).
     - Baik: $-90.0 \le \text{RSRP} < -80.0\text{ dBm}$ (kualitas stabil untuk panggilan & data HD).
     - Cukup: $-100.0 \le \text{RSRP} < -90.0\text{ dBm}$ (batas minimum kenyamanan layanan seluler).
     - Buruk: $\text{RSRP} < -100.0\text{ dBm}$ (berisiko mengalami *call drop* atau paket hilang).

---

## Format Laporan Output Terminal

```text
======================================================================
         SISTEM KLASIFIKASI KONDISIONAL CERDAS (ENGINE 05)
======================================================================
--- PENGUJIAN 1: NILAI AKADEMIK MAHASISWA ---
Input Skor : 80.0 -> Grade: A | Keterangan: Sangat Memuaskan (Cumlaude)
Input Skor : 79.9 -> Grade: B | Keterangan: Memuaskan
Input Skor : 105.0 -> DITOLAK: Skor 105.0 di luar rentang sah (0 - 100)

--- PENGUJIAN 2: KUALITAS SINYAL RSRP SELULER ---
Input RSRP : -78.5 dBm -> Kategori: Sangat Baik | Latensi minimal, throughput maksimal
Input RSRP : -90.0 dBm -> Kategori: Baik        | Kualitas stabil panggilan suara & data
Input RSRP : -105.0 dBm -> Kategori: Buruk       | Sinyal lemah, risiko tinggi call drop
Input RSRP : -150.0 dBm -> DITOLAK: Nilai di luar rentang pembacaan fisik (-140 s.d. -40 dBm)
======================================================================
```

---

## Rubrik Penilaian (Total Bobot: 100%)

| Kriteria Penilaian | Bobot | Deskripsi Capaian |
|:---|:---:|:---|
| **Validasi Masukan & Kondisi Batas** | 30% | Menolak nilai di luar rentang dan menangani nilai batas kritis (misal skor 80.0, 79.9, RSRP -90.0 dBm) secara tepat. |
| **Kebenaran Logika Percabangan** | 40% | Mengimplementasikan struktur `if-elif-else` yang runtut, tanpa dead code, dengan hasil klasifikasi akurat. |
| **Penjelasan Diagnostik Lengkap** | 15% | Memberikan pesan diagnostik kontekstual yang informatif untuk setiap kategori hasil klasifikasi. |
| **Kepatuhan Gaya PEP 8 & Struktur** | 15% | Penamaan fungsi/variabel snake_case, modularitas fungsi, dan blok `if __name__ == '__main__':`. |

