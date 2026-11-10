import argparse


def run_cli(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Runner otomasi terjadwal (cron / Task Scheduler)")
    parser.add_argument("--job-date", required=True, help="Tanggal batch YYYY-MM-DD")
    parser.add_argument("--simulate-fail", action="store_true", help="Simulasikan kegagalan untuk cek exit code")
    args = parser.parse_args(argv)

    if args.simulate_fail:
        print(f"[ERROR] Job tanggal {args.job_date} gagal dieksekusi.")
        return 1
    print(f"[OK] Job tanggal {args.job_date} selesai bersih.")
    return 0


if __name__ == "__main__":
    code_ok = run_cli(["--job-date", "2025-02-01"])
    code_err = run_cli(["--job-date", "2025-02-01", "--simulate-fail"])
    print("Exit code sukses:", code_ok, "| Exit code gagal:", code_err)
