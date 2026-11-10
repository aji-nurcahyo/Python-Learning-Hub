"""Starter code Tugas D03: Polite Catalog & Maintenance Notice Extractor."""

from __future__ import annotations

from pathlib import Path


def is_path_allowed(robots_txt: str, user_agent: str, path: str) -> bool:
    """Memeriksa apakah jalur URL diizinkan oleh aturan robots.txt."""
    # TODO: Gunakan urllib.robotparser.RobotFileParser().parse(...)
    raise NotImplementedError("Implementasikan is_path_allowed")


def parse_idr_price(raw_text: str) -> int:
    """Mengubah string seperti 'Rp 1.450.000' menjadi integer 1450000."""
    # TODO: Gunakan regex re.sub(r'[^\\d]', '', raw_text)
    raise NotImplementedError("Implementasikan parse_idr_price")


def extract_catalog_rows(html: str) -> list[dict]:
    """Mengekstrak data perangkat dari tabel HTML dengan aman terhadap elemen None."""
    # TODO: Gunakan BeautifulSoup(html, 'html.parser') dan selector CSS semantik
    raise NotImplementedError("Implementasikan extract_catalog_rows")


if __name__ == "__main__":
    html_file = Path(__file__).resolve().parent.parent / "datasets" / "catalog_snapshot.html"
    print(f"Snapshot HTML D03 siap diparse dari: {html_file}")
