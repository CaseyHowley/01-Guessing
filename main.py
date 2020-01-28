import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

guessList = []
numGuesses = 0
target = random.randint(1,100)

print("Guess the number!")
print("It's a random number between 1 and 100!")

while True:
    guess = input("Enter a number: ")
    guessList.append(guess)
    try:
        guess = int(guess)
        if guess > target:
            print("Too high!")
            numGuesses += 1
        elif guess < target:
            print("Too low!")
            numGuesses += 1
        else:
            numGuesses += 1
            print("You got it!")
            print("You guessed the number in " + str(numGuesses) + " attempts!")
            print("Your guesses were:")
            print(guessList)
            break
    except:
        print("That wasn't a number!")
        guessList.remove(str(guess))
else:
    print("How did you get here?!")
    print("Whatever you did, you should report it to the developer.")
