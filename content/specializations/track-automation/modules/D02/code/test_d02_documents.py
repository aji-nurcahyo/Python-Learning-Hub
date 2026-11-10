import sys
from pathlib import Path
import openpyxl

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from d02_04_csv_to_excel_pdf_pipeline import generate_excel_and_pdf_bundle


def test_excel_and_pdf_artifacts_generated_valid(tmp_path: Path) -> None:
    csv_file = CODE_DIR.parent / "datasets" / "regional_expense_records.csv"
    xlsx_p, pdf_p = generate_excel_and_pdf_bundle(csv_file, tmp_path)

    assert xlsx_p.exists() and xlsx_p.stat().st_size > 2000
    wb = openpyxl.load_workbook(xlsx_p, data_only=False)
    ws = wb["Rekap_Wilayah"]
    assert ws["C5"].value == "=SUM(C2:C4)"

    assert pdf_p.exists() and pdf_p.stat().st_size > 800
    assert pdf_p.read_bytes().startswith(b"%PDF-")

