import sys
import tempfile
from pathlib import Path
import openpyxl
import pandas as pd
from openpyxl.styles import Font, PatternFill

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from d02_03_fpdf2_pdf_report import render_pdf_summary


def generate_excel_and_pdf_bundle(csv_path: Path, out_dir: Path) -> tuple[Path, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(csv_path)
    summary = (
        df.groupby("region", as_index=False)
        .agg(item_count=("record_id", "count"), total_idr=("amount_idr", "sum"))
        .sort_values("total_idr", ascending=False)
    )

    xlsx_path = out_dir / "regional_expenses.xlsx"
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Rekap_Wilayah"
    ws.append(["Wilayah", "Jumlah Item", "Total (IDR)"])
    for col in range(1, 4):
        c = ws.cell(row=1, column=col)
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="1E3A8A")

    for r_idx, row in enumerate(summary.itertuples(index=False), start=2):
        ws.append([row.region, int(row.item_count), int(row.total_idr)])
        ws.cell(row=r_idx, column=3).number_format = "#,##0"

    last_row = len(summary) + 1
    total_row = last_row + 1
    ws.append(["TOTAL", f"=SUM(B2:B{last_row})", f"=SUM(C2:C{last_row})"])
    ws.cell(row=total_row, column=1).font = Font(bold=True)
    ws.cell(row=total_row, column=3).number_format = "#,##0"
    wb.save(xlsx_path)

    pdf_path = out_dir / "regional_expenses.pdf"
    pdf_rows = [(str(r.region), int(r.item_count), int(r.total_idr)) for r in summary.itertuples(index=False)]
    render_pdf_summary(pdf_rows, pdf_path)
    return xlsx_path, pdf_path


if __name__ == "__main__":
    csv_file = CODE_DIR.parent / "datasets" / "regional_expense_records.csv"
    with tempfile.TemporaryDirectory() as td:
        xlsx_p, pdf_p = generate_excel_and_pdf_bundle(csv_file, Path(td))
        wb = openpyxl.load_workbook(xlsx_p, data_only=False)
        print("Excel generated :", xlsx_p.name, "| formula total:", wb["Rekap_Wilayah"]["C5"].value)
        print("PDF generated   :", pdf_p.name, "| magic:", pdf_p.read_bytes()[:5].decode("ascii"))
