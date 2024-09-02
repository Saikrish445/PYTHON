import random


def SWGgame(computer, mine):
    if computer == mine:
        return None
    elif computer == "s" and mine == "g":
        return True
    elif computer == "w" and mine == "s":
        return True
    elif computer == "g" and mine == "w":
        return True
    else:
        return False


choice = ("s", "w", "g")
computer = random.randint(0, 2)
computer = choice[computer]
mine = input("enter any of these s or w or g:").lower()

win = SWGgame(computer, mine)
print(f"{mine} is your's and {computer} is computer's choice")
if win is None:
    print("Opps! Draw Game")
if win is True:
    print("Hurray! You Won")
else:
    print("Better Luck Next Time")
