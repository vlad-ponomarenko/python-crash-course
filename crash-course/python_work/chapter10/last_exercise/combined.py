import json
from pathlib import Path


path = Path("number.json")


def greet_user(contents):
    user_info = json.loads(contents)
    print(f"Welcome Back, {user_info['name']}")


def register_new_user():
    name = input("Give me a name: ")
    number = int(input("Give me a number: "))
    age = int(input("Give me a your age: "))

    user_info = {"name": name, "number": number, "age": age}

    contents = json.dumps(user_info)
    path.write_text(contents)
    print(f"A user with the following info {contents} has been written to a file!")


try:
    if path.exists():

        contents = path.read_text()
        username = json.loads(contents)["name"]

        verification = input(f"Is your name {username} (y/n)? ")
        if verification.lower() == "n":
            register_new_user()
        else:
            greet_user(contents)

    else:
        register_new_user()


except ValueError:
    print("Please, provide a number, not a string!")
