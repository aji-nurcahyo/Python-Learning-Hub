from pathlib import Path
from bs4 import BeautifulSoup

html_path = Path(__file__).resolve().parent.parent / "datasets" / "catalog_snapshot.html"
soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "html.parser")

title_text = soup.select_one("header h1").get_text(strip=True)
rows = soup.select("table#device-catalog tbody tr.device-row")

print("Judul Halaman :", title_text)
print("Jumlah Baris  :", len(rows))
for row in rows:
    code = row.select_one("td.col-code").get_text(strip=True)
    badge = row.select_one("span.badge-note")
    note = badge.get_text(strip=True) if badge is not None else "-"
    print(f" - {code} | category={row.get('data-category')} | badge={note}")

