"""A number-guessing game."""
import random
# Put your code here
print("hi")
#greet player
print("Greetings, player!")
# get player name
player_name = input("Please enter your name: ")
# choose random number between 1 and 100
random_num = random.randint(1,100)
# repeat forever:
#     get guess
guess = input("Please choose a number between 1 and 100:  ")
#     if guess is incorrect:
if guess != random_num:
    print("Hint: ")
#         give hint
#         increase number of guesses
#     else:
#         congratulate player
else:
    print(f"Congratulations {player_name}!")