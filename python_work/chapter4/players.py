# ['charles', 'martina', 'michael']
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])


# ['martina', 'michael', 'florence']
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])


# ['charles', 'martina', 'michael', 'florence']
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])


# ['michael', 'florence', 'eli']
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])


# # ['michael', 'florence', 'eli']
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])


players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
