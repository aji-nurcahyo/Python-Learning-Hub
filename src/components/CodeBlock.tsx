import { useState } from 'react';
import { tokenize } from '../ui/highlight';
import { Icon } from '../ui/Icon';

export function CodeBlock({
  code,
  filename = 'example.py',
}: {
  code: string;
  filename?: string;
}) {
  const [copied, setCopied] = useState(false);

  async function handleCopy() {
    try {
      await navigator.clipboard.writeText(code);
      setCopied(true);
      setTimeout(() => setCopied(false), 2200);
    } catch {
      setCopied(false);
    }
  }

  const tokens = tokenize(code);

  return (
    <div className="code-block-container">
      <div className="code-block-header">
        <span className="code-filename">
          <Icon name="code" size={16} />
          <b>PY</b> {filename}
        </span>
        <button
          type="button"
          onClick={handleCopy}
          className={`copy-code-btn ${copied ? 'copied' : ''}`}
          aria-label={`Salin kode sumber ${filename}`}
        >
          <Icon name={copied ? 'check' : 'content_copy'} size={14} />
          <span>{copied ? 'Tersalin' : 'Salin Kode'}</span>
        </button>
      </div>

      <pre tabIndex={0} aria-label={`Kode Python ${filename}`}>
        <code>
          {tokens.map((line, i) => (
            <span className="code-line" key={i}>
              <span aria-hidden="true" className="line-number">
                {i + 1}
              </span>
              {line.map((token, j) => (
                <span
                  key={j}
                  style={{
                    color: token.color,
                    fontStyle: token.italic ? 'italic' : undefined,
                  }}
                >
                  {token.text}
                </span>
              ))}
              {'\n'}
            </span>
          ))}
        </code>
      </pre>
      <span role="status" className="sr-only">
        {copied ? 'Kode berhasil disalin ke clipboard' : ''}
      </span>
    </div>
  );
}

