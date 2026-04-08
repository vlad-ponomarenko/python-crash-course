def get_items(*toppings):
    print("\nThe following toppings are provided:")
    for topping in toppings:
        print(f"- {topping}")


get_items("a")
get_items("a", "b")
get_items("c", "b", "a")
