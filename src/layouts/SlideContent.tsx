import { useState } from 'react';
import { Code } from '../ui/Code';
import { MathBlock } from '../ui/Math';
import { Icon } from '../ui/Icon';
import type { SlideData } from '../decks/registry';
import outputs from '../code/outputs.json';

const sources = import.meta.glob('../code/**/*.py', {
  query: '?raw',
  import: 'default',
  eager: true,
}) as Record<string, string>;

export function SlideContent({
  slide,
  meeting,
  base,
}: {
  slide: SlideData;
  meeting: number;
  base: string;
}) {
  const [answer, setAnswer] = useState(false);
  const files =
    slide.files ??
    (slide.example
      ? [{ name: `${slide.example.split('/').pop()}.py`, code: sources[`../code/${slide.example}.py`] }]
      : []);

  // Standardized Cover Slide (Requirement 1 & 3)
  if (slide.kind === 'cover') {
    return (
      <div className="slide-cover-layout">
        <div className="slide-kicker">
          PYTHON LEARNING HUB <span>/</span> CHAPTER {meeting.toString().padStart(2, '0')}
        </div>
        <h1 className="cover-title">{slide.title}</h1>
        <div className="cover-body" dangerouslySetInnerHTML={{ __html: slide.body }} />
        <div className="cover-meta-card">
          <div className="author-name">Aji Pamungkas Tri Nurcahyo</div>
          <div className="author-affiliation">Institut Teknologi Sumatera</div>
        </div>
        <div className="cover-number" aria-hidden="true">
          {meeting.toString().padStart(2, '0')}
        </div>
        <aside className="notes">{slide.notes}</aside>
      </div>
    );
  }

  return (
    <>
      <div className="slide-kicker">
        PYTHON LEARNING HUB <span>/</span> CHAPTER {meeting.toString().padStart(2, '0')}
      </div>
      <h1>{slide.title}</h1>

      <div className={slide.example ? 'code-layout' : 'content-layout'}>
        {slide.example && (
          <div className="code-column">
            {files.map((file) => (
              <Code key={file.name} {...file} />
            ))}
            {slide.dependency && (
              <p className="dependency">
                Simpan <a href={`${base}downloads/examples/${slide.dependency}`} download>{slide.dependency}</a> di folder yang sama.
              </p>
            )}
          </div>
        )}

        <div className="explanation">
          <div dangerouslySetInnerHTML={{ __html: slide.body }} />

          {slide.example && (
            <div className="output-card">
              <h2>
                <Icon name="terminal" size={16} /> Output Terminal · Python 3
              </h2>
              <pre tabIndex={0}>
                {(outputs as Record<string, string>)[slide.example] || '(Program selesai tanpa output teks)'}
              </pre>
              <small>Hasil eksekusi nyata CPython.</small>
              <div className="output-actions">
                <a className="text-link" href={`${base}downloads/examples/${slide.example}.py`} download>
                  <Icon name="download" size={14} /> Unduh {slide.example.split('/').pop()}.py
                </a>
                {slide.files && (
                  <a className="text-link" href={`${base}downloads/examples/p09-module/statistik.py`} download>
                    <Icon name="download" size={14} /> Unduh statistik.py
                  </a>
                )}
              </div>
            </div>
          )}

          {slide.title === 'Studi kasus: rata-rata RSRP' && (
            <div className="math-card compact">
              <span className="math-label">Formula Rata-rata Sinyal:</span>
              <MathBlock tex={'\\bar{x} = \\frac{1}{n} \\sum_{i=1}^{n} x_i'} />
            </div>
          )}

          {slide.title === 'Pencarian linear (linear search)' && (
            <div className="math-card compact">
              <span className="math-label">Kompleksitas Waktu Kasus Terburuk:</span>
              <MathBlock tex={'T(n) = \\mathcal{O}(n)'} />
            </div>
          )}

          {slide.title === 'Selection sort: algoritma manual' && (
            <div className="math-card compact">
              <span className="math-label">Kompleksitas Komparasi Selection Sort:</span>
              <MathBlock tex={'\\sum_{i=1}^{n-1} (n - i) = \\frac{n(n-1)}{2} = \\mathcal{O}(n^2)'} />
            </div>
          )}

          {slide.kind === 'question' && (
            <div className="question-card">
              <h2>
                <Icon name="quiz" size={20} /> {slide.question}
              </h2>
              <button
                className="button primary"
                aria-expanded={answer}
                onClick={() => setAnswer(!answer)}
              >
                <Icon name={answer ? 'visibility_off' : 'visibility'} size={16} />
                <span>{answer ? 'Tutup pembahasan' : 'Buka pembahasan'}</span>
              </button>
              {answer && <p className="answer">{slide.answer}</p>}
            </div>
          )}

          {slide.kind === 'exercise' && (
            <div className="exercise-tip">
              <Icon name="lightbulb" size={18} />
              <span>Kerjakan bertahap: rancang input & output → uji kasus normal → uji kasus batas → dokumentasikan hasil.</span>
            </div>
          )}
        </div>
      </div>

      <footer className="slide-footer">
        <span>Python Learning Hub • Aji Pamungkas Tri Nurcahyo</span>
        <span>Chapter {meeting.toString().padStart(2, '0')}</span>
      </footer>

      <aside className="notes">{slide.notes}</aside>
    </>
  );
}
