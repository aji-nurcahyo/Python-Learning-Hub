import { AssignmentCard, type RubricItem } from './AssignmentCard';

export interface AssignmentData {
  title: string;
  description: string;
  instructions: string[];
  rubric: RubricItem[];
  starterCode?: string;
  starterFilename?: string;
  downloadMdUrl?: string;
  downloadPyUrl?: string;
}

interface AssignmentSectionProps {
  assignment: AssignmentData;
}

export function AssignmentSection({ assignment }: AssignmentSectionProps) {
  return (
    <AssignmentCard
      title={assignment.title}
      description={assignment.description}
      instructions={assignment.instructions}
      rubric={assignment.rubric}
      starterCode={assignment.starterCode}
      starterFilename={assignment.starterFilename}
      downloadMdUrl={assignment.downloadMdUrl}
      downloadPyUrl={assignment.downloadPyUrl}
    />
  );
}
