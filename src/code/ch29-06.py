"""Chapter 29 Example 06: pyproject.toml Configuration & Package Metadata
Python Learning Hub - Professional Python Engineering
"""

import tomllib  # Tersedia bawaan sejak Python 3.11


SAMPLE_PYPROJECT_TOML = """
[build-system]
requires = ["flit_core >=3.2,<4"]
build-backend = "flit_core.buildapi"

[project]
name = "telecom-monitor"
version = "1.0.0"
description = "Sistem Pemantauan Infrastruktur Jaringan Produksi"
readme = "README.md"
requires-python = ">=3.11"
authors = [
    { name = "Aji Pamungkas Tri Nurcahyo", email = "aji@itera.ac.id" }
]
dependencies = [
    "pydantic>=2.0.0",
    "httpx>=0.24.0",
]

[project.scripts]
telecom-cli = "telecom_monitor.cli:main"
"""


def parse_and_validate_package_metadata(toml_text: str) -> dict[str, str | list[str]]:
    data = tomllib.loads(toml_text)
    project = data.get("project", {})

    return {
        "package_name": project.get("name", ""),
        "version": project.get("version", ""),
        "python_requires": project.get("requires-python", ""),
        "dependencies": project.get("dependencies", []),
        "entry_points": list(project.get("scripts", {}).keys()),
    }


def main() -> None:
    print("Membaca dan Memvalidasi Konfigurasi Paket Standar pyproject.toml (PEP 621):\n")
    meta = parse_and_validate_package_metadata(SAMPLE_PYPROJECT_TOML)

    print(f" -> Nama Paket       : {meta['package_name']}")
    print(f" -> Versi Rilis      : {meta['version']}")
    print(f" -> Kompatibilitas   : Python {meta['python_requires']}")
    print(f" -> Dependensi Utama : {meta['dependencies']}")
    print(f" -> CLI Entry Point  : {meta['entry_points']}")


if __name__ == "__main__":
    main()

