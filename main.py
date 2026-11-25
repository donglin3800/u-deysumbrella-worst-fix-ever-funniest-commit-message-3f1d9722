"""Worst Fix Ever: one commit message about a fix that backfired.

The fix in the message silences a smoke alarm by taking out its
batteries. The alarm stops beeping, which was the complaint, and the
house keeps burning, which was the actual problem. The repair works
on the symptom and leaves the disaster untouched.

The program is deterministic: no network, no clock, no randomness.
It always writes the same single line to entry.txt.
"""

import os

MESSAGE = (
    "fix: silence the smoke alarm by removing its batteries "
    "\u2014 quiet house, still on fire"
)


def check_message(text):
    """Refuse anything that would fail the gate before writing it."""
    if not text or text != text.strip():
        raise ValueError("message must not be empty or padded")
    if "\n" in text or "\r" in text:
        raise ValueError("message must be a single line")
    if not 1 <= len(text) <= 100:
        raise ValueError("message must be 1-100 characters, got %d" % len(text))
    return text


def main():
    message = check_message(MESSAGE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(message + "\n")
    with open(path, encoding="utf-8") as handle:
        if handle.read() != message + "\n":
            raise RuntimeError("entry on disk does not match the message")
    print("Wrote %r to %s" % (message, path))


if __name__ == "__main__":
    main()
