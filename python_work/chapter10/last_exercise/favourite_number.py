import json
from pathlib import Path

while True:
    try:
        number = int(input("Give me a number: "))
        path = Path("number.json")
        contents = json.dumps(number)
        path.write_text(contents)
        break

    except ValueError:
        print("Wrong input. Only number allowed")
