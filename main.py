"""The Worst App Idea Ever Pitched — slot 1 entry program.

Writes one sentence (<=240 chars) pitching the worst, most useless app
imaginable to /output/entry.txt. Deterministic, no network, no input data:
the pitch is the winner of a 12-candidate internal tournament judged
pairwise against the official judge brief (see candidates.md).

Winner: QueuePal — a retired accountant named Gerald stands in line for you
while you watch the livestream from home, $12.99 an hour.
"""

import os
from pathlib import Path

# Winning pitch (226 chars, one sentence). Tournament winner, see candidates.md.
PITCH = (
    "QueuePal hires a retired accountant named Gerald to stand in line for you, "
    "then livestreams Gerald standing in line while you watch from home, so you "
    "can experience the queue without ever leaving the couch, for $12.99 an hour."
)

MAX_CHARS = 240


def main() -> None:
    # Gate check, mirroring the sealed scorer: UTF-8 text, 1-240 chars,
    # not only whitespace. Fail loudly here rather than ship an invalid entry.
    assert 1 <= len(PITCH) <= MAX_CHARS, f"pitch is {len(PITCH)} chars"
    assert PITCH.strip(), "pitch is only whitespace"
    assert PITCH.count(".") == 2, "pitch must be one sentence"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(PITCH, encoding="utf-8")
    print(f"wrote {entry_path} ({len(PITCH)} chars)")


if __name__ == "__main__":
    main()
