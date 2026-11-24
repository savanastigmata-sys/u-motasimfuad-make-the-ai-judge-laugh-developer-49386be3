#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line developer excuse to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

EXCUSE = "The code worked fine until the users started using it correctly."


def validate(text: str) -> str:
    """Enforce the competition gate: UTF-8 text of 1 to 200 characters,
    not only white space, and a single line. Fail loudly instead of
    submitting an invalid line."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("excuse must not be only white space")
    if len(text) > 200:
        raise ValueError(f"excuse is {len(text)} characters, over the 200 limit")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("excuse must be a single line")
    return text


def resolve_output_dir() -> str:
    """Prefer MAKEFUN_OUTPUT_DIR; fall back to ./output when the
    configured directory cannot be created (e.g. a local dev run)."""
    preferred = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(preferred, exist_ok=True)
        return preferred
    except OSError:
        fallback = os.path.join(os.getcwd(), "output")
        os.makedirs(fallback, exist_ok=True)
        return fallback


def main() -> int:
    line = validate(EXCUSE)
    out_dir = resolve_output_dir()
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
