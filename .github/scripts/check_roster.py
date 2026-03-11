import re
import sys

ROSTER_FILE = "roster.md"

ENTRY_PATTERN = re.compile(
    r"^- \[.+\]\(https://github\.com/[A-Za-z0-9_.-]+\)\s*[-—]\s*.+$"
)

def main():
    with open(ROSTER_FILE, encoding="utf-8") as f:
        lines = f.readlines()

    if not lines or not lines[0].startswith("# NPC"):
        fail("It looks like the file header was modified or deleted. Please restore the original lines 1-4!")

    if len(lines) < 6:
        fail("roster.md has fewer than 6 lines. Did you add your entry to Line 6?")

    entry = lines[5].rstrip("\n")

    if entry == "- [Your Name](https://github.com/YOUR_USERNAME) - Your Department, Year X":
        print("[PASS] roster.md is untouched (template present).")
        sys.exit(0)

    if not ENTRY_PATTERN.match(entry):
        fail(
            f"Line 6 does not match the required format.\n"
            f"  Got      : {entry!r}\n"
            f"  Expected : - [Your Name](https://github.com/YOUR_USERNAME) - Your Department, Year X"
        )

    if "YOUR_USERNAME" in entry or "Your Name" in entry or "Your Department" in entry:
        fail("Looks like you left the placeholder text in. Replace it with your real info!")

    print(f"[PASS] Format check passed!\n   Entry: {entry}")
    sys.exit(0)

def fail(message: str):
    print(f"[FAIL] Format check FAILED:\n   {message}", file=sys.stderr)
    sys.exit(1)

if __name__ == "__main__":
    main()
