guests = ['A', 'B', 'C']
print(len(guests))
message = 'I want to invite you to dinner'
print(f"Hello {guests[0]}, {message}")
print(f"Hello {guests[1]}, {message}")
print(f"Hello {guests[2]}, {message}")
print(f"{guests[2]} can't make it!")
guests[2] = "D"
print(f"Hello {guests[0]}, {message}")
print(f"Hello {guests[1]}, {message}")
print(f"Hello {guests[2]}, {message}")
print("Bigger table found")

guests.insert(0, "E")
guests.insert(2, "M")
guests.append("L")


print(f"Hello {guests[0]}, {message}")
print(f"Hello {guests[1]}, {message}")
print(f"Hello {guests[2]}, {message}")
print(f"Hello {guests[3]}, {message}")
print(f"Hello {guests[4]}, {message}")
print(f"Hello {guests[5]}, {message}")