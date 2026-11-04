export const meetings = Array.from({ length: 16 }, (_, i) => {
  const number = i + 1;
  return {number, available: number === 9 || number === 10,
    title: number === 9 ? 'Function Design, Module & Docstring' : number === 10 ? 'Struktur Data & Algoritma' : 'Materi sedang disiapkan',
    description: number === 9 ? 'Rancang fungsi yang jelas, susun modul, dan dokumentasikan kode Python.' : number === 10 ? 'Kelola koleksi data, gunakan comprehension, lalu cari dan urutkan data sensor.' : 'Materi modul sedang dalam persiapan kurikulum.',
    tags: number === 9 ? ['Fungsi', 'Module', 'Docstring'] : number === 10 ? ['Struktur data', 'Searching', 'Sorting'] : [],
    path: `pertemuan-${String(number).padStart(2, '0')}/index.html`};
});
export interface SlideData { title: string; body: string; kind: string; notes: string; example?: string; dependency?: string; files?: {name: string; code: string}[]; question?: string; answer?: string }
