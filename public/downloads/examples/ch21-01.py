"""Contoh 21.1: Konsep Struktur Package Python, __init__.py dan Namespace
Python Learning Hub - Level 2: Intermediate Python
"""

# Modul vs Package:
# Modul = Berkas tunggal .py
# Package = Direktori berisi modul dan berkas __init__.py yang mendefinisikan namespace

package_manifest = {
    "package_name": "telecom_core",
    "structure": [
        "telecom_core/__init__.py",
        "telecom_core/models.py",
        "telecom_core/calculators.py",
        "telecom_core/utils/formatters.py"
    ],
    "exposed_symbols": ["SignalCalculator", "BaseStation", "format_dbm"]
}

print(f"Struktur Package Standar PEP 420/517: '{package_manifest['package_name']}'")
for file_path in package_manifest["structure"]:
    print(f"  └── {file_path}")

print("\nSimbol yang diekspor melalui __all__ di __init__.py:")
for symbol in package_manifest["exposed_symbols"]:
    print(f"  * {symbol}")

# Memeriksa namespace modul aktif saat ini
print(f"\nNama namespace aktif (__name__): {__name__}")
print("Ketika dieksekusi langsung sebagai script, __name__ bernilai '__main__'.")
