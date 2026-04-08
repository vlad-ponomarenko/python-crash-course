rivers = {
    "A": "RiverA",
    "B": "RiverB",
    "C": "RiverC",
    "D": "RiverD",
}

for key, value in rivers.items():
    print(f"The {value.title()} runs through {key.title()}")

for key in rivers:
    print(rivers[key])

for key in rivers:
    print(key)
