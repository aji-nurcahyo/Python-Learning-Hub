"""Starter code Tugas D02: Automated Expense Report Builder (Excel + PDF)."""

from __future__ import annotations

from pathlib import Path
import pandas as pd


def export_styled_workbook(df: pd.DataFrame, out_xlsx: Path) -> Path:
    """Membuat workbook .xlsx multi-sheet terformat rapi dengan formula SUM aktif."""
    # TODO: Gunakan openpyxl.Workbook(), PatternFill, Font, number_format='#,##0', dan formula =SUM(...)
    raise NotImplementedError("Implementasikan export_styled_workbook")


def export_executive_pdf(summary_df: pd.DataFrame, out_pdf: Path, title: str = "Executive Expense Report") -> Path:
    """Merender laporan PDF eksekutif menggunakan fpdf.FPDF."""
    # TODO: Gunakan FPDF(), set_font(), cell(..., new_x='LMARGIN', new_y='NEXT'), dan output()
    raise NotImplementedError("Implementasikan export_executive_pdf")


if __name__ == "__main__":
    csv_path = Path(__file__).resolve().parent.parent / "datasets" / "regional_expense_records.csv"
    print(f"Dataset D02 siap diolah dari: {csv_path}")

