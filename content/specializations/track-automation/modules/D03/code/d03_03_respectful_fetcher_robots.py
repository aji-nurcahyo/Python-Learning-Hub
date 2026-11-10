from urllib.robotparser import RobotFileParser
import httpx

ROBOTS_TXT = """
User-agent: *
Disallow: /admin/
Disallow: /private/
Allow: /public/
""".strip()


def is_allowed_by_robots(robots_content: str, user_agent: str, path: str) -> bool:
    rp = RobotFileParser()
    rp.parse(robots_content.splitlines())
    return rp.can_fetch(user_agent, path)


def mock_site(request: httpx.Request) -> httpx.Response:
    if request.url.path == "/robots.txt":
        return httpx.Response(200, text=ROBOTS_TXT)
    if request.url.path == "/public/catalog":
        return httpx.Response(200, text="<html><body><h1>Katalog Terbuka</h1></body></html>")
    return httpx.Response(404, text="Not Found")


if __name__ == "__main__":
    ua = "PythonLearningHubBot/1.0"
    with httpx.Client(base_url="https://portal.mock.local", transport=httpx.MockTransport(mock_site), headers={"User-Agent": ua}, timeout=5.0) as client:
        robots_raw = client.get("/robots.txt").text
        for target_path in ["/public/catalog", "/admin/export"]:
            allowed = is_allowed_by_robots(robots_raw, ua, target_path)
            if allowed:
                status_code = client.get(target_path).status_code
                print(f"{target_path:16s} -> allowed=True  | HTTP {status_code}")
            else:
                print(f"{target_path:16s} -> allowed=False | Dilewati sesuai robots.txt")

