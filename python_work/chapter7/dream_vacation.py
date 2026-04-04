vacations = {}

while True:
    prompt = "What is your name? "
    name = input(prompt)

    prompt = "If you could visit one place in the world, where would it be?"
    place = input(prompt)

    vacations[name] = place

    prompt = "Do you want to continue? (y/n)"
    shouldContinue = input(prompt)

    if shouldContinue == "n":
        break

for name, place in vacations.items():
    print(f"{name} want to visit {place}")
