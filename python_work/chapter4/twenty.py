for i in range(1, 21):
    print(i)



list = range(1, 1000001)

#for number in list:
 #   print(number)



print(min(list))
print(max(list))
print(sum(list))


oddNumbers = range(1,21, 2)
for number in oddNumbers:
    print(number)



threes = range(3, 31, 3)
for number in threes:
    print(number)


print("\nCUBES:")
cubes = [value**3 for value in range(1,11)]
for cube in cubes:
    print(cube)