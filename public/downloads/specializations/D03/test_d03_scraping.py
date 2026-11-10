import sys
from pathlib import Path
import httpx

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from d03_02_table_extraction_to_csv import extract_catalog_items, parse_idr_price
from d03_03_respectful_fetcher_robots import ROBOTS_TXT, is_allowed_by_robots
from d03_04_incremental_html_scraper import collect_paginated_notices, mock_notices_handler


def test_html_table_extraction_and_price_normalization() -> None:
    html_path = CODE_DIR.parent / "datasets" / "catalog_snapshot.html"
    items = extract_catalog_items(html_path.read_text(encoding="utf-8"))
    assert len(items) == 4
    assert items[0]["price_idr"] == 4250000
    assert items[0]["badge"] == "Prioritas"
    assert items[1]["badge"] is None
    assert parse_idr_price("Rp 1.450.000,-") == 1450000


def test_robots_compliance_and_paginated_notices() -> None:
    assert is_allowed_by_robots(ROBOTS_TXT, "TestBot", "/public/catalog") is True
    assert is_allowed_by_robots(ROBOTS_TXT, "TestBot", "/admin/secret") is False

    with httpx.Client(base_url="https://portal.mock.local", transport=httpx.MockTransport(mock_notices_handler), timeout=5.0) as client:
        notices = collect_paginated_notices(client)
        assert len(notices) == 3
