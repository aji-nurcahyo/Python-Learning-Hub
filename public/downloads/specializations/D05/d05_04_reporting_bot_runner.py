import sys
import tempfile
from pathlib import Path
import httpx

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from d05_01_feed_collector import fetch_daily_feed
from d05_02_excel_pdf_publisher import publish_excel_and_pdf
from d05_03_idempotent_notifier import BotStateStore, archive_files_and_rotate, send_completion_webhook


def run_autonomous_bot(
    batch_date: str,
    workspace: Path,
    feed_client: httpx.Client,
    webhook_client: httpx.Client,
) -> dict:
    ledger = BotStateStore(workspace / "ledger.json")
    job_key = f"daily-report-{batch_date}"
    if ledger.is_done(job_key):
        return {"status": "SKIPPED_IDEMPOTENT", "batch_date": batch_date}

    records = fetch_daily_feed(feed_client)
    xlsx_path, pdf_path = publish_excel_and_pdf(records, workspace / "reports", batch_date)
    zip_path = archive_files_and_rotate([xlsx_path, pdf_path], workspace / "archives", f"bundle_{batch_date}.zip", keep=3)

    summary = {
        "batch_date": batch_date,
        "rows_processed": len(records),
        "total_cost_idr": sum(r["cost_idr"] for r in records),
        "archive": zip_path.name,
    }
    webhook_status = send_completion_webhook(webhook_client, "https://hooks.mock.local/daily", summary)
    ledger.record_done(job_key, summary)
    return {
        "status": "EXECUTED",
        "webhook_status": webhook_status,
        "xlsx": xlsx_path.name,
        "pdf": pdf_path.name,
        "zip": zip_path.name,
        "total_cost_idr": summary["total_cost_idr"],
    }


if __name__ == "__main__":
    snap = CODE_DIR.parent / "datasets" / "daily_feed_snapshot.html"
    feed_transport = httpx.MockTransport(lambda req: httpx.Response(200, text=snap.read_text(encoding="utf-8")))
    hook_transport = httpx.MockTransport(lambda req: httpx.Response(202, json={"ok": True}))

    with tempfile.TemporaryDirectory() as td:
        ws = Path(td)
        with (
            httpx.Client(base_url="https://feed.mock.local", transport=feed_transport, timeout=5.0) as fc,
            httpx.Client(transport=hook_transport, timeout=5.0) as hc,
        ):
            r1 = run_autonomous_bot("2025-02-10", ws, fc, hc)
            r2 = run_autonomous_bot("2025-02-10", ws, fc, hc)
        print("Run ke-1 (eksekusi penuh):", r1)
        print("Run ke-2 (uji idempoten) :", r2)
