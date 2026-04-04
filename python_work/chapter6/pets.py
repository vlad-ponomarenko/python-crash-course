cat = {"name": "A", "type": "cat"}

dog = {"name": "B", "type": "dog"}

bird = {"name": "c", "type": "HaWk"}

pets = [cat, dog, bird]

for pet in pets:
    for k, v in pet.items():
        print(f"{k}:{v}")
