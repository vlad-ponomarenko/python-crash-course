from pathlib import Path

path = Path("alice.txt")

try:
    # Adding encoding='utf-8' is a great habit for reading books/files
    contents = path.read_text(encoding="utf-8")

    # 1. Lowercase everything
    # 2. Split into a list of individual words
    words = contents.lower().split()

    # 3. Count exact matches in that list
    count = words.count("the")

    print(f"The word 'the' appears {count} times.")

except FileNotFoundError:
    print(f"The file {path} was not found.")
