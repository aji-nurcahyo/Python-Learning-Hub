import tempfile
from pathlib import Path
import openpyxl
from fpdf import FPDF
from openpyxl.styles import Font, PatternFill


def publish_excel_and_pdf(records: list[dict], out_dir: Path, batch_date: str) -> tuple[Path, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    xlsx_path = out_dir / f"daily_report_{batch_date}.xlsx"
    pdf_path = out_dir / f"daily_report_{batch_date}.pdf"

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Feed_Harian"
    ws.append(["Wilayah", "Insiden", "Biaya (IDR)"])
    for col in range(1, 4):
        cell = ws.cell(row=1, column=col)
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill("solid", fgColor="1E3A8A")

    for idx, rec in enumerate(records, start=2):
        ws.append([rec["region"], rec["incidents"], rec["cost_idr"]])
        ws.cell(row=idx, column=3).number_format = "#,##0"

    last_row = len(records) + 1
    ws.append(["TOTAL", f"=SUM(B2:B{last_row})", f"=SUM(C2:C{last_row})"])
    ws.cell(row=last_row + 1, column=1).font = Font(bold=True)
    ws.cell(row=last_row + 1, column=3).number_format = "#,##0"
    wb.save(xlsx_path)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 10, f"Laporan Harian Infrastruktur ({batch_date})", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 10)
    for rec in records:
        pdf.cell(60, 8, rec["region"], border=1)
        pdf.cell(40, 8, f"{rec['incidents']} insiden", border=1, align="C")
        pdf.cell(60, 8, f"Rp {rec['cost_idr']:,}", border=1, align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.output(str(pdf_path))
    return xlsx_path, pdf_path


if __name__ == "__main__":
    sample = [{"region": "Sumatera", "incidents": 2, "cost_idr": 2400000}, {"region": "Jawa", "incidents": 3, "cost_idr": 4150000}]
    with tempfile.TemporaryDirectory() as td:
        xp, pp = publish_excel_and_pdf(sample, Path(td), "2025-02-10")
        print("Excel:", xp.name, "| exists:", xp.exists())
        print("PDF  :", pp.name, "| magic:", pp.read_bytes()[:5].decode("ascii"))
