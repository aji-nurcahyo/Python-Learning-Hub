import tempfile
from collections import Counter
from pathlib import Path


def build_inventory(root: Path) -> dict:
    ext_counts: Counter[str] = Counter()
    total_bytes = 0
    files = sorted([p for p in root.rglob("*") if p.is_file()])
    for f in files:
        ext = f.suffix.lower() or "<no_ext>"
        ext_counts[ext] += 1
        total_bytes += f.stat().st_size
    return {"file_count": len(files), "total_bytes": total_bytes, "by_extension": dict(sorted(ext_counts.items()))}


with tempfile.TemporaryDirectory() as td:
    base = Path(td)
    (base / "sub").mkdir()
    (base / "report.csv").write_text("id,val\n1,100\n", encoding="utf-8", newline="\n")
    (base / "notes.txt").write_text("catatan operasional", encoding="utf-8", newline="\n")
    (base / "sub" / "backup.csv").write_text("id,val\n2,200\n", encoding="utf-8", newline="\n")

    summary = build_inventory(base)
    print("Total berkas terdeteksi :", summary["file_count"])
    print("Total ukuran (bytes)    :", summary["total_bytes"])
    print("Sebaran ekstensi        :", summary["by_extension"])

