import tempfile
import zipfile
from pathlib import Path


def create_zip_backup(source_dir: Path, zip_path: Path) -> Path:
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for file_path in sorted(source_dir.rglob("*")):
            if file_path.is_file():
                zf.write(file_path, arcname=file_path.relative_to(source_dir))
    return zip_path


def rotate_backups(backup_dir: Path, keep: int = 3) -> list[str]:
    archives = sorted(backup_dir.glob("backup_*.zip"))
    removed: list[str] = []
    if len(archives) > keep:
        for old_zip in archives[: len(archives) - keep]:
            removed.append(old_zip.name)
            old_zip.unlink()
    return removed


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        src = root / "workspace"
        bkp = root / "backups"
        src.mkdir()
        (src / "config.json").write_text('{"env": "prod"}', encoding="utf-8")

        for day in ["20250101", "20250102", "20250103", "20250104"]:
            create_zip_backup(src, bkp / f"backup_{day}.zip")

        removed = rotate_backups(bkp, keep=2)
        remaining = sorted([p.name for p in bkp.glob("backup_*.zip")])
        print("Arsip lama dihapus :", removed)
        print("Arsip dipertahankan:", remaining)
