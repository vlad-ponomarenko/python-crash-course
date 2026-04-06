class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} sells {self.cuisine_type}")

    def open_restaurant(self):
        print("The restaurant is open")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_served):
        self.number_served += number_served


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavours(self):

        print("\nThe following flavors are available: ")
        for flavour in self.flavors:
            print(f"\t{flavour}")


restaurant = Restaurant("Italian Stallion", "Italian")
print(f"{restaurant.restaurant_name}")
print(f"{restaurant.cuisine_type}")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_2 = Restaurant("French Baguette", "French")
restaurant_3 = Restaurant("Japanese Cafe", "Japanese")

restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()

restaurant_3.describe_restaurant()
restaurant_3.open_restaurant()


print(f"Customers served: {restaurant.number_served}")
restaurant.number_served = 5
print(f"Customers served: {restaurant.number_served}")
restaurant.set_number_served(10)
print(f"Customers served: {restaurant.number_served}")
restaurant.increment_number_served(30)
print(f"Customers served: {restaurant.number_served}")


restaurant_4 = IceCreamStand("Japanese Cafe", "Japanese", ["Orange", "Cherry", "Kokos"])
restaurant_4.display_flavours()
