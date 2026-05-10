import random

def roll_dice(number_of_dice, sides):
    rolls = []

    for i in range(number_of_dice):
        roll = random.randint(1, sides)
        rolls.append(roll)

    return rolls


def roll_d20_with_advantage(mode):
    roll_1 = random.randint(1, 20)
    roll_2 = random.randint(1, 20)

    if mode == "adv":
        final_roll = max(roll_1, roll_2)
        print("Advantage rolls:", roll_1, "and", roll_2)
        print("You take the higher roll:", final_roll)

    elif mode == "dis":
        final_roll = min(roll_1, roll_2)
        print("Disadvantage rolls:", roll_1, "and", roll_2)
        print("You take the lower roll:", final_roll)

    return final_roll


print("D&D Dice Roller")
print("----------------")
print("Examples: 1d20, 2d6, adv, dis, q")

while True:
    dice = input("Enter dice to roll: ")

    if dice.lower() == "q":
        print("Goodbye, adventurer.")
        break

    elif dice.lower() == "adv":
        total = roll_d20_with_advantage("adv")

        if total == 20:
            print("Natural 20! Critical success!")
        elif total == 1:
            print("Natural 1... critical fail.")

    elif dice.lower() == "dis":
        total = roll_d20_with_advantage("dis")

        if total == 20:
            print("Natural 20! Critical success!")
        elif total == 1:
            print("Natural 1... critical fail.")

    else:
        if "d" not in dice:
            print("Invalid format. Try something like 1d20, adv, or dis.")
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
