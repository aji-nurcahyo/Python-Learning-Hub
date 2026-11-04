"""Contoh 21.2: Pengenalan Virtual Environment & Perbedaan Antar Platform
Python Learning Hub - Level 2: Intermediate Python
"""

# Konsep virtual environment: Mengisolasi dependensi per proyek agar tidak konflik

panduan_venv = {
    "Windows (PowerShell)": ".venv\\Scripts\\Activate.ps1",
    "Windows (CMD)": ".venv\\Scripts\\activate.bat",
    "Linux / macOS (Bash/Zsh)": "source .venv/bin/activate"
}

print("=== Standar Tata Kelola Virtual Environment (.venv) ===")
print("Langkah 1: Membuat venv   -> python -m venv .venv")
print("Langkah 2: Perintah Aktivasi per Sistem Operasi:")
for os_name, cmd in panduan_venv.items():
    print(f"  * {os_name:<25}: {cmd}")

print("Langkah 3: Instalasi dependensi -> pip install -r requirements.txt")
print("Langkah 4: Deaktivasi           -> deactivate")
print("Kaidah Kritis: Jangan menginstal dependensi proyek ke sistem global!")
