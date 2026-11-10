import json
import tempfile
import zipfile
from pathlib import Path
import httpx


def archive_files_and_rotate(files: list[Path], archive_dir: Path, zip_name: str, keep: int = 3) -> Path:
    archive_dir.mkdir(parents=True, exist_ok=True)
    zip_path = archive_dir / zip_name
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for f in files:
            zf.write(f, arcname=f.name)
    zips = sorted(archive_dir.glob("*.zip"))
    if len(zips) > keep:
        for old in zips[: len(zips) - keep]:
            old.unlink()
    return zip_path


class BotStateStore:
    def __init__(self, state_file: Path) -> None:
        self.state_file = state_file

    def is_done(self, key: str) -> bool:
        if not self.state_file.exists():
            return False
        return key in json.loads(self.state_file.read_text(encoding="utf-8"))

    def record_done(self, key: str, summary: dict) -> None:
        data = json.loads(self.state_file.read_text(encoding="utf-8")) if self.state_file.exists() else {}
        data[key] = summary
        self.state_file.parent.mkdir(parents=True, exist_ok=True)
        self.state_file.write_text(json.dumps(data, indent=2), encoding="utf-8")


def send_completion_webhook(client: httpx.Client, url: str, summary: dict) -> int:
    resp = client.post(url, json=summary)
    resp.raise_for_status()
    return resp.status_code


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        f1 = root / "a.txt"
        f1.write_text("ok", encoding="utf-8")
        zp = archive_files_and_rotate([f1], root / "bkp", "bkp_01.zip", keep=2)
        store = BotStateStore(root / "ledger.json")
        store.record_done("2025-02-10", {"zip": zp.name})
        print("Arsip ZIP  :", zp.name, "| exists:", zp.exists())
        print("State done :", store.is_done("2025-02-10"))
