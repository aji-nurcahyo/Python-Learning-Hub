import re
from pathlib import Path
import httpx
from bs4 import BeautifulSoup


def fetch_daily_feed(client: httpx.Client, path: str = "/daily-feed", max_attempts: int = 3) -> list[dict]:
    html = ""
    for attempt in range(max_attempts):
        resp = client.get(path)
        if resp.status_code in {502, 503, 504} and attempt < max_attempts - 1:
            continue
        resp.raise_for_status()
        html = resp.text
        break

    soup = BeautifulSoup(html, "html.parser")
    rows: list[dict] = []
    for tr in soup.select("table.feed-table tr.feed-row"):
        region = tr.select_one("td.region").get_text(strip=True)
        incidents = int(tr.select_one("td.incidents").get_text(strip=True))
        cost_raw = tr.select_one("td.cost").get_text(strip=True)
        cost_idr = int(re.sub(r"[^\d]", "", cost_raw))
        rows.append({"region": region, "incidents": incidents, "cost_idr": cost_idr})
    return rows


if __name__ == "__main__":
    snap = Path(__file__).resolve().parent.parent / "datasets" / "daily_feed_snapshot.html"
    calls = {"n": 0}

    def mock_feed(req: httpx.Request) -> httpx.Response:
        calls["n"] += 1
        if calls["n"] == 1:
            return httpx.Response(503)
        return httpx.Response(200, text=snap.read_text(encoding="utf-8"))

    with httpx.Client(base_url="https://feed.mock.local", transport=httpx.MockTransport(mock_feed), timeout=5.0) as c:
        data = fetch_daily_feed(c)
    print("Percobaan HTTP:", calls["n"], "| Baris diekstrak:", len(data))
    print("Record feed   :", data)

