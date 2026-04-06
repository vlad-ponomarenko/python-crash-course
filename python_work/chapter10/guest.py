from pathlib import Path


path = Path("guests.txt")
names = ""

while True:
    name = input("Give me your name (or enter quit to stop): ")
    if name == "quit":
        break
    names += f"{name}\n"

path.write_text(names)
