import tempfile
from pathlib import Path
from fpdf import FPDF


def render_pdf_summary(rows: list[tuple[str, int, int]], out_pdf: Path) -> Path:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 15)
    pdf.cell(0, 10, "Laporan Ringkasan Pengeluaran Regional", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("Helvetica", "", 10)
    pdf.cell(0, 8, "Unit Infrastruktur Telekomunikasi - Periode Laporan Q1", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)

    # Table header
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(60, 8, "Wilayah", border=1)
    pdf.cell(40, 8, "Jumlah Item", border=1, align="C")
    pdf.cell(60, 8, "Total (IDR)", border=1, align="R", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("Helvetica", "", 10)
    grand_total = 0
    for region, count, total in rows:
        grand_total += total
        pdf.cell(60, 8, region, border=1)
        pdf.cell(40, 8, str(count), border=1, align="C")
        pdf.cell(60, 8, f"Rp {total:,}", border=1, align="R", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(100, 9, "GRAND TOTAL", border=1)
    pdf.cell(60, 9, f"Rp {grand_total:,}", border=1, align="R", new_x="LMARGIN", new_y="NEXT")

    pdf.output(str(out_pdf))
    return out_pdf


if __name__ == "__main__":
    sample_rows = [("Sumatera", 3, 12600000), ("Jawa", 3, 17200000), ("Kalimantan", 2, 10000000)]
    with tempfile.TemporaryDirectory() as td:
        pdf_path = render_pdf_summary(sample_rows, Path(td) / "executive_report.pdf")
        header = pdf_path.read_bytes()[:5]
        print("PDF tercipta     :", pdf_path.name)
        print("Header valid PDF :", header.decode("ascii"))
        print("Ukuran non-kosong:", pdf_path.stat().st_size > 800)

