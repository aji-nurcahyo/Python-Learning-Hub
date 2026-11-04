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
    description: 'Mengenal sejarah Python, Zen of Python, instalasi CPython, Colab/IDE, serta cara kerja interpreter.',
    competencyFocus: 'PCEP 1.1: Dasar eksekusi & lingkungan Python',
    estimatedHours: 2,
    difficulty: 'Beginner',
    available: false,
    prerequisites: [],
    learningObjectives: [
      'Memahami perbedaan interpreted language dan compiled language',
      'Menjalankan program Python pertama melalui CLI dan script file',
      'Mengenal kaidah penulisan komentar dan indentation',
    ],
    tags: ['Interpreter', 'Syntax', 'Setup'],
  },
  {
    id: 2,
    slug: '02-variables-data-types',
    levelId: 1,
    number: '02',
    title: 'Variables & Data Types',
    subtitle: 'Variabel Dinamis, Tipe Data Skalar & Konversi',
    description: 'Menyimpan nilai dalam memori, tipe int, float, str, bool, type hinting dasar, dan konversi tipe data eksplisit.',
    competencyFocus: 'PCEP 2.1: Literal, variabel, dan konversi tipe',
    estimatedHours: 3,
    difficulty: 'Beginner',
    available: false,
    prerequisites: ['Chapter 01'],
    learningObjectives: [
      'Mendeklarasikan variabel dengan penamaan snake_case sesuai PEP 8',
      'Membedakan tipe data integer, floating-point, boolean, dan string',
      'Melakukan type casting dengan int(), float(), str(), dan bool()',
    ],
    tags: ['Variables', 'Types', 'Casting'],
  },
  {
    id: 3,
    slug: '03-operators-expressions',
    levelId: 1,
    number: '03',
    title: 'Operators & Expressions',
    subtitle: 'Aritmatika, Perbandingan, Logika & Presedensi',
    description: 'Operasi matematika, operator modulo, pembagian bulat, perbandingan nilai, logika boolean, dan aturan presedensi operator.',
    competencyFocus: 'PCEP 2.2: Operator numerik dan boolean',
    estimatedHours: 3,
    difficulty: 'Beginner',
    available: false,
    prerequisites: ['Chapter 02'],
    learningObjectives: [
      'Menggunakan operator aritmatika (+, -, *, /, //, %, **)',
      'Menerapkan operator perbandingan (==, !=, >, <, >=, <=)',
      'Memahami evaluasi ekspresi logika dengan presedensi operator yang benar',
    ],
    tags: ['Arithmetic', 'Logic', 'Precedence'],
  },
  {
    id: 4,
    slug: '04-input-output',
    levelId: 1,
    number: '04',
    title: 'Input & Output',
    subtitle: 'Interaksi Pengguna & Pemformatan Teks Modern',
    description: 'Menerima masukan pengguna dengan input(), validasi dasar, serta memformat output dengan f-strings dan string format.',
    competencyFocus: 'PCEP 2.3: I/O standar dan string formatting',
    estimatedHours: 2,
    difficulty: 'Beginner',
    available: false,
    prerequisites: ['Chapter 03'],
    learningObjectives: [
      'Mengambil input dinamis dan mengonversi tipe data masukan',
      'Menggunakan f-strings untuk interpolasi ekspresi variabel',
      'Memformat angka desimal, persentase, dan perataan kolom tabel',
    ],
    tags: ['I/O', 'f-strings', 'Formatting'],
  },
  {
    id: 5,
    slug: '05-conditional-statements',
    levelId: 1,
    number: '05',
    title: 'Conditional Statements',
    subtitle: 'Pengambilan Keputusan: if, elif, else & Guard Clauses',
    description: 'Merancang alur logika percabangan, kondisi bertingkat, operator ternary, dan pola guard clauses untuk kode yang bersih.',
    competencyFocus: 'PCEP 3.1: Percabangan dan logika alur',
    estimatedHours: 3,
    difficulty: 'Beginner',
    available: false,
    prerequisites: ['Chapter 03', 'Chapter 04'],
    learningObjectives: [
      'Menulis struktur percabangan if, elif, dan else secara tepat',
      'Menggabungkan kondisi majemuk menggunakan and, or, dan not',
      'Menghindari nested if yang terlalu dalam dengan teknik guard clauses',
    ],
    tags: ['Branching', 'if-else', 'Decision Logic'],
  },
  {
    id: 6,
    slug: '06-loops-iteration',
    levelId: 1,
    number: '06',
    title: 'Loops & Iteration',
    subtitle: 'Pengulangan for, while, break, continue & else',
    description: 'Mengulang tugas komputasi dengan for dan while, pemanfaatan range(), kontrol loop break dan continue, serta klausa else pada loop.',
    competencyFocus: 'PCEP 3.2: Pengulangan dan kontrol iterasi',
    estimatedHours: 4,
    difficulty: 'Beginner',
    available: false,
    prerequisites: ['Chapter 05'],
    learningObjectives: [
      'Memilih antara for loop (definite iteration) dan while loop (indefinite iteration)',
      'Memanfaatkan fungsi range(start, stop, step) secara optimal',
      'Mengendalikan siklus loop dengan break, continue, dan else block',
    ],
    tags: ['For Loop', 'While Loop', 'Range'],
  },
  {
    id: 7,
    slug: '07-strings-text-processing',
    levelId: 1,
    number: '07',
    title: 'Strings & Text Processing',
    subtitle: 'Indexing, Slicing, Immutability & Metode String',
    description: 'Eksplorasi mendalam string sebagai sequence immutable: pemotongan slice [start:stop:step], metode bawaan, dan pembersihan teks.',
    competencyFocus: 'PCEP 3.3: Manipulasi sequence teks',
    estimatedHours: 3,
    difficulty: 'Beginner',
    available: false,
    prerequisites: ['Chapter 06'],
    learningObjectives: [
      'Menerapkan indexing positif dan negatif serta slicing sequence',
      'Memanfaatkan metode string penting (strip, split, join, replace, find)',
      'Memahami sifat immutability string dalam memori Python',
    ],
    tags: ['Strings', 'Slicing', 'Text Processing'],
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
      downloadMdUrl: 'downloads/pertemuan-10/tugas.md',
      downloadPyUrl: 'downloads/pertemuan-10/contoh.py',
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
    deckPath: '#chapter/08/slides',
    tugasPath: '#chapter/08/task',
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
      downloadMdUrl: 'downloads/pertemuan-10/tugas.md',
      downloadPyUrl: 'downloads/pertemuan-10/contoh.py',
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
      downloadMdUrl: 'downloads/pertemuan-09/tugas.md',
      downloadPyUrl: 'downloads/pertemuan-09/contoh.py',
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
    deckPath: '#chapter/10/slides',
    tugasPath: '#chapter/10/task',
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
      downloadMdUrl: 'downloads/pertemuan-09/tugas.md',
      downloadPyUrl: 'downloads/pertemuan-09/contoh.py',
    },
  },
  {
    id: 12,
    slug: '12-foundations-capstone',
    levelId: 1,
    number: '12',
    title: 'Foundations Capstone Project',
    subtitle: 'Integrasi Komprehensif: Sistem Pengolahan Data Multi-Module',
    description:
      'Proyek akhir Level 1: membangun aplikasi CLI terstruktur yang mengolah dataset dinamis, menerapkan validasi masukan, modul kustom, dan pengujian assert.',
    competencyFocus: 'Integrasi Kompetensi PCEP',
    estimatedHours: 6,
    difficulty: 'Beginner',
    available: false,
    prerequisites: ['Chapter 01 – 11'],
    learningObjectives: [
      'Mengintegrasikan dictionary, list, set, dan tuple dalam arsitektur data realistis',
      'Menata kode menjadi minimal dua file modul dengan docstring lengkap',
      'Menyusun minimal 10 pengujian assert otomatis untuk menjamin kebenaran logika',
    ],
    tags: ['Capstone', 'Integration', 'CLI Project'],
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
      'Menerapkan fungsi fleksibel dengan arbitrary arguments (*args, **kwargs), fungsi anonim lambda, fungsi sebagai argumen (higher-order), dan closures.',
    competencyFocus: 'PCAP 1.1: Pemrograman fungsional & argument unpacking',
    estimatedHours: 4,
    difficulty: 'Intermediate',
    available: false,
    prerequisites: ['Level 1'],
    learningObjectives: [
      'Menerima jumlah argumen variabel dengan *args dan keyword arguments dengan **kwargs',
      'Menulis ekspresi lambda untuk operasi transformasi singkat',
      'Memahami mekanisme closure memori pada nested functions',
    ],
    tags: ['*args', '**kwargs', 'Lambda', 'Closures'],
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
    ],
    tags: ['Comprehension', 'Generators', 'Iterators', 'Filtering'],
    deckPath: '#chapter/08/slides',
    tugasPath: '#chapter/08/task',
  },
  {
    id: 15,
    slug: '15-searching-sorting-algorithms',
    levelId: 2,
    number: '15',
    title: 'Searching & Sorting Algorithms',
    subtitle: 'Linear Search, Binary Search, Selection Sort & Timsort (sorted)',
    description:
      'Studi algoritma klasik: linear search O(n), binary search O(log n), selection sort O(n²), pemanfaatan sorted() dengan custom key lambda, dan reverse.',
    competencyFocus: 'PCAP 1.3: Algoritma pencarian dan pengurutan terapan',
    estimatedHours: 5,
    difficulty: 'Intermediate',
    available: true,
    prerequisites: ['Chapter 08', 'Chapter 14'],
    learningObjectives: [
      'Mengimplementasikan linear search pada data tidak terurut dengan penanganan kasus None',
      'Mengimplementasikan selection sort secara manual untuk memahami mekanisme swap data',
      'Mengurutkan data dictionary kompleks menggunakan sorted(data, key=lambda x: ...)',
    ],
    tags: ['Algorithms', 'Linear Search', 'Selection Sort', 'Sorting'],
    deckPath: '#chapter/08/slides',
    tugasPath: '#chapter/08/task',
  },
  {
    id: 16,
    slug: '16-algorithm-analysis-problem-solving',
    levelId: 2,
    number: '16',
    title: 'Algorithm Analysis & Problem Solving',
    subtitle: 'Notasi Big-O, Space-Time Tradeoffs & Strategi Algoritmik',
    description:
      'Menganalisis efisiensi algoritma secara formal: notasi O(1), O(log n), O(n), O(n²), memory footprint, dan teknik pemecahan masalah komputasi.',
    competencyFocus: 'PCAP 1.4: Kompleksitas komputasi & optimasi',
    estimatedHours: 4,
    difficulty: 'Intermediate',
    available: false,
    prerequisites: ['Chapter 15'],
    learningObjectives: [
      'Menentukan kompleksitas waktu kasus terbaik, rata-rata, dan terburuk',
      'Membandingkan efisiensi struktur data (list lookup vs set/dict lookup)',
      'Mengoptimalkan algoritma dari kuadratik O(n²) ke linier O(n)',
    ],
    tags: ['Big-O', 'Complexity', 'Optimization'],
  },
  {
    id: 17,
    slug: '17-file-handling-serialization',
    levelId: 2,
    number: '17',
    title: 'File Handling & Data Serialization',
    subtitle: 'Context Manager (with), CSV, JSON & Text Processing',
    description:
      'Membaca dan menulis file lokal dengan aman menggunakan context manager (with open), parsing format CSV terstruktur, serialisasi JSON, dan manajemen path (pathlib).',
    competencyFocus: 'PCAP 2.1: File I/O stream dan format data',
    estimatedHours: 4,
    difficulty: 'Intermediate',
    available: false,
    prerequisites: ['Chapter 11'],
    learningObjectives: [
      'Mengelola file descriptor secara aman tanpa resource leak menggunakan with statement',
      'Membaca dan menulis data tabel menggunakan modul bawaan csv.DictReader dan csv.DictWriter',
      'Melakukan serialisasi dan deserialisasi data menggunakan json.loads() dan json.dumps()',
    ],
    tags: ['Files', 'CSV', 'JSON', 'pathlib'],
  },
  {
    id: 18,
    slug: '18-exception-handling-debugging',
    levelId: 2,
    number: '18',
    title: 'Exception Handling & Debugging',
    subtitle: 'Hierarki Exception, Custom Exception & pdb Debugger',
    description:
      'Membuat program andal: hierarki exception Python, blok try/except/else/finally, raise custom exception kustom, dan teknik debugging dengan pdb/breakpoint.',
    competencyFocus: 'PCAP 2.2: Exception hierarchy dan teknik debugging',
    estimatedHours: 4,
    difficulty: 'Intermediate',
    available: false,
    prerequisites: ['Chapter 11'],
    learningObjectives: [
      'Menangkap beberapa exception spesifik secara hierarkis tanpa bare except:',
      'Mendefinisikan class exception kustom turunan dari Exception bawaan',
      'Menggunakan breakpoint() dan pdb untuk inspeksi call stack saat runtime',
    ],
    tags: ['Exceptions', 'Debugging', 'pdb', 'Robustness'],
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
