import random

print("Welcome to Number Guessing Game!")

secret_number = random.randint(1, 100)
guesses = []

while True:
    guess = int(input("Enter a number (1-100): "))
    guesses.append(guess)

    if(guess == secret_number):
        print("Congratulations! You guessed correctly.")
        print(f"You guessed it in {len(guesses)} attempts.")
        break

    elif(guess < secret_number):
        print("Too low! Try again.")

    else:
        print("Too high! Try again.")

print("Your guesses:", guesses)