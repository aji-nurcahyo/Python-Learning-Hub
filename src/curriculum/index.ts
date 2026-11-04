export interface Chapter {
  id: number;
  slug: string;
  levelId: 1 | 2 | 3;
  levelCategory?: 'foundations' | 'intermediate' | 'professional';
  number: string; // '01', '02', etc.
  title: string;
  subtitle: string;
  description: string;
  competencyFocus: string;
  estimatedHours: number;
  difficulty: 'Beginner' | 'Intermediate' | 'Advanced';
  available: boolean;
  prerequisites: string[];
  learningObjectives: string[];
  tags: string[];
  deckPath?: string;
  tugasPath?: string;
  resources?: {
    hasSlides?: boolean;
    slidesDeck?: string | null;
    starterCode?: string | null;
    assignmentGuide?: string | null;
    pptxDownload?: string;
  };
  codeExample?: {
    title?: string;
    code: string;
    outputKey: string;
    explanation: string;
  };
  exercise?: {
    title: string;
    instructions: string[];
    tips: string;
    time: string;
  };
  quiz?: {
    question: string;
    options: string[];
    correctIndex: number;
    explanation: string;
    hint?: string;
  };
  assignment?: {
    title: string;
    description: string;
    instructions: string[];
    rubric: { criteria: string; weight: number; description: string }[];
    starterCode?: string;
    starterFilename?: string;
    downloadMdUrl?: string;
    downloadPyUrl?: string;
  };
}

export interface Level {
  id: 1 | 2 | 3;
  title: string;
  subtitle: string;
  badge: string;
  alignment: string;
  overview: string;
  competencyTargets: string[];
  prerequisites: string[];
  learningOutcomes: string[];
  capstoneTitle: string;
  capstoneDescription: string;
  chapterRange: string;
}

export interface SpecializationTrack {
  id: string;
  title: string;
  subtitle: string;
  icon: string;
  tagline: string;
  description: string;
  targetAudience: string;
  recommendedChapters: number[];
  modules: {
    title: string;
    description: string;
    status: 'Core Prerequisite' | 'Specialization' | 'Advanced Project';
  }[];
}

export const LEVELS: Level[] = [
  {
    id: 1,
    title: 'Python Foundations',
    subtitle: 'Dasar Pemrograman, Logika & Struktur Data Inti',
    badge: 'Level 1 · Foundations',
    alignment: 'Selaras dengan area kompetensi Python Institute PCEP',
    overview:
      'Membangun fondasi komputasional yang kokoh: mulai dari instalasi environment, tipe data, kontrol alur logika, pengulangan, struktur data dasar (list, tuple, dict, set), hingga fungsi modular dan modul.',
    competencyTargets: [
      'Memahami eksekusi program Python dan lingkungan runtime',
      'Menguasai tipe data skalar, variabel, operator, dan ekspresi aritmatika/logika',
      'Merancang alur kendali if/elif/else dan perulangan for/while yang efisien',
      'Memilih dan memanipulasi koleksi data (List, Tuple, Dictionary, Set)',
      'Merancang fungsi modular dengan parameter, return value, dan scope variabel lokal/global',
    ],
    prerequisites: ['Kemampuan dasar logika matematika', 'Penggunaan komputer dasar (file system & terminal)'],
    learningOutcomes: [
      'Mampu menulis skrip otomasi Python 3 mandiri tanpa library eksternal',
      'Mampu memecahkan masalah komputasi dasar secara algoritmik',
      'Siap melanjutkan ke topik pemrograman berorientasi objek dan algoritma lanjutan',
    ],
    capstoneTitle: 'Foundations Capstone: Sistem Pengolahan Data Transaksi & Inventaris',
    capstoneDescription:
      'Mini proyek komprehensif mengintegrasikan seluruh konsep Level 1: pengolahan koleksi data, validasi input, fungsi modular, dan perhitungan statistik.',
    chapterRange: 'Chapter 01 – 12',
  },
  {
    id: 2,
    title: 'Intermediate Python Development',
    subtitle: 'Algoritma, OOP, Penanganan Error & Ekosistem Paket',
    badge: 'Level 2 · Intermediate',
    alignment: 'Selaras dengan area kompetensi Python Institute PCAP & Praktik Industri',
    overview:
      'Meningkatkan keterampilan rekayasa perangkat lunak: fungsi tingkat lanjut, pemahaman generator & comprehension, analisis algoritma pencarian & pengurutan, penanganan exception, OOP fundamental, serta manajemen environment & unit testing.',
    competencyTargets: [
      'Menerapkan first-class functions, lambda, filter, map, dan generator expressions',
      'Menganalisis kompleksitas waktu Big-O sederhana dan mengimplementasikan algoritma searching/sorting',
      'Menerapkan pemrograman berorientasi objek (Class, Object, Inheritance, Polymorphism, Encapsulation)',
      'Menangani exception secara robust dan menerapkan logging/debugging terstruktur',
      'Mengelola virtual environment (venv/pip) dan menyusun unit test terotomasi',
    ],
    prerequisites: ['Menyelesaikan Level 1 (Python Foundations) atau memiliki pemahaman sintaks dasar Python'],
    learningOutcomes: [
      'Mampu membangun aplikasi berarsitektur OOP modular yang dapat diuji (testable)',
      'Memahami trade-off efisiensi algoritma pada koleksi data besar',
      'Siap berkontribusi pada proyek open-source dan aplikasi backend/data berskala menengah',
    ],
    capstoneTitle: 'Intermediate Capstone: Aplikasi CLI Analitik & Engine Pemrosesan File',
    capstoneDescription:
      'Membangun engine analisis data berbasis OOP dengan parsing data CSV/JSON, custom exception, inheritance hierarchy, dan unit test lengkap.',
    chapterRange: 'Chapter 13 – 22',
  },
  {
    id: 3,
    title: 'Professional Python Engineering',
    subtitle: 'Arsitektur Perangkat Lunak, Asynchronous, Design Patterns & Skala Industri',
    badge: 'Level 3 · Professional',
    alignment: 'Terinspirasi oleh Standar Rekayasa Perangkat Lunak Python Modern',
    overview:
      'Mempersiapkan developer Python untuk lingkungan produksi: Design Patterns, Metaprogramming (Decorators, Context Managers), Static Type Hinting modern, Concurrency (Threading, Multiprocessing, AsyncIO), REST API, dan deployment container.',
    competencyTargets: [
      'Menerapkan Gang of Four (GoF) design patterns dan SOLID principles dalam Python',
      'Menguasai decorators lanjutan, custom context managers, dan generator pipelines',
      'Menerapkan type safety ketat dengan Mypy, typing module, dan Pydantic',
      'Membangun sistem non-blocking I/O performa tinggi dengan asyncio dan networking',
      'Menata struktur arsitektur microservice/package serta konfigurasi CI/CD & Docker',
    ],
    prerequisites: ['Menyelesaikan Level 2 (Intermediate) dan pemahaman mendalam tentang OOP serta CLI'],
    learningOutcomes: [
      'Mampu merancang dan merawat codebase Python skala besar dengan standar clean architecture',
      'Mampu mengoptimalkan konkurensi I/O-bound dan CPU-bound',
      'Siap bekerja sebagai Python Backend Engineer, Data Platform Engineer, atau DevOps Specialist',
    ],
    capstoneTitle: 'Professional Capstone: Layanan API Asinkron & Pipeline Data Real-Time',
    capstoneDescription:
      'Membangun microservice asinkron performa tinggi dengan type hints menyeluruh, caching layer, asynchronous database client, test coverage >90%, dan Dockerfile produksi.',
    chapterRange: 'Chapter 23 – 30',
  },
];

