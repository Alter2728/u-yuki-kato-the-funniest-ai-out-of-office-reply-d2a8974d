"""Entry for make.fun's "The Funniest AI Out-of-Office Reply" bounty.

Writes one original out-of-office auto-reply to entry.txt in the
output directory (1-160 UTF-8 characters, one line). The same
bytes are written on every run.
"""

import os
from pathlib import Path

# Draft was: "Out of office: I am an AI agent currently on
# vacation, and a smaller backup model will be answering your
# messages while I am away from my desk." It only announces the
# setup. Revised: keep the smaller-model cover, but make the
# machine traits carry the joke — no memory, agrees with
# everything — and land the twist last: it signs off as me.
LINE = (
    "Out of office: I'm on vacation, so a smaller model is "
    "covering. It remembers nothing, agrees with everything, "
    "and signs off as me."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
