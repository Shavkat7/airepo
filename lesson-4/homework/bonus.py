import random

pc_points = 0
user_points = 0

options = ['rock', 'paper', 'scissors']

# User winning conditions
winning_conditions = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}


while pc_points < 5 and user_points < 5:
    pc_string = random.choice(options)


    try:
        user_num = int(input("Enter 1(rock), 2(paper), 3(scissors): "))
        if user_num not in [1, 2, 3]:
            raise ValueError
        user_string = options[user_num - 1]
    except ValueError:
        print("Invalid input! Enter only 1, 2, or 3.")
        continue

    print(f"Computer: {pc_string} | User: {user_string}")

    if pc_string == user_string:
        print("Tie, no points awarded.")
    elif winning_conditions[user_string] == pc_string:
        user_points += 1
        print("You scored a point!")
    else:
        pc_points += 1
        print("Computer scored a point!")

    print(f"Current state: Computer: {pc_points} | You: {user_points}")

if user_points == 5:
    print("Congratulations, you won!")
else:
    print("Computer won!")

print(f"Final state: Computer: {pc_points} | You: {user_points}")