import { Icon } from '../ui/Icon';

export function CodeOutput({
  output,
  downloadUrl,
  filename,
}: {
  output: string;
  downloadUrl?: string;
  filename?: string;
}) {
  return (
    <div className="code-output-container">
      <div className="output-header">
        <span className="output-title">
          <Icon name="terminal" size={16} /> Output Eksekusi CPython 3
        </span>
        {downloadUrl && (
          <a href={downloadUrl} download className="output-download-link">
            <Icon name="download" size={14} /> Unduh {filename || '.py'}
          </a>
        )}
      </div>
      <pre tabIndex={0} aria-label="Output terminal hasil eksekusi program">
        {output || '(Program selesai dieksekusi tanpa keluaran teks)'}
      </pre>
      <div className="output-footer-note">
        <Icon name="info" size={14} />
        <small>Hasil eksekusi riil CPython standar. Lingkungan Python lokal tidak mengubah kode sumber.</small>
      </div>
    </div>
  );
}

