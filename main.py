#!/usr/bin/env python3
"""One Line, Big Laugh — variant A entry.

Writes the chosen one-liner to /output/entry.txt first (the grader reads
it from there), then best-effort copies it next to this script in the repo
root. The repo is read-only in the grader sandbox, so the copy is wrapped
in try/except and must never fail the run. Output is exactly LINE, no
trailing newline added.
"""

import os

LINE = "Our policy deletes accounts inactive for 90 days, so my agent deleted mine \u2014 it writes all my code now."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Best-effort repo-root copy only; the grader sandbox is read-only.
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        pass


if __name__ == "__main__":
    main()