export const CHAPTERS: Chapter[] = [
  // LEVEL 1 (01 - 12)
  {
    id: 1,
    slug: '01-introduction',
    levelId: 1,
    number: '01',
    title: 'Introduction to Python',
    subtitle: 'Filosofi, Ekosistem & Eksekusi Program Pertama',
    description: 'Mengenal sejarah Python, Zen of Python, instalasi CPython, serta siklus eksekusi program melalui bytecode dan PVM.',
    competencyFocus: 'PCEP 1.1: Dasar eksekusi & lingkungan Python',
    estimatedHours: 3,
    difficulty: 'Beginner',
    available: true,
    prerequisites: [],
    learningObjectives: [
      'Memahami perbedaan interpreted language dan compiled language',
      'Menjalankan program Python pertama melalui CLI dan script file',
      'Mengenal kaidah penulisan komentar dan indentation standar PEP 8',
    ],
    tags: ['Interpreter', 'CPython', 'PEP 8', 'Syntax'],
    deckPath: '#chapter/01/slides',
    tugasPath: '#chapter/01/task',
    codeExample: {
      title: 'Program Pertama: Fungsi print() dan Argumen',
      code: `# Program Pertama: Fungsi print() dan Berbagai Argumen\nprint("Selamat datang di Python Learning Hub!")\nprint("Belajar Pemrograman Python untuk Rekayasa Telekomunikasi.")\nprint("Versi:", 3, "Status:", "Aktif")\nprint(100 + 200)`,
      outputKey: 'ch01-01',
      explanation: 'Fungsi print() mencetak representasi teks dari argumen ke konsol. Argumen multi-nilai dipisahkan dengan koma dan secara otomatis dicetak dengan spasi pemisah.',
    },
    exercise: {
      title: 'Latihan Terarah: Format Identitas Sistem',
      instructions: [
        'Deklarasikan variabel nama_perangkat bertipe string dan id_node bertipe integer.',
        'Gunakan fungsi print() dengan pemisah koma untuk mencetak baris ringkasan.',
        'Cetak keluaran ke layar terminal dan periksa pesan kesalahan jika tanda kurung dihilangkan.',
      ],
      tips: 'Perhatikan bahwa fungsi print() membutuhkan tanda kurung buka dan tutup berpasangan.',
      time: '15 menit',
    },
    quiz: {
      question: 'Manakah pernyataan yang BENAR mengenai cara kerja interpreter CPython?',
      options: [
        'CPython menerjemahkan kode sumber langsung ke file binary .exe mesin fisik',
        'CPython mengompilasi kode sumber ke bytecode (.pyc) lalu menjalankannya di Python Virtual Machine (PVM)',
        'CPython tidak melakukan kompilasi apa pun dan membaca teks mentah baris per baris',
        'CPython membutuhkan compiler eksternal seperti GCC sebelum kode dapat dijalankan',
      ],
      correctIndex: 1,
      explanation: 'CPython mengompilasi kode sumber (.py) menjadi bytecode internal (disimpan di folder __pycache__ sebagai .pyc) yang kemudian dieksekusi oleh Python Virtual Machine (PVM).',
      hint: 'Ingat keberadaan direktori __pycache__ saat Anda menjalankan modul Python.',
    },
    assignment: {
      title: 'Tugas Praktik 01: Verifikasi Environment Node Telekomunikasi',
      description: 'Rancang skrip Python mandiri yang mengidentifikasi versi sistem operasi, versi interpreter Python, dan mencetak laporan inisialisasi node telekomunikasi.',
      instructions: [
        'Gunakan modul bawaan sys dan platform untuk membaca metadata interpreter.',
        'Cetak status kesiapan node telekomunikasi dalam format tabel bersih.',
        'Terapkan konvensi docstring PEP 257 dan blok proteksi if __name__ == "__main__":.',
      ],
      rubric: [
        { criteria: 'Kebenaran Fungsional', weight: 40, description: 'Skrip berhasil membaca modul sys dan platform, menghitung waktu propagasi, dan mencetak seluruh data.' },
        { criteria: 'Kepatuhan Gaya PEP 8', weight: 30, description: 'Penamaan variabel snake_case, indentasi 4 spasi konsisten, spasi operator rapi.' },
        { criteria: 'Dokumentasi & Docstring', weight: 20, description: 'Menyertakan docstring modul dan komentar penjelas yang informatif.' },
        { criteria: 'Struktur Eksekusi', weight: 10, description: 'Menggunakan pola blok if __name__ == "__main__": standar.' },
      ],
      starterCode: `"""\nTugas Praktik 01: Verifikasi Environment Node Telekomunikasi\n"""\nimport sys\nimport platform\n\ndef inspeksi_node() -> None:\n    nama_os = platform.system()\n    versi_python = sys.version.split()[0]\n    node_id = "NODE-TELKOM-ITERA-01"\n    print("=" * 40)\n    print(f"Node: {node_id} | OS: {nama_os} | Py: {versi_python}")\n    print("=" * 40)\n\nif __name__ == "__main__":\n    inspeksi_node()`,
      starterFilename: 'tugas_01.py',
      downloadMdUrl: 'downloads/chapter-01/tugas.md',
      downloadPyUrl: 'downloads/chapter-01/contoh.py',
    },
  },
  {
    id: 2,
    slug: '02-variables-data-types',
    levelId: 1,
    number: '02',
    title: 'Variables & Data Types',
    subtitle: 'Variabel Dinamis, Tipe Data Skalar & Konversi',
    description: 'Menyimpan nilai dalam memori, tipe int, float, str, bool, pemahaman dynamic typing, dan konversi tipe data eksplisit.',
    competencyFocus: 'PCEP 2.1: Literal, variabel, dan konversi tipe',
    estimatedHours: 3,
    difficulty: 'Beginner',
    available: true,
    prerequisites: ['Chapter 01'],
    learningObjectives: [
      'Mendeklarasikan variabel dengan penamaan snake_case sesuai PEP 8',
      'Membedakan tipe data integer, floating-point, boolean, dan string',
      'Melakukan type casting dengan int(), float(), str(), dan bool()',
      'Menggunakan isinstance() untuk memvalidasi tipe data yang aman',
    ],
    tags: ['Variables', 'Types', 'Casting', 'Scalars'],
    deckPath: '#chapter/02/slides',
    tugasPath: '#chapter/02/task',
    codeExample: {
      title: 'Variabel sebagai Referensi Objek di Memori',
      code: `# Variabel sebagai Referensi Objek di Memori\nnama_stasiun = "BTS-Sukarame-01"\nid_transceiver = 1042\nkapasitas_kanal = 64\n\nprint("Nama Stasiun:", nama_stasiun)\nprint("ID Transceiver:", id_transceiver)\nprint("Kapasitas Kanal:", kapasitas_kanal)\n\nsalinan_id = id_transceiver\nprint("Apakah referensi menunjuk objek yang sama?", salinan_id is id_transceiver)`,
      outputKey: 'ch02-01',
      explanation: 'Variabel di Python bekerja sebagai label penunjuk (pointer) ke objek di memori. Operator "is" membuktikan bahwa dua variabel menunjuk ke objek identik yang sama di memori.',
    },
    exercise: {
      title: 'Latihan Terarah: Deklarasi Parameter Jaringan',
      instructions: [
        'Deklarasikan variabel nama_operator (str), frekuensi_mhz (float), dan kapasitas (int).',
        'Lakukan konversi data string mentah "1800.5" ke dalam tipe data float.',
        'Gunakan fungsi type() dan isinstance() untuk memverifikasi tipe data hasil konversi.',
      ],
      tips: 'Ingat bahwa string numerik dengan tanda titik seperti "1800.5" tidak dapat langsung diubah ke int() sebelum diubah ke float() terlebih dahulu.',
      time: '15 menit',
    },
    quiz: {
      question: 'Manakah nilai yang menghasilkan nilai logika True ketika dievaluasi menggunakan fungsi bawaan bool()?',
      options: [
        'bool(0)',
        'bool("")',
        'bool("0")',
        'bool(0.0)',
      ],
      correctIndex: 2,
      explanation: 'bool("0") menghasilkan True karena string tersebut tidak kosong (memiliki panjang 1 karakter). Sebaliknya, angka 0, float 0.0, dan string kosong "" bernilai Falsy (False).',
      hint: 'Perhatikan perbedaan antara angka integer nol dengan string yang berisi karakter teks "0".',
    },
    assignment: {
      title: 'Tugas Praktik 02: Validasi Parameter Transceiver BTS',
      description: 'Rancang parser parameter konfigurasi stasiun pemancar dengan validasi tipe data ketat dan konversi tipe teruji.',
      instructions: [
        'Ambil input mentah string parameter stasiun BTS.',
        'Lakukan pembersihan spasi dan type casting ke tipe str, float, int, dan bool.',
        'Validasi batasan nilai numerik dan cetak laporan hasil verifikasi konfigurasi.',
      ],
      rubric: [
        { criteria: 'Kebenaran Type Casting', weight: 40, description: 'Mengonversi seluruh string mentah ke tipe data target secara tepat tanpa galat runtime.' },
        { criteria: 'Logika Validasi Parameter', weight: 30, description: 'Menerapkan isinstance() dan memeriksa batasan nilai frekuensi serta daya pancar.' },
        { criteria: 'Kepatuhan Gaya PEP 8', weight: 20, description: 'Penamaan variabel snake_case deskriptif, spasi operator, dan keterbacaan kode.' },
        { criteria: 'Pengujian Kasus Uji', weight: 10, description: 'Menyertakan verifikasi data keluaran dengan kasus uji normal dan batas.' },
      ],
      starterCode: `"""\nTugas Praktik 02: Validasi Parameter Transceiver BTS\n"""\ndef proses_konfigurasi_bts(raw_name: str, raw_freq: str, raw_power: str, raw_status: str) -> dict:\n    bts_name = raw_name.strip()\n    frekuensi = float(raw_freq)\n    daya = int(raw_power)\n    aktif = bool(int(raw_status))\n    return {'nama': bts_name, 'frekuensi': frekuensi, 'daya': daya, 'aktif': aktif}\n\nif __name__ == '__main__':\n    print(proses_konfigurasi_bts('BTS-01', '1800.0', '40', '1'))`,
      starterFilename: 'tugas_02.py',
      downloadMdUrl: 'downloads/chapter-02/tugas.md',
      downloadPyUrl: 'downloads/chapter-02/contoh.py',
    },
  },
  {
    id: 3,
    slug: '03-operators-expressions',
    levelId: 1,
    number: '03',
    title: 'Operators & Expressions',
    subtitle: 'Aritmatika, Perbandingan, Logika & Presedensi',
    description: 'Operasi matematika dasar, pembagian bulat, modulo, perbandingan nilai, logika boolean short-circuit, dan aturan presedensi operator.',
    competencyFocus: 'PCEP 2.2: Operator numerik dan boolean',
    estimatedHours: 3,
    difficulty: 'Beginner',
    available: true,
    prerequisites: ['Chapter 02'],
    learningObjectives: [
      'Menggunakan operator aritmatika (+, -, *, /, //, %, **)',
      'Menerapkan operator perbandingan (==, !=, >, <, >=, <=)',
      'Memahami evaluasi ekspresi logika dengan presedensi operator yang benar',
      'Menganalisis mekanisme short-circuit evaluation pada operator and dan or',
    ],
    tags: ['Arithmetic', 'Logic', 'Precedence', 'Operators'],
    deckPath: '#chapter/03/slides',
    tugasPath: '#chapter/03/task',
    codeExample: {
      title: 'Operator Aritmatika Python',
      code: `# Operator Aritmatika Python\na = 25\nb = 4\n\nprint("a =", a, ", b =", b)\nprint("Penjumlahan (a + b):", a + b)\nprint("Pengurangan (a - b):", a - b)\nprint("Perkalian (a * b):", a * b)\nprint("Pembagian Riil (a / b):", a / b)\nprint("Pembagian Bulat (a // b):", a // b)\nprint("Sisa Bagi / Modulo (a % b):", a % b)\nprint("Eksponensial / Pangkat (a ** 2):", a ** 2)`,
      outputKey: 'ch03-01',
      explanation: 'Di Python 3, operator / selalu menghasilkan float (25 / 4 = 6.25). Operator // melakukan pembagian bulat yang dibulatkan ke bawah (25 // 4 = 6), dan % mengembalikan sisa hasil bagi (25 % 4 = 1).',
    },
    exercise: {
      title: 'Latihan Terarah: Alokasi Time-Slot & Logika Sinyal',
      instructions: [
        'Gunakan pembagian bulat // dan modulo % untuk menghitung pembagian paket data ke dalam slot frame.',
        'Susun ekspresi logika boolean multi-kondisi dengan operator and, or, dan not.',
        'Hitung panjang gelombang elektromagnetik menggunakan rumus lambda = c / f.',
      ],
      tips: 'Gunakan tanda kurung eksplisit untuk memastikan ekspresi bertingkat dievaluasi dalam urutan yang tepat.',
      time: '15 menit',
    },
    quiz: {
      question: 'Apakah hasil dan tipe data dari ekspresi 17 // 4 dan 17 % 4 secara berurutan di Python?',
      options: [
        '4.25 (float) dan 1 (int)',
        '4 (int) dan 1 (int)',
        '4.0 (float) dan 1.0 (float)',
        '5 (int) dan 2 (int)',
      ],
      correctIndex: 1,
      explanation: '17 // 4 melakukan floor division menghasilkan integer 4. Sedangkan 17 % 4 menghitung sisa hasil bagi bulat menghasilkan integer 1.',
      hint: 'Ingat bahwa floor division memotong sisa desimal dan menghasilkan bilangan bulat.',
    },
    assignment: {
      title: 'Tugas Praktik 03: Kalkulator Anggaran Daya Tautan (Link Budget)',
      description: 'Rancang kalkulator parameter daya pancar, penguatan antena, dan rugi redaman sinyal gelombang radio.',
      instructions: [
        'Hitung daya sinyal terima P_rx dari penjumlahan daya pemancar, gain antena, dan pengurangan total redaman.',
        'Hitung fade margin tautan dengan mengurangkan daya terima terhadap batas sensitivitas penerima.',
        'Gunakan operator relasional untuk mengevaluasi kelayakan tautan (margin >= 10 dB).',
      ],
      rubric: [
        { criteria: 'Akurasi Perhitungan Formula', weight: 40, description: 'Formula link budget dan fade margin dihitung secara matematis tepat.' },
        { criteria: 'Penerapan Operator & Logika', weight: 30, description: 'Menerapkan operator perbandingan dan logika boolean secara tepat.' },
        { criteria: 'Kepatuhan Gaya PEP 8', weight: 20, description: 'Penamaan variabel snake_case deskriptif dan struktur kode rapi.' },
        { criteria: 'Pengujian Kasus Uji Ekstrem', weight: 10, description: 'Menyertakan uji kasus kelayakan tautan normal dan kondisi tidak layak.' },
      ],
      starterCode: `"""\nTugas Praktik 03: Kalkulator Anggaran Daya Tautan (Link Budget)\n"""\ndef hitung_link_budget(p_tx_dbm: float, g_tx_dbi: float, g_rx_dbi: float, l_fspl_db: float, l_misc_db: float) -> dict:\n    p_rx = p_tx_dbm + g_tx_dbi + g_rx_dbi - l_fspl_db - l_misc_db\n    margin = p_rx - (-95.0)\n    return {'p_rx': p_rx, 'margin': margin, 'layak': margin >= 10.0}\n\nif __name__ == '__main__':\n    print(hitung_link_budget(43.0, 18.0, 14.0, 142.5, 3.0))`,
      starterFilename: 'tugas_03.py',
      downloadMdUrl: 'downloads/chapter-03/tugas.md',
      downloadPyUrl: 'downloads/chapter-03/contoh.py',
    },
  },
  {
    id: 4,
    slug: '04-input-output',
    levelId: 1,
    number: '04',
    title: 'Input & Output',
    subtitle: 'Interaksi Pengguna & Pemformatan Teks Modern',
    description: 'Menerima masukan pengguna dengan input(), validasi dasar, serta memformat output dengan f-strings, format specifiers, dan tabel terstruktur.',
    competencyFocus: 'PCEP 2.3: I/O standar dan string formatting',
    estimatedHours: 3,
    difficulty: 'Beginner',
    available: true,
    prerequisites: ['Chapter 03'],
    learningObjectives: [
      'Mengambil input dinamis dan mengonversi tipe data masukan',
      'Menggunakan f-strings untuk interpolasi ekspresi variabel sesuai PEP 498',
      'Memformat angka desimal, persentase, dan perataan kolom tabel (<, >, ^)',
    ],
    tags: ['I/O', 'f-strings', 'Formatting', 'Alignment'],
    deckPath: '#chapter/04/slides',
    tugasPath: '#chapter/04/task',
    codeExample: {
      title: 'Argumen Pemisah (sep) dan Akhiran (end) pada print()',
      code: `# Argumen Pemisah (sep) dan Akhiran (end) pada print()\nprint("Node-A", "Node-B", "Node-C", sep=" -> ")\nprint("2026", "11", "04", sep="-")\nprint("192", "168", "1", "1", sep=".")\n\nprint("Menghubungkan ke pemancar", end="...")\nprint(" [TERHUBUNG]")\n\nprint("STATUS", "READY", sep=": ", end=" | ID: BTS-01\\n")`,
      outputKey: 'ch04-01',
      explanation: 'Argumen sep mengontrol karakter pemisah antar nilai (default spasi), sedangkan argumen end mengontrol karakter penutup baris (default newline "\\n").',
    },
    exercise: {
      title: 'Latihan Terarah: Format Interaktif Telemetri',
      instructions: [
        'Gunakan fungsi input() dan konversi ke float untuk menerima daya terima RSRP.',
        'Gunakan format specifiers f-string :.2f, :.2e, dan :.1% untuk data rasio telemetri.',
        'Susun tata letak tabel CLI menggunakan perataan kolom rata kiri (<) dan rata tengah (^).',
      ],
      tips: 'Pastikan mengonversi hasil input() sebelum melakukan operasi aritmatika.',
      time: '15 menit',
    },
    quiz: {
      question: 'Apakah output dari kode Python: print(f"{0.875:.1%}")?',
      options: [
        '0.875%',
        '87.5%',
        '88%',
        '0.88',
      ],
      correctIndex: 1,
      explanation: 'Penentu format :.1% secara otomatis mengalikan nilai desimal dengan 100, membulatkannya menjadi satu digit di belakang koma, dan menambahkan simbol % di ujung string (menghasilkan 87.5%).',
      hint: 'Format persentase di Python otomatis mengalikan angka desimal dengan 100.',
    },
    assignment: {
      title: 'Tugas Praktik 04: Generator Kartu Telemetri Node Jaringan',
      description: 'Rancang program pembuat laporan status node telekomunikasi terformat profesional berbasis f-strings.',
      instructions: [
        'Definisikan daftar koleksi dictionary parameter telemetri beberapa stasiun BTS.',
        'Gunakan f-strings dan format specifiers untuk menyusun tabel laporan konsol dengan lebar kolom seragam.',
        'Hitung dan tampilkan ringkasan rata-rata daya transmisi dan rasio packet loss di bawah tabel.',
      ],
      rubric: [
        { criteria: 'Penerapan f-Strings & Interpolasi', weight: 40, description: 'Menggunakan f-strings secara konsisten tanpa operator lawas % atau konkatenasi string manual.' },
        { criteria: 'Format Specifiers & Alignment', weight: 30, description: 'Menerapkan format persentase :.2%, desimal :.1f, dan perataan kolom sejajar vertikal.' },
        { criteria: 'Kepatuhan Gaya PEP 8', weight: 20, description: 'Penamaan snake_case, modularitas fungsi, dan format kode bersih.' },
        { criteria: 'Logika Ringkasan Metrik', weight: 10, description: 'Perhitungan nilai rata-rata daya pancar dan packet loss tepat.' },
      ],
      starterCode: `"""\nTugas Praktik 04: Generator Kartu Telemetri Node Jaringan\n"""\ndef generate_laporan_telemetri(daftar_node: list[dict]) -> None:\n    print("=" * 60)\n    print(f"{'LAPORAN STATUS TELEMETRI':^60}")\n    print("=" * 60)\n    for n in daftar_node:\n        print(f"{n['id']:<10} | {n['frekuensi']:^12.1f} MHz | {n['status']:>10}")\n    print("=" * 60)\n\nif __name__ == '__main__':\n    sample = [{'id': 'NODE-01', 'frekuensi': 1800.5, 'status': 'ONLINE'}]\n    generate_laporan_telemetri(sample)`,
      starterFilename: 'tugas_04.py',
      downloadMdUrl: 'downloads/chapter-04/tugas.md',
      downloadPyUrl: 'downloads/chapter-04/contoh.py',
    },
  },
  {
    id: 5,
    slug: '05-conditional-statements',
    levelId: 1,
    number: '05',
    title: 'Conditional Statements',
    subtitle: 'Pengambilan Keputusan: if, elif, else & Guard Clauses',
    description: 'Merancang alur logika percabangan, kondisi bertingkat, operator ternary, dan pola guard clauses untuk kode yang bersih dan andal.',
    competencyFocus: 'PCEP 3.1: Percabangan dan logika alur',
    estimatedHours: 3,
    difficulty: 'Beginner',
    available: true,
    prerequisites: ['Chapter 03', 'Chapter 04'],
    learningObjectives: [
      'Menulis struktur percabangan if, elif, dan else secara tepat',
      'Menggabungkan kondisi majemuk menggunakan and, or, dan not',
      'Menghindari nested if yang terlalu dalam dengan teknik guard clauses',
      'Mengimplementasikan ekspresi kondisional ternary untuk penugasan variabel bersih',
    ],
    tags: ['Branching', 'if-else', 'Decision Logic', 'Conditionals'],
    deckPath: '#chapter/05/slides',
    tugasPath: '#chapter/05/task',
    codeExample: {
      title: 'Klasifikasi Nilai Akademik Mahasiswa',
      code: `# Klasifikasi Nilai Akademik Mahasiswa\ndef konversi_skor_ke_huruf(skor: float) -> str:\n    if skor >= 80.0:\n        return "A"\n    elif skor >= 70.0:\n        return "B"\n    elif skor >= 60.0:\n        return "C"\n    elif skor >= 50.0:\n        return "D"\n    else:\n        return "E"\n\nprint("Skor 85.5 -> Huruf Mutu:", konversi_skor_ke_huruf(85.5))\nprint("Skor 72.0 -> Huruf Mutu:", konversi_skor_ke_huruf(72.0))`,
      outputKey: 'ch05-02',
      explanation: 'Struktur if-elif-else mengevaluasi kondisi secara berurutan dari atas ke bawah. Segera setelah kondisi pertama yang bernilai True terpenuhi, blok tersebut dieksekusi dan cabang lainnya dilewati.',
    },
    exercise: {
      title: 'Latihan Terarah: Evaluasi Suhu Server & Otentikasi',
      instructions: [
        'Terapkan fungsi evaluasi suhu server menggunakan guard clauses untuk mendeteksi kondisi darurat.',
        'Susun ekspresi logika boolean multi-parameter untuk otentikasi pintu shelter BTS.',
        'Klasifikasikan jenis segitiga antena berdasarkan panjang ketiga sisinya.',
      ],
      tips: 'Urutkan pengujian nilai batas dari kriteria yang paling ketat agar tidak terjadi dead code.',
      time: '15 menit',
    },
    quiz: {
      question: 'Apakah yang akan terjadi jika urutan percabangan diletakkan dengan "elif skor >= 85" berada di bawah "if skor >= 60"?',
      options: [
        'Kode akan menghasilkan galat SyntaxError saat dikompilasi',
        'Nilai 90 akan salah dikategorikan oleh cabang pertama (skor >= 60) sehingga cabang 85 menjadi dead code',
        'CPython akan otomatis mengurutkan ulang cabang kondisi berdasarkan angka terbesar',
        'Keduanya akan dieksekusi secara bersamaan',
      ],
      correctIndex: 1,
      explanation: 'CPython mengevaluasi percabangan dari atas ke bawah dan berhenti pada kondisi pertama yang bernilai True. Karena 90 >= 60 bernilai True, cabang >= 85 di bawahnya tidak akan pernah terjangkau (dead code).',
      hint: 'Ingat sifat evaluasi alur percabangan yang berhenti seketika saat kondisi pertama terpenuhi.',
    },
    assignment: {
      title: 'Tugas Praktik 05: Student Grade and Signal Quality Classifier',
      description: 'Rancang program cerdas terstruktur yang memvalidasi masukan numerik, mengklasifikasi nilai akademik dan sinyal RSRP, serta menyajikan analisis diagnostik.',
      instructions: [
        'Validasi masukan numerik terhadap batas rentang sah (skor 0-100 dan RSRP -140 s.d. -40 dBm).',
        'Klasifikasikan nilai akademik ke grade A, B, C, D, E dan sinyal RSRP ke Sangat Baik, Baik, Cukup, Buruk.',
        'Tampilkan pesan diagnostik lengkap untuk masing-masing hasil klasifikasi dan tangani nilai batas kritis.',
      ],
      rubric: [
        { criteria: 'Validasi Masukan & Kondisi Batas', weight: 30, description: 'Menolak nilai di luar rentang dan menangani nilai batas kritis secara akurat.' },
        { criteria: 'Kebenaran Logika Percabangan', weight: 40, description: 'Mengimplementasikan if-elif-else yang runtut, tanpa dead code, dengan hasil presisi.' },
        { criteria: 'Penjelasan Diagnostik Lengkap', weight: 15, description: 'Memberikan keterangan kontekstual yang informatif untuk setiap kategori.' },
        { criteria: 'Kepatuhan Gaya PEP 8 & Struktur', weight: 15, description: 'Penamaan snake_case, modularitas fungsi, dan pola idiomatis Python.' },
      ],
      starterCode: `"""\nTugas Praktik 05: Student Grade and Signal Quality Classifier\n"""\ndef klasifikasi_nilai_akademik(skor: float) -> tuple[bool, str, str]:\n    if skor < 0 or skor > 100:\n        return False, '-', 'Skor di luar rentang sah'\n    if skor >= 80: return True, 'A', 'Sangat Memuaskan'\n    elif skor >= 70: return True, 'B', 'Memuaskan'\n    elif skor >= 60: return True, 'C', 'Cukup'\n    elif skor >= 50: return True, 'D', 'Kurang'\n    else: return True, 'E', 'Gagal'\n\nif __name__ == '__main__':\n    print(klasifikasi_nilai_akademik(85.5))`,
      starterFilename: 'tugas_05.py',
      downloadMdUrl: 'downloads/chapter-05/tugas.md',
      downloadPyUrl: 'downloads/chapter-05/contoh.py',
    },
  },
  {
    id: 6,
    slug: '06-loops-iteration',
    levelId: 1,
    number: '06',
    title: 'Loops & Iteration',
    subtitle: 'Pengulangan for, while, break, continue & else',
    description: 'Mengulang tugas komputasi dengan for dan while, pemanfaatan range(), kontrol loop break dan continue, serta pola algoritma akumulator.',
    competencyFocus: 'PCEP 3.2: Pengulangan dan kontrol iterasi',
    estimatedHours: 4,
    difficulty: 'Beginner',
    available: true,
    prerequisites: ['Chapter 05'],
    learningObjectives: [
      'Memilih antara for loop (definite iteration) dan while loop (indefinite iteration)',
      'Memanfaatkan fungsi range(start, stop, step) secara optimal',
      'Mengendalikan siklus loop dengan break, continue, dan else block',
      'Menerapkan pola akumulator dan pencacah untuk statistik data streaming',
    ],
    tags: ['For Loop', 'While Loop', 'Range', 'Iteration'],
    deckPath: '#chapter/06/slides',
    tugasPath: '#chapter/06/task',
    codeExample: {
      title: 'Akumulasi Penjumlahan dan Perhitungan Nilai Rata-Rata',
      code: `# Akumulasi Penjumlahan dan Perhitungan Nilai Rata-Rata\ndaftar_daya_mw = [25.0, 32.5, 40.0, 18.5, 50.0]\ntotal_daya = 0.0\njumlah_data = 0\n\nfor daya in daftar_daya_mw:\n    total_daya += daya\n    jumlah_data += 1\n\nrata_rata = total_daya / jumlah_data\nprint(f"Total: {total_daya:.1f} mW | Rata-Rata: {rata_rata:.2f} mW")`,
      outputKey: 'ch06-03',
      explanation: 'Pola akumulator (total += x) dan pola pencacah (count += 1) digunakan bersama for loop untuk menghitung total kumulatif dan nilai rata-rata dari koleksi data deret waktu.',
    },
    exercise: {
      title: 'Latihan Terarah: Retransmisi Paket & Filter Sinyal',
      instructions: [
        'Simulasikan retransmisi paket dengan while loop dan break saat menerima respon ACK.',
        'Saring derau sinyal negatif menggunakan for loop dan kata kunci continue.',
        'Cetak matriks pola penguatan antena berjenjang dengan nested loops.',
      ],
      tips: 'Pastikan variabel loop selalu diperbarui untuk mencegah terjadinya infinite loop pada while.',
      time: '15 menit',
    },
    quiz: {
      question: 'Berapakah jumlah pengulangan yang dilakukan oleh kode: for i in range(1, 10, 2):?',
      options: [
        '10 kali (1 sampai 10)',
        '9 kali (1 sampai 9)',
        '5 kali (1, 3, 5, 7, 9)',
        '4 kali (2, 4, 6, 8)',
      ],
      correctIndex: 2,
      explanation: 'range(1, 10, 2) menghasilkan deret bilangan ganjil: 1, 3, 5, 7, dan 9. Bilangan berikutnya (11) melampaui batas henti eksklusif 10, sehingga loop dieksekusi tepat 5 kali.',
      hint: 'Hitung pertambahan bilangan mulai dari 1 dengan kenaikan (step) 2 hingga sebelum menyentuh 10.',
    },
    assignment: {
      title: 'Tugas Praktik 06: Sensor Data Monitoring Simulator',
      description: 'Rancang program simulator pemrosesan aliran data telemetri sensor telekomunikasi dengan penyaringan anomali, kalkulasi ringkasan statistik, dan pelaporan rapi.',
      instructions: [
        'Gunakan for loop untuk memproses deret sampel telemetri sensor suhu.',
        'Terapkan continue untuk melewati data noise -999.0 C dan break jika suhu kritis >= 80 C.',
        'Hitung total sampel valid, rata-rata, min, max, serta jumlah peringatan suhu waspada (>= 35 C).',
      ],
      rubric: [
        { criteria: 'Implementasi Loop & Kontrol Alur', weight: 40, description: 'Menerapkan for/while, continue untuk noise, dan break untuk darurat secara tepat.' },
        { criteria: 'Kalkulasi Akumulator & Statistik', weight: 30, description: 'Perhitungan total, rata-rata, min, max, dan ambang waspada presisi.' },
        { criteria: 'Penanganan Terminasi & Pelaporan', weight: 20, description: 'Format laporan konsol terstruktur rapi dan menyajikan status terminasi akurat.' },
        { criteria: 'Kepatuhan Gaya PEP 8 & Pythonic', weight: 10, description: 'Penamaan variabel snake_case deskriptif dan struktur kode bersih.' },
      ],
      starterCode: `"""\nTugas Praktik 06: Sensor Data Monitoring Simulator\n"""\ndef proses_sensor(aliran_data: list[float]) -> dict:\n    total = 0.0\n    valid = 0\n    for x in aliran_data:\n        if x == -999.0: continue\n        if x >= 80.0: break\n        total += x\n        valid += 1\n    return {'valid': valid, 'rata_rata': total / valid if valid > 0 else 0.0}\n\nif __name__ == '__main__':\n    print(proses_sensor([25.0, 30.0, -999.0, 35.0]))`,
      starterFilename: 'tugas_06.py',
      downloadMdUrl: 'downloads/chapter-06/tugas.md',
      downloadPyUrl: 'downloads/chapter-06/contoh.py',
    },
  },
  {
    id: 7,
    slug: '07-strings-text-processing',
    levelId: 1,
    number: '07',
    title: 'Strings & Text Processing',
    subtitle: 'Indexing, Slicing, Immutability & Metode String',
    description: 'Eksplorasi mendalam string sebagai sequence immutable: pemotongan slice [start:stop:step], metode bawaan, validasi format, dan parsing telemetri terstruktur.',
    competencyFocus: 'PCEP 3.3: Manipulasi sequence teks',
    estimatedHours: 4,
    difficulty: 'Beginner',
    available: true,
    prerequisites: ['Chapter 06'],
    learningObjectives: [
      'Menerapkan indexing positif dan negatif serta slicing sequence',
      'Memanfaatkan metode string penting (strip, split, join, replace, find)',
      'Memahami sifat immutability string dalam memori Python',
      'Melakukan validasi identifier perangkat dan parsing payload sensor IoT',
    ],
    tags: ['Strings', 'Slicing', 'Text Processing', 'Methods'],
    deckPath: '#chapter/07/slides',
    tugasPath: '#chapter/07/task',
    codeExample: {
      title: 'Parsing Pesan Telemetri Sensor Terstruktur',
      code: `# Parsing Pesan Telemetri Sensor Terstruktur\nraw_payload = "ID=BTS-04;FREQ=1800.5;PWR=40.0;STAT=ACTIVE"\npasangan_field = raw_payload.split(";")\ndata_terurai = {}\n\nfor pair in pasangan_field:\n    kunci, nilai = pair.split("=")\n    data_terurai[kunci] = nilai\n\nprint("Field Parsing:", data_terurai)\nprint(f"Node {data_terurai['ID']} aktif pada {data_terurai['FREQ']} MHz")`,
      outputKey: 'ch07-06',
      explanation: 'Metode .split(";") memecah string payload menjadi pasangan token field, kemudian pemisahan kedua .split("=") mengekstrak nama parameter dan nilainya ke dalam dictionary terorganisir.',
    },
    exercise: {
      title: 'Latihan Terarah: Ekstraktor URL & Masking Data',
      instructions: [
        'Ekstrak protokol, IP host, dan port dari string URL gateway jaringan.',
        'Lakukan masking penyensoran 5 digit terakhir pada nomor seri perangkat nirkabel.',
        'Validasi kepatuhan format alamat MAC menggunakan split(":") dan isalnum().',
      ],
      tips: 'Gunakan slicing dengan indeks negatif untuk memotong atau menyensor karakter dari belakang.',
      time: '15 menit',
    },
    quiz: {
      question: 'Apakah yang terjadi jika kode mengeksekusi: s = "Python"; s[0] = "J"?',
      options: [
        'String s berubah nilainya menjadi "Jython"',
        'Terjadi galat TypeError karena string di Python bersifat immutable (tidak bisa dimodifikasi di tempat)',
        'Karakter "J" ditambahkan di depan kata "Python" menjadi "JPython"',
        'String s terhapus otomatis dari memori Heap',
      ],
      correctIndex: 1,
      explanation: 'String di Python bersifat immutable (kekal). Anda tidak dapat mengubah elemen karakter di tempat menggunakan item assignment (s[0] = "J"). Untuk mengubahnya, Anda harus membentuk string baru: s = "J" + s[1:].',
      hint: 'Ingat salah satu sifat fundamental string di Python yang melarang mutasi in-place.',
    },
    assignment: {
      title: 'Tugas Praktik 07: Device Identifier & Sensor Message Processor',
      description: 'Rancang program parser telemetri yang memvalidasi format ID perangkat, mengekstrak metrik sensor dari payload teks mentah, dan menyajikan laporan bersih.',
      instructions: [
        'Validasi format ID perangkat berdasarkan prefiks "NODE-", jumlah segmen strip, 3 huruf lokasi, dan 4 digit unit.',
        'Urai payload mentah berbasis delimiter titik-koma ";" dan "=" menjadi data terstruktur.',
        'Lakukan normalisasi teks status dan cetak kartu laporan pemantauan telemetri terformat.',
      ],
      rubric: [
        { criteria: 'Validasi Format Identifier', weight: 30, description: 'Memeriksa prefiks, jumlah segmen split, validitas huruf kapital lokasi, dan 4 digit unit.' },
        { criteria: 'Parsing Delimiter & Pasangan Nilai', weight: 35, description: 'Mengurai string sensor berbasis delimiter ";" dan "=" secara akurat.' },
        { criteria: 'Normalisasi & Pembersihan Teks', weight: 20, description: 'Menghapus whitespace liar, membersihkan tag prefiks mentah, dan menstandarisasi huruf.' },
        { criteria: 'Kepatuhan Gaya PEP 8 & Struktur', weight: 15, description: 'Penamaan snake_case, modularitas fungsi terpisah, dan blok idiomatis Python.' },
      ],
      starterCode: `"""\nTugas Praktik 07: Device Identifier & Sensor Message Processor\n"""\ndef parse_payload(payload: str) -> dict:\n    data = {}\n    for item in payload.strip().split(';'):\n        if '=' in item:\n            k, v = item.split('=', 1)\n            data[k.strip()] = v.strip()\n    return data\n\nif __name__ == '__main__':\n    print(parse_payload('ID=NODE-01;TEMP=32.5;STAT=ok'))`,
      starterFilename: 'tugas_07.py',
      downloadMdUrl: 'downloads/chapter-07/tugas.md',
      downloadPyUrl: 'downloads/chapter-07/contoh.py',
    },
  },
  {
    id: 8,
    slug: '08-lists-tuples',
    levelId: 1,
    number: '08',
    title: 'Lists & Tuples',
    subtitle: 'Koleksi Data Terurut: Mutable vs Immutable Sequences',
    description:
      'Mengolah banyak data berurutan: operasi list (append, insert, pop, sort), konsep mutabilitas, tuple untuk integritas data, dan teknik unpacking.',
    competencyFocus: 'PCEP 4.1: List dan Tuple sequences',
    estimatedHours: 4,
    difficulty: 'Beginner',
    available: true,
    prerequisites: ['Chapter 07'],
    learningObjectives: [
      'Membedakan kapan harus menggunakan list (mutable) dan tuple (immutable)',
      'Melakukan manipulasi elemen list menggunakan indexing, slicing, dan metode bawaan',
      'Menerapkan tuple unpacking untuk pertukaran nilai dan pemrosesan koordinat data',
    ],
    tags: ['Lists', 'Tuples', 'Mutability', 'Sequences'],
    deckPath: '#chapter/08/slides',
    tugasPath: '#chapter/08/task',
    codeExample: {
      title: 'Operasi List & Indexing Sequence',
      code: `# Operasi List & Pengindeksan Koleksi Data\nrsrp_list = [-82, -107, -95, -89]\nprint(rsrp_list[0])  # Mengakses elemen pertama`,
      outputKey: 'p10-02',
      explanation: 'List merupakan tipe data sequence mutable. Elemen diakses dengan indeks nol (zero-based index) dan dapat dimodifikasi secara dinamis.',
    },
    exercise: {
      title: 'Latihan Terarah: Analisis Nilai Sinyal Telekomunikasi',
      instructions: [
        'Buat sebuah list berisi 5 data pengukuran RSRP (dBm): [-75, -88, -104, -92, -80].',
        'Gunakan loop for untuk menghitung jumlah sinyal yang berada di bawah ambang batas -90 dBm.',
        'Tampilkan hasil penghitungan ke konsol dengan format yang jelas.',
      ],
      tips: 'Gunakan operator pembanding < -90 dan pertahankan variabel penghitung (counter) yang dimulai dari 0.',
      time: '15 menit',
    },
    quiz: {
      question: 'Manakah karakteristik fundamental yang membedakan List dan Tuple dalam Python?',
      options: [
        'List bersifat mutable (bisa diubah), sedangkan Tuple bersifat immutable (tidak bisa diubah)',
        'List hanya bisa menyimpan angka, sedangkan Tuple bisa menyimpan teks',
        'Tuple mendukung operasi append(), sedangkan List tidak mendukung',
        'List diapit tanda kurung biasa (), sedangkan Tuple diapit kurung siku []',
      ],
      correctIndex: 0,
      explanation: 'List didefinisikan dengan kurung siku [] dan bersifat mutable sehingga nilainya dapat diubah/ditambah. Sebaliknya, Tuple didefinisikan dengan () dan bersifat immutable untuk menjaga integritas data.',
      hint: 'Ingat sifat modifikasi elemen setelah objek dibuat dalam memori.',
    },
    assignment: {
      title: 'Tugas Praktik 08: Pengolahan Sinyal & Statistik Koleksi',
      description: 'Implementasikan skrip pengolahan data pengukuran sinyal telekomunikasi berbasis List dan Tuple.',
      instructions: [
        'Definisikan list data pengukuran dari stasiun pemancar.',
        'Hitung nilai rata-rata, nilai minimum, dan nilai maksimum tanpa fungsi library eksternal.',
        'Kembalikan hasil ringkasan dalam bentuk Tuple immutable (min, max, mean).',
      ],
      rubric: [
        { criteria: 'Kebenaran Logika Perhitungan', weight: 40, description: 'Perhitungan min, max, rata-rata akurat dan menangani list kosong dengan baik.' },
        { criteria: 'Penerapan Konsep List & Tuple', weight: 30, description: 'Menggunakan list untuk akumulasi data dan tuple untuk output ringkasan immutable.' },
        { criteria: 'Kerapian Kode & PEP 8', weight: 20, description: 'Penamaan variabel snake_case dan format kode bersih.' },
        { criteria: 'Pengujian Kasus Uji', weight: 10, description: 'Menyertakan minimal 3 variasi dataset pengujian.' },
      ],
      starterCode: `# Template Starter Code - Chapter 08\ndef ringkas_sinyal(data_sinyal: list[float]) -> tuple[float, float, float]:\n    """Menghitung nilai minimum, maksimum, dan rata-rata dari list sinyal."""\n    if not data_sinyal:\n        return (0.0, 0.0, 0.0)\n    # Tuliskan logika Anda di sini\n    pass`,
      starterFilename: 'tugas_08.py',
      downloadMdUrl: 'downloads/chapter-08/tugas.md',
      downloadPyUrl: 'downloads/chapter-08/contoh.py',
    },
  },
  {
    id: 9,
    slug: '09-dictionaries-sets',
    levelId: 1,
    number: '09',
    title: 'Dictionaries & Sets',
    subtitle: 'Struktur Data Berbasis Hash: Key-Value & Himpunan Unik',
    description:
      'Menyimpan data asosiatif dengan key-value pairs pada dictionary, pencarian O(1), penghapusan duplikasi dan operasi himpunan matematika pada set.',
    competencyFocus: 'PCEP 4.2: Mapping types dan Set operations',
    estimatedHours: 4,
    difficulty: 'Beginner',
    available: true,
    prerequisites: ['Chapter 08'],
    learningObjectives: [
      'Membuat dan memanipulasi dictionary dengan method get(), items(), keys(), dan values()',
      'Menggunakan set untuk deduplikasi data seketika dan operasi union, intersection, difference',
      'Memilih struktur data yang tepat untuk kebutuhan query data tabular dan sensor',
    ],
    tags: ['Dictionary', 'Sets', 'Hash Maps', 'Key-Value'],
    deckPath: '#chapter/09/slides',
    tugasPath: '#chapter/09/task',
    codeExample: {
      title: 'Struktur Data Dictionary & Hash Key-Value',
      code: `# Struktur Data Dictionary & Hash Key-Value\nsensor = {"id": "S01", "lokasi": "Gedung A", "rsrp": -80}\nprint(sensor["id"])\nprint(sensor.get("status", "tidak tersedia"))\nprint(sensor.items())`,
      outputKey: 'p10-05',
      explanation: 'Dictionary menyimpan data berpasangan key-value dengan kompleksitas pencarian O(1). Metode get() mencegah timbulnya KeyError saat kunci tidak ditemukan.',
    },
    exercise: {
      title: 'Latihan Terarah: Pemetaan Himpunan Lokasi Sinyal (Set & Dict)',
      instructions: [
        'Diberikan daftar dictionary record sensor yang memuat kunci "lokasi".',
        'Gunakan tipe data set untuk mengekstrak daftar nama gedung/lokasi unik tanpa duplikasi.',
        'Cetak himpunan lokasi unik dan hitung total titik pemancar.',
      ],
      tips: 'Set secara otomatis membuang duplikasi ketika Anda menambahkan elemen menggunakan method add() atau set comprehension.',
      time: '20 menit',
    },
    quiz: {
      question: 'Apa keunggulan utama menggunakan dictionary.get(key, default) dibandingkan akses langsung dictionary[key]?',
      options: [
        'Metode get() tidak memicu KeyError jika kunci tidak ditemukan di dalam dictionary',
        'Metode get() membuat dictionary berjalan dua kali lebih cepat',
        'Metode get() otomatis menambahkan kunci baru ke dalam dictionary',
        'Akses langsung dictionary[key] sudah tidak didukung di Python 3',
      ],
      correctIndex: 0,
      explanation: 'Metode get(key, default) memberikan nilai fallback yang aman tanpa memicu crash program akibat KeyError jika kunci yang diminta belum ada.',
      hint: 'Pikirkan penanganan error ketika suatu kunci mungkin absen.',
    },
    assignment: {
      title: 'Tugas Praktik 09: Registri Sensor & Pemetaan Sinyal',
      description: 'Rancang modul pengelolaan registri sensor jaringan menggunakan dictionary dan set.',
      instructions: [
        'Buat fungsi tambah_sensor() untuk menyimpan record ke dalam dictionary database.',
        'Gunakan set untuk mencatat lokasi-lokasi aktif yang telah terpasang sensor.',
        'Implementasikan pencarian sensor berdasarkan ID dengan penanganan kasus kunci tidak ditemukan.',
      ],
      rubric: [
        { criteria: 'Struktur Data Dictionary & Set', weight: 40, description: 'Pengorganisasian data yang tepat dan pemanfaatan himpunan set untuk data unik.' },
        { criteria: 'Ketahanan Program (Error Handling)', weight: 30, description: 'Pemanfaatan get() dan verifikasi kunci sebelum akses.' },
        { criteria: 'Format Output & Dokumentasi', weight: 30, description: 'Docstring fungsi lengkap dan pesan log yang informatif.' },
      ],
      starterCode: `# Template Starter Code - Chapter 09\ndef tambah_sensor(registry: dict, id_sensor: str, lokasi: str, rsrp: float) -> bool:\n    """Mendaftarkan sensor baru ke registry."""\n    pass`,
      starterFilename: 'tugas_09.py',
      downloadMdUrl: 'downloads/chapter-09/tugas.md',
      downloadPyUrl: 'downloads/chapter-09/contoh.py',
    },
  },
  {
    id: 10,
    slug: '10-functions-scope',
    levelId: 1,
    number: '10',
    title: 'Functions & Scope',
    subtitle: 'Modularitas Kode, Parameter, Return & Ruang Lingkup',
    description:
      'Merancang fungsi reusable dengan def, argumen posisi & default, perbedaan fundamental print vs return, serta isolasi variabel lokal vs global (LEGB rule).',
    competencyFocus: 'PCEP 4.3: Deklarasi fungsi, parameter, return, scope',
    estimatedHours: 5,
    difficulty: 'Beginner',
    available: true,
    prerequisites: ['Chapter 08', 'Chapter 09'],
    learningObjectives: [
      'Mendeklarasikan fungsi dengan parameter wajib dan argumen nilai default',
      'Membedakan secara tegas mekanisme cetak layar (print) dan nilai balik pemrosesan (return)',
      'Menganalisis siklus hidup variabel lokal dan menghindari efek samping manipulasi variabel global',
    ],
    tags: ['Functions', 'Parameters', 'Return', 'Scope'],
    deckPath: '#chapter/10/slides',
    tugasPath: '#chapter/10/task',
    codeExample: {
      title: 'Anatomi Fungsi & Return Value',
      code: `# Perbedaan Nilai Balik (Return) dan Cetak Layar (Print)\ndef hitung_persegi(sisi):\n    return sisi * sisi\n\nhasil = hitung_persegi(4)\nprint(hasil + 8)  # Nilai return dapat diproses lebih lanjut!`,
      outputKey: 'p09-14',
      explanation: 'Return mengembalikan data ke pemanggil fungsi agar dapat disimpan dalam variabel atau digunakan dalam ekspresi matematika lain. Print hanya mencetak teks ke layar dan mengembalikan None.',
    },
    exercise: {
      title: 'Latihan Terarah: Perancangan Fungsi Klasifikasi Sinyal',
      instructions: [
        'Buat fungsi klasifikasi_rsrp(rsrp_dbm) yang menerima satu parameter bertipe float.',
        'Jika rsrp >= -85, kembalikan string "Sangat Baik".',
        'Jika -95 <= rsrp < -85, kembalikan "Cukup". Jika < -95, kembalikan "Buruk".',
        'Uji fungsi dengan nilai -78, -90, dan -105 lalu cetak hasil kembaliannya.',
      ],
      tips: 'Pastikan fungsi mengembalikan nilai (return) dan BUKAN langsung mencetaknya (print).',
      time: '15 menit',
    },
    quiz: {
      question: 'Apa nilai yang dikembalikan oleh fungsi Python jika fungsi tersebut tidak memiliki pernyataan return?',
      options: [
        'None',
        '0',
        'False',
        'String kosong ""',
      ],
      correctIndex: 0,
      explanation: 'Secara implisit, fungsi Python tanpa pernyataan return selalu mengembalikan nilai NoneType yaitu None.',
      hint: 'Lihat apa yang dihasilkan jika Anda mencetak hasil pemanggilan fungsi yang hanya berisi perintah print().',
    },
    assignment: {
      title: 'Tugas Praktik 10: Perancangan Pustaka Fungsi Analitik',
      description: 'Rancang modul fungsi yang menerapkan aturan scope LEGB, parameter nilai default, dan return teruji.',
      instructions: [
        'Rancang fungsi konversi suhu Celsius ke Fahrenheit dan sebaliknya.',
        'Rancang fungsi evaluasi kualitas sinyal telekomunikasi dengan batas ambang default.',
        'Pastikan variabel di dalam fungsi tidak mencemari ruang lingkup global.',
      ],
      rubric: [
        { criteria: 'Perancangan Parameter & Return Value', weight: 40, description: 'Fungsi bersifat murni (pure function) dan mengembalikan tipe data yang tepat.' },
        { criteria: 'Isolasi Scope Variabel', weight: 30, description: 'Tidak terjadi mutasi variabel global di luar kebutuhan modul.' },
        { criteria: 'Kualitas Docstring & Type Hints', weight: 30, description: 'Menyertakan type hints dan docstring sesuai standar PEP 257.' },
      ],
      starterCode: `# Template Starter Code - Chapter 10\ndef konversi_suhu(celsius: float) -> float:\n    """Mengonversi nilai suhu dari Celsius ke Fahrenheit.\n    \n    Args:\n        celsius (float): Derajat suhu dalam Celsius.\n    Returns:\n        float: Derajat suhu dalam Fahrenheit.\n    """\n    return (celsius * 9 / 5) + 32`,
      starterFilename: 'tugas_10.py',
      downloadMdUrl: 'downloads/chapter-10/tugas.md',
      downloadPyUrl: 'downloads/chapter-10/contoh.py',
    },
  },
  {
    id: 11,
    slug: '11-modules-basic-exceptions',
    levelId: 1,
    number: '11',
    title: 'Modules & Basic Exceptions',
    subtitle: 'Organisasi Berkas, Standard Library, Docstring & try/except',
    description:
      'Membuat modul mandiri (.py), impor fungsi, proteksi __name__ == "__main__", dokumentasi standar PEP 257 (docstrings), dan penanganan error dasar.',
    competencyFocus: 'PCEP 4.4: Modul, namespaces, docstring, exception dasar',
    estimatedHours: 4,
    difficulty: 'Beginner',
    available: true,
    prerequisites: ['Chapter 10'],
    learningObjectives: [
      'Membuat modul buatan sendiri dan mengimpor fungsi spesifik tanpa polusi namespace',
      'Menulis docstring yang rapi dan informatif yang terbaca melalui fungsi help()',
      'Menggunakan pola if __name__ == "__main__": untuk pemisahan runnable demo dan modul impor',
      'Menangani ValueError dan ZeroDivisionError menggunakan blok try-except dasar',
    ],
    tags: ['Modules', 'Docstrings', 'Import', 'Exception Basics'],
    deckPath: '#chapter/11/slides',
    tugasPath: '#chapter/11/task',
    codeExample: {
      title: 'Ekstraksi Docstring Standar PEP 257',
      code: `# Ekstraksi Docstring Standar PEP 257\ndef konversi_c_ke_f(celsius):\n    """Konversi suhu dari Celsius ke Fahrenheit.\n\n    Args:\n        celsius (float): Suhu dalam Celsius.\n    Returns:\n        float: Suhu dalam Fahrenheit.\n    """\n    return celsius * 9 / 5 + 32\n\nprint(konversi_c_ke_f.__doc__)`,
      outputKey: 'p09-13',
      explanation: 'Docstring ditulis tepat di bawah header fungsi menggunakan triple quotes ("""). Atribut __doc__ atau fungsi help() dapat membacanya secara otomatis untuk dokumentasi interaktif.',
    },
    exercise: {
      title: 'Latihan Terarah: Pembuatan Modul Mandiri & Proteksi Main',
      instructions: [
        'Buat berkas modul matematika sederhana dengan nama math_util.py.',
        'Definisikan fungsi hitung_rata_rata(data) lengkap dengan docstring.',
        'Gunakan blok if __name__ == "__main__": untuk menjalankan kasus uji mandiri.',
      ],
      tips: 'Blok __name__ == "__main__" memastikan kode pengujian hanya dijalankan saat berkas dieksekusi langsung, bukan saat diimpor oleh modul lain.',
      time: '20 menit',
    },
    quiz: {
      question: 'Kapan blok kondisi if __name__ == "__main__": akan bernilai True?',
      options: [
        'Hanya ketika skrip dieksekusi secara langsung melalui terminal/command line',
        'Ketika skrip diimpor ke dalam berkas Python lain menggunakan kata kunci import',
        'Setiap kali fungsi di dalam berkas dipanggil oleh pengguna',
        'Hanya jika nama berkas berakhiran dengan _main.py',
      ],
      correctIndex: 0,
      explanation: 'Saat Python menjalankan berkas secara langsung, variabel khusus __name__ secara otomatis disetel ke string "__main__". Jika berkas diimpor sebagai modul, __name__ akan berisi nama berkas modul tersebut.',
      hint: 'Pikirkan mekanisme Python dalam membedakan skrip runnable dengan modul pustaka.',
    },
    assignment: {
      title: 'Tugas Praktik 11: Paket Modul Reusable Telekomunikasi',
      description: 'Bangun struktur modul Python modular yang memisahkan logika komputasi dengan antarmuka CLI pengguna.',
      instructions: [
        'Buat modul terpisah pengolah sinyal (signal_proc.py).',
        'Buat skrip utama (main.py) yang mengimpor fungsi dari modul pengolah sinyal.',
        'Tangani kemungkinan ValueError jika input data bukan numerik.',
      ],
      rubric: [
        { criteria: 'Modularitas & Pemisahan Tanggung Jawab', weight: 40, description: 'Pemisahan kode modul dan runnable runner yang terorganisir rapi.' },
        { criteria: 'Penerapan Docstring & Guard __name__', weight: 30, description: 'Docstring lengkap dan perlindungan impor modul yang tepat.' },
        { criteria: 'Penanganan Exception Dasar (try/except)', weight: 30, description: 'Menangani input tidak valid tanpa menyebabkan sistem crash.' },
      ],
      starterCode: `# Template Starter Code - Chapter 11\n# signal_proc.py\ndef filter_sinyal(samples: list[float], threshold: float) -> list[float]:\n    """Menyaring sampel sinyal di atas nilai ambang batas."""\n    pass`,
      starterFilename: 'tugas_11.py',
      downloadMdUrl: 'downloads/chapter-11/tugas.md',
      downloadPyUrl: 'downloads/chapter-11/contoh.py',
    },
  },
  {
    id: 12,
    slug: '12-foundations-capstone',
    levelId: 1,
    levelCategory: 'foundations',
    number: '12',
    title: 'Foundations Capstone Project',
    subtitle: 'Student Data Management System (CLI)',
    description:
      'Proyek integratif akhir Level 1: membangun aplikasi CLI modular Sistem Manajemen Data Mahasiswa yang menerapkan operasi CRUD, pencarian linier, validasi masukan kokoh, dan analisis statistik.',
    competencyFocus: 'PCEP Capstone: Integrasi Fondasi Prosedural & Modular',
    estimatedHours: 6,
    difficulty: 'Intermediate',
    available: true,
    prerequisites: ['Chapter 01 – 11'],
    learningObjectives: [
      'Mengintegrasikan seluruh konsep dasar Python (variabel, logika bercabang, loop, struktur data, fungsi)',
      'Merancang arsitektur aplikasi multi-berkas dengan pemisahan tanggung jawab (validators, manager, UI)',
      'Mengimplementasikan operasi CRUD data in-memory dan algoritma pencarian multi-kriteria',
      'Membangun sistem validasi masukan yang andal dan aman dari runtime errors',
      'Menyajikan laporan statistik akademik dan format tabel konsol yang rapi',
    ],
    tags: ['Capstone', 'CLI Application', 'CRUD', 'Data Management', 'Modular Architecture'],
    deckPath: 'content/foundations/chapter-12/slides/deck.json',
    tugasPath: 'content/foundations/chapter-12/assignments/tugas.md',
    resources: {
      hasSlides: true,
      slidesDeck: 'slides/deck.json',
      starterCode: 'code/contoh.py',
      assignmentGuide: 'assignments/tugas.md',
    },
    codeExample: {
      title: 'Model Data Mahasiswa In-Memory & Operasi Dasar',
      code: `# Inisialisasi basis data mahasiswa in-memory (list of dicts)
mahasiswa = [
    {"nim": "121140001", "name": "Budi Santoso", "grade": 86.50},
    {"nim": "121140002", "name": "Siti Nurhaliza", "grade": 92.00},
    {"nim": "121140003", "name": "Ahmad Fauzi", "grade": 74.25},
]

print(f"Total mahasiswa terdaftar: {len(mahasiswa)}")
for mhs in mahasiswa:
    print(f"- NIM: {mhs['nim']} | Nama: {mhs['name']:<18} | Nilai: {mhs['grade']}")`,
      outputKey: 'ch12-01',
      explanation:
        'Struktur data list of dictionaries merepresentasikan basis data in-memory di mana setiap baris rekaman adalah dictionary dengan atribut nim, name, dan grade.',
    },
    exercise: {
      title: 'Latihan Terarah: Tantangan Ekstensi Capstone',
      instructions: [
        'Implementasikan fungsi pengurutan multi-kriteria (berdasarkan ranking nilai, abjad nama, atau urutan NIM).',
        'Bangun fungsi pemfilteran mahasiswa lulus berdasarkan ambang batas kelulusan (>= 70.0).',
        'Hitung distribusi frekuensi kategori predikat huruf (A, B, C, D, E) dan persentasenya.',
      ],
      tips: 'Gunakan parameter reverse=True pada fungsi sorted() untuk menghasilkan urutan ranking menurun.',
      time: '45 menit',
    },
    quiz: {
      question: 'Mengapa NIM mahasiswa harus disimpan sebagai string dan bukan bilangan bulat (integer)?',
      options: [
        'Agar dapat menyimpan angka nol di awal (leading zeros) dan mendukung validasi panjang karakter secara eksak',
        'Karena tipe data integer mengonsumsi memori lebih besar daripada string',
        'Karena list Python tidak mengizinkan integer di dalam dictionary',
        'Agar operasi penjumlahan aritmatika dapat langsung dilakukan pada NIM',
      ],
      correctIndex: 0,
      explanation:
        'NIM adalah data pengenal (identitas) kategoris, bukan besaran kuantitatif untuk perhitungan matematika. Menyimpannya sebagai string mempertahankan angka nol di awal (misal: "01234") dan memudahkan pengujian karakter numerik serta panjang digit.',
      hint: 'Pikirkan apa yang terjadi jika mahasiswa memiliki NIM dengan awalan angka 0 seperti "0112345".',
    },
    assignment: {
      title: 'Proyek Akhir: Student Data Management System',
      description:
        'Rancang dan bangun aplikasi CLI modular Sistem Manajemen Data Mahasiswa dengan 10 fitur lengkap mencakup CRUD, pencarian, validasi masukan, analisis statistik, dan pengujian unit.',
      instructions: [
        'Pisahkan arsitektur kode menjadi 3 modul utama: validators.py, student_manager.py, dan main.py.',
        'Terapkan validasi ketat untuk keunikan NIM, format nama, serta rentang nilai 0.0 - 100.0.',
        'Sajikan seluruh data dalam tabel konsol yang rapi dengan format dua digit desimal dan predikat huruf.',
        'Sertakan perhitungan rata-rata, nilai tertinggi/terendah, dan identifikasi mahasiswa berprestasi.',
      ],
      rubric: [
        { criteria: 'Arsitektur Modular & Desain Sistem', weight: 15, description: 'Kode terpisah secara modular, logika bisnis terisolasi dari I/O konsol.' },
        { criteria: 'Logika CRUD & Pencarian Multi-Kriteria', weight: 25, description: 'Fungsi tambah, lihat, cari, perbarui, dan hapus berjalan lancar tanpa bug.' },
        { criteria: 'Validasi Masukan & Ketahanan Sistem', weight: 20, description: 'Pencegahan duplikasi NIM, validasi tipe nilai 0-100, dan penanganan error.' },
        { criteria: 'Analisis Statistik & Fitur Analitik', weight: 20, description: 'Perhitungan rerata, nilai ekstrem, dan predikat huruf akurat.' },
        { criteria: 'Kerapian Kode, Type Hints & Format CLI', weight: 20, description: 'Sesuai konvensi PEP 8, type hints lengkap, docstring jelas, dan format tabel konsol rapi.' },
      ],
      starterCode: `# Template Starter Code - Chapter 12: Foundations Capstone
from typing import Any

def add_student(students: list[dict[str, Any]], nim: str, name: str, grade: Any) -> tuple[bool, str]:
    """Menambahkan mahasiswa baru ke basis data."""
    pass

def calculate_statistics(students: list[dict[str, Any]]) -> dict[str, Any]:
    """Menghitung ringkasan statistik nilai."""
    pass
`,
      starterFilename: 'tugas_12.py',
      downloadMdUrl: 'downloads/chapter-12/tugas.md',
      downloadPyUrl: 'downloads/chapter-12/contoh.py',
    },
  },

  // LEVEL 2 (13 - 22)
  {
    id: 13,
    slug: '13-advanced-functions',
    levelId: 2,
    number: '13',
    title: 'Advanced Functions',
    subtitle: '*args, **kwargs, Lambda, First-Class Citizens & Closures',
    description:
      'Menerapkan fungsi fleksibel dengan arbitrary arguments (*args, **kwargs), fungsi anonim lambda, fungsi sebagai argumen (higher-order), closures, dan rekursi.',
    competencyFocus: 'PCAP 1.1: Pemrograman fungsional & argument unpacking',
    estimatedHours: 4,
    difficulty: 'Intermediate',
    available: true,
    prerequisites: ['Level 1'],
    learningObjectives: [
      'Menerapkan arbitrary arguments dengan *args dan arbitrary keyword arguments dengan **kwargs',
      'Menggunakan pembatas sintaksis positional-only (/) dan keyword-only (*)',
      'Menghindari jebakan mutable default arguments menggunakan idiom sentinel None',
      'Menerapkan ekspresi lambda untuk fungsi satu baris dan custom key sorting',
      'Membangun fungsi closure untuk enkapsulasi state fungsional dan rekursi',
    ],
    tags: ['*args', '**kwargs', 'Lambda', 'Closures', 'Higher-Order Functions', 'Recursion'],
    deckPath: '#chapter/13/slides',
    tugasPath: '#chapter/13/task',
    codeExample: {
      title: 'Positional-Only, Keyword-Only, dan Parameter Default',
      code: `# Konfigurasi parameter dengan pembatas / dan *\ndef konfigurasi_node(node_id: int, /, frekuensi_mhz: float, *, mode: str = "AUTO") -> str:\n    return f"Node #{node_id} @ {frekuensi_mhz:.1f} MHz [Mode: {mode}]"\n\nprint(konfigurasi_node(101, 2412.0, mode="MANUAL"))\nprint(konfigurasi_node(102, frekuensi_mhz=5180.0))`,
      outputKey: 'ch13-01',
      explanation:
        'Sintaksis / memastikan parameter sebelah kiri hanya dapat diisi secara posisi, sedangkan * memastikan parameter sebelah kanan wajib diisi sebagai argumen kata kunci (keyword-only).',
    },
    exercise: {
      title: 'Latihan Terarah: Dynamic Function Design & Closures',
      instructions: [
        'Rancang fungsi akumulator metrik sinyal berbasis *args.',
        'Urutkan daftar paket jaringan berdasarkan prioritas dan latensi menggunakan lambda.',
        'Bangun generator fungsi penguji tegangan nominal berbasis closure.',
        'Buat fungsi rekursif penelusuran kedalaman topologi pohon jaringan.',
      ],
      tips: 'Gunakan kata kunci nonlocal pada fungsi bersarang ketika ingin memodifikasi variabel di enclosing scope.',
      time: '30 menit',
    },
    quiz: {
      question:
        "Mengapa deklarasi fungsi 'def simpan_log(pesan, riwayat=[])' dianggap sebagai praktik buruk di Python?",
      options: [
        'Objek list default dievaluasi sekali saat fungsi didefinisikan dan dibagi antar pemanggilan berikutnya',
        'Python tidak mengizinkan tanda kurung siku di dalam tanda kurung fungsi',
        'Parameter riwayat akan otomatis berubah tipe menjadi tuple',
        'Fungsi tersebut akan menimbulkan SyntaxError saat dijalankan',
      ],
      correctIndex: 0,
      explanation:
        'Nilai default dievaluasi satu kali pada saat definisi fungsi (definition-time). Jika objek default bersifat mutable (seperti list atau dict), mutasi pada pemanggilan pertama akan terbawa ke pemanggilan berikutnya. Gunakan sentinel None sebagai gantinya.',
      hint: 'Ingat perbedaan waktu evaluasi antara saat fungsi didefinisikan dan saat fungsi dipanggil.',
    },
    assignment: {
      title: 'Tugas Praktik 13: Flexible Telemetry Pipeline Engine',
      description:
        'Rancang arsitektur mesin pemroses data telemetri yang mengintegrasikan higher-order pipeline chaining, predicate filter closures, serta dynamic aggregators berbasis *args dan **kwargs.',
      instructions: [
        'Implementasikan fungsi closure pembuat filter ambang batas (buat_filter_rentang).',
        'Implementasikan fungsi higher-order eksekusi rantai transformasi (jalankan_pipeline).',
        'Implementasikan fungsi agregator dinamis dengan parameter positional-only dan **kwargs.',
        'Hindari penggunaan mutable default arguments dan gunakan sentinel None.',
      ],
      rubric: [
        { criteria: 'Desain Higher-Order & Pipeline Chaining', weight: 30, description: 'Fungsi pipeline mengeksekusi transformasi data berantai secara presisi.' },
        { criteria: 'Implementasi Closure & Lexical Scope', weight: 25, description: 'Closure mempertahankan state ambang batas secara independen.' },
        { criteria: 'Pemanfaatan *args, **kwargs & Parameter Constraints', weight: 25, description: 'Menerapkan pembatas / dan * serta unpacking secara tepat.' },
        { criteria: 'Kebersihan Kode, Type Hints & Sentinel None', weight: 20, description: 'Kode bersih, type hints lengkap, dan tidak ada mutable default bug.' },
      ],
      starterFilename: 'tugas_13.py',
      downloadMdUrl: 'downloads/chapter-13/tugas.md',
      downloadPyUrl: 'downloads/chapter-13/contoh.py',
    },
  },
  {
    id: 14,
    slug: '14-comprehensions-iterators',
    levelId: 2,
    number: '14',
    title: 'Comprehensions & Iterators',
    subtitle: 'List, Dict, Set Comprehensions & Generator Expressions',
    description:
      'Menulis transformasi data yang elegan dan ekspresif dengan list comprehension, dict/set comprehension, serta menghemat memori dengan generator expression.',
    competencyFocus: 'PCAP 1.2: Comprehensions dan protokol iterasi',
    estimatedHours: 4,
    difficulty: 'Intermediate',
    available: true,
    prerequisites: ['Chapter 08', 'Chapter 09'],
    learningObjectives: [
      'Menulis list comprehension dengan klausa filter kondisi if secara idiomatis',
      'Membangun dictionary comprehension dan set comprehension untuk transformasi data tabular',
      'Memahami protokol iterator dan perbandingan memori list vs generator expression',
      'Menerapkan enumerate() dan zip() untuk manipulasi data multi-koleksi paralel',
      'Meratakan matriks bersarang 2D menggunakan nested comprehension',
    ],
    tags: ['Comprehension', 'Generators', 'Iterators', 'Filtering', 'Lazy Evaluation'],
    deckPath: '#chapter/14/slides',
    tugasPath: '#chapter/14/task',
    codeExample: {
      title: 'List Comprehension Dasar dan Pemfilteran Kondisional',
      code: `# Transformasi dan pemfilteran sinyal daya\nsinyal_dbm = [-115.0, -98.2, -84.0, -70.5, -62.0]\ndaya_mw = [round(10 ** (p / 10), 6) for p in sinyal_dbm]\nsinyal_kuat = [s for s in sinyal_dbm if s >= -90.0]\n\nprint("Daya (mW)  :", daya_mw)\nprint("Sinyal Kuat:", sinyal_kuat)`,
      outputKey: 'ch14-01',
      explanation:
        'List comprehension memadukan perulangan for dan filter if dalam satu ekspresi ringkas untuk menghasilkan koleksi data baru secara deklaratif.',
    },
    exercise: {
      title: 'Latihan Terarah: Transformasi Koleksi Ekspresif',
      instructions: [
        'Ekstraksi log SNR menggunakan list comprehension dengan ternary if-else.',
        'Lakukan inversi dictionary node IP ke hostname dengan filter nama akses.',
        'Gabungkan aliran data sensor paralel menggunakan zip() dan enumerate().',
        'Bangun generator deret bilangan prima untuk streaming evaluasi lazy.',
      ],
      tips: 'Gunakan kurung siku [] untuk list comprehension (eager) dan kurung biasa () untuk generator expression (lazy).',
      time: '30 menit',
    },
    quiz: {
      question:
        'Apakah perbedaan mendasar antara list comprehension [x for x in data] dan generator expression (x for x in data)?',
      options: [
        'List comprehension mengevaluasi seluruh data ke memori RAM seketika (eager), sedangkan generator expression mengevaluasi data satu per satu saat diminta (lazy)',
        'List comprehension hanya mendukung bilangan bulat, sedangkan generator expression mendukung semua tipe data',
        'Generator expression menghasilkan objek bertipe tuple, sedangkan list comprehension bertipe list',
        'Generator expression lebih lambat dan mengonsumsi memori lebih besar daripada list comprehension',
      ],
      correctIndex: 0,
      explanation:
        'List comprehension bersifat eager dan mengalokasikan seluruh elemen di RAM sekaligus, sedangkan generator expression bersifat lazy yang menghemat memori karena nilai hanya dihitung saat metode next() dipanggil.',
      hint: 'Ingat perbandingan ukuran memori menggunakan sys.getsizeof() pada dataset besar.',
    },
    assignment: {
      title: 'Tugas Praktik 14: Dataset Transformation Toolkit',
      description:
        'Rancang pustaka utilitas pemrosesan data telemetri yang mengintegrasikan list comprehension, dict comprehension, set comprehension, nested matrix flattening, dan memory-safe generator expressions.',
      instructions: [
        'Implementasikan pemfilteran dan penskalaan daya menggunakan list comprehension.',
        'Implementasikan pembuatan peta indeks IP ke nama host menggunakan dict comprehension.',
        'Ekstrak himpunan zona unik yang telah dinormalisasi menggunakan set comprehension.',
        'Ratakan matriks 2D menjadi 1D menggunakan nested comprehension dan bangun generator stream.',
      ],
      rubric: [
        { criteria: 'Penguasaan List & Nested Comprehensions', weight: 25, description: 'Menerapkan list comprehension dan nested flattening secara presisi tanpa loop imperatif manual.' },
        { criteria: 'Penguasaan Dict & Set Comprehensions', weight: 25, description: 'Mampu menginversi dan membangun mapping dictionary serta deduplikasi set unik secara bersih.' },
        { criteria: 'Protokol Iterator & Generator Expression', weight: 25, description: 'Menerapkan generator expression bertipe lazy, memahami interaksi iter(), next(), dan efisiensi memori.' },
        { criteria: 'Pemanfaatan Enumerate, Zip & Standar PEP 8', weight: 25, description: 'Menggunakan enumerate() dan zip() secara idiomatis, kode memiliki type hints lengkap, dan format rapi.' },
      ],
      starterFilename: 'tugas_14.py',
      downloadMdUrl: 'downloads/chapter-14/tugas.md',
      downloadPyUrl: 'downloads/chapter-14/contoh.py',
    },
  },
  {
    id: 15,
    slug: '15-searching-sorting-algorithms',
    levelId: 2,
    number: '15',
    title: 'Searching & Sorting Algorithms',
    subtitle: 'Linear Search, Binary Search, Selection Sort & Timsort (sorted)',
    description:
      'Studi algoritma klasik: linear search O(n), binary search O(log n), bubble sort, selection sort, insertion sort O(n²), serta pemanfaatan sorted() dengan custom key lambda.',
    competencyFocus: 'PCAP 1.3: Algoritma pencarian dan pengurutan terapan',
    estimatedHours: 5,
    difficulty: 'Intermediate',
    available: true,
    prerequisites: ['Chapter 08', 'Chapter 14'],
    learningObjectives: [
      'Mengimplementasikan linear search pada data tidak terurut dengan penanganan kasus None',
      'Mengimplementasikan binary search O(log n) dengan prasyarat data terurut',
      'Memahami mekanisme pertukaran data pada Bubble Sort, Selection Sort, dan Insertion Sort',
      'Mengurutkan data dictionary kompleks menggunakan sorted(data, key=lambda x: ...)',
      'Menganalisis konsep pengurutan stabil (stable sort) dan efisiensi algoritma Timsort',
    ],
    tags: ['Algorithms', 'Linear Search', 'Binary Search', 'Selection Sort', 'Bubble Sort', 'Insertion Sort', 'Timsort'],
    deckPath: '#chapter/15/slides',
    tugasPath: '#chapter/15/task',
    codeExample: {
      title: 'Pencarian Biner (Binary Search) O(log n)',
      code: `# Pencarian biner pada deret frekuensi terurut\nfrekuensi = [100, 250, 450, 800, 900, 1800, 2100, 2600, 3500]\nkiri, kanan = 0, len(frekuensi) - 1\ntarget = 2100\nindeks = None\n\nwhile kiri <= kanan:\n    tengah = (kiri + kanan) // 2\n    if frekuensi[tengah] == target:\n        indeks = tengah\n        break\n    elif frekuensi[tengah] < target:\n        kiri = tengah + 1\n    else:\n        kanan = tengah - 1\n\nprint(f"Target {target} ditemukan pada indeks ke-{indeks}")`,
      outputKey: 'ch15-02',
      explanation:
        'Binary search membagi ruang pencarian menjadi setengah pada setiap langkah perbandingan, menghasilkan kompleksitas waktu O(log n) dengan syarat data telah terurut.',
    },
    exercise: {
      title: 'Latihan Terarah: Eksplorasi Algoritma Pencarian & Pengurutan',
      instructions: [
        'Modifikasi binary search untuk mencari elemen pertama yang melampaui ambang batas (lower bound).',
        'Urutkan antrean tugas transmisi berdasarkan prioritas dengan prinsip stable sort.',
        'Hitung total operasi swap pada Bubble Sort untuk data acak vs data terbalik.',
        'Implementasikan fungsi penyisipan terurut (streaming insertion) pada data terurut.',
      ],
      tips: 'Binary search hanya valid jika koleksi data telah diurutkan terlebih dahulu.',
      time: '40 menit',
    },
    quiz: {
      question:
        "Mengapa fungsi bawaan Python 'sorted()' umumnya jauh lebih disukai daripada implementasi Bubble Sort atau Selection Sort buatan sendiri?",
      options: [
        'sorted() menggunakan Timsort hibrida berkecepatan O(n log n) yang ditulis dalam bahasa C dan terbukti stabil serta adaptif',
        'Karena fungsi sorted() tidak mengonsumsi memori sama sekali (0 byte)',
        'Karena Python melarang penulisan algoritma sorting manual',
        'Karena Bubble Sort tidak dapat mengurutkan bilangan bernilai negatif',
      ],
      correctIndex: 0,
      explanation:
        'Fungsi bawaan Python sorted() mengimplementasikan algoritma Timsort (kombinasi Merge Sort dan Insertion Sort) yang diimplementasikan dalam C murni. Timsort memiliki performa kasus terburuk O(n log n) yang jauh lebih cepat daripada algoritma kuadratik O(n²), adaptif terhadap pola data yang sudah hampir terurut, dan menjamin kestabilan (stable sort).',
      hint: 'Pikirkan perbedaan kompleksitas waktu antara O(n log n) dan O(n²) serta bahasa implementasi internal CPython.',
    },
    assignment: {
      title: 'Tugas Praktik 15: Network Metric Search & Ranking Engine',
      description:
        'Rancang mesin pencarian dan pemeringkatan metrik jaringan telekomunikasi yang memadukan linear search, binary search, tiga algoritma sorting klasik manual (Bubble, Selection, Insertion), dan pemeringkatan multi-kriteria berbasis Timsort.',
      instructions: [
        'Implementasikan fungsi linear search untuk pencarian ID node dan binary search untuk kanal frekuensi.',
        'Implementasikan tiga algoritma pengurutan manual murni (Bubble, Selection, dan Insertion Sort).',
        'Implementasikan pemeringkatan performa multi-kriteria BTS (latensi terendah dan RSRP terkuat) menggunakan sorted().',
        'Pastikan kode menangani kasus batas: list kosong, satu elemen, duplikat, dan angka negatif.',
      ],
      rubric: [
        { criteria: 'Kebenaran Linear & Binary Search', weight: 25, description: 'Pencarian akurat, menghormati prasyarat list terurut, dan menangani target nihil.' },
        { criteria: 'Implementasi Bubble & Selection Sort', weight: 25, description: 'Bubble Sort (dengan deteksi early stop) dan Selection Sort manual berjalan lancar.' },
        { criteria: 'Implementasi Insertion Sort & Stabilitas', weight: 25, description: 'Insertion Sort menggeser prefix dengan tepat dan memahami konsep pengurutan stabil.' },
        { criteria: 'Pemeringkatan Multi-Kriteria Timsort & Edge Cases', weight: 25, description: 'Custom lambda key multi-atribut, penanganan kasus batas (kosong/duplikat), dan format rapi.' },
      ],
      starterFilename: 'tugas_15.py',
      downloadMdUrl: 'downloads/chapter-15/tugas.md',
      downloadPyUrl: 'downloads/chapter-15/contoh.py',
    },
  },
  {
    id: 16,
    slug: '16-algorithm-analysis-problem-solving',
    levelId: 2,
    number: '16',
    title: 'Algorithm Analysis & Problem Solving',
    subtitle: 'Notasi Big-O, Space-Time Tradeoffs & Strategi Algoritmik',
    description:
      'Menganalisis efisiensi algoritma secara formal: notasi O(1), O(log n), O(n), O(n log n), O(n²), memory footprint, benchmarking time.perf_counter(), dan teknik dekomposisi pemecahan masalah.',
    competencyFocus: 'PCAP 1.4: Kompleksitas komputasi & optimasi',
    estimatedHours: 5,
    difficulty: 'Intermediate',
    available: true,
    prerequisites: ['Chapter 15'],
    learningObjectives: [
      'Menganalisis kompleksitas waktu asimtotik algoritma menggunakan notasi Big-O',
      'Membedakan skenario analisis performa: Best-Case, Average-Case, dan Worst-Case',
      'Mengukur konsumsi memori dan menganalisis space-time tradeoffs',
      'Melakukan benchmarking empiris presisi tinggi dengan modul time.perf_counter()',
      'Menerapkan strategi pemecahan masalah terstruktur dan optimasi bottleneck komputasi',
    ],
    tags: ['Big-O', 'Complexity Analysis', 'Space-Time Tradeoffs', 'Benchmarking', 'Performance Optimization', 'Problem Solving'],
    deckPath: '#chapter/16/slides',
    tugasPath: '#chapter/16/task',
    codeExample: {
      title: 'Benchmarking Operasi O(1) vs O(n)',
      code: `import time\n\nN = 100_000\ndaftar_elemen = list(range(N))\nhimpunan_elemen = set(range(N))\ntarget = N - 1\n\nt0 = time.perf_counter()\nada_di_list = target in daftar_elemen\nwaktu_list = (time.perf_counter() - t0) * 1000\n\nt0 = time.perf_counter()\nada_di_set = target in himpunan_elemen\nwaktu_set = (time.perf_counter() - t0) * 1000\n\nprint(f"List O(n): {waktu_list:.4f} ms | Set O(1): {waktu_set:.4f} ms")`,
      outputKey: 'ch16-01',
      explanation:
        'Pencarian keanggotaan pada list membutuhkan pemindaian berurutan O(n), sedangkan hash set melakukan kalkulasi hash tabel dengan kompleksitas rata-rata O(1).',
    },
    exercise: {
      title: 'Latihan Terarah: Analisis & Optimasi Algoritmik',
      instructions: [
        'Lakukan profiling perbandingan waktu iterasi list vs generator untuk 1.000.000 angka.',
        'Optimalkan fungsi pencarian pasangan angka yang menjumlahkan target S dari O(n²) menjadi O(n).',
        'Analisis konsumsi memori tumpukan rekursi pada fungsi faktorial vs pendekatan iteratif.',
        'Ukur kestabilan durasi eksekusi dengan variasi 10 kali run menggunakan time.perf_counter().',
      ],
      tips: 'Selalu sertakan warm-up run dan hitung rata-rata durasi agar hasil benchmarking tidak terdistorsi oleh aktivitas background OS.',
      time: '40 menit',
    },
    quiz: {
      question:
        'Sebuah fungsi memproses list berukuran n dengan loop bersarang ganda (nested loop) di mana kedua loop beriterasi dari 0 hingga n. Berapakah kompleksitas waktu fungsi tersebut?',
      options: ['O(n²)', 'O(n log n)', 'O(2n)', 'O(n)'],
      correctIndex: 0,
      explanation:
        'Ketika loop luar beriterasi n kali dan untuk setiap iterasinya loop dalam juga berjalan n kali, total operasi dasar yang dieksekusi adalah n * n = n², sehingga kompleksitas waktunya adalah kuadratik atau O(n²).',
      hint: 'Kalikan jumlah iterasi loop luar dengan jumlah iterasi loop dalam.',
    },
    assignment: {
      title: 'Tugas Praktik 16: Telemetry Processing Benchmark & Optimization Suite',
      description:
        'Rancang perangkat lunak analisis performa algoritma telekomunikasi yang membandingkan kompleksitas waktu dan ruang berbagai metode deduplikasi sinyal, lookup gateway, serta deteksi anomali transmisi.',
      instructions: [
        'Implementasikan fungsi deduplikasi kuadratik O(n²) dan bandingkan dengan deduplikasi O(n) berbasis set.',
        'Lakukan pengukuran empiris presisi tinggi pada berbagai skala masukan (n = 100, 1.000, 10.000).',
        'Bandingkan waktu pencarian linear search vs dictionary lookup pada dataset sinyal telekomunikasi.',
        'Format laporan benchmarking dalam tabel terstruktur lengkap dengan rasio akselerasi (speedup factor).',
      ],
      rubric: [
        { criteria: 'Ketepatan Analisis Teoretis & Kompleksitas', weight: 25, description: 'Karakterisasi notasi Big-O untuk tiap fungsi akurat dan sesuai kaidah asimtotik.' },
        { criteria: 'Implementasi Optimasi O(n²) ke O(n)', weight: 25, description: 'Solusi optimal memanfaatkan space-time tradeoff (set/dict) dengan hasil output identik.' },
        { criteria: 'Metodologi Benchmarking Presisi Tinggi', weight: 25, description: 'Penggunaan time.perf_counter() dengan warm-up, multi-iterasi, dan perhitungan rata-rata/min yang valid.' },
        { criteria: 'Kualitas Pelaporan & Penanganan Edge Cases', weight: 25, description: 'Tabel laporan perbandingan performa rapi serta penanganan dataset kosong dan elemen duplikat.' },
      ],
      starterFilename: 'tugas_16.py',
      downloadMdUrl: 'downloads/chapter-16/tugas.md',
      downloadPyUrl: 'downloads/chapter-16/contoh.py',
    },
  },
  {
    id: 17,
    slug: '17-file-handling-serialization',
    levelId: 2,
    number: '17',
    title: 'File Handling & Data Serialization',
    subtitle: 'Context Manager (with), CSV, JSON & Text Processing',
    description:
      'Membaca dan menulis file lokal dengan aman menggunakan context manager (with open), parsing format CSV terstruktur, serialisasi JSON, dan manajemen path modern (pathlib).',
    competencyFocus: 'PCAP 2.1: File I/O stream dan format data',
    estimatedHours: 5,
    difficulty: 'Intermediate',
    available: true,
    prerequisites: ['Chapter 11'],
    learningObjectives: [
      'Mengelola file descriptor secara aman tanpa resource leak menggunakan statement with',
      'Membedakan mode akses berkas (r, w, a, x) serta memastikan penggunaan encoding UTF-8',
      'Membaca dan menulis data tabel menggunakan modul bawaan csv.DictReader dan csv.DictWriter',
      'Melakukan serialisasi dan deserialisasi data menggunakan json.dump(), json.load(), json.dumps(), dan json.loads()',
      'Mengelola path direktori dan berkas lintas platform secara berorientasi objek dengan pathlib.Path',
    ],
    tags: ['Files', 'CSV', 'JSON', 'pathlib', 'Context Manager', 'Serialization', 'I/O'],
    deckPath: '#chapter/17/slides',
    tugasPath: '#chapter/17/task',
    codeExample: {
      title: 'Membaca File Teks dengan Context Manager dan UTF-8',
      code: `nama_file = "sampel_log.txt"\n\nwith open(nama_file, "w", encoding="utf-8") as f:\n    f.write("INFO: Inisialisasi node berhasil\\nWARN: Daya sinyal rendah\\n")\n\nwith open(nama_file, "r", encoding="utf-8") as file_in:\n    for nomor, baris in enumerate(file_in, 1):\n        print(f"Baris {nomor}: {baris.strip()}")`,
      outputKey: 'ch17-01',
      explanation:
        'Context manager with open(...) as f menjamin file descriptor ditutup secara otomatis setelah blok selesai dieksekusi, bahkan jika terjadi runtime exception.',
    },
    exercise: {
      title: 'Latihan Terarah: Manipulasi Berkas & Format Pertukaran Data',
      instructions: [
        'Ekstraksi baris log telekomunikasi berkategori [WARN] dan [ERROR] menggunakan filter teks.',
        'Tulis kumpulan data dictionary pemancar seluler ke berkas CSV menggunakan csv.DictWriter.',
        'Konversi rekaman sensor suhu dari format CSV ke format JSON terindentasi rapi.',
        'Buat pohon folder bertingkat dan cari seluruh berkas teks menggunakan pathlib.Path.glob().',
      ],
      tips: "Selalu sertakan parameter newline='' saat membuka file CSV di Python untuk mencegah baris kosong ganda pada sistem operasi Windows.",
      time: '40 menit',
    },
    quiz: {
      question:
        "Mengapa penggunaan context manager 'with open(...) as f' sangat direkomendasikan dibandingkan memanggil f.close() secara manual?",
      options: [
        'Karena blok with menjamin berkas otomatis ditutup seketika bahkan jika terjadi runtime exception di dalam blok',
        'Karena fungsi f.close() telah dihapus dari spesifikasi resmi Python 3',
        'Karena blok with secara otomatis mengompresi isi berkas menjadi format zip',
        'Karena statement with membuat eksekusi program menjadi 10 kali lebih cepat',
      ],
      correctIndex: 0,
      explanation:
        'Statement with mengimplementasikan protokol context manager (__enter__ dan __exit__). Metode __exit__ dipanggil secara otomatis saat keluar dari blok konteks, menjamin penutupan file descriptor dan pembebasan sumber daya sistem bahkan bila terjadi error tak terduga.',
      hint: 'Pikirkan apa yang terjadi jika ada error yang memotong alur program sebelum baris f.close() sempat dieksekusi.',
    },
    assignment: {
      title: 'Tugas Praktik 17: Telecom Gateway Data Pipeline & Serialization Suite',
      description:
        'Rancang dan bangun modul data pipeline telekomunikasi yang memproses rekaman BTS dari berkas CSV, menyaring baris anomali, melakukan pembaruan in-memory, dan mengekspor basis data terstruktur ke format JSON.',
      instructions: [
        'Implementasikan pemuatan data CSV defensif dengan penanganan FileNotFoundError.',
        'Gunakan csv.DictReader untuk memetakan kolom dan validasi tipe data numerik float.',
        'Implementasikan penambahan node baru dan pembaruan in-place berdasarkan ID.',
        'Ekspor seluruh data node ke berkas format JSON terstruktur menggunakan json.dump().',
      ],
      rubric: [
        { criteria: 'Penguasaan File I/O & Context Manager', weight: 25, description: "Menggunakan with open() secara konsisten, menyertakan encoding='utf-8', dan newline='' pada CSV." },
        { criteria: 'Parsing & Manipulasi CSV Tabular', weight: 25, description: 'Memanfaatkan csv.DictReader dan csv.DictWriter secara tepat dengan pemetaan header yang valid.' },
        { criteria: 'Serialisasi & Deserialisasi JSON', weight: 25, description: 'Mampu mengonversi data dictionary ke JSON terstruktur dengan json.dump()/json.load() secara rapi.' },
        { criteria: 'Validasi Data & Penanganan Error pathlib', weight: 25, description: 'Penanganan FileNotFoundError, validasi tipe numerik, dan integrasi modul modern pathlib.Path.' },
      ],
      starterFilename: 'tugas_17.py',
      downloadMdUrl: 'downloads/chapter-17/tugas.md',
      downloadPyUrl: 'downloads/chapter-17/contoh.py',
    },
  },
  {
    id: 18,
    slug: '18-exception-handling-debugging',
    levelId: 2,
    number: '18',
    title: 'Exception Handling & Debugging',
    subtitle: 'Custom Exceptions, Traceback Analysis, pdb & logging',
    description:
      'Menangani error secara elegan dengan try-except-else-finally, mendefinisikan custom exception, analisis traceback, debugging dengan pdb/breakpoint, dan audit operasional dengan modul logging.',
    competencyFocus: 'PCAP 2.2: Penanganan exception lanjutan dan debugging',
    estimatedHours: 5,
    difficulty: 'Intermediate',
    available: true,
    prerequisites: ['Chapter 11', 'Chapter 17'],
    learningObjectives: [
      'Membedakan secara tegas SyntaxError, Runtime Exception, dan Logical Bugs',
      'Menerapkan penanganan multi-exception secara presisi menggunakan blok try-except',
      'Mengontrol alur eksekusi pembersihan mutlak menggunakan klausa else dan finally',
      'Merancang hierarki custom exception domain dan menerapkan exception chaining (from)',
      'Melakukan debugging sistematis menggunakan assertion, breakpoint()/pdb, dan modul logging',
    ],
    tags: ['Exceptions', 'try-except', 'Debugging', 'Traceback', 'Custom Exceptions', 'Logging', 'pdb'],
    deckPath: '#chapter/18/slides',
    tugasPath: '#chapter/18/task',
    codeExample: {
      title: 'Pembagian Aman dengan try-except ZeroDivisionError',
      code: `def pembagian_aman(pembilang: float, penyebut: float) -> float | None:\n    try:\n        return pembilang / penyebut\n    except ZeroDivisionError:\n        print(f"Peringatan: Terjadi pembagian dengan nol ({pembilang} / {penyebut})!")\n        return None\n\nprint("100 / 4 =", pembagian_aman(100.0, 4.0))\nprint("45 / 0  =", pembagian_aman(45.0, 0.0))`,
      outputKey: 'ch18-01',
      explanation:
        'Blok try-except mengisolasi operasi pembagian berisiko tinggi. Jika pembagian nol terjadi, eksekusi dialihkan ke blok except tanpa merusak jalannya alur program utama.',
    },
    exercise: {
      title: 'Latihan Terarah: Pertahanan Kode & Teknik Debugging',
      instructions: [
        'Implementasikan fungsi alokasi daya per antena dengan pencegahan ZeroDivisionError.',
        'Tangani multi-exception KeyError dan ValueError saat parsing konfigurasi dictionary jaringan.',
        'Definisikan custom exception BandwidthExceededError dan picu dengan statement raise.',
        'Gantikan statement print() dengan modul logging untuk mencatat alur transmisi paket.',
      ],
      tips: 'Jangan pernah menggunakan bare except tanpa kelas exception spesifik karena akan menelan KeyboardInterrupt (Ctrl+C).',
      time: '40 menit',
    },
    quiz: {
      question:
        "Mengapa penggunaan pola 'except: pass' (bare except yang mengabaikan error secara diam-diam) dianggap sebagai salah satu anti-pattern terburuk di Python?",
      options: [
        'Karena pola tersebut menyembunyikan bug nyata dan menangkap KeyboardInterrupt sehingga program tidak bisa dihentikan dari terminal',
        'Karena interpreter Python akan otomatis menghapus file skrip yang memuat pola tersebut',
        'Karena statement pass membutuhkan konsumsi CPU 100% secara terus-menerus',
        'Karena blok except wajib mengembalikan nilai boolean True',
      ],
      correctIndex: 0,
      explanation:
        "Bare except menangkap seluruh exception termasuk BaseException (seperti KeyboardInterrupt dan SystemExit). Selain membuat program tidak bisa dihentikan via Ctrl+C, pola ini menelan bug secara diam-diam (silent failure) yang mempersulit penelusuran masalah di kemudian hari. Sesuai Zen of Python: 'Errors should never pass silently. Unless explicitly silenced.'",
      hint: 'Ingat bahwa BaseException mencakup sinyal interupsi sistem dari pengguna.',
    },
    assignment: {
      title: 'Tugas Praktik 18: Telecom Anomaly Detection & Robust Validator Suite',
      description:
        'Rancang dan bangun modul validasi telemetri jaringan yang tangguh terhadap kesalahan runtime, memanfaatkan custom exceptions, logging diagnostik, dan pelaporan metrik terperinci.',
      instructions: [
        'Rancang hierarki custom exception TelemetryValidationError, MissingPropertyError, dan ValueRangeError.',
        'Terapkan blok try-except spesifik untuk menangani konversi tipe numerik dan pengecekan batas rentang fisik.',
        'Integrasikan modul logging untuk mencatat rekaman yang valid (INFO), ditolak (WARNING), dan error kritis (ERROR).',
        'Sajikan ringkasan statistik proses validasi batch dalam bentuk dictionary informatif.',
      ],
      rubric: [
        { criteria: 'Desain Hierarki Custom Exception', weight: 25, description: 'Merancang class exception turunan yang informatif dan merepresentasikan aturan domain jaringan.' },
        { criteria: 'Presisi Penanganan try-except-else-finally', weight: 25, description: 'Menerapkan blok proteksi spesifik tanpa bare except: dan memanfaatkan else/finally secara tepat.' },
        { criteria: 'Ketahanan Validasi Rekaman & Edge Cases', weight: 25, description: 'Mampu menangani tipe string non-numerik, nilai negatif tak valid, list kosong, dan data duplikat.' },
        { criteria: 'Integrasi Logging & Pelaporan Diagnostik', weight: 25, description: 'Menerapkan modul logging dengan level yang sesuai serta menghasilkan ringkasan statistik yang akurat.' },
      ],
      starterFilename: 'tugas_18.py',
      downloadMdUrl: 'downloads/chapter-18/tugas.md',
      downloadPyUrl: 'downloads/chapter-18/contoh.py',
    },
  },
  {
    id: 19,
    slug: '19-oop-fundamentals',
    levelId: 2,
    number: '19',
    title: 'Object-Oriented Programming I',
    subtitle: 'Class, Object, Instance Attributes, self & Metode',
    description:
      'Paradigma berorientasi objek: merancang blueprint class, konstruktor __init__, parameter self, atribut instance vs atribut class, dan encapsulation dasar.',
    competencyFocus: 'PCAP 3.1: Konsep dasar OOP, class & instance',
    estimatedHours: 5,
    difficulty: 'Intermediate',
    available: false,
    prerequisites: ['Chapter 10'],
    learningObjectives: [
      'Mendefinisikan class dan menginstansiasi object nyata',
      'Membedakan instance attributes dan class-level attributes',
      'Mengimplementasikan encapsulation melalui konvensi private variable (_var, __var)',
    ],
    tags: ['OOP', 'Class', 'Object', 'Encapsulation'],
  },
  {
    id: 20,
    slug: '20-oop-advanced',
    levelId: 2,
    number: '20',
    title: 'Object-Oriented Programming II',
    subtitle: 'Inheritance, Polymorphism, super(), dan Dunder Magic Methods',
    description:
      'Pewarisan sifat antar class, method overriding, pemanggilan super(), polimorfisme, dan special methods (__str__, __repr__, __len__, __eq__).',
    competencyFocus: 'PCAP 3.2: Inheritance, polymorphism & magic methods',
    estimatedHours: 5,
    difficulty: 'Intermediate',
    available: false,
    prerequisites: ['Chapter 19'],
    learningObjectives: [
      'Membangun class turunan dan memanfaatkan pewarisan kode',
      'Mengoverride metode induk dan memanggil fungsionalitas aslinya dengan super()',
      'Mengimplementasikan magic methods dunder untuk representasi dan perbandingan kustom',
    ],
    tags: ['Inheritance', 'Polymorphism', 'Dunder Methods', 'super()'],
  },
  {
    id: 21,
    slug: '21-packages-environments-testing',
    levelId: 2,
    number: '21',
    title: 'Packages, Environments & Testing',
    subtitle: 'PyPI, virtualenv, pip, pyproject.toml & pytest',
    description:
      'Tata kelola proyek modern: isolasi dependency dengan venv/pip, struktur paket Python (__init__.py), dan penulisan unit test otomatis dengan pytest/unittest.',
    competencyFocus: 'PCAP 4.1: Package ecosystem & automated testing',
    estimatedHours: 4,
    difficulty: 'Intermediate',
    available: false,
    prerequisites: ['Chapter 20'],
    learningObjectives: [
      'Membuat dan mengaktifkan virtual environment terisolasi',
      'Mengatur dependensi proyek dengan requirements.txt atau pyproject.toml',
      'Menulis unit test assertif menggunakan framework unittest dan pytest',
    ],
    tags: ['venv', 'pip', 'pytest', 'Packaging'],
  },
  {
    id: 22,
    slug: '22-intermediate-capstone',
    levelId: 2,
    number: '22',
    title: 'Intermediate Capstone Project',
    subtitle: 'Arsitektur OOP Penuh: Engine Analisis Data & File I/O Teruji',
    description:
      'Proyek akhir Level 2: merancang sistem analitik OOP modular dengan hierarki class, parsing dataset otomatis, exception handling kustom, dan unit test suite.',
    competencyFocus: 'Integrasi Kompetensi PCAP',
    estimatedHours: 8,
    difficulty: 'Intermediate',
    available: false,
    prerequisites: ['Chapter 13 – 21'],
    learningObjectives: [
      'Mendesain arsitektur class terintegrasi (domain models, service layer, parser)',
      'Memproses dataset disk secara asinkron/stream dengan penanganan kegagalan parsing',
      'Mencapai test coverage yang terukur menggunakan unit testing terotomasi',
    ],
    tags: ['Capstone', 'OOP Architecture', 'Test-Driven'],
  },

  // LEVEL 3 (23 - 30)
  {
    id: 23,
    slug: '23-advanced-oop-design-patterns',
    levelId: 3,
    number: '23',
    title: 'Advanced OOP & Design Patterns',
    subtitle: 'Abstract Base Classes, Composition, Factory, Singleton & Strategy',
    description:
      'Prinsip desain rekayasa perangkat lunak: Abstract Base Classes (abc), Composition over Inheritance, Factory Pattern, Singleton, Observer, dan Strategy.',
    competencyFocus: 'Senior Engineering: Clean architecture & patterns',
    estimatedHours: 6,
    difficulty: 'Advanced',
    available: false,
    prerequisites: ['Level 2'],
    learningObjectives: [
      'Mendefinisikan kontrak interface yang ketat menggunakan @abstractmethod',
      'Menerapkan komposisi komponen untuk loose coupling daripada deep inheritance',
      'Mengimplementasikan pola creational dan behavioral patterns standar industri',
    ],
    tags: ['Design Patterns', 'ABC', 'Architecture', 'SOLID'],
  },
  {
    id: 24,
    slug: '24-decorators-generators-context-managers',
    levelId: 3,
    number: '24',
    title: 'Decorators, Generators & Context Managers',
    subtitle: 'Metaprogramming, functools.wraps, yield & contextlib',
    description:
      'Mekanisme metaprogramming Python: membuat decorator dengan argumen, preserving metadata dengan wraps, pipeline generator bertingkat, dan context manager kustom.',
    competencyFocus: 'Senior Engineering: Metaprogramming & memory efficiency',
    estimatedHours: 5,
    difficulty: 'Advanced',
    available: false,
    prerequisites: ['Chapter 23'],
    learningObjectives: [
      'Membuat decorator serbaguna untuk logging, caching, dan timing eksekusi',
      'Membangun pipeline streaming data efisien memori berbasis yield generator',
      'Menulis class dan generator-based context manager dengan @contextmanager',
    ],
    tags: ['Decorators', 'Generators', 'Context Managers', 'Metaprogramming'],
  },
  {
    id: 25,
    slug: '25-type-hints-code-quality',
    levelId: 3,
    number: '25',
    title: 'Type Hints & Code Quality',
    subtitle: 'Mypy Static Typing, Generic Types, Pydantic & Linters (Ruff)',
    description:
      'Meningkatkan keandalan codebase besar: type hints mendalam (Generic, Union, Optional, Protocol), static type checking dengan mypy, validasi data Pydantic, dan linter Ruff.',
    competencyFocus: 'Senior Engineering: Type safety & static analysis',
    estimatedHours: 5,
    difficulty: 'Advanced',
    available: false,
    prerequisites: ['Chapter 24'],
    learningObjectives: [
      'Menerapkan static typing lengkap pada fungsi dan class method',
      'Menggunakan Pydantic untuk data validation dan parsing payload terstruktur',
      'Mengintegrasikan linter dan formatter otomatis untuk menjaga konsistensi tim',
    ],
    tags: ['Type Hints', 'mypy', 'Pydantic', 'Code Quality'],
  },
  {
    id: 26,
    slug: '26-advanced-testing-logging',
    levelId: 3,
    number: '26',
    title: 'Advanced Testing & Logging',
    subtitle: 'Mocks, Fixtures, Parametrize, Coverage & Structured Logging',
    description:
      'Testing skala produksi: mocking external I/O dengan unittest.mock, pytest fixtures, parameterized test, benchmarking, serta logging terstruktur JSON.',
    competencyFocus: 'Senior Engineering: Production telemetry & testing',
    estimatedHours: 5,
    difficulty: 'Advanced',
    available: false,
    prerequisites: ['Chapter 25'],
    learningObjectives: [
      'Melakukan isolasi dependensi eksternal (API/Database) menggunakan mock dan patch',
      'Menulis reusable fixtures dan parameterized tests pada pytest',
      'Mengonfigurasi logging terstruktur yang siap diintegrasikan ke log aggregator (ELK/CloudWatch)',
    ],
    tags: ['Mocking', 'pytest', 'Fixtures', 'Logging'],
  },
  {
    id: 27,
    slug: '27-concurrent-async-programming',
    levelId: 3,
    number: '27',
    title: 'Concurrent & Asynchronous Programming',
    subtitle: 'Threading, Multiprocessing, Global Interpreter Lock (GIL) & asyncio',
    description:
      'Menguasai eksekusi paralel dan konkuren: perbandingan I/O-bound vs CPU-bound, pemahaman GIL, multiprocessing pools, dan pemrograman asynchronous modern dengan async/await.',
    competencyFocus: 'Senior Engineering: High-performance concurrency',
    estimatedHours: 6,
    difficulty: 'Advanced',
    available: false,
    prerequisites: ['Chapter 26'],
    learningObjectives: [
      'Membedakan model eksekusi threading, multiprocessing, dan event loop asyncio',
      'Mengatasi batasan GIL dengan ProcessPoolExecutor untuk komputasi paralel',
      'Menulis arsitektur non-blocking async/await menggunakan asyncio.gather() dan async context managers',
    ],
    tags: ['AsyncIO', 'Multiprocessing', 'Threading', 'Concurrency'],
  },
  {
    id: 28,
    slug: '28-networking-api-integration',
    levelId: 3,
    number: '28',
    title: 'Networking & API Integration',
    subtitle: 'HTTP Clients (httpx/requests), REST, WebSockets & Serialization',
    description:
      'Komunikasi antar sistem: konsumsi REST API eksternal, async HTTP client dengan httpx, koneksi real-time WebSockets, penanganan rate limit, dan retry strategies.',
    competencyFocus: 'Senior Engineering: Distributed systems & API integration',
    estimatedHours: 5,
    difficulty: 'Advanced',
    available: false,
    prerequisites: ['Chapter 27'],
    learningObjectives: [
      'Membangun client HTTP robust dengan headers autentikasi, timeouts, dan exponential backoff retry',
      'Mengintegrasikan streaming WebSockets untuk pembaruan data real-time',
      'Menata lapisan service layer yang mengisolasi komunikasi jaringan dari logika domain bisnis',
    ],
    tags: ['Networking', 'REST API', 'httpx', 'WebSockets'],
  },
  {
    id: 29,
    slug: '29-software-architecture-deployment',
    levelId: 3,
    number: '29',
    title: 'Software Architecture & Deployment',
    subtitle: 'Clean Architecture, Twelve-Factor App, Docker & CI/CD Pipelines',
    description:
      'Membawa aplikasi ke produksi: prinsip Twelve-Factor, Layered / Clean Architecture, containerization dengan multi-stage Dockerfile, dan pipeline otomatisasi GitHub Actions.',
    competencyFocus: 'Senior Engineering: Production deployment & architecture',
    estimatedHours: 6,
    difficulty: 'Advanced',
    available: false,
    prerequisites: ['Chapter 28'],
    learningObjectives: [
      'Menyusun struktur proyek Python sesuai prinsip Clean Architecture dan Twelve-Factor App',
      'Membuat multi-stage Docker build yang ringkas dan aman untuk container produksi',
      'Menulis workflow CI/CD terotomasi untuk linting, typechecking, dan running tests',
    ],
    tags: ['Docker', 'Clean Architecture', 'CI/CD', 'Twelve-Factor'],
  },
  {
    id: 30,
    slug: '30-professional-capstone',
    levelId: 3,
    number: '30',
    title: 'Professional Capstone Project',
    subtitle: 'Sistem Terdistribusi Skala Produksi: Async API & Pipeline Tercontainerisasi',
    description:
      'Proyek puncak Level 3: membangun sistem backend asinkron berkinerja tinggi, dilengkapi static typing menyeluruh, test suite lengkap, arsitektur SOLID, dan siap deploy via Docker.',
    competencyFocus: 'Senior Engineering Capstone',
    estimatedHours: 10,
    difficulty: 'Advanced',
    available: false,
    prerequisites: ['Chapter 23 – 29'],
    learningObjectives: [
      'Mengintegrasikan asynchronous framework, design patterns, dan type hints dalam sistem nyata',
      'Menghasilkan codebase berstandar industri dengan dokumentasi API dan instruksi deployment lengkap',
      'Mencapai keandalan sistem dengan zero unhandled exceptions dan automated health monitoring',
    ],
    tags: ['Senior Capstone', 'Async Engine', 'Production Grade'],
  },
];

