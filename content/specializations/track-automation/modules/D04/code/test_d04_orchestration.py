import sys
from pathlib import Path
import httpx
import pytest

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from d04_01_retry_exponential_backoff import run_with_backoff
from d04_02_idempotent_job_ledger import IdempotentLedger, execute_daily_job
from d04_03_webhook_alert_formatter import build_alert_payload, send_webhook_alert
from d04_04_cli_cron_runner import run_cli


def test_backoff_delays_and_exhaustion() -> None:
    waits: list[float] = []

    def always_fail() -> None:
        raise RuntimeError("Down")

    with pytest.raises(RuntimeError):
        run_with_backoff(always_fail, max_attempts=3, base_delay=0.25, sleep_fn=waits.append)
    assert waits == [0.25, 0.5]


def test_idempotent_ledger_skips_duplicate_and_webhook_sends(tmp_path: Path) -> None:
    ledger = IdempotentLedger(tmp_path / "state.json")
    assert execute_daily_job("job-2025-02-01", ledger).startswith("EXECUTED")
    assert execute_daily_job("job-2025-02-01", ledger).startswith("SKIPPED")

    transport = httpx.MockTransport(lambda req: httpx.Response(202))
    with httpx.Client(transport=transport, timeout=3.0) as client:
        status = send_webhook_alert(client, "https://hooks.local/test", build_alert_payload("j", "warn", "ok"))
        assert status == 202
    assert run_cli(["--job-date", "2025-02-01"]) == 0
    assert run_cli(["--job-date", "2025-02-01", "--simulate-fail"]) == 1

