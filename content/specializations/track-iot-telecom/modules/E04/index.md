# Modul E04: Wireless Network & Cellular Signal Analytics

## 1. Empat Pilar Pengukuran Radio LTE / 5G
Saat melakukan *drive test* (survei jalan raya kualitas jaringan seluler), perangkat uji merekam empat metrik utama yang saling melengkapi:
- **RSSI (*Received Signal Strength Indicator*):** total daya wideband yang diterima antena, mencakup sinyal sel target **ditambah** interferensi sel tetangga **dan** *thermal noise*.
- **RSRP (*Reference Signal Received Power*):** daya murni dari sinyal referensi per *Resource Element* milik sel pengirim (dalam dBm, umumnya `-65 dBm` hingga `-120 dBm`). Mengukur kekuatan **cakupan** murni.
- **RSRQ (*Reference Signal Received Quality*):** rasio antara RSRP berbobot jumlah Resource Block terhadap total RSSI ($N \times \text{RSRP} / \text{RSSI}$, satuan dB). Mengukur kebersihan sinyal di tengah kepadatan beban kanal.
- **SINR vs SNR:**
  - **SNR (*Signal-to-Noise Ratio*):** $\text{SNR} = S / N$, membandingkan daya sinyal hanya terhadap derau termal latar belakang.
  - **SINR (*Signal-to-Interference-plus-Noise Ratio*):** $\text{SINR} = S / (I + N)$, memasukkan gangguan ko-kanal dari menara tetangga ($I$). Pada jaringan seluler padat frekuensi, **SINR jauh lebih rendah dari SNR** dan secara langsung menentukan skema modulasi (QPSK/16QAM/64QAM) serta kecepatan unduh nyata!

---

## 2. Memisahkan Masalah Coverage vs Interferensi
Melihat dua metrik sekaligus menghindarkan teknisi dari perbaikan keliru:
1. **`COVERAGE_BLINDSPOT`:** `RSRP < -105 dBm` -> daya pancar menara tidak menjangkau lokasi (butuh penyesuaian *tilt* antena atau menara pengisi baru).
2. **`HIGH_INTERFERENCE` (*Pilot Pollution*):** `RSRP >= -90 dBm` tetapi `SINR <= 3 dB` -> sinyal sebenarnya sangat kuat, namun menara bertabrakan dengan sinyal sel tetangga sehingga memicu *ping-pong handover* dan throughput anjlok. Memperbesar daya pancar justru memperburuk kondisi ini!

---

## 3. Link Budget & Free-Space Path Loss (FSPL)
Sebagai tolok ukur batas fisik teoretis di ruang bebas (sebelum penghalang gedung/pepohonan):
$$\text{FSPL(dB)} = 32.44 + 20\log_{10}(d_{\text{km}}) + 20\log_{10}(f_{\text{MHz}})$$
Setiap penggandaan jarak ($2\times d$) atau penggandaan frekuensi ($2\times f$) menambah rugi propagasi sebesar **$\approx 6\text{ dB}$**.

