pizzas = ['CheesePizza', 'Margharitta', 'SalamiPizza']
for pizza in pizzas:
    print(f"I like {pizza}")

friends_pizzas = pizzas[:]
print(friends_pizzas)
friends_pizzas.append("BrocolliPizza")


print(pizzas)
print(friends_pizzas)