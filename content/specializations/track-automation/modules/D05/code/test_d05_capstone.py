import sys
from pathlib import Path
import httpx
import openpyxl

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from d05_04_reporting_bot_runner import run_autonomous_bot


def test_autonomous_reporting_bot_end_to_end_and_idempotent(tmp_path: Path) -> None:
    snap = CODE_DIR.parent / "datasets" / "daily_feed_snapshot.html"
    webhook_calls = {"count": 0}

    def hook_handler(req: httpx.Request) -> httpx.Response:
        webhook_calls["count"] += 1
        return httpx.Response(202)

    feed_t = httpx.MockTransport(lambda req: httpx.Response(200, text=snap.read_text(encoding="utf-8")))
    hook_t = httpx.MockTransport(hook_handler)

    with (
        httpx.Client(base_url="https://feed.mock.local", transport=feed_t, timeout=5.0) as fc,
        httpx.Client(transport=hook_t, timeout=5.0) as hc,
    ):
        first = run_autonomous_bot("2025-02-10", tmp_path, fc, hc)
        second = run_autonomous_bot("2025-02-10", tmp_path, fc, hc)

    assert first["status"] == "EXECUTED"
    assert first["total_cost_idr"] == 8400000
    assert second["status"] == "SKIPPED_IDEMPOTENT"
    assert webhook_calls["count"] == 1

    wb = openpyxl.load_workbook(tmp_path / "reports" / first["xlsx"], data_only=False)
    assert wb["Feed_Harian"]["C5"].value == "=SUM(C2:C4)"
    assert (tmp_path / "reports" / first["pdf"]).read_bytes().startswith(b"%PDF-")
    assert (tmp_path / "archives" / first["zip"]).exists()

