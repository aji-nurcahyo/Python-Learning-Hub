# Tugas Terstruktur D01: Safe Workspace Organizer & Rotating Backup

## Instruksi Implementasi (`tugas.py`)
1. `organize_by_extension(base_dir: Path, dry_run: bool = True) -> list[tuple[str, str]]`: rencanakan pengelompokan ekstensi (`.csv`/`.xlsx` -> `spreadsheets`, `.pdf`/`.txt` -> `documents`, sisanya -> `others`) dan pindahkan hanya jika `dry_run=False`.
2. `find_exact_duplicates(root_dir: Path) -> list[list[str]]`: kembalikan daftar nama berkas ber-SHA-256 sama (dibaca dalam chunk 64 KB).
3. `create_rotating_backup(source_dir: Path, backup_dir: Path, archive_name: str, keep: int = 3) -> list[str]`: arsipkan `source_dir` ke file ZIP terkompresi lalu hapus arsip tertua jika jumlah `.zip` melebihi `keep`.

## Rubrik Penilaian (Total 100 Poin)
- Keamanan Dry-Run & Penggunaan pathlib (30%)
- Akurasi Deduplikasi SHA-256 (25%)
- Logika Rotasi Backup ZIP (25%)
- Unit Testing Terisolasi (Pytest) (20%)

