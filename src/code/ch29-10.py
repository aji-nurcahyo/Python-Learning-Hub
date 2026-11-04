"""Chapter 29 Example 10: GitHub Actions CI Workflow Specification
Python Learning Hub - Professional Python Engineering
"""


class WorkflowValidator:
    """Validator struktur deklarasi pipeline Continuous Integration (CI)."""

    REQUIRED_TOP_KEYS = ["name", "on", "jobs"]

    @classmethod
    def validate_workflow_spec(cls, workflow: dict) -> list[str]:
        issues = []
        for key in cls.REQUIRED_TOP_KEYS:
            if key not in workflow:
                issues.append(f"Kunci wajib '{key}' tidak ditemukan di root deklarasi.")

        jobs = workflow.get("jobs", {})
        if not jobs:
            issues.append("Setidaknya harus ada satu job di dalam pipeline.")

        for job_name, job_spec in jobs.items():
            if "runs-on" not in job_spec:
                issues.append(f"Job '{job_name}' tidak memiliki spesifikasi runner 'runs-on'.")
            if "steps" not in job_spec or len(job_spec["steps"]) == 0:
                issues.append(f"Job '{job_name}' harus memiliki daftar 'steps' eksekusi.")

        return issues


def main() -> None:
    print("Memvalidasi Struktur Deklarasi GitHub Actions CI Pipeline:\n")

    ci_definition = {
        "name": "Production Quality Gate",
        "on": ["push", "pull_request"],
        "jobs": {
            "test-suite": {
                "runs-on": "ubuntu-latest",
                "steps": [
                    {"name": "Checkout Source", "uses": "actions/checkout@v4"},
                    {"name": "Setup Python 3.12", "uses": "actions/setup-python@v5"},
                    {"name": "Install Dependencies", "run": "pip install -r requirements.txt"},
                    {"name": "Run Automated Tests", "run": "pytest --cov=src"},
                ],
            }
        },
    }

    issues = WorkflowValidator.validate_workflow_spec(ci_definition)
    if not issues:
        print("[OK] Definisi Workflow CI valid dan memenuhi standar keamanan otomatisasi:")
        job = ci_definition["jobs"]["test-suite"]
        print(f" -> Pipeline Name : {ci_definition['name']}")
        print(f" -> Trigger Event : {ci_definition['on']}")
        print(f" -> Target Runner : {job['runs-on']}")
        print(f" -> Total Steps   : {len(job['steps'])} tahapan eksekusi")
    else:
        print(f"[ERROR] Ditemukan {len(issues)} ketidaksesuaian: {issues}")


if __name__ == "__main__":
    main()

