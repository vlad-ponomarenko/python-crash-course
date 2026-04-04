prompt = "How many people are in your dinner group? "
amount = input(prompt)
amount = int(amount)

if amount > 8:
    print("You will have to wait for a table")
else:
    print("Your table is ready")
