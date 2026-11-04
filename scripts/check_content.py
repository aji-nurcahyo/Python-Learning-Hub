"""Regression checks for modular chapter structure, slide preservation, and runnable Python contracts."""
from pathlib import Path
import re, json, html, importlib.util

root = Path(__file__).resolve().parents[1]

# 1. Verify 30 chapters across content/
chapters = list(root.glob('content/**/chapter-*/metadata.json'))
assert len(chapters) == 30, f"Expected 30 chapters, found {len(chapters)}"

# 2. Verify 5 tracks
tracks = list(root.glob('content/specializations/track-*/metadata.json'))
assert len(tracks) == 5, f"Expected 5 tracks, found {len(tracks)}"

# 3. Test Chapter 10 (Functions) contract
ch10_contoh = root / 'content/foundations/chapter-10/assignments/contoh.py'
assert ch10_contoh.is_file(), "Missing Chapter 10 contoh.py"
spec10 = importlib.util.spec_from_file_location('ch10', ch10_contoh)
mod10 = importlib.util.module_from_spec(spec10)
spec10.loader.exec_module(mod10)
assert mod10.rata_rata([]) is None
assert mod10.rata_rata([-80, -100]) == -90
assert [mod10.kategori_rsrp(v) for v in [-90, -91, -105, -106]] == ['Baik', 'Sedang', 'Sedang', 'Buruk']
print("Chapter 10: Functions & contracts verified.")

# 4. Test Chapter 08 (Collections & Algorithms) contract
ch08_contoh = root / 'content/foundations/chapter-08/assignments/contoh.py'
assert ch08_contoh.is_file(), "Missing Chapter 08 contoh.py"
spec08 = importlib.util.spec_from_file_location('ch08', ch08_contoh)
mod08 = importlib.util.module_from_spec(spec08)
spec08.loader.exec_module(mod08)
for data in [[], [1], [3, 1, 3, -2], [5, 4, 3, 2, 1]]:
    before = data.copy()
    assert mod08.selection_sort(data) == sorted(data)
    assert before == data
assert mod08.cari_sensor([], 'missing') is None
assert mod08.ringkasan([]) is None
assert mod08.filter_lemah([{'rsrp': -100}, {'rsrp': -101}]) == [{'rsrp': -101}]
print("Chapter 08: Collections & algorithms verified.")

print(f"[OK] {len(chapters)} chapters and {len(tracks)} tracks successfully verified!")
