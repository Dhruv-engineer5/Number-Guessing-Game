import random

File = "History.txt"
def history():
    file = open(File , 'r')
    lines = file.readline()
    if len == 0 :
        print("Nothing")
        return
    else:
        print(file.read)

def Add():
    file = open(File , 'a')
    file.write("com's guess:"+ str(secret_number) + '\n')
    file.write("Your guess:"+ str(guesses) + '\n''\n')

print("Hi,Welcome to Number Guessing Game!")
secret_number = random.randint(1, 100)
guesses = []

while True:

    guess = int(input("Enter a number (1-100): "))
    guesses.append(guess)

    if(guess == secret_number):
        print("Congratulations! You guessed correctly.")
        print(f"You guessed it in {len(guesses)} attempts.")
        Add()

        i = input("Do you want to see history! y/n").strip().lower()
        if i == "y":
            history()
        break

    elif(guess < secret_number):
        print("Too low! Try again.")

    else:
        print("Too high! Try again.")

print("Your guesses:", guesses)