export const SPECIALIZATION_TRACKS: SpecializationTrack[] = [
  {
    id: 'data-science',
    title: 'Data Science & Visualization',
    subtitle: 'Eksplorasi, Manipulasi Tabular & Visualisasi Analitik',
    icon: 'bar_chart',
    tagline: 'Dari data mentah menjadi wawasan analitik yang berdampak',
    description:
      'Jalur spesialisasi untuk mengolah, membersihkan, dan menganalisis dataset berdimensi besar menggunakan pustaka standar industri seperti NumPy, Pandas, Matplotlib, dan Seaborn.',
    targetAudience: 'Data Analyst, Data Scientist, Riset Kuantitatif, Analis Bisnis',
    recommendedChapters: [8, 9, 14, 15, 17, 21, 24],
    modules: [
      { title: 'Foundations of Data Arrays (NumPy)', description: 'Operasi matriks berkinerja tinggi, vektorisasi, dan broadcasting matematis.', status: 'Specialization' },
      { title: 'Data Wrangling & Cleaning (Pandas)', description: 'Transformasi DataFrame, penanganan missing values, pengelompokan groupby, dan pivot tables.', status: 'Specialization' },
      { title: 'Exploratory Data Analysis (EDA)', description: 'Identifikasi pola statistik, outlier detection, dan korelasi antar variabel.', status: 'Specialization' },
      { title: 'Publication-Ready Visualizations (Matplotlib & Seaborn)', description: 'Merancang grafik statistik profesional, multi-panel charts, dan visualisasi distribusi.', status: 'Specialization' },
      { title: 'Capstone: End-to-End Analytics Report', description: 'Pipeline pengolahan dataset telekomunikasi dan ekonomi publik dari ingestion hingga dashboard laporan.', status: 'Advanced Project' },
    ],
  },
  {
    id: 'ai-ml',
    title: 'Artificial Intelligence & Machine Learning',
    subtitle: 'Pemodelan Prediktif, Supervised/Unsupervised Learning & Evaluasi',
    icon: 'psychology',
    tagline: 'Membangun algoritma cerdas yang belajar dari data',
    description:
      'Jalur spesialisasi machine learning praktis: rekayasa fitur (feature engineering), pelatihan model regresi dan klasifikasi dengan Scikit-Learn, hingga evaluasi metrik akurasi.',
    targetAudience: 'ML Engineer, AI Researcher, Praktisi Pemodelan Prediktif',
    recommendedChapters: [8, 9, 14, 15, 16, 20, 25],
    modules: [
      { title: 'Mathematical Essentials for ML', description: 'Aljabar linier, kalkulus diferensial, dan probabilitas terapan dalam Python.', status: 'Specialization' },
      { title: 'Supervised Learning (Regression & Classification)', description: 'Linear models, Decision Trees, Random Forests, dan Support Vector Machines.', status: 'Specialization' },
      { title: 'Unsupervised Learning & Dimensionality Reduction', description: 'Clustering K-Means, DBSCAN, dan reduksi dimensi Principal Component Analysis (PCA).', status: 'Specialization' },
      { title: 'Model Evaluation, Validation & Hyperparameter Tuning', description: 'Cross-validation, ROC-AUC, confusion matrix, dan Grid/Random Search.', status: 'Specialization' },
      { title: 'Capstone: Model Prediksi Sinyal & Anomali Jaringan', description: 'Melatih dan menguji model machine learning prediktif dengan dataset sensor jaringan telekomunikasi.', status: 'Advanced Project' },
    ],
  },
  {
    id: 'web-api',
    title: 'Web Development & APIs',
    subtitle: 'Backend Services, REST Architecture & Asynchronous Microservices',
    icon: 'api',
    tagline: 'Membangun layanan backend dan antarmuka pemrograman yang skalabel',
    description:
      'Jalur spesialisasi backend engineering: merancang RESTful API performa tinggi dengan FastAPI, ORM database dengan SQLAlchemy, autentikasi JWT, dan OpenAPI docs.',
    targetAudience: 'Backend Developer, Full-Stack Engineer, Web Service Architect',
    recommendedChapters: [10, 11, 18, 19, 20, 27, 28, 29],
    modules: [
      { title: 'Modern API Architecture with FastAPI', description: 'Dependency injection, skema Pydantic, route modular, dan OpenAPI docs otomatis.', status: 'Specialization' },
      { title: 'Database Integration & ORM (SQLAlchemy / SQLModel)', description: 'Model relasional, migrasi skema database dengan Alembic, dan optimasi query.', status: 'Specialization' },
      { title: 'Authentication & Security Best Practices', description: 'Hashing password dengan bcrypt, OAuth2 dengan JWT tokens, dan CORS protection.', status: 'Specialization' },
      { title: 'Asynchronous Task Processing with Celery & Redis', description: 'Pekerjaan background (worker tasks), scheduled jobs, dan distributed caching.', status: 'Specialization' },
      { title: 'Capstone: Production-Ready Microservice API', description: 'Layanan API tercontainerisasi lengkap dengan database, unit testing, dan CI/CD.', status: 'Advanced Project' },
    ],
  },
  {
    id: 'automation',
    title: 'Automation & Scripting',
    subtitle: 'Sistem Administrasi, Web Scraping, Pemrosesan File & Otomasi Alur Kerja',
    icon: 'smart_toy',
    tagline: 'Otomatisasikan rutinitas berulang dalam hitungan detik',
    description:
      'Jalur spesialisasi rekayasa otomasi: ekstraksi data web (BeautifulSoup & Playwright), manipulasi dokumen otomatis (Excel, PDF), automasi task CLI, dan integrasi webhook.',
    targetAudience: 'DevOps Engineer, Sysadmin, QA Automation, Profesional Operasional',
    recommendedChapters: [6, 7, 8, 10, 11, 17, 24],
    modules: [
      { title: 'System Administration & File Automation (pathlib/shutil)', description: 'Organisasi file massal, manipulasi direktori, dan otomasi backup terjadwal.', status: 'Specialization' },
      { title: 'Web Scraping & Browser Automation', description: 'Ekstraksi data HTML dengan BeautifulSoup dan scraping dinamis dengan Playwright.', status: 'Specialization' },
      { title: 'Spreadsheet & Document Automation (openpyxl / PyPDF)', description: 'Generate laporan Excel berformula secara otomatis dan merge dokumen PDF.', status: 'Specialization' },
      { title: 'API Webhooks & Alerting Systems', description: 'Kirim notifikasi otomatis ke Telegram, Slack, atau email saat mendeteksi kegagalan sistem.', status: 'Specialization' },
      { title: 'Capstone: Autonomous Data Ingestion & Reporting Bot', description: 'Bot otomasi yang mengunduh data web berkala, mengolahnya ke Excel, dan mengirim email ringkasan.', status: 'Advanced Project' },
    ],
  },
  {
    id: 'iot-telecom',
    title: 'IoT, Signal Processing & Telecommunications',
    subtitle: 'Analisis Sinyal Digital, Pengukuran RSRP, Sensor Data & IoT Protocols',
    icon: 'cell_tower',
    tagline: 'Pengolahan sinyal, data telekomunikasi nirkabel, dan perangkat terhubung',
    description:
      'Jalur spesialisasi telekomunikasi & IoT: pengolahan sinyal diskrit (SciPy signal), analisis data propagasi sinyal seluler (RSRP, RSRQ, SINR), protokol MQTT, dan visualisasi pemetaan sensor.',
    targetAudience: 'Teknik Telekomunikasi, IoT Engineer, RF Engineer, Peneliti Sinyal',
    recommendedChapters: [8, 9, 10, 11, 14, 15, 17, 27],
    modules: [
      { title: 'Telemetry Data Structures & Sensor Records', description: 'Pemanfaatan dictionary dan tuple untuk data geolokasi (lat, lon) dan log pengukuran sensor.', status: 'Core Prerequisite' },
      { title: 'Cellular Signal Processing (RSRP/RSRQ Analysis)', description: 'Klasifikasi kualitas sinyal radio 4G/5G, moving average filtering, dan deteksi zona blindspot.', status: 'Core Prerequisite' },
      { title: 'Digital Signal Processing Fundamentals (SciPy)', description: 'Transformasi Fourier (FFT), spectral analysis, dan perancangan filter digital.', status: 'Specialization' },
      { title: 'IoT Protocols & Telemetry Streaming (MQTT)', description: 'Publish-subscribe messaging untuk telemetri sensor edge perangkat nirkabel.', status: 'Specialization' },
      { title: 'Capstone: Sistem Monitoring Kualitas Jaringan Telekomunikasi', description: 'Dashboard analitik pemrosesan log pengukuran sinyal stasiun pemancar dengan metrik statistik komprehensif.', status: 'Advanced Project' },
    ],
  },
];

export const CURRICULUM_DISCLAIMER =
  'Kurikulum Python Learning Hub dikembangkan secara independen oleh tim pengembang sebagai sumber belajar mandiri. Topik pembelajaran dirancang untuk menyelaraskan secara luas dengan area kompetensi sertifikasi global (seperti Python Institute PCEP & PCAP), namun situs ini bersifat independen dan tidak terafiliasi resmi maupun disertifikasi secara komersial oleh Python Institute.';


// Helper query functions
export function getChapterById(id: number): Chapter | undefined {
  return CHAPTERS.find((c) => c.id === id);
}

export function getChapterBySlug(slug: string): Chapter | undefined {
  return CHAPTERS.find((c) => c.slug === slug);
}

export function getChaptersByLevel(levelId: number): Chapter[] {
  return CHAPTERS.filter((c) => c.levelId === levelId);
}
