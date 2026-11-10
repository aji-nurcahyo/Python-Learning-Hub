import tempfile
from pathlib import Path
import openpyxl
from openpyxl.styles import Font

wb = openpyxl.Workbook()
ws_detail = wb.active
ws_detail.title = "Detail"
ws_detail.append(["Region", "Amount"])
data = [("Sumatera", 4500000), ("Sumatera", 2800000), ("Jawa", 6200000), ("Kalimantan", 5100000)]
for row in data:
    ws_detail.append(list(row))

ws_summary = wb.create_sheet("Ringkasan")
ws_summary.append(["Region", "Total_Biaya"])
ws_summary.append(["Sumatera", '=SUMIF(Detail!A2:A5,"Sumatera",Detail!B2:B5)'])
ws_summary.append(["Jawa", '=SUMIF(Detail!A2:A5,"Jawa",Detail!B2:B5)'])
ws_summary.append(["Kalimantan", '=SUMIF(Detail!A2:A5,"Kalimantan",Detail!B2:B5)'])
ws_summary.append(["GRAND TOTAL", "=SUM(B2:B4)"])
ws_summary["A5"].font = Font(bold=True)
ws_summary["B5"].font = Font(bold=True)

with tempfile.TemporaryDirectory() as td:
    out = Path(td) / "multisheet_formulas.xlsx"
    wb.save(out)
    reopened = openpyxl.load_workbook(out, data_only=False)
    print("Daftar sheet        :", reopened.sheetnames)
    print("Formula Sumatera B2 :", reopened["Ringkasan"]["B2"].value)
    print("Formula Grand Total :", reopened["Ringkasan"]["B5"].value)
