import random


random_number = random.randint(1, 100)
attempts = 0

while True:
    user_input = int(input("Guess the number: "))
    attempts += 1
    if user_input < random_number:
        print("The number you entered is too low.")
    elif user_input > random_number:
        print("The number you entered is too high.")
    else:
        print(f"You guessed the number in {attempts} attempts!")
        break
