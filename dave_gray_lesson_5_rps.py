# how to get user input in python
# input() function is used to take input from the user

# value = input('Please enter a value:\n')
# print(value)

import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# print(RPS(2))   # Terminal output: RPS.PAPER
# print(RPS.ROCK)  # Terminal output: RPS.ROCK
# print(RPS["ROCK"])  # Terminal output: RPS.ROCK
# print(RPS["ROCK"].value)  # Terminal output: 1
# sys.exit()

print('')
playerchoice = input('Enter... \n1 for Rock\n2 for Paper\n3 for Scissors\n\n')
1
# convert the input to an integer as playerchoice is a string (this way we can compare it to the numbers 1, 2, and 3)
player = int(playerchoice)

# if playerchoice is less than 1 or greater than 3, print an error message
if player < 1 or player > 3:
    sys.exit("Invalid choice. Please enter a number between 1 and 3.")

computerchoice = random.choice("123")

computer = int(computerchoice)

print('')
# replace RPS. with an empty string to get the name of the choice without the enum prefix
print("Player chose: " + str(RPS(player)).replace("RPS.", "") + ".")
# replace RPS. with an empty string to get the name of the choice without the enum prefix
print("Python chose: " + str(RPS(computer)).replace("RPS.", "") + ".")
print('')

if player == 1 and computer == 3:
    print("Rock crushes Scissors.\t🎉  Player wins! 🎉")
elif player == 2 and computer == 1:
    print("Paper covers Rock.\t🎉  Player wins! 🎉")
elif player == 3 and computer == 2:
    print("Scissors cuts Paper.\t🎉  Player wins! 🎉")
elif player == computer:
    print("😒  It's a tie! 😒")
else:
    print("🐍  Python win! 🐍")
