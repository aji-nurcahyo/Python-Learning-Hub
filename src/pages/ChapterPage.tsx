import { useState } from 'react';
import { CHAPTERS, type Chapter } from '../curriculum';
import { DifficultyBadge } from '../components/DifficultyBadge';
import { PrerequisiteList } from '../components/PrerequisiteList';
import { LearningObjectives } from '../components/LearningObjectives';
import { CodeBlock } from '../components/CodeBlock';
import { CodeOutput } from '../components/CodeOutput';
import { ExerciseCard } from '../components/ExerciseCard';
import { QuizCard } from '../components/QuizCard';
import { AssignmentCard } from '../components/AssignmentCard';
import { ChapterNavigation } from '../components/ChapterNavigation';
import { Icon } from '../ui/Icon';
import outputs from '../code/outputs.json';

interface ChapterPageProps {
  chapterId: number;
  onNavigateHome: () => void;
  onNavigateLevel: (levelId: number) => void;
  onNavigateChapter: (chapterId: number) => void;
}

// Sample educational resources for active chapters (Chapters 08, 09, 10, 11)
const CHAPTER_CONTENT_MAP: Record<
  number,
  {
    codeExample: { code: string; outputKey: string; explanation: string };
    exercise: { title: string; instructions: string[]; tips: string; time: string };
    quiz: {
      question: string;
      options: string[];
      correctIndex: number;
      explanation: string;
      hint?: string;
    };
    assignment: {
      title: string;
      description: string;
      instructions: string[];
      rubric: { criteria: string; weight: number; description: string }[];
      starterCode?: string;
      downloadMdUrl?: string;
      downloadPyUrl?: string;
    };
  }
