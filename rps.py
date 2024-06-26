# Play command line Rock-Paper-Scissors, 3 game tournament
# by Krisha
import random


p1 = "You win!"

userwins = 0
compwins = 0

i = 3

while i > 0:

    # winner found so breaks
    if userwins == 2 or compwins == 2:
        break

    # get computer's choice
    options = ["rock", "paper", "scissors"]
    computer = str(random.choice(options))

    user = input("Choose rock, paper, or scissors?: ") #get player's choice

    print("player 2 choice: " + computer)

    # checks who won & adds 1 pt for winner
    if user == computer:
        print("draw")
    elif user == "paper" and computer == "rock":
        print(p1)
        userwins += 1
    elif user == "rock" and computer == "scissors":
        print(p1)
        userwins += 1

    elif user == "scissors" and computer == "paper":
        print(p1)
        userwins += 1
    else:
        print("player2 wins")
        compwins += 1
    i += 1

#if one side wins twice, they win the 3-game tournament
# otherwise continues to 3rd game bc the players drawed once --> then one player accumulates 2 pts
if userwins == 2:
    print("You win the 3-game tournament!")
elif compwins == 2:
    print("Computer wins the 3-game tournament")
