# Tugas Terstruktur D02: Automated Expense Report Builder (Excel + PDF)

## Instruksi Implementasi (`tugas.py`)
1. `export_styled_workbook(df: pd.DataFrame, out_xlsx: Path) -> Path`: buat workbook memiliki dua sheet (`Detail` berisi semua baris input dan `Rekap_Wilayah` berisi ringkasan per wilayah + formula `=SUM(...)`), header biru tebal, serta format angka `#,##0`.
2. `export_executive_pdf(summary_df: pd.DataFrame, out_pdf: Path, title: str) -> Path`: buat dokumen PDF memakai `fpdf.FPDF` menampilkan judul, tabel berbingkai per wilayah, serta baris total keseluruhan.
3. Validasi dengan `pytest` bahwa file Excel memiliki formula asli dan PDF memiliki magic header `b"%PDF-"`.

## Rubrik Penilaian (Total 100 Poin)
- Formatting & Styling Excel OpenPyXL (30%)
- Kebenaran Formula & Multi-Sheet (25%)
- Kualitas Tata Letak PDF fpdf2 (25%)
- Unit Testing Artefak Dokumen (Pytest) (20%)
