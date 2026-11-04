import { Icon } from '../ui/Icon';

export function ExerciseCard({
  title,
  instructions,
  tips,
  timeEstimate = '15–20 menit',
}: {
  title: string;
  instructions: string[];
  tips?: string;
  timeEstimate?: string;
}) {
  return (
    <div className="exercise-card-component">
      <div className="exercise-card-top">
        <div className="exercise-badge">
          <Icon name="fitness_center" size={18} />
          <span>Latihan Terarah</span>
        </div>
        <span className="exercise-time">
          <Icon name="timer" size={16} /> Estimasi: {timeEstimate}
        </span>
      </div>

      <h3 className="exercise-title">{title}</h3>

      <div className="exercise-steps">
        <b>Langkah Pengerjaan:</b>
        <ol>
          {instructions.map((step, idx) => (
            <li key={idx}>{step}</li>
          ))}
        </ol>
      </div>

      {tips && (
        <div className="exercise-tip-box">
          <Icon name="tips_and_updates" size={18} />
          <div>
            <b>Tips Pengujian:</b>
            <p>{tips}</p>
          </div>
        </div>
      )}
    </div>
  );
}

