while True:
    age = input("How old are you? ")
    if age == "quit":
        break

    age = int(age)

    price = 3
    if age > 12:
        price = 15
    elif age > 3:
        price = 10

    print(f"\nThe ticket will cost you {price} Dollars")
