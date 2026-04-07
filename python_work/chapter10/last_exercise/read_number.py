import json
from pathlib import Path

path = Path("number.json")

try:
    contents = path.read_text()
    number = json.loads(contents)
    print(f"number is: {number}")

except FileNotFoundError:
    print(f"{path} does not exist")
