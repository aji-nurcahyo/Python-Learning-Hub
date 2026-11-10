# Register Lisensi Sumber Daya & Panduan Atribusi
## Python Learning Hub — Source-License & Attribution Register

Dokumen ini memetakan status legalitas, ketentuan lisensi sumber terbuka (*open source licenses*), persyaratan atribusi, dan batasan adaptasi konten dari seluruh sumber daya edukasi eksternal yang diacu dalam pengembangan **Python Learning Hub**.

---

## 1. Prinsip Kepatuhan Hak Cipta & Lisensi (*Safe Harbor Policy*)

Platform **Python Learning Hub** adalah Sumber Pembelajaran Terbuka (*Open Educational Resource / OER*) yang bersifat nirlaba, bebas diakses publik, dan didedikasikan untuk peningkatan literasi komputasi dan rekayasa telekomunikasi.

Untuk menjamin kepatuhan hak cipta 100% tanpa pelanggaran:

1. **Bukan Penggandaan Mentah (*No Raw Copy-Paste*):** Materi tidak disalin secara mentah. Penjelasan konsep ditulis ulang menggunakan narasi bahasa Indonesia yang orisinal, kontekstual, dan disesuaikan dengan kurikulum teknik.
2. **Contoh Kode Orisinal & Aplikatif:** Contoh kode Python disesuaikan secara khusus dengan kasus rekayasa telekomunikasi (analisis sinyal RSRP/RSRQ, kalkulasi dBm/Watt, telemetri IoT, pengolahan log router).
3. **Penyematan Atribusi Terbuka (*Clear Attribution*):** Setiap modul mencantumkan nama penulis asli, organisasi, tautan sumber asli, dan lisensi yang menaunginya.
4. **Penghormatan Klausul Non-Komersial (*NC Clauses*):** Sumber yang berlisensi `CC BY-NC` (seperti *Think Python* dan *CS50*) dihormati sepenuhnya. Platform ini tidak menarik biaya, tidak menampilkan iklan komersial, dan tidak memerlukan langganan berbayar.
5. **Penghormatan Klausul ShareAlike (*SA Clauses*):** Materi turunan yang mengadopsi struktur dari sumber berlisensi `CC BY-SA` atau `CC BY-NC-SA` dilisensikan kembali di bawah lisensi terbuka yang setara.

---

## 2. Register Lisensi Sumber Referensi Utama

| Sumber Referensi | Pemegang Hak Cipta / Organisasi | Jenis Lisensi | Izin Adaptasi / Turunan | Izin Non-Komersial | Kewajiban Atribusi (*Credit*) | Klausul ShareAlike (*SA*) |
|:---|:---|:---|:---:|:---:|:---|:---:|
| **Python 3 Official Tutorial** | Python Software Foundation (PSF) | PSF License Agreement 2.0 | **Ya** (Bebas) | **Ya** | Ya (Sertakan PSF copyright notice) | Tidak |
| **Think Python (3rd Edition)** | Allen B. Downey (Green Tea Press) | CC BY-NC 4.0 / CC BY-NC 3.0 | **Ya** (Bebas untuk edukasi) | **Ya** (Khusus non-komersial) | Ya (Wajib cantumkan nama Allen Downey) | Tidak |
| **30 Days of Python** | Asabeneh S. Yetayeh | MIT License | **Ya** (Sangat permisif) | **Ya** | Ya (Sertakan copyright notice MIT) | Tidak |
| **CS50’s Intro to Python (CS50P)** | David J. Malan / Harvard University | CC BY-NC-SA 4.0 | **Ya** (Adaptasi edukasi) | **Ya** (Khusus non-komersial) | Ya (Cantumkan Harvard CS50 & David Malan) | **Ya** (Harus berlisensi setara) |
| **Software Carpentry (Python)** | The Carpentries (Software Carpentry) | CC BY 4.0 (Teks) & BSD 3-Clause (Kode) | **Ya** (Sangat permisif) | **Ya** | Ya (Cantumkan The Carpentries) | Tidak |
| **Learn Python** | Oleksii Trekhleb | MIT License | **Ya** (Sangat permisif) | **Ya** | Ya (Sertakan copyright notice MIT) | Tidak |
| **pytest Documentation** | Holger Krekel & pytest-dev team | MIT License | **Ya** (Sangat permisif) | **Ya** | Ya (Sertakan copyright notice MIT) | Tidak |
| **Python Packaging User Guide** | Python Packaging Authority (PyPA) | CC BY-SA 3.0 | **Ya** (Bebas) | **Ya** | Ya (Cantumkan PyPA & link sumber) | **Ya** (Harus berlisensi setara) |
| **Upstream Software Foundation** | Program Studi Informatika ITERA | MIT License | **Ya** (Arsitektur web & deck) | **Ya** | Ya (Sertakan salinan `LICENSE.upstream`) | Tidak |

