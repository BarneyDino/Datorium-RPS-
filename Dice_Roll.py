import random
while(True):
    a = [1, 2, 3, 4]
    b = (1, 2, 3, 4, 5, 6)
    c = (1, 2, 3, 4, 5, 6, 7, 8)
    d = (1, 2, 3, 4, 5, 6, 7, 8, 10)
    e = (1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12)
    f = (1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

    d4 = random.choice(a)
    d6 = random.choice(b)
    d8 = random.choice(c)
    d10 = random.choice(d)
    d12 = random.choice(e)
    d20 = random.choice(f)

    Dice_Roll = input("What dice do you want to roll? (d4, d6, d8, d10, d12, d20):")

    if Dice_Roll == "d4":
        print(f"on a 1d4 you rolled a", d4)
    elif Dice_Roll == "d6":
        print(f"on a 1d6 you rolled a", d6)
    elif Dice_Roll == "d8":
        print(f"on a 1d8 you rolled a", d8)
    elif Dice_Roll == "d10":
        print(f"on a 1d10 you rolled a", d10)
    elif Dice_Roll == "d12":
        print(f"on a 1d12 you rolled a", d12)
    elif Dice_Roll == "d20":
        print(f"on a 1d20 you rolled a", d20)
