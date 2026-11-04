"""Contoh 21.3: Konfigurasi pyproject.toml Standar PEP 621
Python Learning Hub - Level 2: Intermediate Python
"""

pyproject_sample = """[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "telecom-toolkit"
version = "1.0.0"
authors = [{ name = "Aji Pamungkas Tri Nurcahyo" }]
dependencies = ["pydantic>=2.0"]

[project.optional-dependencies]
dev = ["pytest>=7.0", "ruff>=0.1.0"]"""

print("=== Format Standar: pyproject.toml ===")
print(pyproject_sample)
print("\nInstalasi editable: $ pip install -e .[dev]")
