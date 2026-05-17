import random

while True:

    AI = random.randint(1, 3)

    x = input("Choose rock, paper or scissors: ")

    if x == "rock":
        if AI == 2:
            print("You win!")
        elif AI == 3:
            print("You lose!")
        elif AI == 1:
            print("It was a draw!")

    elif x == "paper":
        if AI == 1:
            print("You win!")
        elif AI == 2:
            print("You lost!")
        elif AI == 3:
            print("It was a draw!")

    elif x == "scissors":
        if AI == 1:
            print("You lose!")
        elif AI == 2:
            print("It was a draw!")
        elif AI == 3:
            print("You win!")

    else:
        print("Choose from the list please.")
        continue

    if AI == 1:
        print("AI used Rock!")
    elif AI == 2:
        print("AI used Scissors!")
    elif AI == 3:
        print("AI used Paper!")

    print()
