guests = ['A', 'B', 'C']
message = 'I want to invite you to dinner'
print(f"Hello {guests[0]}, {message}")
print(f"Hello {guests[1]}, {message}")
print(f"Hello {guests[2]}, {message}")
print(f"{guests[2]} can't make it!")
guests[2] = "D"
print(f"Hello {guests[0]}, {message}")
print(f"Hello {guests[1]}, {message}")
print(f"Hello {guests[2]}, {message}")