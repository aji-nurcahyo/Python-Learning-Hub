export interface PlatformCommands {
  windows: string;
  linux: string;
  macos: string;
}

export interface TutorialSection {
  heading: string;
  explanation: string;
  commands?: PlatformCommands;
  codeSnippet?: {
    code: string;
    language: string;
    filename?: string;
  };
  expectedOutput?: string;
  callout?: {
    type: 'info' | 'warning' | 'tip';
    title: string;
    text: string;
  };
}

export interface GettingStartedTutorial {
  id: string;
  number: string;
  title: string;
  subtitle: string;
  estimatedMinutes: number;
  objectives: string[];
  prerequisites: string[];
  sections: TutorialSection[];
  verificationChecklist: string[];
  commonMistakes: {
    issue: string;
    cause: string;
    solution: string;
  }[];
  officialReferences: {
    title: string;
    url: string;
  }[];
}

export const GETTING_STARTED_TUTORIALS: GettingStartedTutorial[] = [
  {
    id: 'development-tools',
    number: '01',
    title: 'Understanding Python Development Tools',
    subtitle: 'Memahami Perangkat Kerja dan Ekosistem Pemrograman Python',
    estimatedMinutes: 12,
    objectives: [
      'Membedakan peran Python Interpreter (runtime) dengan Code Editor / IDE (seperti VS Code)',
      'Memahami mengapa IDE tidak sama dengan Python Interpreter',
      'Memilih antara alur kerja skrip (.py) dan dokumen interaktif (.ipynb)',
      'Mengenal peran ekstensi editor dalam mendukung produktivitas pemrograman',
    ],
    prerequisites: [
      'Komputer dengan sistem operasi Windows 10/11, Linux, atau macOS',
      'Koneksi internet untuk mengunduh perangkat lunak pendukung',
    ],
    sections: [
      {
        heading: 'Peta Ekosistem Tooling Python',
        explanation:
          'Banyak pemula mengira bahwa menginstal editor teks seperti VS Code otomatis membuat program Python dapat berjalan. Faktanya, arsitektur pengembangan Python terdiri atas komponen-komponen terpisah dengan tanggung jawab spesifik:\n\n' +
          '1. **Python Interpreter (CPython):** Mesin eksekusi inti yang membaca kode .py, mengompilasinya menjadi bytecode, dan menjalankannya di atas Python Virtual Machine (PVM).\n' +
          '2. **Code Editor vs IDE:** Code Editor (seperti VS Code) adalah penyunting teks ringan yang membutuhkan interpreter eksternal. IDE berskala penuh (seperti PyCharm) menggabungkan editor, debugger, profiler, dan toolchain dalam satu aplikasi terintegrasi.\n' +
          '3. **Terminal / CLI:** Antarmuka baris perintah tempat pengembang memanggil Python Interpreter, mengelola paket dependensi, dan mengeksekusi skrip.\n' +
          '4. **Jupyter Notebook & JupyterLab:** Lingkungan komputasi berbasis web untuk eksplorasi data bertahap per sel (cell-by-cell).',
        callout: {
          type: 'warning',
          title: 'Miskonsepsi Penting',
          text: 'Menginstal VS Code saja BELUM menginstal Python di komputer Anda. Anda wajib menginstal CPython resmi dari python.org agar VS Code memiliki interpreter untuk mengeksekusi kode.',
        },
      },
      {
        heading: 'Perbandingan Workflow: Script (.py) vs Notebook (.ipynb)',
        explanation:
          'Pilihlah format berkas dan paradigma kerja yang sesuai dengan karakteristik pekerjaan Anda:\n\n' +
          '- **Skrip Python Linear (.py):** Berformat teks polos UTF-8, dieksekusi dari baris pertama hingga selesai, memori dibersihkan saat selesai, sangat ramah Git version control, dan menjadi standar untuk aplikasi produksi, modul, CLI, serta API backend.\n' +
          '- **Jupyter Notebook (.ipynb):** Berformat dokumen JSON terstruktur, dieksekusi sel per sel (state tersimpan di RAM kernel), menampilkan grafik inline secara visual, dan menjadi standar untuk eksplorasi data, machine learning, dan laporan riset interaktif.',
      },
    ],
    verificationChecklist: [
      'Memahami bahwa Python Interpreter adalah mesin eksekusi utama',
      'Mengetahui perbedaan mendasar antara skrip .py dan notebook .ipynb',
      'Mengetahui kapan harus menggunakan VS Code lokal vs Google Colab di cloud',
    ],
    commonMistakes: [
      {
        issue: 'Membuka berkas .py menggunakan Microsoft Word',
        cause: 'Word menyisipkan format teks biner khusus yang merusak sintaksis teks polos Python.',
        solution: 'Selalu gunakan Code Editor khusus seperti Visual Studio Code, Sublime Text, atau Notepad++.',
      },
      {
        issue: 'Mengira tombol "Run" di IDE menggantikan terminal',
        cause: 'Kurangnya pemahaman tentang alur eksekusi baris perintah sistem.',
        solution: 'Pahami perintah terminal yang dipanggil oleh tombol GUI (seperti `python app.py`).',
      },
    ],
    officialReferences: [
      { title: 'Python Executive Summary (python.org)', url: 'https://www.python.org/doc/essays/blurb/' },
      { title: 'Python in Visual Studio Code Overview', url: 'https://code.visualstudio.com/docs/languages/python' },
    ],
  },
  {
    id: 'installing-python',
    number: '02',
    title: 'Installing Python',
    subtitle: 'Panduan Instalasi Python Interpreter di Windows, Linux, dan macOS',
    estimatedMinutes: 15,
    objectives: [
      'Mengunduh dan menginstal rilis stabil resmi CPython dari python.org',
      'Memahami dan mengaktifkan opsi "Add python.exe to PATH" di Windows',
      'Memasang Python 3, pip, dan modul venv di Linux (Ubuntu/Debian)',
      'Menginstal Python resmi di macOS menggunakan installer .pkg atau Homebrew',
      'Memverifikasi keberhasilan instalasi melalui terminal menggunakan perintah py atau python3',
    ],
    prerequisites: [
      'Akses administrator/root pada komputer Anda',
      'Koneksi internet aktif untuk mengunduh installer resmi (~35 MB)',
    ],
    sections: [
      {
        heading: 'Sumber Unduhan Resmi & Rilis Stabil',
        explanation:
          'Selalu unduh rilis stabil resmi dari Python Software Foundation di [python.org/downloads/](https://www.python.org/downloads/). ' +
          'Pilihlah versi stabil (seperti cabang Python 3.11 atau 3.12) dan hindari versi pre-release (alpha/beta) untuk pembelajaran umum agar paket data science pihak ketiga dapat berjalan dengan lancar.',
      },
      {
        heading: 'Langkah Instalasi Berdasarkan Sistem Operasi',
        explanation:
          'Ikuti instruksi khusus platform Anda. Di Windows, langkah paling krusial adalah memastikan kotak pilihan **"Add python.exe to PATH"** dicentang di awal instalasi.',
        commands: {
          windows: '# Di Windows, jalankan installer resmi .exe dan centang:\n# [x] Add python.exe to PATH\n# [x] Use admin privileges when installing py.exe',
          linux: '# Pada Ubuntu / Debian:\nsudo apt update\nsudo apt install -y python3 python3-pip python3-venv python3-dev',
          macos: '# Menggunakan Homebrew:\nbrew install python\n# Atau unduh .pkg dari python.org lalu jalankan:\n/Applications/Python\\ 3.12/Install\\ Certificates.command',
        },
        callout: {
          type: 'warning',
          title: 'Perhatian Khusus Windows',
          text: 'Jika lupa mencentang "Add python.exe to PATH", terminal akan menampilkan pesan "python is not recognized". Buka kembali installer dan pilih Modify untuk mengaktifkannya.',
        },
      },
      {
        heading: 'Perintah Verifikasi Interpreter di Terminal',
        explanation:
          'Buka jendela terminal baru (PowerShell di Windows, Terminal di macOS/Linux) dan jalankan perintah verifikasi berikut:',
        commands: {
          windows: 'py --version\npy -m pip --version',
          linux: 'python3 --version\npython3 -m pip --version',
          macos: 'python3 --version\npython3 -m pip --version',
        },
        expectedOutput: 'Python 3.12.x\npip 24.x.x from ... (python 3.12)',
      },
    ],
    verificationChecklist: [
      'Perintah `py --version` (Windows) atau `python3 --version` (Linux/macOS) berhasil mencetak versi Python 3.10+',
      'Perintah pip mencetak versi pip tanpa error',
      'Terminal dapat dipanggil dari direktori mana saja',
    ],
    commonMistakes: [
      {
        issue: 'PowerShell membuka Microsoft Store saat mengetik "python"',
        cause: 'App Execution Aliases bawaan Windows mencegat perintah sebelum interpreter asli.',
        solution: 'Buka Windows Settings -> Apps -> App execution aliases -> Matikan toggle untuk "App Installer (python.exe)".',
      },
      {
        issue: 'pip install error "CERTIFICATE_VERIFY_FAILED" di macOS',
        cause: 'Sertifikat root SSL bawaan macOS belum dipasang ke folder Python.',
        solution: 'Jalankan skrip "/Applications/Python 3.x/Install Certificates.command" melalui terminal atau Finder.',
      },
    ],
    officialReferences: [
      { title: 'Python Software Foundation Downloads', url: 'https://www.python.org/downloads/' },
      { title: 'Using Python on Windows', url: 'https://docs.python.org/3/using/windows.html' },
      { title: 'Using Python on Unix platforms', url: 'https://docs.python.org/3/using/unix.html' },
      { title: 'Using Python on a Mac', url: 'https://docs.python.org/3/using/mac.html' },
    ],
  },
  {
    id: 'vscode-setup',
    number: '03',
    title: 'Installing & Configuring VS Code',
    subtitle: 'Menginstal dan Mengonfigurasi Visual Studio Code untuk Pengembangan Python',
    estimatedMinutes: 15,
    objectives: [
      'Menginstal Visual Studio Code resmi pada sistem operasi Anda',
      'Memasang ekstensi resmi Python by Microsoft',
      'Membuka folder kerja proyek (Open Folder) secara terstruktur',
      'Memilih dan mengonfigurasi Python Interpreter aktif',
      'Menjalankan skrip Python dari Integrated Terminal',
      'Melakukan debugging dasar dengan breakpoint dan inspeksi variabel',
    ],
    prerequisites: [
      'Python Interpreter telah terpasang (Tutorial 02)',
      'Komputer dengan sistem operasi Windows, Linux, atau macOS',
    ],
    sections: [
      {
        heading: 'Instalasi VS Code & Ekstensi Python',
        explanation:
          'Unduh VS Code dari [code.visualstudio.com](https://code.visualstudio.com/). ' +
          'Setelah instalasi selesai, buka panel Extensions (`Ctrl+Shift+X` / `Cmd+Shift+X`), cari kata kunci **Python**, dan pasang ekstensi resmi buatan **Microsoft** (`ms-python.python`).',
      },
      {
        heading: 'Konsep Krusial: Open Folder Workspace',
        explanation:
          'Selalu buka direktori kerja proyek Anda menggunakan menu **File > Open Folder...** (`Ctrl+K, Ctrl+O`). ' +
          'Membuka folder utuh memungkinkan VS Code mendeteksi konfigurasi workspace, Virtual Environment (`.venv`), dan modul lokal antarfile secara otomatis.',
        callout: {
          type: 'tip',
          title: 'Praktik Terbaik',
          text: 'Jangan membuka file .py secara mandiri tanpa folder induknya. Selalu buat folder proyek (misalnya "ProyekPython") dan buka foldernya di VS Code.',
        },
      },
      {
        heading: 'Memilih Python Interpreter di VS Code',
        explanation:
          'Tekan `Ctrl+Shift+P` (atau `Cmd+Shift+P` di macOS), ketik `Python: Select Interpreter`, dan pilih versi Python atau Virtual Environment yang terpasang di komputer Anda. Status interpreter akan terlihat di pojok kanan bawah bilah status.',
      },
      {
        heading: 'Menulis, Menjalankan, dan Debugging Kode',
        explanation:
          'Buat berkas baru bernama `app.py`, tulis kode pengujian, dan jalankan melalui Integrated Terminal (`Ctrl+` `) atau tombol Run di pojok kanan atas editor.',
        codeSnippet: {
          filename: 'app.py',
          language: 'python',
          code: 'def sapa(nama: str) -> str:\n    return f"Halo, {nama}! Selamat datang di Python Learning Hub."\n\npesan = sapa("Programmer")\nprint(pesan)',
        },
        expectedOutput: 'Halo, Programmer! Selamat datang di Python Learning Hub.',
      },
    ],
    verificationChecklist: [
      'Ekstensi Python by Microsoft aktif di VS Code',
      'Python Interpreter terdeteksi di status bar pojok kanan bawah',
      'Integrated Terminal dapat dibuka dengan `Ctrl + ` `',
      'Berkas `app.py` berhasil dieksekusi dan menghasilkan teks sapaan',
    ],
    commonMistakes: [
      {
        issue: 'Pesan error "No Python interpreter is selected"',
        cause: 'VS Code belum mengasosiasikan workspace dengan binary python lokal.',
        solution: 'Tekan Ctrl+Shift+P, ketik "Python: Select Interpreter", dan pilih interpreter resmi yang terinstal.',
      },
      {
        issue: 'Garis merah bergelombang di bawah kata kunci Python valid',
        cause: 'Language server (Pylance) masih dalam proses indexing pertama kali.',
        solution: 'Tunggu beberapa detik, atau reload jendela VS Code via Command Palette: "Developer: Reload Window".',
      },
    ],
    officialReferences: [
      { title: 'Getting Started with Python in VS Code', url: 'https://code.visualstudio.com/docs/python/python-tutorial' },
      { title: 'Python Debugging in VS Code', url: 'https://code.visualstudio.com/docs/python/debugging' },
    ],
  },
  {
    id: 'jupyter-setup',
    number: '04',
    title: 'Jupyter Notebook & JupyterLab',
    subtitle: 'Bekerja dengan Dokumen Komputasi Interaktif Jupyter',
    estimatedMinutes: 15,
    objectives: [
      'Memahami struktur internal dokumen notebook (.ipynb)',
      'Menginstal JupyterLab dan Jupyter Notebook menggunakan pip',
      'Menjalankan server lokal JupyterLab dari terminal',
      'Membuat dan mengeksekusi sel kode (code cells) dan teks Markdown (markdown cells)',
      'Memilih dan merestart Jupyter Kernel saat proses komputasi bermasalah',
    ],
    prerequisites: [
      'Python Interpreter dan pip sudah terverifikasi (Tutorial 02)',
    ],
    sections: [
      {
        heading: 'Instalasi JupyterLab & Notebook via Pip',
        explanation:
          'JupyterLab adalah antarmuka komputasi interaktif generasi terbaru dari Project Jupyter. Pasang melalui terminal dengan perintah berikut:',
        commands: {
          windows: 'py -m pip install --upgrade pip\npy -m pip install jupyterlab notebook',
          linux: 'python3 -m pip install --upgrade pip\npython3 -m pip install jupyterlab notebook',
          macos: 'python3 -m pip install --upgrade pip\npython3 -m pip install jupyterlab notebook',
        },
      },
      {
        heading: 'Menjalankan Server JupyterLab',
        explanation:
          'Buka terminal di folder kerja proyek Anda dan ketik perintah berikut untuk membuka dashboard browser:',
        commands: {
          windows: 'jupyter lab',
          linux: 'jupyter lab',
          macos: 'jupyter lab',
        },
        callout: {
          type: 'info',
          title: 'Terminal Backend',
          text: 'Jangan menutup jendela terminal tempat perintah `jupyter lab` berjalan. Terminal tersebut bertindak sebagai backend server komputasi. Untuk berhenti, tekan Ctrl+C dua kali di terminal.',
        },
      },
      {
        heading: 'Eksekusi Sel Kode & Markdown',
        explanation:
          'Di dalam notebook, tekan `Shift + Enter` untuk mengeksekusi sel aktif dan melompat ke sel berikutnya. ' +
          'Ubah tipe sel menjadi Markdown (tekan tombol `Esc` lalu `M`) untuk menulis dokumentasi berformat rapi.',
        codeSnippet: {
          filename: 'analisis.ipynb',
          language: 'python',
          code: 'daya_mw = 100\nkehilangan_db = 3.0\ndaya_terima = daya_mw * (10 ** (-kehilangan_db / 10))\nprint(f"Daya Diterima: {daya_terima:.2f} mW")',
        },
        expectedOutput: 'Daya Diterima: 50.12 mW',
      },
    ],
    verificationChecklist: [
      'JupyterLab terbuka di peramban web pada alamat `http://localhost:8888/lab`',
      'Dapat membuat dokumen notebook baru berekstensi `.ipynb`',
      'Sel kode berhasil dijalankan dengan tombol Shift + Enter',
      'Kernel indikator di pojok kanan atas menunjukkan status Idle (lingkaran putih)',
    ],
    commonMistakes: [
      {
        issue: 'Pesan error "Port 8888 is already in use"',
        cause: 'Ada proses server Jupyter lama yang belum dimatikan di latar belakang.',
        solution: 'Jupyter akan otomatis mencoba port berikutnya (8889), atau tentukan port manual: `jupyter lab --port 8900`.',
      },
      {
        issue: 'Variabel tidak dikenali (NameError) padahal sel sudah ditulis',
        cause: 'Sel di bawah dijalankan sebelum sel pendefinisian di atas dieksekusi.',
        solution: 'Gunakan menu Kernel > Restart Kernel and Run All Cells untuk memastikan urutan linear dari atas ke bawah.',
      },
    ],
    officialReferences: [
      { title: 'Project Jupyter Official Installation Guide', url: 'https://jupyter.org/install' },
      { title: 'JupyterLab User Guide', url: 'https://jupyterlab.readthedocs.io/' },
    ],
  },
  {
    id: 'virtual-environment',
    number: '05',
    title: 'Virtual Environment & Package Management',
    subtitle: 'Isolasi Dependensi Proyek dengan Virtual Environment dan Pip',
    estimatedMinutes: 18,
    objectives: [
      'Memahami pentingnya isolasi dependensi untuk mencegah konflik versi pustaka',
      'Membuat direktori Virtual Environment lokal (.venv) menggunakan modul standar venv',
      'Mengaktifkan dan menonaktifkan Virtual Environment di Windows, Linux, dan macOS',
      'Mengatasi pesan error PowerShell Execution Policy secara aman',
      'Memasang paket dengan pip dan mengunci dependensi via requirements.txt',
    ],
    prerequisites: [
      'Python Interpreter dan pip terpasang (Tutorial 02)',
      'Folder proyek kerja telah dibuka di terminal atau VS Code (Tutorial 03)',
    ],
    sections: [
      {
        heading: 'Mengapa Virtual Environment Diperlukan?',
        explanation:
          'Setiap proyek memiliki kebutuhan versi pustaka yang berbeda. Jika Anda menginstal paket langsung ke Python global sistem, versi paket antarproyek akan saling menimpa (*dependency conflict*). ' +
          'Virtual Environment membuat salinan lingkungan kerja Python mandiri di dalam folder `.venv` proyek Anda sehingga tidak mencemari sistem operasi.',
      },
      {
        heading: 'Membuat Virtual Environment (.venv)',
        explanation:
          'Gunakan modul bawaan `venv` di terminal pada folder proyek Anda:',
        commands: {
          windows: 'py -m venv .venv',
          linux: 'python3 -m venv .venv',
          macos: 'python3 -m venv .venv',
        },
      },
      {
        heading: 'Mengaktifkan Virtual Environment',
        explanation:
          'Aktifkan environment sebelum menginstal paket. Tandanya prompt terminal akan memuat awalan `(.venv)`.',
        commands: {
          windows: '# Di Windows PowerShell:\nSet-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass\n.\\.venv\\Scripts\\Activate.ps1\n# Atau di CMD: .\\.venv\\Scripts\\activate.bat',
          linux: 'source .venv/bin/activate',
          macos: 'source .venv/bin/activate',
        },
        callout: {
          type: 'warning',
          title: 'PowerShell Execution Policy',
          text: 'Jangan gunakan `Set-ExecutionPolicy Unrestricted` secara permanen. Parameter `-Scope Process -ExecutionPolicy Bypass` adalah metode paling aman karena hanya berlaku untuk sesi terminal saat ini.',
        },
      },
      {
        heading: 'Mengelola Paket dengan pip dan requirements.txt',
        explanation:
          'Saat `(.venv)` aktif, instal paket yang diperlukan dan bekukan versinya ke berkas `requirements.txt`:',
        commands: {
          windows: 'pip install requests numpy\npip freeze > requirements.txt\npip list',
          linux: 'pip install requests numpy\npip freeze > requirements.txt\npip list',
          macos: 'pip install requests numpy\npip freeze > requirements.txt\npip list',
        },
      },
    ],
    verificationChecklist: [
      'Folder `.venv` berhasil terbuat di dalam direktori proyek',
      'Prompt terminal menampilkan teks `(.venv)` di sisi kiri',
      'Perintah `pip list` hanya menampilkan paket yang baru diinstal di `.venv`',
      'Perintah `deactivate` berhasil mengembalikan terminal ke status normal',
    ],
    commonMistakes: [
      {
        issue: 'Mengunggah folder .venv ke repositori Git',
        cause: 'Lupa menambahkan .venv ke dalam berkas .gitignore.',
        solution: 'Tambahkan baris `.venv/` ke file `.gitignore` agar file biner lokal tidak terunggah ke Git.',
      },
      {
        issue: 'Menginstal paket saat .venv belum aktif',
        cause: 'Paket terpasang ke lingkungan global dan tidak tercatat di requirements.txt proyek.',
        solution: 'Pastikan tanda `(.venv)` selalu terlihat di terminal sebelum menjalankan `pip install`.',
      },
    ],
    officialReferences: [
      { title: 'Python Documentation — venv module', url: 'https://docs.python.org/3/library/venv.html' },
      { title: 'Python Packaging Authority (PyPA) Tutorial', url: 'https://packaging.python.org/en/latest/tutorials/installing-packages/' },
    ],
  },
  {
    id: 'google-colab',
    number: '06',
    title: 'Google Colab',
    subtitle: 'Bekerja dengan Cloud Jupyter Notebook di Google Colab',
    estimatedMinutes: 12,
    objectives: [
      'Memahami kelebihan dan batasan Google Colaboratory',
      'Membuat notebook dan mengeksekusi kode Python di cloud',
      'Menginstal paket tambahan menggunakan perintah `!pip`',
      'Menghubungkan penyimpanan permanen Google Drive (`drive.mount`)',
      'Memahami realitas keterbatasan alokasi GPU gratis dan masa aktif runtime',
    ],
    prerequisites: [
      'Akun Google aktif dan peramban web modern (Google Chrome, Firefox, Safari, Edge)',
    ],
    sections: [
      {
        heading: 'Mengenal Google Colaboratory',
        explanation:
          'Google Colab adalah layanan cloud hosting Jupyter Notebook gratis yang berjalan di atas server Google Cloud Platform. ' +
          'Sangat cocok bagi pemula yang tidak memiliki akses komputer berspesifikasi tinggi atau pengguna tablet/Chromebook karena tidak membutuhkan instalasi lokal apa pun.',
      },
      {
        heading: 'Instalasi Paket & Integrasi Google Drive',
        explanation:
          'Gunakan tanda seru `!` untuk menjalankan perintah shell Linux di Colab, dan gunakan modul utilitas bawaan untuk mengakses file Google Drive:',
        codeSnippet: {
          filename: 'colab_setup.py',
          language: 'python',
          code: '# Menginstal paket pihak ketiga\n!pip install rich -q\n\n# Menghubungkan Google Drive untuk penyimpanan permanen\nfrom google.colab import drive\ndrive.mount("/content/drive")\nprint("Google Drive terhubung ke /content/drive/MyDrive")',
        },
      },
      {
        heading: 'Realitas Batasan Teknis (Runtime Limitations)',
        explanation:
          'Pahami batasan utama akun Colab gratis agar tidak kehilangan data pekerjaan:\n\n' +
          '1. **Ephemeral Disk:** Berkas yang disimpan di folder `/content/` akan dihapus bersih saat sesi berakhir. Selalu salin file penting ke Google Drive atau unduh ke komputer Anda.\n' +
          '2. **Idle Timeout:** Koneksi akan terputus jika notebook dibiarkan tanpa eksekusi selama ~60-90 menit.\n' +
          '3. **Durasi Maksimal Sesi:** Maksimal 12 jam per sesi eksekusi berkelanjutan.\n' +
          '4. **Akses GPU Terbatas:** Akses GPU gratis (NVIDIA T4) dialokasikan berdasarkan ketersediaan dinamis (*best-effort*), bukan kuota tak terbatas.',
        callout: {
          type: 'warning',
          title: 'Etika Pemakaian GPU',
          text: 'Gunakan runtime CPU standar untuk materi dasar logika. Mengaktifkan GPU saat tidak diperlukan akan memboroskan kuota dinamis harian Anda.',
        },
      },
    ],
    verificationChecklist: [
      'Dapat membuka dan membuat notebook baru di https://colab.research.google.com',
      'Sel kode berhasil dijalankan dan menampilkan hasil di browser',
      'Dapat mengunduh file notebook (.ipynb) ke komputer lokal',
    ],
    commonMistakes: [
      {
        issue: 'File dataset hilang setelah notebook ditutup beberapa jam',
        cause: 'File diunggah ke folder sementara /content/ yang otomatis di-reset oleh sistem Colab.',
        solution: 'Simpan file di Google Drive dan hubungkan menggunakan `drive.mount("/content/drive")`.',
      },
    ],
    officialReferences: [
      { title: 'Google Colab Official FAQ', url: 'https://research.google.com/colaboratory/faq.html' },
      { title: 'Overview of Colaboratory Features', url: 'https://colab.research.google.com/notebooks/basic_features_overview.ipynb' },
    ],
  },
  {
    id: 'running-projects',
    number: '07',
    title: 'Running Python Projects',
    subtitle: 'Menjalankan Proyek Python Modular & Navigasi Workspace',
    estimatedMinutes: 15,
    objectives: [
      'Membuat direktori kerja proyek dan melakukan navigasi terminal (cd, ls, pwd)',
      'Menulis dan mengeksekusi skrip Python (.py) dari baris perintah',
      'Memahami fungsi idiom `if __name__ == "__main__":`',
      'Mengimpor fungsi dari modul file lokal secara terpisah',
      'Membaca laporan kesalahan (traceback error) dari bawah ke atas',
    ],
    prerequisites: [
      'Python Interpreter terpasang (Tutorial 02)',
      'Pemahaman dasar navigasi terminal (Tutorial 01)',
    ],
    sections: [
      {
        heading: 'Navigasi Direktori Kerja Proyek',
        explanation:
          'Setiap proyek mandiri dikelola di foldernya masing-masing. Buka terminal dan lakukan navigasi:',
        commands: {
          windows: 'mkdir ProyekPertama\ncd ProyekPertama\nGet-Location\ndir',
          linux: 'mkdir -p ~/ProyekPertama\ncd ~/ProyekPertama\npwd\nls -la',
          macos: 'mkdir -p ~/ProyekPertama\ncd ~/ProyekPertama\npwd\nls -la',
        },
      },
      {
        heading: 'Skrip Pengujian Kesiapan Lingkungan (main.py)',
        explanation:
          'Buat berkas `main.py` di dalam folder kerja Anda dengan kode standar berikut:',
        codeSnippet: {
          filename: 'main.py',
          language: 'python',
          code: 'def main() -> None:\n    print("Python Learning Hub")\n    print("Development Environment Ready!")\n\nif __name__ == "__main__":\n    main()',
        },
        commands: {
          windows: 'py main.py',
          linux: 'python3 main.py',
          macos: 'python3 main.py',
        },
        expectedOutput: 'Python Learning Hub\nDevelopment Environment Ready!',
      },
      {
        heading: 'Memahami Cara Membaca Traceback Error',
        explanation:
          'Saat kode mengalami error, Python mencetak pesan Traceback. Cara membacanya yang benar adalah **dari baris paling bawah ke atas**:\n\n' +
          '1. **Baris Terbawah:** Menunjukkan tipe exception (misal `ZeroDivisionError` atau `ValueError`) dan pesan kesalahannya.\n' +
          '2. **Baris di Atasnya:** Menunjukkan nama berkas dan nomor baris persis tempat error tersebut dipicu.',
      },
    ],
    verificationChecklist: [
      'Berkas `main.py` dibuat di dalam folder proyek',
      'Skrip dieksekusi dari terminal menggunakan `py main.py` atau `python3 main.py`',
      'Keluaran terminal persis mencetak teks "Development Environment Ready!"',
    ],
    commonMistakes: [
      {
        issue: 'Error "[Errno 2] No such file or directory: main.py"',
        cause: 'Terminal sedang berada di direktori yang berbeda dari lokasi berkas main.py disimpan.',
        solution: 'Gunakan perintah `pwd` (atau `Get-Location`) untuk memeriksa folder saat ini, lalu pindah dengan `cd nama_folder`.',
      },
    ],
    officialReferences: [
      { title: 'Python Tutorial — Modules and Packages', url: 'https://docs.python.org/3/tutorial/modules.html' },
      { title: 'Errors and Exceptions in Python', url: 'https://docs.python.org/3/tutorial/errors.html' },
    ],
  },
  {
    id: 'troubleshooting',
    number: '08',
    title: 'Troubleshooting & Environment Verification',
    subtitle: 'Diagnostik Masalah dan Verifikasi Aman Lingkungan Kerja Python',
    estimatedMinutes: 20,
    objectives: [
      'Mendiagnosis dan memperbaiki masalah perintah python tidak dikenali di terminal',
      'Mengatasi error PowerShell Execution Policy tanpa merusak keamanan sistem',
      'Menyelesaikan ModuleNotFoundError akibat salah interpreter atau venv tidak aktif',
      'Mengatasi kendala port conflict dan kernel unresponsive di JupyterLab',
      'Menjalankan alur verifikasi menyeluruh 8 langkah sebelum memulai kurikulum',
    ],
    prerequisites: [
      'Telah mempraktikkan Tutorial 01 sampai 07',
    ],
    sections: [
      {
        heading: 'Katalog Masalah & Solusi Cepat Aman',
        explanation:
          'Berikut adalah ringkasan perbaikan aman untuk kendala yang sering dialami:\n\n' +
          '- **`python: command not found`:** Buka kembali installer Python di Windows, klik *Modify*, centang *Add Python to environment variables*, lalu buka terminal baru.\n' +
          '- **PowerShell Execution Policy Terblokir:** Jalankan `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` sebelum menjalankan skrip aktivasi venv.\n' +
          '- **`ModuleNotFoundError`:** Pastikan terminal menampilkan tanda `(.venv)` dan pilih interpreter yang tepat di VS Code (`Ctrl+Shift+P > Python: Select Interpreter`).\n' +
          '- **Jupyter Port Conflict:** Jalankan `jupyter lab --port 8900` untuk menggunakan port alternatif jika port 8888 sedang dipakai.',
        callout: {
          type: 'warning',
          title: 'Prinsip Keamanan Sistem',
          text: 'Jangan pernah mematikan proteksi keamanan sistem atau menjalankan seluruh perintah dengan hak Administrator / root jika tidak benar-benar diperlukan.',
        },
      },
      {
        heading: 'Alur Verifikasi Menyeluruh 8 Langkah',
        explanation:
          'Lakukan uji coba akhir sebelum memulai materi pembelajaran pemrograman:\n\n' +
          '1. Verifikasi Python Interpreter (`py --version` atau `python3 --version`).\n' +
          '2. Verifikasi Package Manager (`pip --version`).\n' +
          '3. Uji coba pembuatan Virtual Environment (`python -m venv .test_env`).\n' +
          '4. Uji coba aktivasi Virtual Environment (`(.test_env)` terlihat).\n' +
          '5. Uji coba instalasi paket mandiri (`pip install requests`).\n' +
          '6. Uji coba deaktivasi (`deactivate`).\n' +
          '7. Pembersihan folder uji (`.test_env`).\n' +
          '8. Eksekusi skrip `main.py` terverifikasi.',
        commands: {
          windows: 'py content/getting-started/code/main.py',
          linux: 'python3 content/getting-started/code/main.py',
          macos: 'python3 content/getting-started/code/main.py',
        },
        expectedOutput: 'Python Learning Hub\nDevelopment Environment Ready!',
      },
    ],
    verificationChecklist: [
      'Semua 8 langkah verifikasi lulus tanpa galat',
      'Workstation siap untuk memulai modul pembelajaran Level 1 (Chapter 01)',
    ],
    commonMistakes: [
      {
        issue: 'Menjalankan Set-ExecutionPolicy Unrestricted secara sistem global',
        cause: 'Membaca tutorial internet lama yang mengorbankan keamanan sistem operasi Windows.',
        solution: 'Selalu gunakan `-Scope Process -ExecutionPolicy Bypass` agar izin hanya berlaku sementara untuk terminal saat ini.',
      },
    ],
    officialReferences: [
      { title: 'Python Windows FAQ Troubleshooting', url: 'https://docs.python.org/3/faq/windows.html' },
      { title: 'Pip Troubleshooting Guide', url: 'https://pip.pypa.io/en/stable/topics/troubleshooting/' },
    ],
  },
];
