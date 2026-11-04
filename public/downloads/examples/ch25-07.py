"""Chapter 25 Example 07: Static Checking vs Runtime Type Validation
Python Learning Hub - Professional Python Engineering
"""


def register_port(device_id: str, port_number: int) -> str:
    """Type hint mendokumentasikan ekspektasi tipe, tetapi tidak otomatis menolaknya saat runtime."""
    # Validasi runtime eksplisit tetap diperlukan untuk data dari sumber luar (file/network)
    if not isinstance(device_id, str):
        raise TypeError(f"device_id harus berupa string, bukan {type(device_id).__name__}")
    if not isinstance(port_number, int):
        raise TypeError(f"port_number harus berupa int, bukan {type(port_number).__name__}")

    return f"Port {device_id}:{port_number} berhasil diregistrasi"


def main() -> None:
    print(register_port("SWITCH-01", 8080))

    try:
        # Menyerahkan tipe yang salah saat runtime
        # Pada pemeriksaan statis (mypy), baris berikut akan ditandai error
        register_port("SWITCH-01", "8080")  # type: ignore[arg-type]
    except TypeError as err:
        print(f"Runtime validation berhasil menangkap: {err}")


if __name__ == "__main__":
    main()

