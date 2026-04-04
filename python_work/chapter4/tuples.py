dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# causes TypeError
# dimensions[0] = 250

# A Tuple with one element
my_t = (3,)


dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

# Writing Over a Tuple
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
