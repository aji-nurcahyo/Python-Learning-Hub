import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from d01_02_safe_dry_run_organizer import organize_directory
from d01_03_checksum_deduplication import find_duplicates
from d01_04_zip_backup_rotation import create_zip_backup, rotate_backups


def test_dry_run_leaves_files_untouched_until_disabled(tmp_path: Path) -> None:
    (tmp_path / "data.csv").write_text("a,b\n1,2\n", encoding="utf-8")
    plan = organize_directory(tmp_path, dry_run=True)
    assert plan == [("data.csv", "spreadsheets/data.csv")]
    assert (tmp_path / "data.csv").exists()

    organize_directory(tmp_path, dry_run=False)
    assert not (tmp_path / "data.csv").exists()
    assert (tmp_path / "spreadsheets" / "data.csv").exists()


def test_sha256_duplicates_and_zip_rotation(tmp_path: Path) -> None:
    (tmp_path / "a.txt").write_text("identical-payload", encoding="utf-8")
    (tmp_path / "b.txt").write_text("identical-payload", encoding="utf-8")
    assert find_duplicates(tmp_path) == [["a.txt", "b.txt"]]

    bkp_dir = tmp_path / "zips"
    for i in range(1, 5):
        create_zip_backup(tmp_path, bkp_dir / f"backup_0{i}.zip")
    removed = rotate_backups(bkp_dir, keep=2)
    assert removed == ["backup_01.zip", "backup_02.zip"]
    assert sorted(p.name for p in bkp_dir.glob("*.zip")) == ["backup_03.zip", "backup_04.zip"]