---

## 3. Matriks Hak & Batasan Legalitas (*Legal Permissions Matrix*)

### 1. Python Software Foundation License (PSF 2.0)
- **Cakupan:** Dokumentasi resmi Python (`docs.python.org/3/`).
- **Ketentuan:** Mengizinkan modifikasi, penerjemahan, dan pendistribusian ulang baik untuk kebutuhan komersial maupun non-komersial.
- **Tindakan Platform:** Digunakan sebagai rujukan kanonikal sintaks, kutipan singkat definisi resmi interpreter, dan tabel fungsi bawaan.
- **Teks Atribusi Standar:**
  > *"Python Documentation is Copyright © 2001–2026 Python Software Foundation. Used under the PSF License Agreement."*

### 2. Creative Commons Attribution-NonCommercial (CC BY-NC 4.0)
- **Cakupan:** Buku *Think Python* oleh Allen B. Downey.
- **Ketentuan:** Mengizinkan penggandaan, adaptasi, dan pengolahan ulang materi untuk tujuan non-komersial, asalkan memberikan kredit/atribusi yang layak kepada penulis.
- **Tindakan Platform:** Mengadaptasi model mental pemahaman variabel sebagai label referensi memori, diagram alur eksekusi fungsi, dan analogi komputasional. Seluruh teks diterjemahkan dan diparafrase ke dalam bahasa Indonesia.
- **Teks Atribusi Standar:**
  > *"Bagian dari model konseptual dan analogi pembelajaran ini diadaptasi dari Think Python (3rd Edition) oleh Allen B. Downey di bawah lisensi Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)."*

### 3. MIT License
- **Cakupan:** Repositori *30-Days-Of-Python* (Asabeneh Yetayeh), *learn-python* (Oleksii Trekhleb), *pytest*, dan repositori upstream *Pengkom ITERA*.
- **Ketentuan:** Lisensi sumber terbuka paling permisif di dunia. Mengizinkan penggunaan bebas, modifikasi, penggabungan, publikasi, sublisensi, dan komersialisasi dengan satu syarat mutlak: menyertakan pemberitahuan hak cipta asli dan pelepasan tanggung jawab (*disclaimer*).
- **Tindakan Platform:** Mengadaptasi variasi soal latihan Level 1/2/3 dari *30 Days of Python*, pola arsitektur kode dari *learn-python*, serta arsitektur antarmuka React/Reveal dari *Pengkom ITERA*.
- **Teks Atribusi Standar:**
  > *"Pola latihan dan contoh kode diadaptasi dari repositori 30-Days-Of-Python oleh Asabeneh S. Yetayeh dan learn-python oleh Oleksii Trekhleb di bawah lisensi MIT License."*

### 4. Creative Commons Attribution-NonCommercial-ShareAlike (CC BY-NC-SA 4.0)
- **Cakupan:** Materi *CS50’s Introduction to Programming with Python* (Harvard University).
- **Ketentuan:** Mengizinkan remix, transformasi, dan pembuatan materi turunan non-komersial dengan syarat: wajib memberikan atribusi kepada Harvard University / David J. Malan dan mendistribusikan materi turunan di bawah lisensi yang sama (`CC BY-NC-SA 4.0`).
- **Tindakan Platform:** Mengadaptasi metodologi pengujian otomatis menggunakan `pytest` untuk tugas mandiri dan struktur problem set yang menuntut ketelitian logika.
- **Teks Atribusi Standar:**
  > *"Desain studi kasus dan metodologi evaluasi unit testing terinspirasi oleh materi kurikulum CS50P (CS50's Introduction to Programming with Python) oleh David J. Malan dan Harvard University, dilisensikan di bawah CC BY-NC-SA 4.0."*

