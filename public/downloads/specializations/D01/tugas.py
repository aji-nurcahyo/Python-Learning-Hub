"""Starter code Tugas D01: Safe Workspace Organizer & Rotating Backup."""

from __future__ import annotations

from pathlib import Path


def organize_by_extension(base_dir: Path, dry_run: bool = True) -> list[tuple[str, str]]:
    """Merencanakan atau memindahkan file berdasarkan ekstensi secara aman."""
    # TODO: Gunakan CATEGORY_MAP + shutil.move hanya saat dry_run=False
    raise NotImplementedError("Implementasikan organize_by_extension")


def find_exact_duplicates(root_dir: Path) -> list[list[str]]:
    """Mendeteksi kelompok berkas identik memakai SHA-256 chunk 64 KB."""
    # TODO: Baca byte per chunk dan kelompokkan path dengan hash identik
    raise NotImplementedError("Implementasikan find_exact_duplicates")


def create_rotating_backup(source_dir: Path, backup_dir: Path, archive_name: str, keep: int = 3) -> list[str]:
    """Membuat ZIP terkompresi dan mempertahankan tepat N backup terbaru."""
    # TODO: Gunakan zipfile.ZipFile(ZIP_DEFLATED) lalu unlink file .zip terlama
    raise NotImplementedError("Implementasikan create_rotating_backup")


if __name__ == "__main__":
    print("Starter D01 siap diuji aman menggunakan tempfile / pytest tmp_path.")
