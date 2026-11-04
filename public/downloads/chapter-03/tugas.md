# Tugas Praktik Chapter 03: Kalkulator Anggaran Daya Tautan (Link Budget)

## Deskripsi Tugas
Dalam perencanaan jaringan transmisi radio nirkabel, perhitungan **Link Budget** (anggaran daya tautan) digunakan untuk memastikan bahwa daya sinyal yang tiba di antena penerima masih cukup kuat untuk didekode tanpa menimbulkan galat transmisi bit (*Bit Error Rate*).

Rumus dasar estimasi daya terima ($P_{\text{rx}}$) dalam domain logaritmik ($\text{dBm}$):
$$P_{\text{rx}} = P_{\text{tx}} + G_{\text{tx}} + G_{\text{rx}} - L_{\text{fspl}} - L_{\text{misc}}$$

Di mana:
- $P_{\text{tx}}$: Daya pemancar ($\text{dBm}$).
- $G_{\text{tx}}$: Penguatan antena pemancar ($\text{dBi}$).
- $G_{\text{rx}}$: Penguatan antena penerima ($\text{dBi}$).
- $L_{\text{fspl}}$: Redaman propagasi ruang bebas (*Free Space Path Loss*, $\text{dB}$).
- $L_{\text{misc}}$: Redaman kabel dan konektor ($\text{dB}$).

Margin tautan (*Fade Margin*) dihitung dengan:
$$\text{Margin} = P_{\text{rx}} - S_{\text{rx}}$$
Di mana $S_{\text{rx}}$ adalah sensitivitas batas penerima (misal: $-95.0\text{ dBm}$). Tautan radio dianggap andal jika $\text{Margin} \ge 10.0\text{ dB}$.

---

## Petunjuk Pengerjaan

1. **Unduh Starter Code:** Buka berkas `tugas_03.py`.
2. **Implementasikan Logika Komputasi:**
   - Hitung $P_{\text{rx}}$ menggunakan operator penjumlahan dan pengurangan aritmatika.
   - Hitung nilai margin tautan.
   - Gunakan operator perbandingan relasional dan logika boolean untuk menentukan apakah tautan memenuhi syarat keandalan ($\text{Margin} \ge 10.0$).
3. **Format Laporan Output Terminal:**
   ```text
   ==================================================
           ANALISIS LINK BUDGET TAUTAN RADIO
   ==================================================
   Daya Pemancar (P_tx)        : 43.0 dBm
   Penguatan Total Antena      : 32.0 dBi (Tx: 18.0 dBi, Rx: 14.0 dBi)
   Total Redaman Lintasan      : 145.5 dB (FSPL: 142.5 dB, Misc: 3.0 dB)
   --------------------------------------------------
   Daya Sinyal Terima (P_rx)   : -70.5 dBm
   Sensitivitas Penerima (S_rx): -95.0 dBm
   Fade Margin                 : 24.5 dB
   --------------------------------------------------
   Kelayakan Tautan            : MEMENUHI SYARAT (MARGIN >= 10 dB)
   ==================================================
   ```

---

## Rubrik Penilaian (Total Bobot: 100%)

| Kriteria Penilaian | Bobot | Deskripsi Capaian |
|:---|:---:|:---|
| **Akurasi Perhitungan Formula** | 40% | Mengimplementasikan formula Link Budget dan Fade Margin dengan presisi matematis yang tepat. |
| **Penerapan Operator & Logika** | 30% | Menggunakan operator relasional dan ekspresi boolean untuk mengevaluasi kelayakan transmisi tautan. |
| **Kepatuhan Gaya PEP 8** | 20% | Penamaan variabel deskriptif, spasi antar operator konsisten, dan modularitas fungsi. |
| **Pengujian Kasus Uji Ekstrem** | 10% | Menyertakan kasus uji di mana tautan dinyatakan tidak layak karena margin tidak mencukupi. |

