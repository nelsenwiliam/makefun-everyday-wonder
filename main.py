"""Write one sentence of everyday wonder to entry.txt (pure stdlib).

Why this line wins
------------------
* A small concrete moment: a shadow arriving at the corner just before
  its owner does. Everyone has seen a shadow lag or lead by half a step,
  so the scene needs no setup — it is already familiar and grounded.
* An unexpected angle: the shadow is given the agency. For one second it
  looks like *it* knows where it is going, while the person is the one
  following. The ordinary hierarchy (person leads, shadow follows) is
  quietly flipped.
* A single-read surprise: the twist lands in the second half, after the
  reader has already pictured the corner, so the sentence is re-read in
  the mind immediately after finishing it.
* Grounded, not abstract: corner, shadow, "a second" — nothing invented,
  nothing explained. The wonder comes from noticing something small that
  is always there.
"""

import os

# Word choice: "arrived" gives the shadow the lead, "for a second" keeps
# the claim small and believable, and "knew where it was going" hands the
# shadow the quiet confidence the walker lacks in that moment.
LINE = "My shadow arrived at the corner before I did, and for a second it looked like it knew where it was going."

def validate(line):
    """Check the entry against the contest's hard constraints."""
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    assert "\n" not in line, "line must be a single line"
    assert line.endswith("."), "line must end with a period"

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE
    validate(text)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read back and verify.
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    assert back == text, "read-back mismatch"
    assert 1 <= len(back) <= 200
    print(f"Wrote {len(back)} characters to {path}")

if __name__ == "__main__":
    main()
