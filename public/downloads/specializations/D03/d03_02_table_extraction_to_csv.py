import re
from pathlib import Path
from bs4 import BeautifulSoup


def parse_idr_price(raw_price: str) -> int:
    digits = re.sub(r"[^\d]", "", raw_price)
    return int(digits) if digits else 0


def extract_catalog_items(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    items: list[dict] = []
    for row in soup.select("table#device-catalog tbody tr.device-row"):
        name_el = row.select_one("td.col-name")
        badge_el = row.select_one("span.badge-note")
        badge_text = badge_el.get_text(strip=True) if badge_el is not None else ""
        full_name = name_el.get_text(" ", strip=True) if name_el is not None else ""
        clean_name = full_name.removesuffix(badge_text).strip() if badge_text else full_name

        items.append(
            {
                "code": row.select_one("td.col-code").get_text(strip=True),
                "name": clean_name,
                "badge": badge_text or None,
                "region": row.select_one("td.col-region").get_text(strip=True),
                "price_idr": parse_idr_price(row.select_one("td.col-price").get_text(strip=True)),
                "status": row.select_one("td.col-status").get_text(strip=True),
            }
        )
    return items


if __name__ == "__main__":
    html_path = Path(__file__).resolve().parent.parent / "datasets" / "catalog_snapshot.html"
    records = extract_catalog_items(html_path.read_text(encoding="utf-8"))
    print("Total item diekstrak:", len(records))
    for rec in records:
        print(rec)
