export function DifficultyBadge({
  difficulty,
}: {
  difficulty: 'Beginner' | 'Intermediate' | 'Advanced';
}) {
  const cls =
    difficulty === 'Beginner'
      ? 'diff-beginner'
      : difficulty === 'Intermediate'
      ? 'diff-intermediate'
      : 'diff-advanced';

  return <span className={`difficulty-badge ${cls}`}>{difficulty}</span>;
}

