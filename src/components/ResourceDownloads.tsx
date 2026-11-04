import { Icon } from '../ui/Icon';

interface ResourceDownloadsProps {
  pptxUrl?: string;
  starterCodeUrl?: string;
  guideUrl?: string;
  pdfUrl?: string;
}

export function ResourceDownloads({
  pptxUrl = 'downloads/Materi_Pengkom_Pertemuan_9_10_Python.pptx',
  starterCodeUrl,
  guideUrl,
  pdfUrl,
}: ResourceDownloadsProps) {
  return (
    <div className="chapter-resources-panel">
      <div className="resources-heading">
        <Icon name="folder_zip" size={20} />
        <h4>Berkas & Sumber Pembelajaran Chapter</h4>
      </div>
      <div className="resources-links-grid">
        {pptxUrl && (
          <a href={pptxUrl} className="resource-link-btn" download>
            <Icon name="file_present" size={18} />
            <div>
              <span className="res-title">Slide Presentasi (.pptx)</span>
              <span className="res-sub">PowerPoint sumber dapat disunting</span>
            </div>
          </a>
        )}
        {starterCodeUrl && (
          <a href={starterCodeUrl} className="resource-link-btn" download>
            <Icon name="code" size={18} />
            <div>
              <span className="res-title">Starter Code Python (.py)</span>
              <span className="res-sub">Template pengerjaan latihan & tugas</span>
            </div>
          </a>
        )}
        {guideUrl && (
          <a href={guideUrl} className="resource-link-btn" download>
            <Icon name="description" size={18} />
            <div>
              <span className="res-title">Panduan Instruksi (.md)</span>
              <span className="res-sub">Spesifikasi tugas & rubrik penilaian</span>
            </div>
          </a>
        )}
        {pdfUrl && (
          <a href={pdfUrl} className="resource-link-btn" target="_blank" rel="noreferrer">
            <Icon name="picture_as_pdf" size={18} />
            <div>
              <span className="res-title">Dokumen Cetak PDF</span>
              <span className="res-sub">Format cetak siap dibaca offline</span>
            </div>
          </a>
        )}
      </div>
    </div>
  );
}