> = {
  8: {
    codeExample: {
      code: `# Operasi List & Pengindeksan Koleksi Data
rsrp_list = [-82, -107, -95, -89]
print(rsrp_list[0])  # Mengakses elemen pertama`,
      outputKey: 'p10-02',
      explanation:
        'List merupakan tipe data sequence mutable. Elemen diakses dengan indeks nol (zero-based index) dan dapat dimodifikasi secara dinamis.',
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
      explanation:
        'List didefinisikan dengan kurung siku [] dan bersifat mutable sehingga nilainya dapat diubah/ditambah. Sebaliknya, Tuple didefinisikan dengan () dan bersifat immutable untuk menjaga integritas data.',
      hint: 'Ingat sifat modifikasi elemen setelah objek dibuat dalam memori.',
    },
    assignment: {
      title: 'Tugas Praktik 08: Pengolahan Sinyal & Statistik Koleksi',
      description:
        'Implementasikan skrip pengolahan data pengukuran sinyal telekomunikasi berbasis List dan Tuple.',
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
      starterCode: `# Template Starter Code - Chapter 08
def ringkas_sinyal(data_sinyal: list[float]) -> tuple[float, float, float]:
    """Menghitung nilai minimum, maksimum, dan rata-rata dari list sinyal."""
    if not data_sinyal:
        return (0.0, 0.0, 0.0)
    # Tuliskan logika Anda di sini
    pass`,
      downloadMdUrl: 'downloads/pertemuan-10/tugas.md',
      downloadPyUrl: 'downloads/pertemuan-10/contoh.py',
    },
  },
  9: {
    codeExample: {
      code: `# Struktur Data Dictionary & Hash Key-Value
sensor = {"id": "S01", "lokasi": "Gedung A", "rsrp": -80}
print(sensor["id"])
print(sensor.get("status", "tidak tersedia"))
print(sensor.items())`,
      outputKey: 'p10-05',
      explanation:
        'Dictionary menyimpan data berpasangan key-value dengan kompleksitas pencarian O(1). Metode get() mencegah timbulnya KeyError saat kunci tidak ditemukan.',
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
      explanation:
        'Metode get(key, default) memberikan nilai fallback yang aman tanpa memicu crash program akibat KeyError jika kunci yang diminta belum ada.',
      hint: 'Pikirkan penanganan error ketika suatu kunci mungkin absen.',
    },
    assignment: {
      title: 'Tugas Praktik 09: Registri Sensor & Pemetaan Sinyal',
      description:
        'Rancang modul pengelolaan registri sensor jaringan menggunakan dictionary dan set.',
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
      downloadMdUrl: 'downloads/pertemuan-10/tugas.md',
      downloadPyUrl: 'downloads/pertemuan-10/contoh.py',
    },
  },
  10: {
    codeExample: {
      code: `# Perbedaan Nilai Balik (Return) dan Cetak Layar (Print)
def hitung_persegi(sisi):
    return sisi * sisi

hasil = hitung_persegi(4)
print(hasil + 8)  # Nilai return dapat diproses lebih lanjut!`,
      outputKey: 'p09-14',
      explanation:
        'Return mengembalikan data ke pemanggil fungsi agar dapat disimpan dalam variabel atau digunakan dalam ekspresi matematika lain. Print hanya mencetak teks ke layar dan mengembalikan None.',
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
      explanation:
        'Secara implisit, fungsi Python tanpa pernyataan return selalu mengembalikan nilai NoneType yaitu None.',
      hint: 'Lihat apa yang dihasilkan jika Anda mencetak hasil pemanggilan fungsi yang hanya berisi perintah print().',
    },
    assignment: {
      title: 'Tugas Praktik 10: Perancangan Pustaka Fungsi Analitik',
      description:
        'Rancang modul fungsi yang menerapkan aturan scope LEGB, parameter nilai default, dan return teruji.',
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
      starterCode: `# Template Starter Code - Chapter 10
def konversi_suhu(celsius: float) -> float:
    """Mengonversi nilai suhu dari Celsius ke Fahrenheit.
    
    Args:
        celsius (float): Derajat suhu dalam Celsius.
    Returns:
        float: Derajat suhu dalam Fahrenheit.
    """
    return (celsius * 9 / 5) + 32`,
      downloadMdUrl: 'downloads/pertemuan-09/tugas.md',
      downloadPyUrl: 'downloads/pertemuan-09/contoh.py',
    },
  },
  11: {
    codeExample: {
      code: `# Ekstraksi Docstring Standar PEP 257
def konversi_c_ke_f(celsius):
    """Konversi suhu dari Celsius ke Fahrenheit.

    Args:
        celsius (float): Suhu dalam Celsius.
    Returns:
        float: Suhu dalam Fahrenheit.
    """
    return celsius * 9 / 5 + 32

print(konversi_c_ke_f.__doc__)`,
      outputKey: 'p09-13',
      explanation:
        'Docstring ditulis tepat di bawah header fungsi menggunakan triple quotes ("""). Atribut __doc__ atau fungsi help() dapat membacanya secara otomatis untuk dokumentasi interaktif.',
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
      explanation:
        'Saat Python menjalankan berkas secara langsung, variabel khusus __name__ secara otomatis disetel ke string "__main__". Jika berkas diimpor sebagai modul, __name__ akan berisi nama berkas modul tersebut.',
      hint: 'Pikirkan mekanisme Python dalam membedakan skrip runnable dengan modul pustaka.',
    },
    assignment: {
      title: 'Tugas Praktik 11: Paket Modul Reusable Telekomunikasi',
      description:
        'Bangun struktur modul Python modular yang memisahkan logika komputasi dengan antarmuka CLI pengguna.',
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
      downloadMdUrl: 'downloads/pertemuan-09/tugas.md',
      downloadPyUrl: 'downloads/pertemuan-09/contoh.py',
    },
  },
};

