cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())


# true
car = "bmw"
print(car == "bmw")

# true
car2 = "bmw"
print(car == car2)

# true
car = "Audi"
print(car.lower() == "audi")

requested_topping = "mushrooms"

if requested_topping != "anchovies":
    print("Hold the anchovies!")

# numerical comparisons
age = 18
print(age == 18)

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

print(age < 17)
print(age <= 21)
print(age > 21)
print(age >= 21)

age_0 = 22
age_1 = 18
multiple_condition = age_0 >= 21 and age_1 >= 21

# for better readability
another_condition = (age_0 >= 21) and (age_1 >= 21)

or_condition = age_0 >= 21 or age_1 <= 21

# checking whether a value is in a list

requested_toppings = ["mushrooms", "onions", "pineapple"]
list_condition_1 = "mushrooms" in requested_toppings
list_condition_2 = "pepperoni" in requested_toppings

banned_users = ["andrew", "carolina", "david"]
user = "marie"

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# Boolean Expression
game_active = True
can_edit = False
