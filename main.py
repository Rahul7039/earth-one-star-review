#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun entry.

Writes the chosen one-sentence alien review of Earth, byte-identical,
to /output/entry.txt. The line is a fixed constant; it is never
generated or paraphrased at runtime.
"""

import os

ENTRY = "One star — I came to conquer, stayed because the dosa was glorious, and left because your species charges money for water that falls free from the sky."

# Gate: one sentence, at most 200 characters, not only whitespace.
assert ENTRY.strip(), "entry must not be blank"
assert "\n" not in ENTRY, "entry must be a single line"
assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "entry must be one sentence"
assert len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters, over the 200 limit"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
