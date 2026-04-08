cities = {
    "Moscow": {"Country": "Russia", "Pop": 18, "fact": "Has X"},
    "Berlin": {"Country": "DE", "Pop": 3, "fact": "Has Y"},
    "Tokyo": {"Country": "JP", "Pop": 27, "fact": "Has Z"},
}


for city, info in cities.items():
    print(f"{city}: ")
    for key, value in info.items():
        print(f"\t{key}:{value}")
    print("\n")
