while True:

    try:
        number_1 = int(input("Give first number: "))
        number_2 = int(input("Give second number: "))
        print(number_1 + number_2)
        break
    except ValueError:
        print("Please, input a number, not a string")
