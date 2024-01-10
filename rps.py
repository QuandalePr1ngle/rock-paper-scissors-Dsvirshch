#
# ROCK, PAPER, SCISSORS - Iterācija 1
# 
# 1. Spēle prasa ievadīt ciparu no 1 līdz 3 (izmanto input, https://www.w3schools.com/python/python_user_input.asp)
# 2. Dators iedomājas ciparu no 1 līdz 3  (izmanto random, https://www.w3schools.com/python/ref_random_randint.asp)
# 3. Atkarībā no ievadītajiem cipariem un datora, izdrukā paziņojumu par zaudējumu, uzvaru, vai neizšķirtu (izmanto if, else https://www.w3schools.com/python/python_conditions.asp)
#

ROCK = "1"
SCISSOR = "2"
PAPER = "3"

print("Welcome to Rock, Paper, Scissors!")


import random
import time
# ROCK, PAPER, SCISSORS - Iterācija 1
# 
# 1. Spēle prasa ievadīt ciparu no 1 līdz 3 (izmanto input, https://www.w3schools.com/python/python_user_input.asp)
# 2. Dators iedomājas ciparu no 1 līdz 3  (izmanto random, https://www.w3schools.com/python/ref_random_randint.asp)
# 3. Atkarībā no ievadītajiem cipariem un datora, izdrukā paziņojumu par zaudējumu, uzvaru, vai neizšķirtu (izmanto if, else https://www.w3schools.com/python/python_conditions.asp)
#

ROCK = "1"
SCISSOR = "2"
PAPER = "3"
time.sleep(0.9)
print("Welcome to Rock, Paper, Scissors!")
for Round in range(5):
    time.sleep(0.4)
    Round += 1
    print("Round " + str(Round))
    Your_input = input("1-Rock, 2-Scissors, 3-Paper: ")
    if Your_input == "1":
        RPS = "Rock"
    elif Your_input == "2":
        RPS = "Scissors"
    elif Your_input == "3":
        RPS = "Paper"
    else:
        RPS = "idk"
    time.sleep(0.9)
    print("You chose " + RPS)
    Comp_input = random.randint(1, 3)
    if Comp_input == 1 and Your_input == "1":
        time.sleep(0.9)
        print("Computer chose Rock")
        time.sleep(0.9)
        print("Draw")
    elif Comp_input == 1 and Your_input == "2":
        time.sleep(0.95)
        print("Computer chose Rock")
        time.sleep(0.95)
        print("You lose!")
        CompScore =+ 1
    elif Comp_input == 1 and Your_input == "3":
        time.sleep(0.95)
        print("Computer chose Rock")
        time.sleep(0.95)
        print("You won!!")
        YourScore =+ 1
    elif Comp_input == 2 and Your_input == "1":
        time.sleep(0.95)
        print("Computer chose Scissors")
        time.sleep(0.95)
        print("You won!!")
        YourScore =+ 1
    elif Comp_input == 2 and Your_input == "2":
        time.sleep(0.95)
        print("Computer chose Scissors")
        time.sleep(0.95)
        print("Draw")
    elif Comp_input == 2 and Your_input == "3":
        time.sleep(0.9)
        print("Computer chose Scissors")
        time.sleep(0.9)
        print("You lose!")
        CompScore =+ 1
    elif Comp_input == 3 and Your_input == "1":
        time.sleep(0.9)
        print("Computer chose Paper")
        time.sleep(0.9)
        print("You lose!")
        CompScore =+ 1
    elif Comp_input == 3 and Your_input == "2":
        time.sleep(0.9)
        print("Computer chose Paper")
        time.sleep(0.9)
        print("You won!!")
        YourScore =+ 1
    elif Comp_input == 3 and Your_input == "3":
        time.sleep(0.7)
        print("Computer chose Paper")
        time.sleep(0.7)
        print("Draw")
    else:
        time.sleep(0.5)
        print("Something went wrong")

if YourScore > CompScore:
    print("You won with the score" + str(YourScore))
elif YourScore < CompScore:
    print("You lost with the score" + str(YourScore))
elif YourScore == CompScore:
    print("Draw!!!!")

