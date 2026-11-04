import { Icon } from '../ui/Icon';

export function LearningObjectives({ objectives }: { objectives: string[] }) {
  if (!objectives || objectives.length === 0) return null;

  return (
    <div className="learning-objectives-card">
      <div className="objectives-header">
        <Icon name="verified" size={20} />
        <h3>Target Capaian Pembelajaran</h3>
      </div>
      <ul className="objectives-list">
        {objectives.map((obj, i) => (
          <li key={i}>
            <Icon name="arrow_right_alt" size={16} className="objective-arrow" />
            <span>{obj}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}

