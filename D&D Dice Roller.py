import random

def roll_dice(number_of_dice, sides):
    rolls = []

    for i in range(number_of_dice):
        roll = random.randint(1, sides)
        rolls.append(roll)

    return rolls

print("D&D Dice Roller")
print("----------------")

while True:
    dice = input("Enter dice to roll, like 1d20, 2d6, or q to quit: ")

    if dice.lower() == "q":
        print("Goodbye, adventurer.")
        break

    if "d" not in dice:
        print("Invalid format. Try something like 1d20.")
        continue

    parts = dice.lower().split("d")

    number_of_dice = int(parts[0])
    sides = int(parts[1])

    rolls = roll_dice(number_of_dice, sides)
    total = sum(rolls)

    print("Rolls:", rolls)
    print("Total:", total)

    if sides == 20 and number_of_dice == 1:
        if total == 20:
            print("Natural 20! Critical success!")
        elif total == 1:
            print("Natural 1... critical fail.")
