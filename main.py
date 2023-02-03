import random

def game():
    name = input("Enter your name:")

    #prompt player to make their choice
    choice = input('Choose between "rock","paper" and "scissors" ')
    options = ["rock", "paper", "scissors"]

    #This code is selecting a random value from a list called "options" and assigning it to the variable "computer_choice"
    #The function "random.choice" is from the "random" module in Python, and it is used to randomly select an item from a sequence
    computer_choice = random.choice(options)

    print(f"The computer chose:", computer_choice)

    #assigning the display messsage
    message1 = "you've tied"
    message2 = "you've lost"
    message3 = "you've won"

    #conditions to get the winner
    if choice==computer_choice:
        print(name, message1)
    elif choice == "rock" and computer_choice == "scissors":
        print(name, message3)
    elif choice == "rock" and computer_choice == "paper":
        print(name, message2)
    elif choice == "paper" and computer_choice == "scissors":
        print(name, message2)
    elif choice == "paper" and computer_choice == "rock":
        print(name, message3)
    elif choice == "scissors" and computer_choice == "paper":
        print(name, message3)
    else:
        print(name, message2)

game()