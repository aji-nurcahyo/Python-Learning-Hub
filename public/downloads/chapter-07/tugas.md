# Tugas Praktik Chapter 07: Device Identifier & Sensor Message Processor

## Deskripsi Tugas
Dalam arsitektur *Internet of Things* (IoT) dan integrasi jaringan sensor telekomunikasi, data mentah dari ribuan node pemancar dikirimkan dalam bentuk paket teks terkompresi. Sistem gerbang (*Gateway Parser*) bertugas memvalidasi identitas pengirim (Device ID), membersihkan derau teks, mengurai parameter kunci-nilai, dan merekonstruksi laporan status yang mudah dipahami manusia.

Anda diminta membuat program pengolah teks telekomunikasi mandiri bernama `tugas_07.py` yang mengintegrasikan seluruh teknik manipulasi string Python.

---

## Petunjuk Pengerjaan

1. **Unduh Starter Code:** Buka berkas `tugas_07.py`.
2. **Kaidah Validasi Identifier Perangkat (Device ID):**
   - Format sah: `PREFIX-KODE_LOKASI-NOMOR_NODE` (Contoh: `NODE-LPG-0123`).
   - Harus diawali dengan prefiks `"NODE-"`.
   - Terdiri dari tepat 3 segmen yang dipisahkan tanda strip `-`.
   - Segmen kedua (kode lokasi) harus berupa 3 huruf alfabet kapital (misal: `"LPG"`).
   - Segmen ketiga harus berupa 4 digit numerik (misal: `"0123"`).
3. **Penguraian Payload Telemetri Sensor:**
   Format string sensor mentah:
   `"  RAW_MSG:ID=NODE-LPG-0123;TEMP=36.4C;BATT=94%;RSRP=-82.5dBm;STAT=ok  "`
   - Bersihkan teks dengan `.strip()` dan buang prefiks `"RAW_MSG:"`.
   - Pisahkan field menggunakan delimiter titik-koma `";"`.
   - Urai setiap pasangan `kunci=nilai`.
   - Normalisasikan nilai status (`STAT`) menjadi format huruf kapital (`"OK"`).
4. **Penyajian Laporan:**
   Susun hasil parsing ke dalam laporan antarmuka CLI yang rapi dengan f-strings.

---

## Format Laporan Output Terminal

```text
======================================================================
     GERBANG TELEMETRI IOT: PARSER PESAN & IDENTIFIER (ENGINE 07)
======================================================================
--- 1. UJI VALIDASI FORMAT IDENTIFIER PERANGKAT ---
Uji 'NODE-LPG-0123'  -> VALID   | Lokasi: LPG, Unit: 0123
Uji 'NODE-BDL-99'    -> DITOLAK | Segmen ketiga harus tepat 4 digit
Uji 'GATEWAY-01'     -> DITOLAK | Harus diawali prefiks 'NODE-'

--- 2. PENGURAIAN PAYLOAD TELEMETRI SENSOR ---
Payload Mentah       : '  RAW_MSG:ID=NODE-LPG-0123;TEMP=36.4C;BATT=94%;RSRP=-82.5dBm;STAT=ok  '
Identitas Perangkat  : NODE-LPG-0123 (Status ID: VALID)
Suhu Sensor          : 36.4 C
Sisa Daya Baterai    : 94%
Kuat Sinyal RSRP     : -82.5 dBm
Status Operasional   : OK (Ternormalisasi)
----------------------------------------------------------------------
Pesan Status Ringkas : "Node NODE-LPG-0123 [LPG] beroperasi NORMAL dengan baterai 94%."
======================================================================
```

---

## Rubrik Penilaian (Total Bobot: 100%)

| Kriteria Penilaian | Bobot | Deskripsi Capaian |
|:---|:---:|:---|
| **Validasi Format Identifier** | 30% | Memeriksa prefiks, jumlah segmen split, validitas huruf kapital lokasi, dan 4 digit angka unit. |
| **Parsing Delimiter & Pasangan Nilai** | 35% | Mengurai string sensor berbasis delimiter `;` dan `=` secara akurat menjadi dictionary/struktur data. |
| **Normalisasi & Pembersihan Teks** | 20% | Menghapus whitespace liar, membersihkan tag prefiks mentah, dan menstandarisasi huruf besar/kecil. |
| **Kepatuhan Gaya PEP 8 & Struktur** | 15% | Penamaan snake_case, modularitas fungsi terpisah, dan blok `if __name__ == '__main__':`. |