### 5. Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Cakupan:** Kurikulum *Software Carpentry: Programming with Python*.
- **Ketentuan:** Mengizinkan penggunaan dan adaptasi materi secara bebas untuk keperluan apa pun, cukup dengan memberikan atribusi kepada The Carpentries.
- **Tindakan Platform:** Mengadopsi prinsip pengolahan data array numerik bertahap dan pola pemrograman defensif (*defensive programming*).
- **Teks Atribusi Standar:**
  > *"Konsep analisis data bertahap dan pemrograman defensif merujuk pada kurikulum Software Carpentry: Programming with Python oleh The Carpentries di bawah lisensi CC BY 4.0."*

---

## 4. Templat Atribusi Footer & Dokumen Modul

Setiap berkas modul `index.md` yang mengadopsi materi terbuka wajib menyertakan blok referensi dan atribusi di bagian penutup dengan format standar berikut:

```markdown
---

## Referensi & Sumber Rujukan Terbuka
1. **Python Software Foundation.** *The Python Tutorial (Python 3.12/3.13)*. https://docs.python.org/3/tutorial/ — Berlisensi PSF License.
2. **Downey, Allen B.** *Think Python: How to Think Like a Computer Scientist (3rd Edition)*. Green Tea Press. https://allendowney.github.io/ThinkPython/ — Berlisensi CC BY-NC 4.0.
3. **Yetayeh, Asabeneh S.** *30 Days of Python*. https://github.com/Asabeneh/30-Days-Of-Python — Berlisensi MIT License.
4. **Malan, David J.** *CS50's Introduction to Programming with Python*. Harvard University. https://cs50.harvard.edu/python/ — Berlisensi CC BY-NC-SA 4.0.

> *Atribusi Hak Cipta: Seluruh materi edukasi pada modul ini dikompilasi, diterjemahkan, dan dikembangkan secara independen oleh Aji Pamungkas Tri Nurcahyo untuk platform edukasi nirlaba terbuka Python Learning Hub.*
```

---

## 5. Penyimpanan Berkas Lisensi Legal di Direktori Repositori

1. `LICENSE`: Berkas lisensi utama repositori Python Learning Hub (MIT License).
2. `public/downloads/LICENSE.upstream`: Salinan lisensi MIT repositori fondasi peramban slide Pengkom ITERA.
3. `THIRD_PARTY_NOTICES.md`: Catatan hak cipta lengkap seluruh pustaka npm (React, Reveal.js, Shiki, KaTeX, Google Fonts) dan pustaka referensi Python.

---

## 6. Tambahan Inventaris Ekosistem Specialization Tracks (`requirements-specializations.txt`)

Seluruh pustaka pihak ketiga yang dimanfaatkan pada implementasi 25 Modul Spesialisasi (`A01`–`E05`) menggunakan lisensi open-source permisif / standar industri:

| Paket / Referensi | Track Terkait | Lisensi | Tautan Dokumentasi Resmi |
| :--- | :--- | :--- | :--- |
| `numpy`, `pandas`, `scipy`, `matplotlib`, `seaborn` | Track A, B, E | BSD-3-Clause / PSF-based | [numpy.org](https://numpy.org), [pandas.pydata.org](https://pandas.pydata.org), [scipy.org](https://scipy.org) |
| `scikit-learn`, `joblib`, `nbformat` | Track A, B | BSD-3-Clause | [scikit-learn.org](https://scikit-learn.org) |
| `fastapi`, `pydantic`, `sqlalchemy`, `httpx` | Track C, D | MIT / BSD-3-Clause | [fastapi.tiangolo.com](https://fastapi.tiangolo.com), [docs.sqlalchemy.org](https://docs.sqlalchemy.org) |
| `beautifulsoup4`, `openpyxl` | Track D | MIT | [openpyxl.readthedocs.io](https://openpyxl.readthedocs.io) |
| `fpdf2` | Track D | LGPL-3.0 | [py-pdf.github.io/fpdf2](https://py-pdf.github.io/fpdf2/) |
| `pyserial`, `paho-mqtt`, `pytest` | Track A–E | BSD-3-Clause / EPL-2.0 / MIT | [pyserial.readthedocs.io](https://pyserial.readthedocs.io), [eclipse.dev/paho](https://eclipse.dev/paho) |

*Catatan: Seluruh dataset CSV, log serial, drive test RF, serta snapshot HTML pada `content/specializations/*/modules/*/datasets/` merupakan data sintetis edukatif buatan mandiri (`Python Learning Hub`) tanpa data pribadi pelanggan (PII) maupun informasi berpemilik operator mana pun.*


