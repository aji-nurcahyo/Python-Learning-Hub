"""Chapter 29 Example 09: Python Package Distribution (Wheel vs SDist)
Python Learning Hub - Professional Python Engineering
"""


class PackageDistributionInspector:
    """Inspektor struktur artefak distribusi Python (Wheel .whl dan Source Distribution .tar.gz)."""

    @staticmethod
    def inspect_distribution_tag(wheel_filename: str) -> dict[str, str]:
        # Standar PEP 427: {distribution}-{version}(-{build tag})?-{python tag}-{abi tag}-{platform tag}.whl
        base_name = wheel_filename.removesuffix(".whl")
        parts = base_name.split("-")
        if len(parts) >= 5:
            return {
                "package": parts[0],
                "version": parts[1],
                "python_tag": parts[2],
                "abi_tag": parts[3],
                "platform": parts[4],
                "format": "Pure Python Wheel (Universal)",
            }
        return {"format": "Non-standard package naming"}


def main() -> None:
    print("Menganalisis Metadata Distribusi Paket Python Standar (Wheel):\n")
    sample_wheel = "telecom_monitor-1.0.0-py3-none-any.whl"
    info = PackageDistributionInspector.inspect_distribution_tag(sample_wheel)

    print(f"File Artefak  : {sample_wheel}")
    print(f" -> Paket     : {info['package']}")
    print(f" -> Versi     : {info['version']}")
    print(f" -> Tag Python: {info['python_tag']}")
    print(f" -> ABI Tag   : {info['abi_tag']} (Nir-ketergantungan C extensions)")
    print(f" -> Platform  : {info['platform']} (Cross-platform universal)")
    print(f" -> Tipe      : {info['format']}")


if __name__ == "__main__":
    main()

