import random
from time import sleep

choice = ["Rock","Paper","Scissors"]
computer = random.choice(choice)

player = False

while player == False:
    print("Welcome To Rock,Paper and Scissors!!!")
    print("\nPlease, wait the game is loading....")
    sleep(3)
    player = input("Which one do you want to choose?\n'Rock:'Rock'\n'Paper': 'Paper'\n'Scissors': 'Scissors'\n'Stop the game': 'Stop':")
    if player == computer:
        print("\nPlease Wait We Are Loading Your Results...")
        sleep(1)
        print("It's a Tie!!!")
    elif player == "Rock":
        if computer == "Paper":
            print("\nPlease Wait We Are Loading Your Results...")
            sleep(1)
            print("You Have Lost!!")
        else:
            print("\nPlease Wait We Are Loading Your Results...")
            sleep(1)
            print("You Have Won!!")
    elif player == "Scissors":
        if computer == "Rock":
            print("\nPlease Wait We Are Loading Your Results...")
            sleep(1)
            print("You Have Lost!!")
        else:
            print("\nPlease Wait We Are Loading Your Results...")
            sleep(1)
            print("You Have Won!!")
    elif player == "Paper":
        if computer == "Scissors":
            print("\nPlease Wait We Are Loading Your Results...")
            sleep(1)
            print("You Have Lost!!")
        else:
            print("\nPlease Wait We Are Loading Your Results...")
            sleep(1)
            print("You Have Won!!")
    elif player == "Stop":
        print("Thanks For Playing!!")
        break
    else:
        print("That's not a valid play!!")
        break

    player = False
