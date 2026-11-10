# Tutorial 03 — Installing & Configuring VS Code
## Menginstal dan Mengonfigurasi Visual Studio Code untuk Pengembangan Python

> **Bagian:** Getting Started with Python  
> **Target Audiens:** Pengembang yang ingin menyiapkan editor kode modern dengan tooling Python terintegrasi  
> **Fokus Utama:** Instalasi ekstensi Python, pemilihan interpreter, terminal terintegrasi, eksekusi skrip, dan debugging

---

## 1. Tujuan Pembelajaran (Learning Objectives)

Setelah menyelesaikan tutorial ini, Anda diharapkan mampu:
1. Memasang **Visual Studio Code (VS Code)** resmi pada sistem operasi Anda.
2. Menginstal dan mengaktifkan **Python Extension** resmi buatan Microsoft.
3. Membuka folder kerja (*project folder*) dengan struktur direktori yang benar di VS Code.
4. Memilih dan mengganti **Python Interpreter** aktif menggunakan Command Palette.
5. Membuka dan menggunakan **Integrated Terminal** untuk menjalankan perintah secara efisien.
6. Menulis, menyimpan, dan mengeksekusi file kode Python (`.py`).
7. Memanfaatkan fitur **Debugging** dasar menggunakan breakpoint, inspeksi variabel, dan langkah eksekusi (*step over / step into*).
8. Mengatasi kendala umum deteksi interpreter dan lingkungan kerja di VS Code.

---

## 2. Prasyarat (Prerequisites)

- Telah menyelesaikan **Tutorial 02: Installing Python** (Python Interpreter sudah terinstal dan terverifikasi di terminal).
- Komputer dengan sistem operasi Windows, Linux, atau macOS.

---

## 3. Instalasi Visual Studio Code

