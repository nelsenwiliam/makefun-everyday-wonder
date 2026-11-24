"""Write one sentence of everyday wonder to entry.txt (pure stdlib)."""

import os

LINE = "My shadow arrived at the corner before I did, and for a second it looked like it knew where it was going."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "line must be a single line"
    assert text.endswith("."), "line must end with a period"
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
