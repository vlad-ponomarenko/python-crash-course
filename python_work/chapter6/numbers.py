numbers = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
}

for key in numbers:
    print(f"{key}'s favourite number is: {numbers[key]}")


numbers = {
    "A": [1, 2, 3],
    "B": [2, 3, 4],
    "C": 3,
    "D": 4,
    "E": 5,
}

for name, numbers in numbers.items():
    print(f"{name.title}'s favourite numbers are:")
    for number in numbers:
        print(number)