export function ChapterPage({
  chapterId,
  onNavigateHome,
  onNavigateLevel,
  onNavigateChapter,
}: ChapterPageProps) {
  const chapter: Chapter | undefined = CHAPTERS.find((c) => c.id === chapterId);

  const [activeTab, setActiveTab] = useState<'overview' | 'code' | 'practice' | 'assignment'>('overview');

  if (!chapter) {
    return (
      <div className="hub-page-container document placeholder">
        <div className="eyebrow">CHAPTER TIDAK DITEMUKAN</div>
        <h1>Chapter {chapterId} Belum Terdaftar</h1>
        <p>Silakan kembali ke kurikulum untuk memilih chapter 1 hingga 30.</p>
        <button type="button" className="button primary" onClick={onNavigateHome}>
          <Icon name="arrow_back" size={18} /> <span>Kembali ke Beranda Hub</span>
        </button>
      </div>
    );
  }

  const chapterContent = CHAPTER_CONTENT_MAP[chapter.id];

  const prevChapter = CHAPTERS.find((c) => c.id === chapter.id - 1);
  const nextChapter = CHAPTERS.find((c) => c.id === chapter.id + 1);

  // Render for Upcoming / Coming Soon Chapters
  if (!chapter.available) {
    return (
      <div className="hub-chapter-page upcoming-view">
        {/* Breadcrumb */}
        <div className="page-breadcrumb">
          <button type="button" className="breadcrumb-back-btn" onClick={() => onNavigateLevel(chapter.levelId)}>
            <Icon name="arrow_back" size={16} />
            <span>Level {chapter.levelId}</span>
          </button>
          <span className="breadcrumb-separator">/</span>
          <span className="breadcrumb-current">Chapter {chapter.number}: {chapter.title}</span>
        </div>

        {/* Header */}
        <header className="chapter-header-banner upcoming-banner">
          <div className="chapter-meta-badges">
            <span className="status-badge upcoming">Segera Hadir</span>
            <span className="ch-level-chip">Level {chapter.levelId}</span>
            <DifficultyBadge difficulty={chapter.difficulty} />
            <span className="ch-hours-chip">
              <Icon name="schedule" size={14} /> {chapter.estimatedHours} jam pembelajaran
            </span>
          </div>

          <h1 className="chapter-title">
            <span className="ch-num-prefix">Chapter {chapter.number} ·</span> {chapter.title}
          </h1>
          <p className="chapter-subtitle">{chapter.subtitle}</p>
          <p className="chapter-desc">{chapter.description}</p>

          <div className="chapter-competency-alert">
            <Icon name="radar" size={20} />
            <div>
              <strong>Target Fokus Kompetensi:</strong>
              <p>{chapter.competencyFocus}</p>
            </div>
          </div>
        </header>

        {/* Coming Soon Notice Card */}
        <div className="coming-soon-notice-card">
          <div className="notice-icon-box">
            <Icon name="construction" size={32} />
          </div>
          <div className="notice-content">
            <h3>Materi Sedang Dalam Tahap Penyusunan</h3>
            <p>
              Silabus, tujuan pembelajaran, dan prasyarat chapter ini telah dirancang sesuai kurikulum.
              Materi slide interaktif, contoh eksekusi kode, dan tugas mandiri akan dirilis secara bertahap.
              Selesaikan chapter-chapter dasar yang telah tersedia terlebih dahulu untuk membangun pemahaman yang solid.
            </p>
            <div className="notice-actions">
              <button
                type="button"
                className="button primary"
                onClick={() => onNavigateLevel(chapter.levelId)}
              >
                <Icon name="arrow_back" size={18} />
                <span>Lihat Silabus Level {chapter.levelId}</span>
              </button>
              <button
                type="button"
                className="button subtle"
                onClick={onNavigateHome}
              >
                <span>Katalog Chapter</span>
              </button>
            </div>
          </div>
        </div>

        {/* Prereqs & Objectives Preview */}
        <div className="chapter-preview-grid">
          <PrerequisiteList prerequisites={chapter.prerequisites} />
          <LearningObjectives objectives={chapter.learningObjectives} />
        </div>

        {/* Navigation to Prev / Next */}
        <ChapterNavigation
          prevChapter={prevChapter}
          nextChapter={nextChapter}
          onNavigate={(targetId) => onNavigateChapter(targetId)}
        />
      </div>
    );
  }

  // Render for Active Chapters (e.g. Ch 8, 9, 10, 11)
  const codeOutputText = chapterContent
    ? outputs[chapterContent.codeExample.outputKey as keyof typeof outputs] || ''
    : '';

  return (
    <div className="hub-chapter-page active-view">
      {/* Breadcrumb */}
      <div className="page-breadcrumb">
        <button type="button" className="breadcrumb-back-btn" onClick={() => onNavigateLevel(chapter.levelId)}>
          <Icon name="arrow_back" size={16} />
          <span>Level {chapter.levelId}</span>
        </button>
        <span className="breadcrumb-separator">/</span>
        <span className="breadcrumb-current">Chapter {chapter.number}: {chapter.title}</span>
      </div>

      {/* Chapter Active Header */}
      <header className="chapter-header-banner">
        <div className="chapter-meta-badges">
          <span className="status-badge ready">● Tersedia</span>
          <span className="ch-level-chip">Level {chapter.levelId}</span>
          <DifficultyBadge difficulty={chapter.difficulty} />
          <span className="ch-hours-chip">
            <Icon name="schedule" size={14} /> {chapter.estimatedHours} jam pembelajaran
          </span>
        </div>

        <h1 className="chapter-title">
          <span className="ch-num-prefix">Chapter {chapter.number} ·</span> {chapter.title}
        </h1>
        <p className="chapter-subtitle">{chapter.subtitle}</p>
        <p className="chapter-desc">{chapter.description}</p>

        <div className="chapter-competency-alert">
          <Icon name="verified" size={20} />
          <div>
            <strong>Fokus Kompetensi:</strong>
            <p>{chapter.competencyFocus}</p>
          </div>
        </div>

        {/* Interactive Deck Launch Bar */}
        <div className="chapter-launch-bar">
          <div className="launch-group">
            {chapter.deckPath && (
              <a className="button primary button-lg" href={chapter.deckPath}>
                <Icon name="slideshow" size={20} />
                <span>Buka Presentasi Interaktif Reveal.js</span>
              </a>
            )}
            {chapter.deckPath && (
              <a className="button subtle button-lg" href={`${chapter.deckPath}?view=read`}>
                <Icon name="menu_book" size={20} />
                <span>Mode Baca Dokumen</span>
              </a>
            )}
            {chapter.tugasPath && (
              <a className="button subtle button-lg" href={chapter.tugasPath}>
                <Icon name="assignment" size={20} />
                <span>Tugas Mandiri</span>
              </a>
            )}
          </div>
        </div>
      </header>

      {/* Tabs Navigation for Chapter Content */}
      <div className="chapter-tabs-nav" role="tablist">
        <button
          type="button"
          role="tab"
          aria-selected={activeTab === 'overview'}
          className={activeTab === 'overview' ? 'active' : ''}
          onClick={() => setActiveTab('overview')}
        >
          <Icon name="info" size={18} />
          <span>Ikhtisar & Kompetensi</span>
        </button>
        <button
          type="button"
          role="tab"
          aria-selected={activeTab === 'code'}
          className={activeTab === 'code' ? 'active' : ''}
          onClick={() => setActiveTab('code')}
        >
          <Icon name="terminal" size={18} />
          <span>Contoh Kode & Output CPython</span>
        </button>
        <button
          type="button"
          role="tab"
          aria-selected={activeTab === 'practice'}
          className={activeTab === 'practice' ? 'active' : ''}
          onClick={() => setActiveTab('practice')}
        >
          <Icon name="fitness_center" size={18} />
          <span>Latihan & Kuis Konsep</span>
        </button>
        <button
          type="button"
          role="tab"
          aria-selected={activeTab === 'assignment'}
          className={activeTab === 'assignment' ? 'active' : ''}
          onClick={() => setActiveTab('assignment')}
        >
          <Icon name="assignment" size={18} />
          <span>Tugas & Rubrik Penilaian</span>
        </button>
      </div>

      {/* Tab Panels */}
      <div className="chapter-tab-content">
        {/* Tab: Overview */}
        {activeTab === 'overview' && (
          <div className="tab-pane-overview">
            <div className="chapter-preview-grid">
              <PrerequisiteList prerequisites={chapter.prerequisites} />
              <LearningObjectives objectives={chapter.learningObjectives} />
            </div>

            <div className="pedagogy-callout">
              <Icon name="psychology" size={24} />
              <div>
                <h4>Pendekatan Belajar Terarah</h4>
                <p>
                  Mulailah dengan menyimak materi presentasi interaktif Reveal.js untuk memahami konsep visual dan rumus komputasional.
                  Lanjutkan dengan membaca contoh kode nyata, mencoba latihan mandiri, menjawab kuis penguatan konsep, dan menyelesaikan tugas terstruktur.
                </p>
              </div>
            </div>
          </div>
        )}

        {/* Tab: Code & Output */}
        {activeTab === 'code' && chapterContent && (
          <div className="tab-pane-code">
            <div className="section-heading-clean">
              <div>
                <div className="eyebrow">EKSEKUSI PYTHON 3 ASLI</div>
                <h3>Kode Sumber & Hasil Keluaran Terminal</h3>
              </div>
              <p>
                Kode berikut dijalankan langsung di mesin penerjemah Python tanpa simulasi.
              </p>
            </div>

            <div className="code-output-side-by-side">
              <div className="code-side">
                <CodeBlock
                  code={chapterContent.codeExample.code}
                  filename={`contoh_ch${chapter.number}.py`}
                />
              </div>
              <div className="output-side">
                <CodeOutput output={codeOutputText} />
              </div>
            </div>

            <div className="code-explanation-card">
              <Icon name="lightbulb" size={20} />
              <div>
                <strong>Penjelasan Mekanisme:</strong>
                <p>{chapterContent.codeExample.explanation}</p>
              </div>
            </div>
          </div>
        )}

        {/* Tab: Practice & Quiz */}
        {activeTab === 'practice' && chapterContent && (
          <div className="tab-pane-practice">
            <div className="practice-grid">
              <ExerciseCard
                title={chapterContent.exercise.title}
                instructions={chapterContent.exercise.instructions}
                tips={chapterContent.exercise.tips}
                timeEstimate={chapterContent.exercise.time}
              />
              <QuizCard
                question={chapterContent.quiz.question}
                answer={`Kunci Jawaban: ${chapterContent.quiz.options[chapterContent.quiz.correctIndex]}\n\nPembahasan: ${chapterContent.quiz.explanation}`}
                hint={chapterContent.quiz.hint}
              />
            </div>
          </div>
        )}

        {/* Tab: Assignment */}
        {activeTab === 'assignment' && chapterContent && (
          <div className="tab-pane-assignment">
            <AssignmentCard
              title={chapterContent.assignment.title}
              description={chapterContent.assignment.description}
              instructions={chapterContent.assignment.instructions}
              rubric={chapterContent.assignment.rubric}
              starterCode={chapterContent.assignment.starterCode}
              downloadMdUrl={chapterContent.assignment.downloadMdUrl}
              downloadPyUrl={chapterContent.assignment.downloadPyUrl}
            />
          </div>
        )}
      </div>

      {/* Navigation to Prev / Next */}
      <ChapterNavigation
        prevChapter={prevChapter}
        nextChapter={nextChapter}
        onNavigate={(targetId) => onNavigateChapter(targetId)}
      />
    </div>
  );
}
