from random import randint

random_number = randint(1, 10)

user_guess = input("Guess a number between 1 and 10: ")

if user_guess == random_number:
    print("You Guessed the number!")
else:
    print("Nope that was not the number!")

