"""Modul Validasi Masukan Pengguna (validators.py)

Menyediakan fungsi validasi untuk NIM, nama mahasiswa, dan nilai akademik.
Modul ini bersifat murni (tanpa interaksi I/O input/print) agar mudah diuji.
"""

from typing import Any


def validate_nim(nim: str, students: list[dict[str, Any]] | None = None) -> tuple[bool, str]:
    """Validasi format dan keunikan NIM mahasiswa.

    Args:
        nim: String nomor induk mahasiswa yang akan divalidasi.
        students: Daftar data mahasiswa yang telah terdaftar (opsional).

    Returns:
        tuple[bool, str]: Status validasi (True/False) dan pesan keterangan.
    """
    if not isinstance(nim, str):
        return False, "NIM harus berupa teks (string)."

    cleaned = nim.strip()
    if not cleaned:
        return False, "NIM tidak boleh kosong."

    if not cleaned.isdigit():
        return False, "NIM hanya boleh terdiri dari karakter digit angka (0-9)."

    if len(cleaned) < 5 or len(cleaned) > 15:
        return False, "Panjang NIM harus di antara 5 hingga 15 karakter digit."

    if students is not None:
        for student in students:
            if student.get("nim") == cleaned:
                return False, f"Mahasiswa dengan NIM '{cleaned}' sudah terdaftar."

    return True, "NIM valid."


def validate_name(name: str) -> tuple[bool, str]:
    """Validasi format nama lengkap mahasiswa.

    Args:
        name: String nama mahasiswa.

    Returns:
        tuple[bool, str]: Status validasi (True/False) dan pesan keterangan.
    """
    if not isinstance(name, str):
        return False, "Nama harus berupa teks (string)."

    cleaned = name.strip()
    if not cleaned:
        return False, "Nama tidak boleh kosong."

    if len(cleaned) < 2:
        return False, "Nama mahasiswa minimal terdiri dari 2 karakter."

    # Nama hanya boleh memuat huruf alfabet, spasi, titik (gelar/singkatan), dan tanda petik/hubung
    allowed_symbols = {" ", ".", "'", "-"}
    for char in cleaned:
        if not (char.isalpha() or char in allowed_symbols):
            return False, "Nama hanya boleh memuat huruf alfabet, spasi, titik, atau tanda hubung."

    return True, "Nama valid."


def validate_grade(grade_input: Any) -> tuple[bool, str, float | None]:
    """Validasi rentang nilai akademik mahasiswa (0.0 - 100.0).

    Args:
        grade_input: Nilai angka atau representasi string angka.

    Returns:
        tuple[bool, str, float | None]: Status validasi, pesan keterangan, dan nilai float jika valid.
    """
    if grade_input is None or (isinstance(grade_input, str) and not grade_input.strip()):
        return False, "Nilai tidak boleh kosong.", None

    try:
        val = float(grade_input)
    except (ValueError, TypeError):
        return False, "Nilai harus berupa representasi angka numerik yang valid.", None

    if val < 0.0 or val > 100.0:
        return False, f"Nilai {val:.2f} di luar jangkauan valid. Nilai harus berada dalam rentang 0.0 s.d. 100.0.", None

    return True, "Nilai valid.", round(val, 2)

