import sys
import glob

def main():
    # Find all Markdown files in participants/ EXCEPT README.md
    files = glob.glob("participants/*.md")
    files = [f for f in files if not f.endswith("README.md")]

    if not files:
        # It's okay if no files exist yet (e.g., someone just editing roster.md)
        sys.exit(0)

    for record in files:
        with open(record, encoding="utf-8") as f:
            content = f.read()

        # Simple verification checks
        if "## About Me" not in content:
            fail(f"File {record} is missing the '## About Me' heading.")
        
        if "## Contact" not in content:
            fail(f"File {record} is missing the '## Contact' heading.")
        
        if "[你的名字或暱稱]" in content:
            fail(f"File {record} still has the placeholder '[你的名字或暱稱]'. Please update it!")
        
        if "你的帳號" in content:
            fail(f"File {record} still has the placeholder '你的帳號'. Please update it!")

    print("[PASS] All participant files passed formatting checks!")
    sys.exit(0)

def fail(message: str):
    print(f"[FAIL] Format check FAILED:\n   {message}", file=sys.stderr)
    sys.exit(1)

if __name__ == "__main__":
    main()
