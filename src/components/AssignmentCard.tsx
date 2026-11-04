import { useState } from 'react';
import { Icon } from '../ui/Icon';
import { CodeBlock } from './CodeBlock';

export interface RubricItem {
  criteria: string;
  weight: number;
  description: string;
}

export interface AssignmentCardProps {
  title: string;
  description: string;
  instructions: string[];
  rubric: RubricItem[];
  starterCode?: string;
  starterFilename?: string;
  downloadMdUrl?: string;
  downloadPyUrl?: string;
  deadlineNotice?: string;
}

export function AssignmentCard({
  title,
  description,
  instructions,
  rubric,
  starterCode,
  starterFilename = 'tugas.py',
  downloadMdUrl,
  downloadPyUrl,
  deadlineNotice = 'Kerjakan secara mandiri atau dalam kelompok praktikum sesuai arahan instruktur.',
}: AssignmentCardProps) {
  const [showStarter, setShowStarter] = useState(false);

  const totalWeight = rubric.reduce((sum, item) => sum + item.weight, 0);

  return (
    <div className="assignment-card-component">
      <div className="assignment-card-top">
        <div className="assignment-badge">
          <Icon name="assignment" size={20} />
          <span>Tugas & Praktik Mandiri</span>
        </div>
        <span className="assignment-notice">
          <Icon name="verified_user" size={16} /> Rubrik Terstruktur (100%)
        </span>
      </div>

      <h3 className="assignment-title">{title}</h3>
      <p className="assignment-desc">{description}</p>

      <div className="assignment-instructions">
        <h4>
          <Icon name="format_list_numbered" size={18} /> Petunjuk Pengerjaan
        </h4>
        <ol>
          {instructions.map((step, idx) => (
            <li key={idx}>{step}</li>
          ))}
        </ol>
      </div>

      {starterCode && (
        <div className="assignment-starter-section">
          <button
            type="button"
            className="starter-toggle-button"
            onClick={() => setShowStarter((prev) => !prev)}
            aria-expanded={showStarter}
          >
            <Icon name={showStarter ? 'expand_less' : 'code'} size={18} />
            <span>{showStarter ? 'Sembunyikan Kode Starter' : `Lihat Template Starter Code (${starterFilename})`}</span>
          </button>
          {showStarter && (
            <div className="starter-code-box">
              <CodeBlock code={starterCode} filename={starterFilename} />
            </div>
          )}
        </div>
      )}

      <div className="assignment-rubric-section">
        <h4>
          <Icon name="fact_check" size={18} /> Rubrik Penilaian ({totalWeight}%)
        </h4>
        <div className="rubric-table-wrapper">
          <table className="rubric-table">
            <thead>
              <tr>
                <th style={{ width: '30%' }}>Kriteria Penilaian</th>
                <th style={{ width: '15%', textAlign: 'center' }}>Bobot</th>
                <th style={{ width: '55%' }}>Deskripsi Capaian</th>
              </tr>
            </thead>
            <tbody>
              {rubric.map((item, idx) => (
                <tr key={idx}>
                  <td className="rubric-criteria">
                    <strong>{item.criteria}</strong>
                  </td>
                  <td className="rubric-weight">{item.weight}%</td>
                  <td className="rubric-desc">{item.description}</td>
                </tr>
              ))}
            </tbody>
            <tfoot>
              <tr>
                <td><strong>Total Akumulasi</strong></td>
                <td className="rubric-weight"><strong>{totalWeight}%</strong></td>
                <td>Standar penilaian kualitas rekayasa kode Python</td>
              </tr>
            </tfoot>
          </table>
        </div>
      </div>

      <div className="assignment-actions">
        {downloadMdUrl && (
          <a className="button primary" href={downloadMdUrl} download>
            <Icon name="download" size={16} /> <span>Unduh Panduan (.md)</span>
          </a>
        )}
        {downloadPyUrl && (
          <a className="button subtle" href={downloadPyUrl} download>
            <Icon name="download" size={16} /> <span>Unduh Starter (.py)</span>
          </a>
        )}
        <div className="assignment-deadline-info">
          <Icon name="info" size={16} />
          <span>{deadlineNotice}</span>
        </div>
      </div>
    </div>
  );
}