Unduh VS Code secara resmi dari Microsoft:
- **Situs Resmi:** [https://code.visualstudio.com/](https://code.visualstudio.com/)
- Pilih installer yang sesuai:
  - **Windows:** User Installer (64-bit). Centang opsi *"Add to PATH"* dan *"Add 'Open with Code' action to Windows Explorer context menu"*.
  - **Linux:** Paket `.deb` (Ubuntu/Debian) atau `.rpm` (Fedora/RHEL), atau melalui Snap: `sudo snap install --classic code`.
  - **macOS:** File `.zip` -> seret aplikasi `Visual Studio Code.app` ke direktori `/Applications`.

---

## 4. Menginstal Ekstensi Python Resmi

VS Code secara bawaan adalah editor teks serbaguna. Agar memiliki fitur cerdas (*IntelliSense*, auto-completion, linting, dan debugging) untuk bahasa Python, kita harus memasang ekstensi resmi:

1. Buka VS Code.
2. Buka panel **Extensions** dengan menekan pintasan:
   - Windows/Linux: `Ctrl + Shift + X`
   - macOS: `Cmd + Shift + X`
3. Ketik kata kunci: `Python` pada kotak pencarian.
4. Pilih ekstensi **Python** yang diterbitkan secara resmi oleh **Microsoft** (ID: `ms-python.python`).
5. Klik tombol **Install**. Ekstensi pendukung seperti *Pylance* (analisis bahasa) akan ikut terpasang otomatis.

---

## 5. Membuka Folder Kerja Proyek (Crucial Concept: Open Folder)

> 💡 **Aturan Emas Pengembang:** Jangan pernah membuka file Python tunggal secara terisolasi tanpa folder proyek! Selalu buka direktori kerja menggunakan menu **File > Open Folder...**. Hal ini memungkinkan VS Code mengenali konfigurasi workspace, Virtual Environment (`.venv`), dan modul lokal.

1. Buat folder baru di komputer Anda, misalnya: `D:\ProyekPython` atau `~/proyek-python`.
2. Di VS Code, klik menu **File > Open Folder...** (atau tekan `Ctrl + K, Ctrl + O`).
3. Pilih folder yang telah Anda buat, lalu klik **Select Folder**.
4. Jika muncul kotak dialog *"Do you trust the authors of the files in this folder?"*, klik **Yes, I trust the authors**.

---

## 6. Memilih Python Interpreter Aktif (Select Interpreter)

VS Code perlu mengetahui executable Python mana yang harus digunakan untuk menganalisis dan mengeksekusi kode Anda:

1. Buka **Command Palette** dengan menekan:
   - Windows/Linux: `Ctrl + Shift + P`
   - macOS: `Cmd + Shift + P`
2. Ketik: `Python: Select Interpreter` lalu tekan `Enter`.
3. Daftar interpreter Python yang terdeteksi di komputer Anda akan muncul (misalnya: *Python 3.12.x 64-bit* atau Virtual Environment `('.venv': venv)`).
4. Klik salah satu interpreter rilis stabil yang ingin Anda gunakan.
5. Versi Python yang dipilih kini akan terlihat di pojok kanan bawah bilah status (*Status Bar*) VS Code.

---

## 7. Membuat dan Menjalankan Skrip Python Pertama

1. Di panel kiri **Explorer** (`Ctrl + Shift + E`), klik ikon **New File** (atau klik kanan -> *New File*).
2. Beri nama file: `app.py`.
3. Tulis kode sederhana berikut:
   ```python
   def sapa(nama: str) -> str:
       return f"Halo, {nama}! Selamat datang di Python Learning Hub."

   pesan = sapa("Programmer")
   print(pesan)
   ```
4. Simpan berkas dengan menekan `Ctrl + S` (atau `Cmd + S`).
5. **Cara Menjalankan Skrip:**
   - **Metode 1 (GUI):** Klik tombol segitiga hijau **Run Python File** di pojok kanan atas jendela editor.
   - **Metode 2 (Integrated Terminal):** Tekan `Ctrl + \`` (backtick) untuk membuka terminal terintegrasi, lalu ketik perintah:
     - Windows: `py app.py` atau `python app.py`
     - Linux/macOS: `python3 app.py`

**Keluaran Terminal yang Diharapkan:**
```text
Halo, Programmer! Selamat datang di Python Learning Hub.
```

---

## 8. Menggunakan Fitur Debugging & Breakpoint

Debugging memungkinkan Anda menghentikan eksekusi program di baris tertentu untuk memeriksa nilai variabel dalam memori langkah demi langkah:

1. **Memasang Breakpoint:** Arahkan kursor mouse ke sebelah kiri nomor baris pada baris `pesan = sapa("Programmer")`. Titik merah redup akan muncul. Klik sekali untuk mengaktifkan **Breakpoint** (titik merah menyala, atau tekan tombol `F9`).
2. **Memulai Debug:** Tekan tombol `F5` pada keyboard (atau buka menu **Run > Start Debugging**).
3. Jika muncul pilihan konfigurasi, pilih **Python File (Debug the currently active Python file)**.
4. Program akan berjalan dan seketika berhenti tepat di baris yang memiliki breakpoint sebelum baris tersebut dieksekusi.
5. **Panel Variabel:** Di panel sisi kiri, perhatikan bagian **Variables > Locals**. Anda dapat melihat seluruh variabel yang aktif di memori.
6. **Bilah Navigasi Debug (Debug Toolbar):**
   - **Continue (`F5`):** Melanjutkan jalannya program hingga breakpoint berikutnya.
   - **Step Over (`F10`):** Menjalankan baris saat ini dan maju ke baris berikutnya tanpa masuk ke dalam isi fungsi.
   - **Step Into (`F11`):** Masuk ke dalam definisi fungsi untuk memeriksa baris di dalamnya secara mendalam.
   - **Step Out (`Shift + F11`):** Menyelesaikan eksekusi fungsi saat ini dan kembali ke pemanggil.
   - **Stop (`Shift + F5`):** Menghentikan sesi debugging.

---

## 9. Kesalahan Umum & Solusi Kendala (Troubleshooting)

| Masalah | Penyebab | Solusi |
| :--- | :--- | :--- |
| **"No Python interpreter is selected"** di bilah bawah | VS Code belum menemukan lokasi instalasi Python secara otomatis. | Buka Command Palette (`Ctrl+Shift+P`), ketik `Python: Select Interpreter`, lalu pilih rilis Python yang terdaftar atau klik *Enter interpreter path* dan arahkan ke lokasi executable `python.exe` / `python3`. |
| **Garis merah bergelombang di bawah kata kunci valid** | Language server (Pylance) belum selesai mengindeks workspace. | Tunggu beberapa detik hingga proses indexing selesai, atau reload jendela VS Code dengan `Ctrl+Shift+P` -> `Developer: Reload Window`. |
| **Terminal terintegrasi membuka PowerShell versi lama yang terblokir** | Kebijakan eksekusi skrip PowerShell bawaan Windows. | Gunakan Terminal Command Prompt di VS Code atau konfigurasikan bypass execution policy untuk sesi saat ini (dijelaskan di Tutorial 05). |

---

## 10. Referensi Resmi

- Visual Studio Code Official Docs: [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
- Visual Studio Code Official Docs: [Python Debugging Tutorial](https://code.visualstudio.com/docs/python/debugging)
- Visual Studio Code Official Docs: [Environments in VS Code](https://code.visualstudio.com/docs/python/environments)

