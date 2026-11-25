"""Funniest One-Line Out-of-Office Reply — one-line OOO reply entry.

The entry is a single out-of-office email auto-reply, one line long.
It writes the reply to /output/entry.txt deterministically.

Craft: it reads like a real away message, then turns on the inbox
itself — the thing left in charge has quit, which is the joke's punch
on the last word, with no beach or limited-email cliché.
"""

import os


ENTRY = "Out of office. I left my inbox in charge and it has already resigned."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    tmp_path = os.path.join(out_dir, ".entry.txt.tmp")
    final_path = os.path.join(out_dir, "entry.txt")
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, final_path)
    os.chmod(final_path, 0o644)


if __name__ == "__main__":
    main()
