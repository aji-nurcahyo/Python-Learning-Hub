import tempfile
from pathlib import Path
import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Biaya_Regional"

headers = ["Wilayah", "Kategori", "Biaya (IDR)"]
ws.append(headers)

header_fill = PatternFill("solid", fgColor="1E3A8A")
header_font = Font(bold=True, color="FFFFFF")
for col_idx in range(1, len(headers) + 1):
    cell = ws.cell(row=1, column=col_idx)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center")

rows = [
    ["Sumatera", "Pemeliharaan", 4500000],
    ["Jawa", "Energi", 6200000],
    ["Kalimantan", "Pemeliharaan", 5100000],
]
for r_idx, row in enumerate(rows, start=2):
    ws.append(row)
    ws.cell(row=r_idx, column=3).number_format = "#,##0"

ws.column_dimensions["A"].width = 16
ws.column_dimensions["B"].width = 18
ws.column_dimensions["C"].width = 18

with tempfile.TemporaryDirectory() as td:
    out_xlsx = Path(td) / "styled_report.xlsx"
    wb.save(out_xlsx)
    loaded = openpyxl.load_workbook(out_xlsx)
    print("Sheet dibuat      :", loaded.sheetnames)
    print("Header font bold  :", loaded["Biaya_Regional"]["A1"].font.bold)
    print("Format sel C2     :", loaded["Biaya_Regional"]["C2"].number_format)

