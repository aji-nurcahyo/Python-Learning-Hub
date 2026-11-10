import hashlib
import tempfile
from collections import defaultdict
from pathlib import Path


def sha256_file(path: Path, chunk_size: int = 65536) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        while chunk := fh.read(chunk_size):
            h.update(chunk)
    return h.hexdigest()


def find_duplicates(root: Path) -> list[list[str]]:
    buckets: dict[str, list[str]] = defaultdict(list)
    for f in sorted(root.rglob("*")):
        if f.is_file():
            buckets[sha256_file(f)].append(f.name)
    return [sorted(names) for names in buckets.values() if len(names) > 1]


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / "laporan_asli.txt").write_text("Data QoS Q1 2025", encoding="utf-8")
        (root / "salinan_revisi.txt").write_text("Data QoS Q1 2025", encoding="utf-8")
        (root / "berkas_unik.txt").write_text("Data Berbeda", encoding="utf-8")

        dups = find_duplicates(root)
        print("Kelompok file identik SHA-256:", dups)

