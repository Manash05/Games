# Number guessing game using python


import time

number = 78         # The number selected for the game
count = 1
print("\n\t*** WELCOME TO THE NUMBER GUESSING GAME ***\n")
print("You will be given 10 chances to guess the number correctly.\n"
      "You will be given instruction based on your choices to help you guess the number correctly.\n")
while count <= 9:
    print(count, end="")
    guess = int(input(". Guess the number: "))
    if guess < number:
        print("Oops...wrong choice. Try something GREATER. ")

    elif guess > number:
        print("Oops...wrong choice. Try something SMALLER. ")

    else:
        print("Hurrah...you guessed the number correctly in", count, "guesses. You won. ")
        break
    print("No. of guesses left: ", 10 - count, "\n")
    time.sleep(0.4)         # Program sleeps for 0.4 seconds

    count += 1              # Increment of count by 1

if count == 10:
    print(count, end="")
    guess = int(input(". Guess the number: "))
    if guess == number:
        print("Hurrah...you guessed the number correctly in", count, "guesses. You won. ")  # Win message
    else:
        print("Oops...you have used all your chances.\n"                                    # Lose message
              "The number was", number)
        print("Better luck next time.")

