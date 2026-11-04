import { useState } from 'react';
import { Icon } from '../ui/Icon';

export function QuizCard({
  question,
  answer,
  hint,
}: {
  question: string;
  answer: string;
  hint?: string;
}) {
  const [revealed, setRevealed] = useState(false);
  const [showHint, setShowHint] = useState(false);

  return (
    <div className="quiz-card-component">
      <div className="quiz-badge">
        <Icon name="quiz" size={18} />
        <span>Cek Pemahaman Konseptual</span>
      </div>

      <h3 className="quiz-question">{question}</h3>

      {hint && (
        <div className="quiz-hint-box">
          <button
            type="button"
            className="quiz-hint-btn"
            onClick={() => setShowHint(!showHint)}
          >
            <Icon name="lightbulb" size={16} />
            <span>{showHint ? 'Sembunyikan Petunjuk' : 'Tampilkan Petunjuk'}</span>
          </button>
          {showHint && <p className="quiz-hint-text">{hint}</p>}
        </div>
      )}

      <div className="quiz-actions">
        <button
          type="button"
          className="button primary quiz-reveal-btn"
          aria-expanded={revealed}
          onClick={() => setRevealed(!revealed)}
        >
          <Icon name={revealed ? 'visibility_off' : 'visibility'} size={16} />
          <span>{revealed ? 'Tutup Kunci Pembahasan' : 'Buka Kunci Pembahasan'}</span>
        </button>
      </div>

      {revealed && (
        <div className="quiz-answer-panel" role="region" aria-label="Pembahasan jawaban">
          <div className="answer-heading">
            <Icon name="check_circle" size={18} />
            <b>Pembahasan & Analisis:</b>
          </div>
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
}

