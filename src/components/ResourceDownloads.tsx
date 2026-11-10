import { Icon } from '../ui/Icon';
import { getAssetUrl } from '../curriculum/resources';

interface ResourceDownloadsProps {
  pptxUrl?: string | null;
  starterCodeUrl?: string | null;
  notebookUrl?: string | null;
  datasetUrl?: string | null;
  guideUrl?: string | null;
  pdfUrl?: string | null;
}

export function ResourceDownloads({
  pptxUrl,
  starterCodeUrl,
  notebookUrl,
  datasetUrl,
  guideUrl,
  pdfUrl,
}: ResourceDownloadsProps) {
  const resolvedPptx = pptxUrl ? getAssetUrl(pptxUrl) : null;
  const resolvedCode = starterCodeUrl ? getAssetUrl(starterCodeUrl) : null;
  const resolvedNotebook = notebookUrl ? getAssetUrl(notebookUrl) : null;
  const resolvedDataset = datasetUrl ? getAssetUrl(datasetUrl) : null;
  const resolvedGuide = guideUrl ? getAssetUrl(guideUrl) : null;
  const resolvedPdf = pdfUrl ? getAssetUrl(pdfUrl) : null;

  if (
    !resolvedPptx &&
    !resolvedCode &&
    !resolvedNotebook &&
    !resolvedDataset &&
    !resolvedGuide &&
    !resolvedPdf
  ) {
    return null;
  }

  return (
    <div className="chapter-resources-panel">
      <div className="resources-heading">
        <Icon name="folder_zip" size={20} />
        <h4>Unduhan & Sumber Pembelajaran Chapter</h4>
      </div>
      <div className="resources-links-grid">
        {resolvedPptx && (
          <a href={resolvedPptx} className="resource-link-btn" download>
            <Icon name="file_present" size={18} />
            <div>
              <span className="res-title">Download PPTX</span>
              <span className="res-sub">Slide PowerPoint sumber (.pptx)</span>
            </div>
          </a>
        )}

        {resolvedCode && (
          <a href={resolvedCode} className="resource-link-btn" download>
            <Icon name="code" size={18} />
            <div>
              <span className="res-title">Download Python Code</span>
              <span className="res-sub">Berkas contoh & latihan Python (.py)</span>
            </div>
          </a>
        )}

        {resolvedNotebook && (
          <a href={resolvedNotebook} className="resource-link-btn" download>
            <Icon name="menu_book" size={18} />
            <div>
              <span className="res-title">Download Notebook</span>
              <span className="res-sub">Dokumen Jupyter Notebook (.ipynb)</span>
            </div>
          </a>
        )}

        {resolvedDataset && (
          <a href={resolvedDataset} className="resource-link-btn" download>
            <Icon name="table_chart" size={18} />
            <div>
              <span className="res-title">Download Dataset</span>
              <span className="res-sub">Berkas data pendukung latihan</span>
            </div>
          </a>
        )}

        {resolvedGuide && (
          <a href={resolvedGuide} className="resource-link-btn" download>
            <Icon name="description" size={18} />
            <div>
              <span className="res-title">Download Assignment Guide</span>
              <span className="res-sub">Panduan tugas & rubrik penilaian (.md)</span>
            </div>
          </a>
        )}

        {resolvedPdf && (
          <a href={resolvedPdf} className="resource-link-btn" target="_blank" rel="noreferrer">
            <Icon name="picture_as_pdf" size={18} />
            <div>
              <span className="res-title">Download PDF</span>
              <span className="res-sub">Format cetak siap dibaca offline</span>
            </div>
          </a>
        )}
      </div>
    </div>
  );
}
