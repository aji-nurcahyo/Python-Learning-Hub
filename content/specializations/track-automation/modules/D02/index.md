# Modul D02: Spreadsheet & PDF Document Automation

## 1. Mengapa Otomasi Dokumen Menghemat Ratusan Jam Kerja?
Banyak tim operasional dan administrasi menghabiskan berjam-jam tiap minggu menyalin CSV ke Excel, menebalkan header, menyesuaikan lebar kolom, menulis `=SUM(...)`, lalu mengekspor ringkasan PDF. Python mengubah pekerjaan manual 2 jam tersebut menjadi skrip deterministik kurang dari 1 detik.

---

## 2. Workbook Excel Profesional dengan `openpyxl`
Berbeda dengan `df.to_excel()` polos, **`openpyxl`** memberi kendali penuh atas presentasi dan fungsionalitas spreadsheet:
- **Styling Sel:** `Font(bold=True, color="FFFFFF")` dan `PatternFill("solid", fgColor="1E3A8A")`.
- **Format Angka:** `cell.number_format = "#,##0"` agar angka jutaan terbaca seketika.
- **Formula Hidup:** tulis string `"=SUM(B2:B5)"` langsung ke `cell.value` sehingga spreadsheet tetap dinamis saat diedit penerima.
- **Auto-Fit Lebar Kolom:** hitung `max(len(str(val)))` per kolom + padding agar teks tidak terpotong `###`.

---

## 3. Laporan PDF Eksekutif Memakai `fpdf2`
Pustaka **`fpdf2`** (`from fpdf import FPDF`) murni Python tanpa dependensi peramban berat, ideal untuk mencetak PDF invoice, sertifikat, maupun ringkasan eksekutif:
- Gunakan `set_font("Helvetica", "B", 14)` untuk judul.
- Gunakan `pdf.cell(w, h, text, border=1, new_x="LMARGIN", new_y="NEXT")` untuk membangun baris tabel bersih.
- Verifikasi file PDF hasil dengan memeriksa prefiks biner `%PDF-` dan ukuran byte.

