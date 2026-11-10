# Latihan Mandiri D02 — Excel & PDF Document Automation

## Latihan 1: Styling Workbook & Formula
1. Muat `datasets/regional_expense_records.csv` menggunakan Pandas.
2. Buat workbook Excel berisi dua sheet: `Detail` dan `Rekap_Wilayah`.
3. Terapkan `PatternFill` & `Font(bold=True)` pada header serta format ribuan `#,##0` pada kolom biaya.
4. Sisipkan formula `=SUM(...)` di baris total lalu ekspor ringkasan wilayah ke dokumen PDF dengan `fpdf2`.

