import random
from time import sleep

choices = ["Froakie", "Litten", "Rowlet"]

computer = random.choice(choices)

player = False

name = input("Hello, please enter your name: ")
while player == False:

    print(f"Hello, {name} Welcome to PokeMon Battle Game!!")
    player = input("Which pokemon do you want to choose?\n'Litten': 'Litten'\n'Froakie': 'Froakie'\n'Rowlet': 'Rowlet': 'Stop': ")
    if player == computer:
        print("Tie!!!")
    elif player == "Litten":
        if computer == "Froakie":
            print("\nPlease, wait we are loading your results....")
            sleep(2)

            print("You Lost!!!")
        else:
            print("You Won!!!")
    elif player == "Froakie":
        if computer == "Rowlet":
            print("\nPlease, wait we are loading your results....")
            sleep(2)
            print("You Have Lost!!!")
        else:
            print("You Have Won!!!")
    elif player == "Rowlet":
        if computer == "Litten":
            print("You Have Lost!!")
        else:
            print("\nPlease, wait we are loading your results....")
            sleep(2)
            print("You Have Won!!!")
    elif player == "Stop":
        print("Thanks For Playing!!!!")
        break
    else:
        print("That's not a valid play!!")

    player = False
