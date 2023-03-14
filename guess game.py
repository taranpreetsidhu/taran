import random

actual_number = random.randint(0,100)
tries = 10
attempts = 0
print('Guess number between 0 and 100.\nYou have maximum 10 chances')
while attempts < tries:
    attempts += 1
    guess = int(input("guess the number:"))
    if guess<actual_number:
        print("your guess was too low")

    elif guess > actual_number:
        print("your guess was too high")

    else:
        print(f"you guessed the number in {attempts} attempts")
        break
    