import random
import time

h = 1
while h == 1:
    print("\tWelcome to the game of ROCK, PAPER and SCISSORS\n")
    print("The game will be of ten (10) points.")
    your_score = 0
    comp_score = 0
    count = 1
    while count <= 10:
        print("\n", end='')
        print(count, end=' ')
        you = input("'r' for Rock\n  'p' for Paper\n  's' for Scissor\nEnter your choice: ")
        your_choice = you.lower()
        c_choice = ["r", "p", "s"]
        comp_choice = random.choice(c_choice)
        if your_choice == "r":
            if comp_choice == "s":
                your_score += 1
                print("\n\t SCOREBOARD")
                print("You chose ROCK\nComputer chose SCISSORS")
                print("Your score = ", your_score, "\nComputer score = ", comp_score)
                time.sleep(0.5)
            elif comp_choice == "p":
                comp_score += 1
                print("\n\t SCOREBOARD")
                print("You chose ROCK\nComputer chose PAPER")
                print("Your score = ", your_score, "\nComputer score = ", comp_score)
                time.sleep(0.5)
            elif comp_choice == "r":
                print("\n\t SCOREBOARD")
                print("You chose ROCK\nComputer chose ROCK")
                print("Your score = ", your_score, "\nComputer score = ", comp_score)
                time.sleep(0.5)
        elif your_choice == "p":
            if comp_choice == "r":
                your_score += 1
                print("\n\t SCOREBOARD")
                print("You chose PAPER\nComputer chose ROCK")
                print("Your score = ", your_score, "\nComputer score = ", comp_score)
                time.sleep(0.5)
            elif comp_choice == "s":
                comp_score += 1
                print("\n\t SCOREBOARD")
                print("You chose PAPER\nComputer chose SCISSORS")
                print("Your score = ", your_score, "\nComputer score = ", comp_score)
                time.sleep(0.5)
            elif comp_choice == "p":
                print("\n\t SCOREBOARD")
                print("You chose PAPER\nComputer chose PAPER")
                print("Your score = ", your_score, "\nComputer score = ", comp_score)
                time.sleep(0.5)
        elif your_choice == "s":
            if comp_choice == "p":
                your_score += 1
                print("\n\t SCOREBOARD")
                print("You chose SCISSORS\nComputer chose PAPER")
                print("Your score = ", your_score, "\nComputer score = ", comp_score)
                time.sleep(0.5)
            elif comp_choice == "r":
                comp_score += 1
                print("\n\t SCOREBOARD")
                print("You chose SCISSORS\nComputer chose ROCK")
                print("Your score = ", your_score, "\nComputer score = ", comp_score)
                time.sleep(0.5)
            elif comp_choice == "s":
                print("\n\t SCOREBOARD")
                print("You chose SCISSORS\nComputer chose SCISSORS")
                print("Your score = ", your_score, "\nComputer score = ", comp_score, )
                time.sleep(0.5)
        else:
            print("Wrong Input.")
        count += 1
    print("\n--GAME RESULT--")
    if your_score == comp_score:
        print("GAME DRAWN")
    elif your_score > comp_score:
        print("HURRAH...YOU WON")
    else:
        print("YOU LOST...BETTER LUCK NEXT TIME")
    print("--Thank You--")
    h = int(input("Enter 1 to continue\nEnter 2 to exit: "))
if h == 2:
    print("--THANK YOU--")
else:
    print("Wrong Input.")
