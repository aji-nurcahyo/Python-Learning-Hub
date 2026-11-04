import { Icon } from '../ui/Icon';

export function PrerequisiteList({ prerequisites }: { prerequisites: string[] }) {
  if (!prerequisites || prerequisites.length === 0) {
    return (
      <div className="prereq-box empty">
        <Icon name="check_circle" size={16} />
        <span>Tidak ada prasyarat khusus. Cocok untuk pembelajar awal.</span>
      </div>
    );
  }

  return (
    <div className="prereq-box">
      <div className="prereq-title">
        <Icon name="lock_open" size={16} />
        <span>Prasyarat Pembelajaran:</span>
      </div>
      <div className="prereq-tags">
        {prerequisites.map((p, idx) => (
          <span key={idx} className="prereq-tag">
            {p}
          </span>
        ))}
      </div>
    </div>
  );
}

