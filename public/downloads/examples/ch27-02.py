"""Chapter 27 Example 02: Threading Basics & Thread Lifecycle
Python Learning Hub - Professional Python Engineering
"""

import threading
import time


def ping_node(node_id: str, results: dict[str, str]) -> None:
    """Mensimulasikan operasi I/O latency ping simpul jaringan di thread terpisah."""
    time.sleep(0.02)
    results[node_id] = "REACHABLE (24ms)"


def main() -> None:
    nodes = ["BTS-JKT-01", "BTS-BDG-02", "BTS-SMG-03"]
    threads: list[threading.Thread] = []
    results: dict[str, str] = {}

    print("Memulai multi-threaded ping simpul...")
    for node in nodes:
        t = threading.Thread(target=ping_node, args=(node, results), name=f"Thread-{node}")
        threads.append(t)
        t.start()

    # Menunggu seluruh thread menyelesaikan tugasnya (join)
    for t in threads:
        t.join()

    print("Hasil Ping Node (Terurut):")
    for node in sorted(results.keys()):
        print(f" * {node}: {results[node]}")


if __name__ == "__main__":
    main()

