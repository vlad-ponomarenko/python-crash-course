from dice import Die

my_dice = Die()


for i in range(1, 11):
    my_dice.roll_die()


my_dice = Die(10)
for i in range(1, 11):
    my_dice.roll_die()


my_dice = Die(20)
for i in range(1, 11):
    my_dice.roll_die()
