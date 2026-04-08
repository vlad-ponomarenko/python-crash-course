prompt = "\n Which topping would you like to add to your pizza? "
active = True
while active:
    topping = input(prompt)
    if topping == "quit":
        break
    else:
        print(f"I will add {topping} to your pizza")
