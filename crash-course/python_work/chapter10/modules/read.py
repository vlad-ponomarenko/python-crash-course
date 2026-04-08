from pathlib import Path

cats_path = Path("cats.txt")
dogs_path = Path("dogs.txt")

files = [cats_path, dogs_path]

for file in files:

    try:
        file = file.read_text()
        for line in file.splitlines():
            print(line)
    except FileNotFoundError:
        # print(f"The file {file} is missing.")
        pass
