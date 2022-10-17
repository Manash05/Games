# Number guessing game using python

import time
import random


def game(number):               # Defining a function
    print("You will be given 10 chances to guess the number correctly.\n"
          "You will be given instruction based on your choices to help you guess the number correctly.\n")
    count = 1
    while count <= 9:
        print(count, end="")
        guess = int(input(". Guess the number: "))
        if guess < number:
            print("Oops...wrong choice. Try something GREATER. ")

        elif guess > number:
            print("Oops...wrong choice. Try something SMALLER. ")

        else:
            print("Hurrah...you guessed the number correctly in", count, "guesses. You won. ")
            break               # Terminates the loop
        print("No. of guesses left: ", 10 - count, "\n")
        time.sleep(0.4)         # Programs sleeps for 0.4 seconds

        count = count + 1       # Increment of count by 1

    if count == 10:
        print(count, end="")    # 'end=' indicates that the end character is whitespace and not a newline.
        guess = int(input(". Guess the number: "))
        if guess == number:
            print("Hurrah...you guessed the number correctly in", count, "guesses. You won. ")
        else:
            print("Oops...you have used all your chances.\n"
                  "The number was", number)
            print("Better luck next time.")


print("\n\t*** WELCOME TO THE NUMBER GUESSING GAME ***\n")
print("You choose a two digit number for your friend to guess it.\nor \n"
      "The computer generates the two digit number for you to guess.")
repeat = 1
while repeat == 1:
    choice = int(input("\nEnter '1' if you want to set the two digit number by yourself.\n"
                       "Enter '2' if you want the computer to generate the two digit number.\n"
                       "Enter your choice: "))

    if choice == 1:
        num = int(input("Enter the number for the game: "))
        print("\n\t--GAME STARTS--\n")
        game(num)                       # Function is called

    elif choice == 2:
        num = random.randint(1, 99)     # Takes a random number from 1 to 99
        print("\n\t--GAME STARTS--\n")
        game(num)

    else:
        print("Wrong Input.")
        break

    repeat = int(input("Enter '1' to continue playing.\n"
                       "Enter '2' to exit.\n"
                       "Enter your choice: "))
if repeat == 2:
    print("\n\t--THANK YOU--")
else:
    print("Wrong Input.")
