import json
import tempfile
from pathlib import Path


class IdempotentLedger:
    def __init__(self, ledger_path: Path) -> None:
        self.ledger_path = ledger_path

    def _load(self) -> dict[str, str]:
        if not self.ledger_path.exists():
            return {}
        return json.loads(self.ledger_path.read_text(encoding="utf-8"))

    def has_completed(self, job_key: str) -> bool:
        return job_key in self._load()

    def mark_completed(self, job_key: str, status: str = "completed") -> None:
        data = self._load()
        data[job_key] = status
        self.ledger_path.parent.mkdir(parents=True, exist_ok=True)
        self.ledger_path.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")


def execute_daily_job(job_key: str, ledger: IdempotentLedger) -> str:
    if ledger.has_completed(job_key):
        return f"SKIPPED ({job_key} sudah selesai sebelumnya)"
    ledger.mark_completed(job_key, "ok")
    return f"EXECUTED ({job_key} diproses sukses)"


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as td:
        ledger = IdempotentLedger(Path(td) / "job_state.json")
        print("Eksekusi 1:", execute_daily_job("daily-sync-2025-02-01", ledger))
        print("Eksekusi 2:", execute_daily_job("daily-sync-2025-02-01", ledger))
        print("Eksekusi 3:", execute_daily_job("daily-sync-2025-02-02", ledger))
