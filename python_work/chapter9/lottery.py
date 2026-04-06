from random import choice

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "B", "C", "D", "E"]

choosen_elements = []

for i in range(1, 5):
    choosen_element = choice(list)
    list.remove(choosen_element)
    choosen_elements.append(choosen_element)

print(choosen_elements)
