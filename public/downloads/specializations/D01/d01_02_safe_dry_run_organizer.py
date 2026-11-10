import shutil
import tempfile
from pathlib import Path

CATEGORY_MAP = {
    ".csv": "spreadsheets",
    ".xlsx": "spreadsheets",
    ".pdf": "documents",
    ".txt": "documents",
    ".log": "logs",
}


def organize_directory(inbox: Path, dry_run: bool = True) -> list[tuple[str, str]]:
    actions: list[tuple[str, str]] = []
    for item in sorted(inbox.iterdir()):
        if not item.is_file():
            continue
        folder_name = CATEGORY_MAP.get(item.suffix.lower(), "others")
        target_dir = inbox / folder_name
        dest = target_dir / item.name
        actions.append((item.name, f"{folder_name}/{item.name}"))
        if not dry_run:
            target_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(item), str(dest))
    return actions


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as td:
        inbox = Path(td)
        for fname in ["qos_jan.csv", "sop.pdf", "error.log", "unknown.bin"]:
            (inbox / fname).write_text(f"dummy {fname}", encoding="utf-8")

        preview = organize_directory(inbox, dry_run=True)
        print("Mode DRY-RUN (rencana)  :", preview)
        print("Masih di root pasca dry :", sorted([p.name for p in inbox.iterdir() if p.is_file()]))

        organize_directory(inbox, dry_run=False)
        print("Folder terbentuk        :", sorted([p.name for p in inbox.iterdir() if p.is_dir()]))
        print("Root tersisa file       :", [p.name for p in inbox.iterdir() if p.is_file()])
