import random

print("Guess the Number!")
secret = random.randint(1, 10)

while True:
    guess = int(input("Enter a number between 1 and 10: "))
    if guess == secret:
        print("You won!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
