import random

comp_num = random.randint(0, 100)
user_guess = int(input("Enter your guess: "))
trials = 1
try_again = ""
options = ['Y', 'YES', 'y', 'yes', 'ok']

while trials < 10:
    if user_guess == comp_num:
        print("You guessed it right!")
        trials += 1
        break
    elif user_guess > comp_num:
        print("Too high!")
        trials += 1
        user_guess = int(input("Enter your guess: "))
    elif user_guess < comp_num:
        print("Too low!")
        trials += 1
        user_guess = int(input("Enter your guess: "))
    if trials == 10:
        print("You lost. Want to play again?")
        if try_again in options:
            trials = 0
        else:
            break