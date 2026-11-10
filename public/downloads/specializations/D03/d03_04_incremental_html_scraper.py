import httpx
from bs4 import BeautifulSoup

MOCK_PAGES = {
    1: "<ul><li class='notice'>[2025-02-01] Pemeliharaan Node A</li><li class='notice'>[2025-02-02] Kalibrasi Node B</li></ul>",
    2: "<ul><li class='notice'>[2025-02-03] Upgrade Firmware C</li></ul>",
    3: "<ul></ul>",
}


def mock_notices_handler(request: httpx.Request) -> httpx.Response:
    page = int(request.url.params.get("page", "1"))
    return httpx.Response(200, text=MOCK_PAGES.get(page, "<ul></ul>"))


def collect_paginated_notices(client: httpx.Client) -> list[str]:
    notices: list[str] = []
    page = 1
    while True:
        html = client.get("/notices", params={"page": page}).text
        soup = BeautifulSoup(html, "html.parser")
        rows = [li.get_text(strip=True) for li in soup.select("li.notice")]
        if not rows:
            break
        notices.extend(rows)
        page += 1
    return notices


if __name__ == "__main__":
    with httpx.Client(base_url="https://portal.mock.local", transport=httpx.MockTransport(mock_notices_handler), timeout=5.0) as client:
        collected = collect_paginated_notices(client)
        print("Total pengumuman terkumpul:", len(collected))
        for item in collected:
            print(" -", item)
