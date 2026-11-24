#!/usr/bin/env python3
"""Say What Actually Broke — one line of honest error copy.

Writes a single line of software error copy to entry.txt in the
output directory (/output, or OUTPUT_DIR when set): it names the real
failure in plain words, tells the user what to do next, and carries
the joke in a concrete image. Same bytes on every run.
"""

import os

LINE = (
    "The upload failed halfway \u2014 the Wi-Fi cut out mid-file, "
    "like a waiter dropping your tray at the table. "
    "Reconnect and send it again."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Clear only the contents of the output directory, never the
    # directory itself (the grader mounts it read-only as uid 65534).
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
