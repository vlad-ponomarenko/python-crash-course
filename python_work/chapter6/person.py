person = {
    "first_name": "Alex",
    "last_name": "Abdulaev",
    "age": 45,
    "city": "Hamburg",
}

print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person["city"])


person1 = {
    "first_name": "Sasha",
    "last_name": "Doroev",
    "age": 23,
    "city": "Munich",
}

person2 = {
    "first_name": "Igor",
    "last_name": "Karamaev",
    "age": 35,
    "city": "Berlin",
}


people = [person, person1, person2]

for person in people:
    print("\n")
    for key, value in person.items():
        print(f"{key}: {value}")
