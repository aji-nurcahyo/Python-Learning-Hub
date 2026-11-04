# Tugas Praktik Chapter 04: Generator Kartu Telemetri Node Jaringan

## Deskripsi Tugas
Dalam operasional pusat kendali jaringan (*Network Operation Center* / NOC), data telemetri ribuan BTS dikumpulkan dan ditampilkan secara berkala ke konsol engineer lapangan. Data mentah harus diformat dengan presisi tinggi, memiliki perataan kolom yang sejajar, serta menyertakan ringkasan metrik statistik.

Anda diminta membuat program mandiri `tugas_04.py` yang menerima atau memproses data telemetri transceiver BTS, menghitung metrik performa, dan mencetak **Kartu Telemetri Node Jaringan** terformat profesional.

---

## Petunjuk Pengerjaan

1. **Unduh Starter Code:** Buka berkas `tugas_04.py`.
2. **Spesifikasi Data Transceiver:**
   Tiap record stasiun memiliki:
   - `id_node` (misal: `"NODE-01"`)
   - `nama_lokasi` (misal: `"Gedung Rektorat"`)
   - `frekuensi_mhz` (misal: `1800.5`)
   - `daya_tx_watt` (misal: `40.0`)
   - `packet_loss_ratio` (misal: `0.0125` &rarr; `1.25%`)
   - `status_operasional` (misal: `"ONLINE"`)
3. **Persyaratan Pemformatan Konsol:**
   - Gunakan f-strings murni (PEP 498).
   - Format angka desimal frekuensi dan daya dengan `:.1f`.
   - Format packet loss dengan format persentase `:.2%`.
   - Susun data dalam tabel dengan lebar kolom yang konsisten:
     - ID: lebar 10 rata kiri (`<`)
     - Lokasi: lebar 18 rata kiri (`<`)
     - Frekuensi: lebar 14 rata tengah (`^`)
     - Daya: lebar 10 rata tengah (`^`)
     - Packet Loss: lebar 12 rata kanan (`>`)
     - Status: lebar 10 rata kanan (`>`)
   - Tampilkan baris pembatas garis rangkap `"=" * 80`.
4. **Ringkasan Statistik:**
   Di bawah tabel, tampilkan rata-rata daya pancar dan rata-rata packet loss dari seluruh node yang dipantau.

---

## Rubrik Penilaian (Total Bobot: 100%)

| Kriteria Penilaian | Bobot | Deskripsi Capaian |
|:---|:---:|:---|
| **Penerapan f-Strings & Interpolasi** | 40% | Menggunakan f-strings secara konsisten tanpa operator lama `%` atau konkatenasi string manual. |
| **Format Specifiers & Alignment** | 30% | Menerapkan format persentase `:.2%`, desimal `:.1f`, dan perataan kolom (`<`, `^`, `>`) yang sejajar rapi. |
| **Kepatuhan Gaya PEP 8** | 20% | Penamaan fungsi dan variabel menggunakan `snake_case`, struktur kode modular, dan dokumentasi docstring. |
| **Logika Ringkasan Metrik** | 10% | Perhitungan nilai rata-rata daya pancar dan packet loss tepat. |
