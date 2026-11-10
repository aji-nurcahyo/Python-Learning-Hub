#!/usr/bin/env python3
"""
Runner & Verifier untuk modul Spesialisasi (Tracks A-E).
Menjalankan semua skrip contoh (*.py selain test_*.py), pytest suites (test_*.py),
serta validasi notebook (*.ipynb), lalu memperbarui src/code/spec-outputs.json.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent.parent
SPEC_DIR = ROOT / "content" / "specializations"
OUTPUTS_FILE = ROOT / "src" / "code" / "spec-outputs.json"
DOWNLOADS_DIR = ROOT / "public" / "downloads" / "specializations"


def sync_module_downloads(mod_path: Path, mod_id: str) -> None:
    target_dir = DOWNLOADS_DIR / mod_id
    target_dir.mkdir(parents=True, exist_ok=True)
    for sub in ("code", "notebooks", "datasets"):
        src_sub = mod_path / sub
        if src_sub.exists():
            for f in src_sub.iterdir():
                if f.is_file():
                    shutil.copy2(f, target_dir / f.name)
    for fname in ("tugas.md", "tugas.py"):
        src_f = mod_path / "assignments" / fname
        if src_f.exists():
            shutil.copy2(src_f, target_dir / fname)


def run_module_scripts(track_filter: str | None = None, check_only: bool = False) -> int:
    if OUTPUTS_FILE.exists():
        outputs: dict[str, str] = json.loads(OUTPUTS_FILE.read_text(encoding="utf-8"))
    else:
        outputs = {}

    tracks = sorted([p for p in SPEC_DIR.iterdir() if p.is_dir() and p.name.startswith("track-")])
    if track_filter:
        tracks = [t for t in tracks if t.name == track_filter or t.name == f"track-{track_filter}"]

    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    env["MPLBACKEND"] = "Agg"

    total_scripts = 0
    total_tests = 0
    total_notebooks = 0
    failures: list[str] = []

    for track_path in tracks:
        modules_dir = track_path / "modules"
        if not modules_dir.exists():
            continue

        for mod_path in sorted([p for p in modules_dir.iterdir() if p.is_dir()]):
            mod_id = mod_path.name
            if not check_only:
                sync_module_downloads(mod_path, mod_id)
            code_dir = mod_path / "code"
            if not code_dir.exists():
                continue

            py_files = sorted(code_dir.glob("*.py"))
            example_files = [f for f in py_files if not f.name.startswith("test_") and not f.name.startswith("_")]
            test_files = [f for f in py_files if f.name.startswith("test_")]

            for py_file in example_files:
                total_scripts += 1
                key = f"spec/{mod_id}/{py_file.stem}"
                res = subprocess.run(
                    [sys.executable, str(py_file)],
                    cwd=str(mod_path),
                    env=env,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    timeout=45,
                )
                if res.returncode != 0:
                    failures.append(f"[SCRIPT FAIL] {key}: exit={res.returncode}\n{res.stderr.strip()}")
                else:
                    clean_out = res.stdout.rstrip("\r\n")
                    if check_only:
                        recorded = outputs.get(key)
                        if recorded != clean_out:
                            failures.append(f"[OUTPUT MISMATCH] {key}")
                    else:
                        outputs[key] = clean_out
                    print(f"  [OK] {key}")

            if test_files:
                total_tests += len(test_files)
                res_test = subprocess.run(
                    [sys.executable, "-m", "pytest", "-q", *map(str, test_files)],
                    cwd=str(mod_path),
                    env=env,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    timeout=60,
                )
                if res_test.returncode != 0:
                    failures.append(
                        f"[PYTEST FAIL] {mod_id}:\n{res_test.stdout.strip()}\n{res_test.stderr.strip()}"
                    )
                else:
                    summary = res_test.stdout.strip().splitlines()[-1] if res_test.stdout.strip() else "passed"
                    print(f"  [PYTEST OK] {mod_id}: {summary}")

            # Validate notebooks if nbformat is installed
            for nb_file in sorted(mod_path.rglob("*.ipynb")):
                total_notebooks += 1
                try:
                    import nbformat

                    nb = nbformat.read(nb_file, as_version=4)
                    ns: dict[str, object] = {}
                    for idx, cell in enumerate(nb.cells):
                        if cell.cell_type == "code":
                            src = cell.source.strip()
                            if src:
                                old_cwd = os.getcwd()
                                try:
                                    os.chdir(str(mod_path))
                                    exec(compile(src, f"{nb_file.name}#cell{idx}", "exec"), ns)
                                finally:
                                    os.chdir(old_cwd)
                    print(f"  [NOTEBOOK OK] {mod_id}/{nb_file.name}")
                except Exception as exc:
                    failures.append(f"[NOTEBOOK FAIL] {mod_id}/{nb_file.name}: {exc}")

    if not check_only:
        sorted_outputs = {k: outputs[k] for k in sorted(outputs.keys())}
        OUTPUTS_FILE.write_text(json.dumps(sorted_outputs, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(
        f"\nRingkasan: scripts={total_scripts}, test_files={total_tests}, notebooks={total_notebooks}, failures={len(failures)}"
    )
    if failures:
        print("\nDetail Kegagalan:")
        for err in failures:
            print(err)
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Run & verify Python Learning Hub specialization code.")
    parser.add_argument("--track", help="Filter track name, e.g. track-data-science or data-science")
    parser.add_argument("--check", action="store_true", help="Verify outputs match spec-outputs.json without overwriting")
    args = parser.parse_args()
    return run_module_scripts(track_filter=args.track, check_only=args.check)


if __name__ == "__main__":
    raise SystemExit(main())
