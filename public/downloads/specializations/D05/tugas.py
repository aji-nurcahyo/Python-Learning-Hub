"""Starter code Capstone D05: Autonomous Daily Ingestion & Reporting Bot."""

from __future__ import annotations

from pathlib import Path
import httpx


def collect_daily_feed(client: httpx.Client, path: str = "/daily-feed") -> list[dict]:
    """Mengunduh HTML feed dengan retry selektif dan mengekstrak record bersih."""
    # TODO: Implementasikan retry 502/503/504 dan BeautifulSoup extraction
    raise NotImplementedError("Implementasikan collect_daily_feed")


def publish_report_bundle(records: list[dict], out_dir: Path, batch_date: str) -> tuple[Path, Path]:
    """Memproduksi workbook Excel berformula =SUM() dan ringkasan PDF fpdf2."""
    # TODO: Hasilkan file .xlsx dan .pdf pada out_dir
    raise NotImplementedError("Implementasikan publish_report_bundle")


def run_bot_once(
    batch_date: str,
    workspace: Path,
    feed_client: httpx.Client,
    webhook_client: httpx.Client,
) -> dict:
    """Orkestrator harian idempoten: Collect -> Excel/PDF -> ZIP -> Webhook -> Commit Ledger."""
    # TODO: Pastikan status ledger dicatat hanya sesudah semua artefak & webhook sukses
    raise NotImplementedError("Implementasikan run_bot_once")


if __name__ == "__main__":
    html_file = Path(__file__).resolve().parent.parent / "datasets" / "daily_feed_snapshot.html"
    print(f"Starter Capstone D05 siap diuji dengan fixture: {html_file}")
