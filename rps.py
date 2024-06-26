# Play command line Rock-Paper-Scissors
# by Krisha
import random


p1 = "You win!"

userwins = 0
compwins = 0

i = 3

while i > 0:

    if userwins == 2 or compwins == 2:
        break

    options = ["rock", "paper", "scissors"]
    computer = str(random.choice(options))

    user = input("Choose rock, paper, or scissors?: ")

    print("player 2 choice: " + computer)

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

if userwins == 2:
    print("You win the tournament!")
elif compwins == 2:
    print("Computer wins the tournament")
