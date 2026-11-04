import { Icon } from '../ui/Icon';
import { getAssetUrl } from '../curriculum/resources';

interface ResourceDownloadsProps {
  pptxUrl?: string | null;
  starterCodeUrl?: string | null;
  guideUrl?: string | null;
  pdfUrl?: string | null;
}

export function ResourceDownloads({
  pptxUrl,
  starterCodeUrl,
  guideUrl,
  pdfUrl,
}: ResourceDownloadsProps) {
  const resolvedPptx = pptxUrl ? getAssetUrl(pptxUrl) : null;
  const resolvedCode = starterCodeUrl ? getAssetUrl(starterCodeUrl) : null;
  const resolvedGuide = guideUrl ? getAssetUrl(guideUrl) : null;
  const resolvedPdf = pdfUrl ? getAssetUrl(pdfUrl) : null;

  return (
    <div className="chapter-resources-panel">
      <div className="resources-heading">
        <Icon name="folder_zip" size={20} />
        <h4>Berkas & Sumber Pembelajaran Chapter</h4>
      </div>
      <div className="resources-links-grid">
        {resolvedPptx ? (
          <a href={resolvedPptx} className="resource-link-btn" download>
            <Icon name="file_present" size={18} />
            <div>
              <span className="res-title">Slide Presentasi (.pptx)</span>
              <span className="res-sub">PowerPoint sumber dapat disunting</span>
            </div>
          </a>
        ) : (
          <div
            className="resource-link-btn disabled"
            aria-disabled="true"
            title="Slide PowerPoint belum tersedia untuk modul ini"
          >
            <Icon name="block" size={18} />
            <div>
              <span className="res-title">PowerPoint belum tersedia</span>
              <span className="res-sub">Materi disajikan via Reveal.js interaktif</span>
            </div>
          </div>
        )}

        {resolvedCode && (
          <a href={resolvedCode} className="resource-link-btn" download>
            <Icon name="code" size={18} />
            <div>
              <span className="res-title">Starter Code Python (.py)</span>
              <span className="res-sub">Template pengerjaan latihan & tugas</span>
            </div>
          </a>
        )}

        {resolvedGuide && (
          <a href={resolvedGuide} className="resource-link-btn" download>
            <Icon name="description" size={18} />
            <div>
              <span className="res-title">Panduan Instruksi (.md)</span>
              <span className="res-sub">Spesifikasi tugas & rubrik penilaian</span>
            </div>
          </a>
        )}

        {resolvedPdf && (
          <a href={resolvedPdf} className="resource-link-btn" target="_blank" rel="noreferrer">
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
